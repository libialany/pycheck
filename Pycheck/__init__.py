# Imports
from distutils.log import info
from requests import get

# Variables
REPO_PREFIX = "https://api.github.com/repos/"

# Exceptions
class Invalid_Repo(Exception):
    def __init__(self, repo):
        self.repo = repo
        super().__init__(
            "GitHub api could not find your repo or any releases (repo: " + repo + ")"
        )


# Functions
def is_current(current_version: str, repo: str) -> bool:
    version_data = get(REPO_PREFIX + str(repo) + "/releases/latest").json()

    if "message" in version_data.keys():
        # Is repo valid/does it contain releases
        if version_data["message"] == "Not Found":
            raise Invalid_Repo(repo)

    return version_data["tag_name"] == current_version


def get_release_age(current_version: str, repo: str) -> int:
    version_list = get(REPO_PREFIX + str(repo) + "/releases").json()  # Get version list

    age = 0

    for version in version_list:  # Loop through version list
        if str(version["tag_name"]) == current_version:
            return age
        age += 1


def get_current_release(repo: str):
    version_data = get(
        REPO_PREFIX + str(repo) + "/releases/latest"
    ).json()  # Get latest version data

    if "message" in version_data.keys():
        if version_data["message"] == "Not Found":  # Invalid Repo or no releases
            raise Invalid_Repo(repo)

    return Release(repo, version_data["tag_name"])


def get_releases(repo) -> list:
    list_o_versions = []
    version_list = get(REPO_PREFIX + str(repo) + "/releases/").json()

    if isinstance(version_list, dict):
        raise Invalid_Repo(repo)

    for version in version_list:
        list_o_versions.append(Release(repo, "", version))
    
    return list_o_versions


# Class
class Release:
    def __init__(self, repo: str, tag_name: str, info_override: dict = None):
        self.repo: str = repo

        if info_override is None:
            version_list = get(REPO_PREFIX + str(self.repo) + "/releases/").json()

            if isinstance(version_list, dict):
                raise Invalid_Repo(repo)

            for version in version_list:
                if version["tag_name"] == tag_name:
                    self.info = version

            self.tag_name: str = tag_name

        else:
            self.info = info_override
            self.tag_name: str = self.info["tag_name"]

        self.name: str = self.info["name"]
        self.age: int = get_release_age(self.info["tag_name"], self.repo)
        self.is_latest: bool = not bool(self.age)
