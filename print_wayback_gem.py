import os
import re
from pathlib import Path

re_user = re.compile(r"UserDownloads:([0-9,\+]+)")

for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    for file in filter(lambda x: x.endswith('.html'), files):
        f = Path(root) / file
        date = Path(f).parents[4].name
        with open(f) as f:
            for m in re_user.findall(f.read()):
                if m is None:
                    print(date, "-")
                    continue
                # print(m)
                users = m.replace(',', '')
                print(date, users)
