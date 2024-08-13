from PIL import Image, ImageChops
import os
from utils import create_thumbnail, check_corrupted  


def test_thumbnail_comparison() -> None:
    """Test the comparison of generated and expected thumbnails."""
    asset_id: str = "test_video"
    timestamp: str = "00:00:00"
    video_path: str = "video/test_video.mp4"

    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    video_file_path: str = os.path.join(base_dir, video_path)

    if not os.path.exists(video_file_path):
        raise FileNotFoundError(f"Video file not found at {video_file_path}")

    thumbnail_path: str = os.path.join(base_dir, "thumbnail", f"{asset_id}.png")

    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)

    create_thumbnail(
        video_file_path, thumbnail_path, asset_id, timestamp, skip_checksum=True
    )

    generated_thumbnail_path: str = os.path.join(
        base_dir, "thumbnail", "test_video.png"
    )
    expected_thumbnail_path: str = os.path.join(base_dir, "video", "test_thumbnail.png")

    if not os.path.exists(expected_thumbnail_path):
        raise FileNotFoundError(
            f"Expected thumbnail file not found at {expected_thumbnail_path}"
        )

    generated_thumbnail: Image.Image = Image.open(generated_thumbnail_path)
    expected_thumbnail: Image.Image = Image.open(expected_thumbnail_path)

    diff: Image.Image = ImageChops.difference(generated_thumbnail, expected_thumbnail)

    assert (
        not diff.getbbox()
    ), "The generated thumbnail does not match the expected thumbnail."


def test_corrupted_video() -> None:
    """Test the comparison of generated and expected thumbnails."""
    asset_id: str = "invalid"
    video_path: str = "video/invalid.mov"  
    result = check_corrupted(video_path, asset_id) 
    assert result is False


def test_not_corrupted_video() -> None:
    """Test the comparison of generated and expected thumbnails."""
    asset_id: str = "valid"
    video_path: str = "video/valid.mov"   
    result = check_corrupted(video_path, asset_id) 
    assert result is True

    

    