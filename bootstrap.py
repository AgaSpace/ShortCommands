import subprocess
import os
import sys
from pathlib import Path
import urllib.request
import zipfile
import io
import shutil
import shlex
import re
from typing import Optional, Union, Collection, Set

OptionalPath = Union[None, Path, str]


def download_tshock(url=r"https://github.com/Pryaxis/TShock/releases/download/v4.4.0-pre11/TShock4.4.0_Pre11_Terraria1.4.0.5.zip", dest: OptionalPath=None):
    if dest is None:
        dest = "./TShock"
    dest: Path = Path(dest)
    with urllib.request.urlopen(url) as response:
        buff = io.BytesIO()
        shutil.copyfileobj(response, buff)
        buff.seek(0)
        with zipfile.ZipFile(buff) as zf:
            dest.mkdir(exist_ok=True)
            zf.extractall(dest)

if __name__ == "__main__":
    download_tshock()
