import base64

import requests

ENV_BASE = "https://api.lsk.lightspeed.app"  # or https://api.lsk.lightspeed.app
TOKEN_URL = f"{ENV_BASE}/oauth/token?"
# REFRESH_TOKEN = "37fde1cd-3daa-44ae-bfbb-d9af8978cbb4"

ACCESS_TOKEN = "9f6fe1e5-b154-453e-a11a-727fefdb60a8"
REFRESH_TOKEN = "ca44e6bf-1b53-4b69-9d8f-44fd6a756fdf"
CLIENT_ID = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
CLIENT_SECRET = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"

basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

# HEADERS = {"Authorization": f"Basic {basic}",
#            "Content-Type": "application/x-www-form-urlencoded",
#            "Accept": "application/json",
#            }
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

data = {
    "grant_type": "refresh_token",
    "refresh_token": REFRESH_TOKEN,
}


def refresh_access_token():
    # resp = requests.post(TOKEN_URL, headers=HEADERS, data=data, timeout=30)
    resp = requests.post(
        TOKEN_URL,
        auth=(CLIENT_ID, CLIENT_SECRET),
        headers=HEADERS,
        data=data,
        timeout=30
    )
    resp.raise_for_status()
    tokens = resp.json()

    access_token = tokens["access_token"]
    refresh_token = tokens["refresh_token"]  # usually rotates—store the new one
    print("refreshed access_token:", access_token)


if __name__ == '__main__':
    refresh_access_token()
