1. Get Your Coda API Token
Go to https://coda.io/account, scroll to "API settings," and generate an API token.
     - Store this token securely.

2. List Table Rows With the API

```bash
cd /data/input/
curl -X GET "https://coda.io/apis/v1/docs/dTwB_SP81yq/tables/grid-cjvFiXp3a3/rows?useColumnNames=true" \
  -H "Authorization: Bearer <YOUR_API_TOKEN>" \
  >livestream_fulldata_table.json
```

## TODO:

3. Convert The JSON to CSV
The API response is JSON. Each row has a values object mapping column names to values.
