
"""
openphotos - a dead-simple CLI to download your full iCloud Photos library.

This is a thin, friendly wrapper around icloudpd (https://github.com/icloud-photos-downloader/icloud_photos_downloader).
All the actual iCloud/download logic lives in icloudpd - this tool just makes
running it a one-command, no-flags experience.
"""

import os
import shutil
import subprocess
import sys


def prompt(text, default=None):
    suffix = f" [{default}]" if default else ""
    value = input(f"{text}{suffix}: ").strip()
    return value or default


def check_icloudpd_installed():
    if shutil.which("icloudpd") is None:
        print("icloudpd isn't installed yet. Installing it now...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "icloudpd"]
        )
        if result.returncode != 0:
            print("\nCouldn't install icloudpd automatically.")
            print("Try installing it yourself with: pip install icloudpd")
            sys.exit(1)
        if shutil.which("icloudpd") is None:
            print("\nicloudpd installed, but isn't on your PATH yet.")
            print("Try opening a new terminal, or add ~/.local/bin to your PATH.")
            sys.exit(1)


def main():
    print("openphotos - download your iCloud Photos library\n")

    check_icloudpd_installed()

    email = prompt("Your iCloud email")
    if not email:
        print("An iCloud email is required.")
        sys.exit(1)

    folder_name = prompt("Folder name to save photos into", default="icloud_photos")
    destination = os.path.abspath(os.path.expanduser(f"~/{folder_name}"))

    os.makedirs(destination, exist_ok=True)

    print(f"\nSaving photos to: {destination}")
    print("You may be asked for your iCloud password and a 2FA code below.\n")

    try:
        subprocess.run(
            [
                "icloudpd",
                "--directory", destination,
                "--username", email,
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("\nicloudpd exited with an error. Scroll up for details.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopped. Run 'openphotos' again anytime to pick up where you left off.")
        sys.exit(0)

    print(f"\nDone. Your photos are in: {destination}")


if __name__ == "__main__":
    main()
