import requests
from pathlib import Path


def download_to_local(url: str, out_path: Path, parent_mkdir: bool=True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib.Path object")
    if parent_mkdir:
        out_path.mkdir(parents=True, exist_ok=True)
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        # Write the file out binary mode to prevent any newline conversions
        out_path.write_bytes(r.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False
