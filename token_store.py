import json, os, tempfile
from pathlib import Path
from typing import Any, Dict

TOKEN_PATH = Path(__file__).with_name("tokens.json")

def load_tokens() -> Dict[str, Any]:
    if not TOKEN_PATH.exists():
        return {}
    return json.loads(TOKEN_PATH.read_text(encoding="utf-8"))

def save_tokens(tokens: Dict[str, Any]) -> None:
    TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)

    fd, tmp = tempfile.mkstemp(dir=str(TOKEN_PATH.parent), prefix=TOKEN_PATH.name, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(tokens, f, indent=2, sort_keys=True)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, TOKEN_PATH)  # atomic replace
    finally:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except OSError:
            pass
