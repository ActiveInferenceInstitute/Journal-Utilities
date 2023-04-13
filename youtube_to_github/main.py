import json
import time
import os
import csv
import shutil
import time
import sys
import logging
from typing import List, Generator, Dict
# downloaded file
from typing_extensions import Literal
import requests
import yt_dlp # python3.8 -m pip install -U yt-dlp
from github import Github # python3.8 -m pip install PyGithub 
from pydub import AudioSegment # 2 packages to install to get to work
from pydub.utils import make_chunks
# local
import settings

'''
Step 1: getting the links of videos on a channel
'''

type_property_map = {
    "videos": "videoRenderer",
    "streams": "videoRenderer",
    "shorts": "reelItemRenderer"
}

logging.basicConfig(filename='info.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def get_initial_data(session: requests.Session, url: str) -> str:
    session.cookies.set("CONSENT", "YES+cb", domain=".youtube.com")
    response = session.get(url)

    html = response.text
    #print(html)
    return html


def get_ajax_data(
    session: requests.Session,
    api_endpoint: str,
    api_key: str,
    next_data: dict,
    client: dict,
) -> dict:
    data = {
        "context": {"clickTracking": next_data["click_params"], "client": client},
        "continuation": next_data["token"],
    }
    response = session.post(api_endpoint, params={"key": api_key}, json=data)
    return response.json()


def get_json_from_html(html: str, key: str, num_chars: int = 2, stop: str = '"') -> str:
    pos_begin = html.find(key) + len(key) + num_chars
    pos_end = html.find(stop, pos_begin)
    return html[pos_begin:pos_end]


def get_next_data(data: dict) -> dict:
    raw_next_data = next(search_dict(data, "continuationEndpoint"), None)
    if not raw_next_data:
        return None
    next_data = {
        "token": raw_next_data["continuationCommand"]["token"],
        "click_params": {"clickTrackingParams": raw_next_data["clickTrackingParams"]},
    }

    return next_data


def search_dict(partial: dict, search_key: str) -> Generator[dict, None, None]:
    stack = [partial]
    while stack:
        current_item = stack.pop(0)
        if isinstance(current_item, dict):
            for key, value in current_item.items():
                if key == search_key:
                    yield value
                else:
                    stack.append(value)
        elif isinstance(current_item, list):
            for value in current_item:
                stack.append(value)


def get_videos_items(data: dict, selector: str) -> Generator[dict, None, None]:
    return search_dict(data, selector)


def get_videos(
    url: str, api_endpoint: str, selector: str, limit: int, sleep: int
) -> Generator[dict, None, None]:
    session = requests.Session()
    session.headers[
        "User-Agent"
    ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    is_first = True
    quit = False
    count = 0
    while True:
        if is_first:
            html = get_initial_data(session, url)
            client = json.loads(
                get_json_from_html(html, "INNERTUBE_CONTEXT", 2, '"}},') + '"}}'
            )["client"]
            api_key = get_json_from_html(html, "innertubeApiKey", 3)
            session.headers["X-YouTube-Client-Name"] = "1"
            session.headers["X-YouTube-Client-Version"] = client["clientVersion"]
            data = json.loads(
                get_json_from_html(html, "var ytInitialData = ", 0, "};") + "}"
            )
            next_data = get_next_data(data)
            is_first = False
        else:
            data = get_ajax_data(session, api_endpoint, api_key, next_data, client)
            next_data = get_next_data(data)
            #last_data.append(next_data)
        for result in get_videos_items(data, selector):
            try:
                count += 1
                yield result
                if count == limit:
                    quit = True
                    break
            except GeneratorExit:
                quit = True
                break

        if not next_data or quit:
            break

        time.sleep(sleep)
    session.close()

def get_channel(
    channel_id: str = None,
    channel_url: str = None,
    limit: int = None,
    sleep: int = 1,
    sort_by: Literal["newest", "oldest", "popular"] = "newest",
    content_type: Literal["videos", "shorts", "streams"] = "videos",
) -> Generator[dict, None, None]:

    """Get videos for a channel.

    Parameters:
        channel_id (``str``, *optional*):
            The channel id from the channel you want to get the videos for.
            If you prefer to use the channel url instead, see ``channel_url`` below.

        channel_url (``str``, *optional*):
            The url to the channel you want to get the videos for.
            Since there is a few type's of channel url's, you can use the one you want
            by passing it here instead of using ``channel_id``.

        limit (``int``, *optional*):
            Limit the number of videos you want to get.

        sleep (``int``, *optional*):
            Seconds to sleep between API calls to youtube, in order to prevent getting blocked.
            Defaults to 1.

        sort_by (``str``, *optional*):
            In what order to retrieve to videos. Pass one of the following values.
            ``"newest"``: Get the new videos first.
            ``"oldest"``: Get the old videos first.
            ``"popular"``: Get the popular videos first. Defaults to "newest".

        content_type (``str``, *optional*):
            In order to get content type. Pass one of the following values.
            ``"videos"``: Videos
            ``"shorts"``: Shorts
            ``"streams"``: Streams
    """

    sort_by_map = {"newest": "dd", "oldest": "da", "popular": "p"}    
    url = "{url}/{content_type}?view=0&sort={sort_by}&flow=grid".format(
        url=channel_url or f"https://www.youtube.com/channel/{channel_id}",
        content_type=content_type,
        sort_by=sort_by_map[sort_by],
    )
    api_endpoint = "https://www.youtube.com/youtubei/v1/browse"
    videos = get_videos(url, api_endpoint, type_property_map[content_type], limit, sleep)
    for video in videos:
        yield video

def find_pos(text_elm, first_search: str, second_search: str) -> str:
    first_pos = text_elm.find(first_search)
    last_pos = first_pos + text_elm[first_pos:].find(second_search)
    return text_elm[first_pos:last_pos]

def get_channel_id_and_name(youtube_link: str) -> str:
    # convert channel into channel id
    response = requests.get(youtube_link)
    channel_id = find_pos(response.text, '" href="https://www.youtube.com/channel/', '">')
    return channel_id.split('/')[-1]


'''
Step 2 Downloading the videos
'''

def make_folder(folder_name: str) -> None:
    try:
        os.makedirs(folder_name)
    except:
        pass


def download_m4a(urls: List[str]) -> List[str]:
    ''' Takes in list of URLS
    returns list of downloaded file names
    '''
    make_folder('original')

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        #'format': 'm4a',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        "external_downloader_args": ['-loglevel', 'panic'],
        "quiet": True,
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                error_code = ydl.download(url)
            except yt_dlp.utils.DownloadError:
                pass

    for file in os.listdir():
        if file.endswith('.m4a'):
            os.rename(file, f'./original/{file}')

    return [file for file in os.listdir('./original') if file.endswith('.m4a')]

'''
Step 3: get the file pairings for upload

Download data to csv from the following link:
https://community.coda.io/t/export-your-table-data-to-a-csv/30779 

'''

def csv_get_folder(files_to_upload: List[str], folder_names: List[str]) -> Dict[str, List[Dict[str, str]]]:

    #print(files_to_upload)
    files_to_insert: Dict[str, List[Dict[str, str]]] = {folder:[] for folder in folder_names}
    unknown_folder_to_insert: List[str] = [] # links to unkown videos
    youtube_links_to_files: List[str] = []

    with open('Active Inference Institute Livestreams.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_file) # headers
        for row in csv_reader:
            parent_folder_name = row[0]
            folder_name = row[1]
            youtube_link = row[3]
            youtube_id = youtube_link.split('/')[-1].split('v=')[-1].split('&')[0]
            youtube_title = row[4]
            found_index = -1
            if parent_folder_name not in folder_names and parent_folder_name != 'Symposium':
                unknown_folder_to_insert.append(youtube_id)
                continue
            for index, file in enumerate(files_to_upload):
                if youtube_id in file:
                    print(parent_folder_name, folder_name, youtube_id, youtube_title)
                    # modify symposium
                    parent_folder_name = parent_folder_name.replace('Symposium', 'Applied Active Inference Symposium')
                    files_to_insert[parent_folder_name].append({'filename': file, 'folder': folder_name})
                    found_index = index
                    youtube_links_to_files.append(youtube_link)
                    break
            if found_index != -1:
                del files_to_upload[found_index]
            else:
                unknown_folder_to_insert.append(youtube_id)
    
    return files_to_insert, youtube_links_to_files

'''
Step 4: Chunk files for upload
'''

def chunk_audio(files_to_upload: Dict[str, List[Dict[str, str]]]) -> Dict[str, List[Dict[str, str]]]:
    # files_to_upload = {'parent': [{'filename', 'folder'}]}
    # chunks the files and updates the dict with the new chunks and file_names

    #https://dataunbox.com/split-audio-files-using-python/
    #https://unix.stackexchange.com/questions/280767/how-do-i-split-an-audio-file-into-multiple
    #https://stackoverflow.com/questions/65857983/how-can-i-split-an-audio-file-into-multiple-audio-wav-files-from-folder
    make_folder('chunked') # creating a folder named chunked
    chunked_files_to_upload: Dict[str, List[Dict[str, str]]] = {}

    for parent_folder, files in files_to_upload.items():
        chunked_files_to_upload[parent_folder] = []
        for file in files:
            file_name = file['filename']
            folder = file['folder']

            myaudio = AudioSegment.from_file(f'./original/{file_name}', "m4a")
            chunk_length_ms = 1_500_000 # pydub calculates in millisec
            chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
            for i, chunk in enumerate(chunks):
                chunk_name = file_name.replace(".m4a", f'_{i}.m4a')
                chunk_path = f'./chunked/{chunk_name}'
                print(f'exporting: {chunk_name}')
                # https://stackoverflow.com/questions/62598172/m4a-mp4-audio-file-encoded-with-pydubffmpeg-doesnt-play-on-android
                chunk.export(chunk_path, format="ipod")
                chunked_files_to_upload[parent_folder].append({'filename': chunk_name, 'folder': folder})
    
    return chunked_files_to_upload


'''
Step 5: uploading to github
'''

def github_upload(files_to_upload: Dict[str, List[Dict[str, str]]]) -> None:
    # https://stackoverflow.com/questions/61292766/read-content-of-file-which-is-in-github-using-pygithub

    # files_to_upload = {'parent': [{'filename', 'folder'}]}
    print('in github')
    print(files_to_upload)

    g = Github(settings.github_token)
    GITHUB_REPO = 'ActiveInferenceJournal'
    GITHUB_USER = 'ActiveInferenceInstitute'
    repo = g.get_user(GITHUB_USER).get_repo(GITHUB_REPO)

    current_path: str = './chunked/'
    for parent_folder, files in files_to_upload.items():
        #parent_contents = repo.get_contents(parent_folder)
        for file in files:
            file_name = file['filename']
            folder = file['folder']
            
            folder = folder.replace('stream', 'Stream').replace(' #', '_').split('.')[0]
            git_path: str = f'{parent_folder}/{folder}/Audio/{file_name}'

            # get file contents for upload
            with open(f'{current_path}{file_name}', 'rb') as file:
                content = bytes(bytearray(file.read()))

            # upload file
            #print(git_path)
            is_not_uploaded = True
            while is_not_uploaded: # to retry uploading because of connection error
                try:
                    repo.create_file(git_path, f'committing {file_name} Audio', content, branch='main')
                    logging.info(f'uploaded {file_name} -- {git_path}')
                except Exception as error:
                    logging.error(f'github upload: {error}')
                    time.sleep(4)
                    continue
                is_not_uploaded = False

            print(file_name, folder)


def main() -> None:
    chunked_files = {}
    if not os.path.isfile('chunked.json'):
        # Get the links from the channel
        youtube_link = settings.youtube_channel
        
        channel_id = get_channel_id_and_name(youtube_link)

        # TODO could replace this with grabbing the links from the CSV
        all_streams = [f'https://www.youtube.com/watch?v={video["videoId"]}' for video in get_channel(channel_id, content_type='streams')]
        all_streams.extend(f'https://www.youtube.com/watch?v={video["videoId"]}' for video in get_channel(channel_id, content_type='videos'))

        # check what links are new
        with open('uploaded_links.json', 'r') as file:
            uploaded_links = json.load(file)['links']
        new_uploads: List[str] = list(set(all_streams) - set(uploaded_links))
        print(new_uploads, '\n', all_streams, '\n', uploaded_links) # TEST statement

        files_downloaded = download_m4a(new_uploads)

        folder_names = ["Applied Active Inference Symposium", "BookStream", "GuestStream", "MathStream", "Livestream", "ModelStream", "OrgStream", "ReviewStream", "Roundtable", "Twitter Spaces"]
        if not len(files_downloaded):
            print("all files uploaded")
            sys.exit()

        original_file_pairings, used_links = csv_get_folder(files_downloaded, folder_names)
        chunked_files = chunk_audio(original_file_pairings)
        print('All chunked files')
        print(chunked_files)
        with open('chunked.json', 'w') as file: # write chunked results to file for future runs if errors
            json.dump(chunked_files, file)
    else:
        with open('chunked.json', 'r') as file:
            chunked_files = json.load(file)
        print('uploading already chunked files if wanting to get new files rerun this program after successfully uploading the current chunked files')
    
    github_upload(chunked_files)

    # saving what files have been used in previous runs
    uploaded_links.extend(used_links)
    with open('uploaded_links.json', 'w') as file:
        json.dump({'links': uploaded_links}, file)
    #os.remove('chunked.json') # delete as all files were uploaded
    # remove folders  (locally) https://stackoverflow.com/questions/6996603/how-can-i-delete-a-file-or-folder-in-python
    shutil.rmtree('original')
    shutil.rmtree('chunked')

if __name__ == '__main__':
    main()

'''
TODO
https://community.coda.io/t/export-your-table-data-to-a-csv/30779
https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

# to get info on the files that have been uploaded
https://waylonwalker.com/git-python-all-commits/
# change links to only be the linkIds for easy comparison? if trying to use CSV youtube links.. 
'''
