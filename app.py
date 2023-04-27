from pyVersions import getSortedPythonVersions, createDownloadURL, downloadInstaller
import os
sortedVersions = getSortedPythonVersions()
print(sortedVersions)

selectedVersion = input("Select Python Version: ")

if selectedVersion not in sortedVersions:
    raise ValueError(f"Invalid version {selectedVersion}")

url, ext = createDownloadURL(selectedVersion)

savePath = os.path.join("pythonFiles", f"python-{selectedVersion}{ext}")

downloadInstaller(url, savePath)