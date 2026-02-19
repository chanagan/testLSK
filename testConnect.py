import base64
import requests

# Replace these with your credentials from Lightspeed Developer Portal
client_id = "devp-prod-hildenboroughhotelslimitedincislandhousekeywest57861-d012acc1f3b07f995edde92132b1845d"
client_secret = "nwsec-fca5e6d1cc93aef4b3cf66a7dfbed70afa297c79823580816917cd09c3027c4915015e7f5f161226c37b86c7bb2e706b0c3e2045a36c9dc7c9294c20fa0063ce"
authorization_code = "Y4Gxli"
redirect_uri = "https://localhost"

# Base64 encode client_id:client_secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

token_url = "https://api.lsk.lightspeed.app/oauth/token"

payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

headers = {
    "Authorization": f"Basic {b64_auth_str}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(token_url, data=payload, headers=headers)
response_data = response.json()

access_token = response_data.get("access_token")
refresh_token = response_data.get("refresh_token")

print("Access token:", access_token)
print("Refresh token:", refresh_token)
