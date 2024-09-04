## TODO
- [x] move WorkingCopy MD file to Transcripts/WorkingCopy folder for
    - [x] PIP
    - [x] Social Sciences
    - [x] 2023 Ecosystem Symposium
    - [x] update links in the Coda table
- [x] clean up filename references
    - [x] rename journal_filename to metadata_filename
    - [x] rename processed_transcript_filename to prose_filename
    - [x] update session set workingcopy_filename

- add all existing processed transcripts in Metadata and Transcripts/Prose to database that were not in initial USB card
    - Roundtable_2023.2
- add `insert_metadata_youtube_api` to `download_and_transcribe`, `pip install yt-dlp` and test
- Collect speaker information for all transcripts

---

## Notes on Steps
* download audio transcript
* run through Assembly
* create a speakers list
* generate a single source transcript
* when done, generate final MD (with or w/o terms) and SRT

## If a Single Session
* generate a Pandoc PDF
* generate a Pandoc HTML

## If a course OR Guestreams with multiple sessions
* combine into one MD
* generate Pandoc PDF
* generate Pandoc HTML


/mnt/md0/projects/ActiveInferenceJournal/MathStream/MathStream_005/Transcripts/Prose/ma005-1_ActInf MathStream 005.1 ~ Cristian Bodnar ~ Topological Deep Learning.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/MathStream/MathStream_005/Transcripts/Prose/ma005-1_ActInf MathStream 005.1 ~ Cristian Bodnar ~ Topological Deep Learning.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/MathStream/MathStream_006/Transcripts/Prose/ma006-1_ma006-1 ~ Sean Tull ~ Active Inference in String Diagrams.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/MathStream/MathStream_004/Transcripts/Prose/ActInf MathStream #004 ~ David Spivak, 'Category Theory'.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2021.1/Transcripts/Prose/Active Inference Institute 2021 Quarterly Roundtable 1.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2023.2/Transcripts/Prose/rt2023-2_Active Inference Institute ~ 2023 Quarterly Roundtable 2_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2023.2/Transcripts/Prose/rt2023-2_Active Inference Institute ~ 2023 Quarterly Roundtable 2._transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2023.1/Transcripts/Prose/Active Inference Institute ~ 2023 Quarterly Roundtable 1_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2021.3/Transcripts/Prose/Active Inference Institute 2021 Quarterly Roundtable 3.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2021.2/Transcripts/Prose/Active Inference Institute 2021 Quarterly Roundtable 2.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2023.3/Transcripts/Prose/rt2023-3_Active Inference Institute ~ 2023 Quarterly Roundtable 3_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2023.3/Transcripts/Prose/rt2023-3_Active Inference Institute ~ 2023 Quarterly Roundtable 3_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2022.4/Transcripts/Prose/Active Inference Institute 2022 Quarterly Roundtable 4.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2022.2/Transcripts/Prose/Active Inference Institute 2022 Quarterly Roundtable 2.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2022.1/Transcripts/Prose/Active Inference Institute 2022 Quarterly Roundtable 1.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2021.4/Transcripts/Prose/Active Inference Institute 2021 Quarterly Roundtable 4.odt
/mnt/md0/projects/ActiveInferenceJournal/Roundtable/Roundtable_2022.3/Transcripts/Prose/Active Inference Institute 2022 Quarterly Roundtable 3.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_058/Transcripts/Prose/gs058-1_gs058-1 Working with Edelman.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_058/Transcripts/Prose/gs058-1_gs058-1 Working with Edelman.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_023/Transcripts/Prose/ActInf GuestStream #023 (2022) ~ Ramstead et al., 'Rebooting the Free Energy Principle Literature'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_032/Transcripts/Prose/ActInf GuestStream 032.1 _ Adam Pease 'A Neuro-Symbolic Approach to Language Understanding'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_032/Transcripts/Prose/ActInf GuestStream 032.1 _ Adam Pease 'A Neuro-Symbolic Approach to Language Understanding'.pdf
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_044/Transcripts/Prose/gs044-1_ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category Theory, Consciousness, Integrated Information.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_044/Transcripts/Prose/gs044-1_ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category Theory, Consciousness, Integrated Information.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_047/Transcripts/Prose/gs047-1_ActInf GuestStream 047.1 - Predicting, Reflecting Framework for Dual Process Theory - Bellini-Leite_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_047/Transcripts/Prose/gs047-1_ActInf GuestStream 047.1 - Predicting, Reflecting Framework for Dual Process Theory - Bellini-Leite_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_019/Transcripts/Prose/ActInf GuestStream #019 (2022) ~ Marco Facchin, 'Extended Predictive Minds'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_021/Transcripts/Prose/ActInf GuestStream #021 (2022) ~ Adam Safron, 'Deflating deflationary accounts of free will'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_057/Transcripts/Prose/gs057-1_ActInf GuestStream 057.1~ Andy Keller, Natural Neural Structure.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_057/Transcripts/Prose/gs057-1_ActInf GuestStream 057.1~ Andy Keller, Natural Neural Structure.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_025/Transcripts/Prose/ActInf GuestStream #025 (2022) ~ Autistic-Like Traits, 'Positive Schizotypy, Predictive Mind'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_041/Transcripts/Prose/gs041-1_gs041-1 Elliot, Steven.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_041/Transcripts/Prose/gs041-1_gs041-1 Elliot, Steven.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_056/Transcripts/Prose/gs056-1_ActInf GuestStream 056.1 ~ Gregoire Sergeant Agency with structured latent state-spaces.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_056/Transcripts/Prose/gs056-1_ActInf GuestStream 056.1 ~ Gregoire Sergeant Agency with structured latent state-spaces.wav.sentences.csv
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_035/Transcripts/Prose/ActInf GuestStream 035 _ Jordan Hall & Matthew Pirkowski.pdf
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_035/Transcripts/Prose/ActInf GuestStream 035 _ Jordan Hall & Matthew Pirkowski.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_036/Transcripts/Prose/gs036 ~ Ben Falandays, A Potential Mechanism for Gibsonian Resonance.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_036/Transcripts/Prose/gs036.1 ~ Ben Falandays.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_020/Transcripts/Prose/ActInf GuestStream #020 (2022) ~ Shannon Proksch, 'Coordination Dynamics of Multi-agent Interaction'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_015/Transcripts/Prose/gs015-3_ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_015/Transcripts/Prose/ActInf GuestStream #015 (2022) ~ Bobby Azarian, 'Universal Bayesianism; Integrated Evolutionary Synthesis'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_015/Transcripts/Prose/gs015-3_ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_051/Transcripts/Prose/gs051-1_ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_051/Transcripts/Prose/gs051-1_ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_024/Transcripts/Prose/GuestStream 024.pdf
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_024/Transcripts/Prose/GuestStream 024.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_050/Transcripts/Prose/gs050-1_ActInf GuestStream 050.1 ~ Becattini.m4a_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_050/Transcripts/Prose/gs050-1_ActInf GuestStream 050.1 ~ Becattini.m4a_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_055/Transcripts/Prose/gs055-1_gs055-1 ~ Pang, Fornito Geometric constraints.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_055/Transcripts/Prose/gs055-1_gs055-1 ~ Pang, Fornito Geometric constraints.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_040/Transcripts/Prose/ActInf GuestStream 040.1 ~ Wanja Wiese ~ Could large language models be conscious_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_031/Transcripts/Prose/ActInf GuestStream 031 ~ Brett Kagan & Adeel Razi, 'Free Energy Principle & Active Inference in Synthetic Biological Intelligence'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_054/Transcripts/Prose/gs054-1_ActInf GuestStream 054.1 ~ Gomez-Emilsson.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_054/Transcripts/Prose/gs054-1_ActInf GuestStream 054.1 ~ Gomez-Emilsson.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_029/Transcripts/Prose/ActInf GuestStream #029 ~ Shanna Dobson, 'Making Up Our Minds'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_026/Transcripts/Prose/ActInf GuestStream #026 ~ Tamari & Fischer, 'From Users to SenseMakers and Stigmergic Annotation'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_046/Transcripts/Prose/gs046-1_gs046-1 ~ Denise Holt, Active Inference AI & the Spatial Web_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_046/Transcripts/Prose/gs046-1_gs046-1 ~ Denise Holt, Active Inference AI & the Spatial Web_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_034/Transcripts/Prose/ActInf GuestStream 034 _ Avel Guenin-Carlut _  Physics of Creation.pdf
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_034/Transcripts/Prose/ActInf GuestStream 034 _ Avel Guenin-Carlut _  Physics of Creation.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_049/Transcripts/Prose/gs049-1_ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_049/Transcripts/Prose/gs049-1_ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_030/Transcripts/Prose/ActInf GuestStream #030 ~ Kyrtin Atreides, 'The Human Governance Problem'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_018/Transcripts/Prose/ActInf GuestStream #018 (2022) ~ Robertson et al., 'The Literalist Fallacy & the Free Energy Principle'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_048/Transcripts/Prose/gs048-1_ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_048/Transcripts/Prose/gs048-1_ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_038/Transcripts/Prose/ActInf GuestStream 038.1 ~ Max Berg Oversampled and undersolved_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_014/Transcripts/Prose/ActInf GuestStream #014 (2022) ~ Bohlen, Esteves et al., 'Osteopathy and Mental Health'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_037/Transcripts/Prose/ActInf GuestStream 037.1 ~ Baba Brinkman.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_052/Transcripts/Prose/gs052-1_ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.m4a_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_052/Transcripts/Prose/gs052-1_ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.m4a_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_027/Transcripts/Prose/ActInf GuestStream #027 ~ John Vervaeke, 'Awakening from the Meaning Crisis'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_028/Transcripts/Prose/ActInf GuestStream #028 ~ Giovanni Rolla, 'Reconceiving rationality'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_022/Transcripts/Prose/ActInf GuestStream #022 (2022) ~ Anna Lembke, 'Dopamine Nation'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_017/Transcripts/Prose/ActInf GuestStream #017 (2022) ~ Mahault Albarracin, 'Epistemic Communities under Active Inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_039/Transcripts/Prose/gs039-1_ActInf GuestStream 039.1 ~ Sources of Richness.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_053/Transcripts/Prose/gs053-1_ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_053/Transcripts/Prose/gs053-1_ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_045/Transcripts/Prose/gs045-1_ActInf GuestStream 045.1 ~ Ramstead & Albarracin The inner screen model of consciousness_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/GuestStream/GuestStream_045/Transcripts/Prose/gs045-1_ActInf GuestStream 045.1 ~ Ramstead & Albarracin The inner screen model of consciousness_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Twitter Spaces/TwitterSpaces_002/Transcripts/Prose/Active Inference ~ Twitter Spaces 002 ~ 'Can Web3 survive without cognitive modeling'.odt
/mnt/md0/projects/ActiveInferenceJournal/Twitter Spaces/TwitterSpaces_001/Transcripts/Prose/Active Inference ~ Twitter spaces 001 ~ December 9th 2021.odt
/mnt/md0/projects/ActiveInferenceJournal/ReviewStream/End of 2022 Review/Transcripts/Prose/2022 Active Inference Livestream Review.pdf
/mnt/md0/projects/ActiveInferenceJournal/ReviewStream/End of 2022 Review/Transcripts/Prose/2022 Active Inference Livestream Review.odt
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/AcII_BookStream_001 ~ Khezri's 'Governing Continuous Transformation'.odt
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/Active Inference BookStream 001.010 ~  Governing Continuous Transformation_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/bs001_012_Active Inference BookStream 001.012 ~  Governing Continuous Transformation.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/AcII_BookStream_001 ~ Khezri's 'Governing Continuous Transformation'.pdf
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/Active Inference BookStream 001.09 ~  Governing Continuous Transformation_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_001/Transcripts/Prose/Active Inference BookStream 001.08 ~  Governing Continuous Transformation_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_002/Transcripts/Prose/bs002_02_Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_002/Transcripts/Prose/bs002_02_Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_002/Transcripts/Prose/bs002_0_Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/BookStream/BookStream_002/Transcripts/Prose/bs002_0_Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_035/Transcripts/Prose/ActInf Livestream 035 (2022) 'A Tale of Two Architectures'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_035/Transcripts/Prose/ActInf Livestream 035 (2022) 'A Tale of Two Architectures'.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_038/Transcripts/Prose/ActInf Livestream 038 ~ 'The evolution of brain architectures for predictive coding and ActInf'.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_038/Transcripts/Prose/ActInf Livestream 038 ~ 'The evolution of brain architectures for predictive coding and ActInf'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_036/Transcripts/Prose/ActInf Livestream 036 (2022) ~ 'Modelling ourselves'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_036/Transcripts/Prose/ActInf Livestream 036 (2022) ~ 'Modelling ourselves'.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_047/Transcripts/Prose/ActInf Livestream 047 ~ 'Enactive-Dynamic Social Cognition' & 'Active Inference and Abduction'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-2_Active Inference LiveStream 054.2 ~ Smithe, Compositional Account of the Bayesian Brain.m4a_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-0_Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain (Smithe).wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-0_Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain (Smithe).wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-1_ls054-1 Compositional Account of the Bayesian Brain (Smithe).wav.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-2_Active Inference LiveStream 054.2 ~ Smithe, Compositional Account of the Bayesian Brain.m4a_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_054/Transcripts/Prose/ls054-1_ls054-1 Compositional Account of the Bayesian Brain (Smithe).wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_045/Transcripts/Prose/ActInf Livestream 045 ~ 'The free energy principle made simpler but not too simple'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_050/Transcripts/Prose/ActInf Livestream #050 ~ 'Interoception as modeling, allostasis as control'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_037/Transcripts/Prose/ActInf Livestream 037 ~ 'Free Energy - A User's Guide'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_037/Transcripts/Prose/ActInf Livestream 037 ~ 'Free Energy - A User's Guide'.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_048/Transcripts/Prose/ActInf Livestream 048 ~ 'Communication as Socially Extended Active Inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_053/Transcripts/Prose/ls053-2_ls053-2_Friston, Manrique 'Snakes & Ladders' & 'To copy or not'.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_053/Transcripts/Prose/ls053-1_ls053-1_Friston, Manrique 'Snakes & Ladders' & 'To copy or not'.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_053/Transcripts/Prose/ls053-0_ActInf Livestream 053-0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_052/Transcripts/Prose/ActInf Livestream 052.2 ~ Geometric Methods for Sampling_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_052/Transcripts/Prose/ActInf Livestream 052.0 ~ Geometric Methods.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_052/Transcripts/Prose/ActInf Livestream 052.1 ~ Da Costa ~ Geometric Methods for Sampling.md
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_040/Transcripts/Prose/LiveStream_040.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_040/Transcripts/Prose/LiveStream_040.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_044/Transcripts/Prose/ActInf Livestream 044 ~ 'Therapeutic Alliance as Active Inference The Role of Therapeutic Touch'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_051/Transcripts/Prose/ActInf Livestream #051 ~ 'Canonical neural networks perform active inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_051/Transcripts/Prose/ActInf Livestream #051 ~ 'Canonical neural networks perform active inference'.pdf
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_039/Transcripts/Prose/ActInf Livestream 039 ~ 'Morphogenesis as Bayesian inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_042/Transcripts/Prose/ActInf Livestream 042 ~ 'Robot navigation as hierarchical active inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_043/Transcripts/Prose/ActInf Livestream 043 ~ 'Predictive Coding a Theoretical and Experimental Review'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_046/Transcripts/Prose/ActInf Livestream 046.0 ~ 'Active inference models do not contradict folk psychology'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_041/Transcripts/Prose/ActInf Livestream 041 ~ 'Extended active inference - Constructing predictive cognition beyond skulls'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_049/Transcripts/Prose/ActInf Livestream #049 ~ 'A Worked Example of the Bayesian Mechanics of Classical Objects'.odt
/mnt/md0/projects/ActiveInferenceJournal/Livestream/LiveStream_049/Transcripts/Prose/ActInf_Livestream_49_'A Worked Example of the Bayesian Mechanics of Classical Objects'.odt
/mnt/md0/projects/ActiveInferenceJournal/OrgStream/OrgStream_002/Transcripts/Prose/ActInf OrgStream 002 _ Eugene Leventhal.odt
/mnt/md0/projects/ActiveInferenceJournal/OrgStream/OrgStream_003/Transcripts/Prose/ActInf OrgStream #003.1.odt
/mnt/md0/projects/ActiveInferenceJournal/OrgStream/OrgStream_003/Transcripts/Prose/ActInf OrgStream #003.1.pdf
/mnt/md0/projects/ActiveInferenceJournal/OrgStream/OrgStream_001/Transcripts/Prose/ActInf OrgStream 001 _ Richard D. Bartlett.odt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_007/Transcripts/Prose/ActInf ModelStream 007 ~ Conor Heins & Daphne Demekas, 'pymdp'.odt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_006/Transcripts/Prose/ActInf ModelStream #006 ~ 'Branching Time Active Inference - the theory and its generality'.odt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_005/Transcripts/Prose/ActInf ModelStream #005 ~ 'Contrastive Active Inference'.odt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_008/Transcripts/Prose/mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_008/Transcripts/Prose/mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_009/Transcripts/Prose/mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_009/Transcripts/Prose/mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/ModelStream/ModelStream_009/Transcripts/Prose/mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference_transcripts.zip
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2022 Symposium on Robotics/Transcripts/Prose/2022 Applied Active Inference Symposium on Robotics.odt
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2022 Symposium on Robotics/Transcripts/Prose/2022 Applied Active Inference Symposium on Robotics.pdf
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2021 Symposium with Karl Friston/Transcripts/Prose/v2 - Karl Friston, Applied Active Inference Symposium, ActInfLab, June 21, 2021.pdf
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_08_Int1-Sess08-NynkeBoiten.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_04_Int1-Sess04-InesHipolito.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_05_Int1-Sess05-Aswin Paul.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_01_Int1-Sess01-AndreBastos.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_02_Int1-Sess02-KeithDuggar.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_07_Int1-Sess07-ShannaDobson.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval/Transcripts/Prose/3Symp_1_06_Int1-Sess06-TakuyaIsomura.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_01_Int2-Sess01-JeanFrancoisCloutier.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_06_3Symp_2_06.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_07_3Symp_2_07.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_05_3Symp_2_05.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_09_3Symp_2_09-Roundtable.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_03_3Symp_2_03.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_04_3Symp_2_04.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_02_3Symp_2_02.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval/Transcripts/Prose/3Symp_2_08_3Symp_2_08.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_015/Transcripts/Prose/ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 Chapter 6, part 2_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_015/Transcripts/Prose/ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 Chapter 6, part 2_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_002/Transcripts/Prose/AATxtBk_C01-02_ActInf Textbook Group ~ Cohort 1 ~ Meeting 2 Chapter 1_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_002/Transcripts/Prose/AATxtBk_C01-02_ActInf Textbook Group ~ Cohort 1 ~ Meeting 2 Chapter 1_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001/Transcripts/Prose/AATxtBk_C01-01_ActInf Textbook Group ~ Cohort 1 ~ Meeting 1 Onboarding.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001/Transcripts/Prose/AATxtBk_C01-01_ActInf Textbook Group ~ Cohort 1 ~ Meeting 1 Onboarding.m4a.sentences.csv_transcript.txt
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Prose/cFPIP-02W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 2.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Prose/cFPIP-02W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Prose/cFPIP-05L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Prose/cFPIP-05L_lGCSOxLTx0ADSPqI-qbiYtzaJGLqansa5nZ51Z2fXVE.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Prose/cFPIP-01W Physics as Information Processing ~ Ander Aguirre ~ Discussion 1.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Prose/cFPIP-01W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/cFPIP-01L_Physics as Information Processing  ~ Chris Fields ~ Lecture 1.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/cFPIP-01L.pdf
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/images
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/cFPIP-01L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Prose/cFPIP-02L_Physics as Information Processing  ~ Chris Fields ~ Lecture 2.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Prose/cFPIP-02L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Prose/cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Prose/cFPIP-06W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Prose/cFPIP-03L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Prose/cFPIP-03L_Physics as Information Processing  ~ Chris Fields ~ Lecture 3.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Course_overview/Transcripts/Prose/cFPIP-00_Physics as Information Processing by Chris Fields ~ Course overview.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Prose/cFPIP-03W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 3.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Prose/cFPIP-03W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Prose/cFPIP-04W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 4.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Prose/cFPIP-04W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Prose/cFPIP-06L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Prose/cFPIP-01L_Physics as Information Processing ~ Chris Fields ~ Lecture 6.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Prose/cFPIP-05W.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Prose/cFPIP-05W__jw7UOQnkPAQImExl_1b8wyN9FlAVTJNtVW73dqAqvM.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Prose/cFPIP-04L.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Prose/cFPIP-04L_Physics as Information Processing  ~ Chris Fields ~ Lecture 4.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Discussion/Transcripts/Prose/AIFSS-04D_Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Discussion/Transcripts/Prose/AIFSS-03D_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/NormsScripts_Lecture/Transcripts/Prose/AIFSS-02L_Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/Conclusion_Lecture/Transcripts/Prose/AIFSS-07D__CFu479uX_Dpl7Q96JdGGjkKi6oApOIKZM4YltI3bgI.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/SocialConstraints_Lecture/Transcripts/Prose/AIFSS-06L_Fi2TnamAj5zrT6SATPcBDEJ7gcPsqzx2FaRU4IDli2I.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Lecture/Transcripts/Prose/AIFSS-04L Semiotics and Semantics Lecture ~ Sganzerla.wav.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/Introduction_Lecture/Transcripts/Prose/AIFSS-01L_6EjIMXEBkcfaMf8_Fx9oH1QkjrulQf_ZPS_b7bZTCfw.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Discussion/Transcripts/Prose/AIFSS-02D_Basics of Active Inference Discussion ~ Ben White ~ Active Inference for the Social Sciences 2023-07-25.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Lecture/Transcripts/Prose/AIFSS-03L_Collective Behavior Lecture ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/SocialConstraints_Discussion/Transcripts/Prose/AIFSS-06D_ongHRUoNubAhK6QNBAtygHYVFOAI3deSq1qI2vJ5L0k.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Lecture/Transcripts/Prose/AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.sentences.csv_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/MorphStream/MorphStream_001/Transcripts/Prose/mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a_transcript.md
/mnt/md0/projects/ActiveInferenceJournal/MorphStream/MorphStream_001/Transcripts/Prose/mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a_transcript.txt
