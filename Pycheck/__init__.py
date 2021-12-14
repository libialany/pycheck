# Imports
from requests import get


def is_current(current_version: str, repo: str):
    version_data = get(
        "https://api.github.com/repos/" + str(repo) + "/releases/latest"
    ).json()  # Get latest version data

    if "message" in version_data.keys():
        if version_data["message"] == "Not Found":  # Invalid Repo or no releases
            raise Exception("Invalid repository")

    return version_data["name"] == current_version


def get_current_release(repo: str):
    version_data = get(
        "https://api.github.com/repos/" + str(repo) + "/releases/latest"
    ).json()  # Get latest version data

    if "message" in version_data.keys():
        if version_data["message"] == "Not Found":  # Invalid Repo or no releases
            raise Exception("Invalid repository")

    return version_data["name"]


def get_release_age(currentVersion: str, repo: str):
    version_list = get(
        "https://api.github.com/repos/" + str(repo) + "/releases"
    ).json()  # Get version list

    age = 0

    for version in version_list:  # Loop through version list
        if str(version["name"]) == currentVersion:
            return age
        age += 1
