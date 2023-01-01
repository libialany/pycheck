"""

This module allows you to track, compare and view data about the releases from a GitHub Repository.

Copyright (c) 2022 Thomas Landstra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""

# Imports
from requests import get
import os

# Variables
REPO_PREFIX = "https://api.github.com/repos/"
TOKEN = os.environ.get("git_key")


# Exceptions
class Invalid_Repo(Exception):
    """An Excepption raised when GitHub couldn't find any repo or released for that repo.

    Args:
        repo (str): The respository name and its owner on GitHub - "ThomasLandstra/pycheck".
    """

    def __init__(self, repo: str):
        self.repo = repo
        super().__init__(
            f"GitHub api could not find your repo or couldn't find any releases (repo: {repo} )"
        )


# Functions
def is_current(current_version: str, repo: str) -> bool:
    """Checks to see if the current reported version is the most up to date version.

    Args:
        current_version (str): The current version's tag.
        repo (str): The GitHub Repository to be checked.

    Raises:
        Invalid_Repo: The GitHub Repository was invalid or there are no releases for the repository.

    Returns:
        bool: True if current version is up to date.
    """

    version_data = get(
        f"{REPO_PREFIX}{repo}/releases/latest", headers={"Authorization": TOKEN}
    ).json()

    if "message" in version_data.keys():
        # Is repo valid/does it contain releases
        if version_data["message"] == "Not Found":
            raise Invalid_Repo(repo)

    return version_data["tag_name"] == current_version


def get_release_age(current_version: str, repo: str) -> int:
    """Return how many releases since the reported current verion.

    Args:
        current_version (str): The current version's tag.
        repo (str): The GitHub Repository to be checked.

    Returns:
        int: How many versions have been released since the reported version.
    """
    version_list = get(
        f"{REPO_PREFIX}{repo}/releases", headers={"Authorization": TOKEN}
    ).json()  # Get version list

    age = 0

    for version in version_list:  # Loop through version list
        if str(version["tag_name"]) == current_version:
            return age
        age += 1


def get_current_release(repo: str):
    """Get the tag of the latest release.

    Args:
        repo (str): The GitHub Repository to be checked.

    Raises:
        Invalid_Repo: The GitHub Repository was invalid or there are no releases for the repository.

    Returns:
        Release: An object used to interact with data about the GitHub release.
    """
    data = get(
        f"{REPO_PREFIX}{repo}/releases/latest", headers={"Authorization": TOKEN}
    ).json()  # Get latest version data

    if "message" in data.keys():
        if data["message"] == "Not Found":  # Invalid Repo or no releases
            raise Invalid_Repo(repo)

    return Release(repo, "", data)


def get_releases(repo) -> list:
    """Returns a list of releases in the form of Release objects.

    Args:
        repo (str): The GitHub Repository to be checked.

    Raises:
        Invalid_Repo: The GitHub Repository was invalid or there are no releases for the repository.

    Returns:
        list: A list of Release objects used to interact with data about the GitHub releases.
    """
    list_o_versions = []
    version_list = get(
        f"{REPO_PREFIX}{repo}/releases", headers={"Authorization": TOKEN}
    ).json()

    if isinstance(version_list, dict):
        raise Invalid_Repo(repo)

    for version in version_list:
        list_o_versions.append(Release(repo, "", version))

    return list_o_versions


# Class
class Release:
    """An object used to interact with data about the GitHub release.

    Args:
        repo (str): The GitHub Repository to be checked.
        tag_name (str): The tag of the GitHub release.
        info_override (dict, optional): If the data has already been fetched, set this to that data for performance. Defaults to None.

    Raises:
        Invalid_Repo: The GitHub Repository was invalid or there are no releases for the repository.
    """

    def __init__(self, repo: str, tag_name: str, info_override: dict = None):
        self.repo: str = repo

        if info_override is None:
            version_list = get(
                f"{REPO_PREFIX}{repo}/releases", headers={"Authorization": TOKEN}
            ).json()

            if isinstance(version_list, dict):
                raise Invalid_Repo(repo)

            for version in version_list:
                if version["tag_name"] == tag_name:
                    self.info: dict = version

            self.tag_name: str = tag_name

        else:
            self.info: dict = info_override
            self.tag_name: str = self.info["tag_name"]

        self.name: str = self.info["name"]
        self.age: int = get_release_age(self.info["tag_name"], self.repo)
        self.is_latest: bool = not bool(self.age)

    def __str__(self):
        return f"Release name is {self.name} and age sinde the latest version is {self.age} and tag_name is {self.tag_name}"
