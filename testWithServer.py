# pip install flask requests
from flask import Flask, request
import threading
import webbrowser
from urllib.parse import urlencode
import base64
import requests

# ---- CONFIG ----
ENV_BASE = "https://api.lsk.lightspeed.app"  # or https://api.lsk.lightspeed.app
CLIENT_ID = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
CLIENT_SECRET = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"
REDIRECT_URI = "https://localhost"
SCOPES = ["financial-api"]  # change to what you need
STATE = "dev-state-123"
# ---------------

AUTHORIZE_URL = f"{ENV_BASE}/oauth/authorize"
TOKEN_URL = f"{ENV_BASE}/oauth/token"

app = Flask(__name__)
captured = {}

@app.get("/callback")
def callback():
    captured["code"] = request.args.get("code")
    captured["state"] = request.args.get("state")
    return "Authorization received. You can close this tab."

def run_server():
    # app.run(host="localhost", ssl_context="adhoc", debug=False)
    app.run(host="localhost", ssl_context="adhoc", debug=False)
#

# # Start local server
# threading.Thread(target=run_server, daemon=True).start()
# print(f"Listening on {REDIRECT_URI}")
#
# # Open browser to authorize
# params = {
#     "response_type": "code",
#     "client_id": CLIENT_ID,
#     "redirect_uri": REDIRECT_URI,
#     "scope": " ".join(SCOPES),
#     # "state": STATE,
# }
# auth_url = f"{AUTHORIZE_URL}?{urlencode(params)}"
# print("Open (or it will auto-open):", auth_url)
# webbrowser.open(auth_url)
#
# # Wait for code (simple busy wait)
# print("Waiting for authorization code...")
# while "code" not in captured:
#     pass
#
# code = captured["code"]
code = "4oruXG"
print("Got code:", code)

# Exchange code for tokens
basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
headers = {
    "Authorization": f"Basic {basic}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}
data = {"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI}

resp = requests.post(TOKEN_URL, headers=headers, data=data, timeout=30)
resp.raise_for_status()
tokens = resp.json()

print("Access token:", tokens["access_token"])
print("Refresh token:", tokens.get("refresh_token"))


#