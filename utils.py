import hashlib
import requests
import ffmpeg
from constants import BASE_URL
from typing import Dict, Any


def calculate_checksum(file_path: str, hash_algorithm: str = "sha256") -> str:
    """Calculate the checksum of a file."""
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def check_corrupted(
    video_path: str, asset_id: str, skip_checksum: bool = False
) -> bool:
    """Check if the video file is corrupted by comparing checksums."""
    if skip_checksum:
        return True

    checksum_sha256 = calculate_checksum(video_path, "sha256")
    checksum_md5 = calculate_checksum(video_path, "md5")
    checksum_sha1 = calculate_checksum(video_path, "sha1")

    response = requests.get(f"{BASE_URL}/playground/{asset_id}/metadata")
    correct_checksum: Dict[str, Any] = response.json()

    correct_sha256 = correct_checksum.get("sha256")
    correct_md5 = correct_checksum.get("md5")
    correct_sha1 = correct_checksum.get("sha1")

    if (
        (correct_sha1 == checksum_sha1)
        and (correct_sha256 == checksum_sha256)
        and (correct_md5 == checksum_md5)
    ):
        return True
    return False


def create_thumbnail(
    video_path: str,
    thumbnail_path: str,
    asset_id: str,
    timestamp: str,
    skip_checksum: bool = False,
) -> None:
    """Create a thumbnail from a video file if it is not corrupted."""
    if check_corrupted(video_path, asset_id, skip_checksum):
        (
            ffmpeg.input(video_path, ss=timestamp)
            .output(thumbnail_path, vframes=1)
            .overwrite_output()
            .run()
        )
        print(f"Your thumbnail saved at {thumbnail_path}")
    else:
        print("Invalid / Corrupted File.")
