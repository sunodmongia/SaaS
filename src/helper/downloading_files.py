import requests
from pathlib import Path


def download_file(url: str, dest_path: Path, parent_mkdir: bool = True):
    if not isinstance(dest_path, Path):
        raise ValueError(f"{dest_path} must be a Path object")

    if parent_mkdir:
        dest_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        dest_path.write_bytes(response.content)
        return True
    
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False