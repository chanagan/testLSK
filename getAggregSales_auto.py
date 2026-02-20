from lsk_tokens import get_access_token, refresh_lsk_tokens
from token_store import load_tokens
import requests

CLIENT_ID = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
CLIENT_SECRET = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"

# ---- CONFIG ----
ENV_BASE = "https://api.lsk.lightspeed.app"  # or https://api.lsk.lightspeed.app
BUS_LOC_ID = "994053000790018"
GROUP_BY = "accountingGroup"
REPORT_ID = "aggregatedSales"

ACCESS_TOKEN = "e8ffc37c-d95c-478f-81d7-4bece0582ab3"
REFRESH_TOKEN = "98b63e4d-7a9a-4b9a-a495-4d33ebe55dbf"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}",
           "Accept": "application/json",
           }
URL = f"{ENV_BASE}/f/finance/{BUS_LOC_ID}/{REPORT_ID}"
PARAMS = {
    "groupBy": GROUP_BY,
    "date": "date",
}
def get_daily_totals():
    repDate = "2025-02-19"
    token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    # token = "a3d6bfca-2882-4dc9-914e-24e5324a4d39"
    PARAMS["date"] = repDate
    response = requests.get(
        url=URL, params=PARAMS, headers={"Authorization":f"Bearer {token}",}
    )
    response.raise_for_status()
    data = response.json()
    print(data)

def refresh_token_file():
    tokens = load_tokens()
    refresh_token = tokens.get("refresh_token")
    payload = refresh_lsk_tokens(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        refresh_token=refresh_token,
    )
    print (payload)

if __name__ == '__main__':
    get_daily_totals()
    # refresh_token_file()
#
# CLIENT_ID = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
# CLIENT_SECRET = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"
# REDIRECT_URI = "https://localhost"
# SCOPES = ["financial-api"]  # change to what you need
# STATE = "dev-state-123"
# ---------------
