
ENV_BASE = "https://api.lsk.lightspeed.app"  # or https://api.lsk.lightspeed.app
TOKEN_URL = f"{ENV_BASE}/oauth/token"

ACCESS_TOKEN = "21f34811-79eb-4cc3-85bf-939d734e6b81"
REFRESH_TOKEN = "2373715e-10fe-4796-b8ca-8b93eb3af8df"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}",
           "Accept": "application/json",
           }

# {
#     "access_token": "21f34811-79eb-4cc3-85bf-939d734e6b81",
#     "token_type": "bearer",
#     "refresh_token": "2373715e-10fe-4796-b8ca-8b93eb3af8df",
#     "expires_in": 3599,
#     "scope": "financial-api"
# }