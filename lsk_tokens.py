import time
import base64
import requests
from typing import Dict, Any

from token_store import load_tokens, save_tokens

TOKEN_URL_PROD = "https://api.lsk.lightspeed.app/oauth/token"
SKEW_SECONDS = 60  # refresh 1 minute early

def _basic_auth_header(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")

def refresh_lsk_tokens(
    client_id: str,
    client_secret: str,
    refresh_token: str,
    token_url: str = TOKEN_URL_PROD,
    timeout: float = 20.0,
) -> Dict[str, Any]:
    headers = {
        "Authorization": _basic_auth_header(client_id, client_secret),
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    r = requests.post(token_url, headers=headers, data=data, timeout=timeout)
    r.raise_for_status()
    payload = r.json()

    # store an absolute expiry timestamp for convenience
    payload["expires_at"] = int(time.time()) + int(payload.get("expires_in", 3600))
    return payload

def get_access_token(client_id: str, client_secret: str) -> str:
    tokens = load_tokens()

    access = tokens.get("access_token")
    expires_at = int(tokens.get("expires_at", 0))
    if access and expires_at > int(time.time()) + SKEW_SECONDS:
        return access

    rt = tokens.get("refresh_token")
    if not rt:
        raise RuntimeError("No refresh_token found in tokens.json (need initial auth once).")

    new_tokens = refresh_lsk_tokens(client_id, client_secret, rt)

    # LSK returns a new refresh_token; always persist it.
    # If it ever doesn't, keep the old one.
    if "refresh_token" not in new_tokens:
        new_tokens["refresh_token"] = rt

    save_tokens(new_tokens)
    return new_tokens["access_token"]
