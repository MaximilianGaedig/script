#!/usr/bin/env python3

from argparse import ArgumentParser
from os import path
from zipfile import ZipFile

parser = ArgumentParser(description="Generate update server metadata")
parser.add_argument("zip")

zip_path = parser.parse_args().zip

with ZipFile(zip_path) as f:
    with f.open("META-INF/com/android/metadata") as metadata:
        data = dict(line[:-1].decode().split("=") for line in metadata)        
        for channel in ("beta", "stable", "testing"):
            with open(path.join(path.dirname(zip_path), data["pre-device"] + "-" + channel), "w") as output:
                build_id = data["post-build"].split("/")[3]
                # fix fingerprint spoofing
                incremental = data["post-build"].split("/")[4].split(":")[0]
                print(data["post-build-incremental"], data["post-timestamp"], build_id, channel,file=output)