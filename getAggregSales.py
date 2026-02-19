import requests

# ---- CONFIG ----
ENV_BASE = "https://api.lsk.lightspeed.app"  # or https://api.lsk.lightspeed.app
BUS_LOC_ID = "994053000790018"
GROUP_BY = "accountingGroup"
REPORT_ID = "aggregatedSales"

ACCESS_TOKEN = "d6eefc18-4577-45e8-93ff-22b9a5d4e2f7"
REFRESH_TOKEN = "282e192c-d401-405f-b841-0e2e20614983"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}",
           "Accept": "application/json",
           }
URL = f"{ENV_BASE}/f/finance/{BUS_LOC_ID}/{REPORT_ID}"
PARAMS = {
    "groupBy": GROUP_BY,
    "date": "date",
}
def get_daily_totals():
    repDate = "2025-02-18"

    PARAMS["date"] = repDate
    response = requests.get(
        url=URL, params=PARAMS, headers=HEADERS
    )
    response.raise_for_status()
    data = response.json()
    print(data)


if __name__ == '__main__':
    get_daily_totals()
#
# CLIENT_ID = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
# CLIENT_SECRET = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"
# REDIRECT_URI = "https://localhost"
# SCOPES = ["financial-api"]  # change to what you need
# STATE = "dev-state-123"
# ---------------
