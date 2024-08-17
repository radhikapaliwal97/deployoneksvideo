import argparse
import os
import requests
from constants import BASE_URL
from utils import create_thumbnail
from typing import NamedTuple, Dict, Optional

# Define Args as a NamedTuple
class Args(NamedTuple):
    asset_id: str
    timestamp: str


def main() -> None:
    """Main function to handle command line arguments and process video files."""
    args: Args = handle_command_line_arguments()
    print("argsargsargsargs", args)

    video_path: str = f"video/{args.asset_id}.mov"   # This is the path of video
    thumbnail_path: str = f"thumbnail/{args.asset_id}.png" # This is the path of thubnail where it stored

    if os.path.exists(video_path):
        print("i exist")
        create_thumbnail(video_path, thumbnail_path, args.asset_id, args.timestamp)
    else:
        print("i don't exist")
        response: requests.Response = requests.get(
            f"{BASE_URL}/playground/{args.asset_id}", allow_redirects=True
        )
        content_type: Optional[str] = response.headers.get("Content-Type")

        content_type_to_extension: Dict[str, str] = {
            "video/quicktime": "mov",
            "video/mpeg": "mp4",
        }

        if content_type not in content_type_to_extension:
            raise ValueError(f"Unsupported content type: {content_type}")

        extension: str = content_type_to_extension[content_type]
        video_file_path: str = f"video/{args.asset_id}.{extension}"

        with open(video_file_path, "wb") as f:
            f.write(response.content)

        create_thumbnail(video_file_path, thumbnail_path, args.asset_id, args.timestamp)


def handle_command_line_arguments() -> Args:
    """Handle command line arguments and return them as an Args namedtuple."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser("thumbnail_exercise")
    parser.add_argument(
        "asset_id", help="An asset id for metadata and video asset retrieval.", type=str
    )
    parser.add_argument(
        "timestamp",
        help="Timestamp to grab a thumbnail from the video asset.",
        type=str,
    )
    args: argparse.Namespace = parser.parse_args()
    return Args(asset_id=args.asset_id, timestamp=args.timestamp)


if __name__ == "__main__":
    main()
