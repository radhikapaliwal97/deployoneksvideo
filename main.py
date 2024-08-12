import argparse
from collections import namedtuple

Args = namedtuple("Args", "asset_id, timestamp")


def main():
    asset_id, timestamp = handle_command_line_arguments()

    # implementation from here


def handle_command_line_arguments() -> Args:
    parser = argparse.ArgumentParser("thumbnail_exercise")
    parser.add_argument(
        "asset_id", help="An asset id for metadata and video asset retrieval.", type=str
    )
    parser.add_argument(
        "timestamp",
        help="Timestamp to grab a thumbnail from the video asset.",
        type=str,
    )
    args = parser.parse_args()

    print("Asset id: " + args.asset_id)
    print("Timestamp: " + args.timestamp)

    return Args(asset_id=args.asset_id, timestamp=args.timestamp)


if __name__ == "__main__":
    main()
