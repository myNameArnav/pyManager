from util import getOS

import requests
import re


def getSortedPythonVersions():
    response = requests.get("https://www.python.org/ftp/python/")
    versions = re.findall(r'<a href="([\d\.]+)/">', response.text)
    versions.pop(0)

    def versionKey(version):
        return tuple(map(int, version.split(".")))

    sortedVersions = sorted(versions, key=versionKey)
    return sortedVersions

def createDownloadURL(version):
    os, arch = getOS()
    baseURL = f"https://www.python.org/ftp/python/{version}/"
    if os == "Windows":
        ext = ".exe"
        installer = f"python-{version}{ext}"
    elif os == "Linux":
        ext = ".tgz"
        installer = f"Python-{version}{ext}"
    elif os == "Darwin": # macOS
        ext = ".pkg"
        installer = f"python-{version}-{arch}{ext}"
    else:
        raise ValueError("Unsupported OS")
    return baseURL + installer, ext

def downloadInstaller(url, savePath):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(savePath, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)