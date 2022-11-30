from waybackpy import WaybackMachineCDXServerAPI

import os
import re
import sys
from pathlib import Path
import requests


user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"

def download_files(url):
    cdx = WaybackMachineCDXServerAPI(url, user_agent)

    targetdir = Path(url.replace('/', '_'))

    os.makedirs(targetdir, exist_ok=True)


    for item in cdx.snapshots():
        url = item.archive_url
        fpath = targetdir / f"{item.timestamp}.snapshot"
        if not os.path.exists(fpath):
            print(f"Downloading {item}")
            response = requests.get(url)
            with open(fpath, "wb") as f:
                f.write(response.content)
        else:
            print(f'Reusing file for snapshot {item.timestamp}')

re_user = re.compile(r"UserDownloads:([0-9,\+]+)")

def print_numbers(url):
    targetdir = Path(url.replace('/', '_'))
    for f in os.scandir(targetdir):
        if f.is_dir():
            continue
        date = f.name.rstrip(".snapshot")
        with open(f) as f:
            for m in re_user.findall(f.read()):
                if m is None:
                    print(date, "-")
                    continue
                # print(m)
                users = m.replace(',', '')
                print(date, users)

if __name__ == '__main__':
    url = "https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb"
    if len(sys.argv) > 1:
        url = sys.argv[1]

    download_files(url)
    print_numbers(url)
