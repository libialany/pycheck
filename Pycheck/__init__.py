from requests import get


def isCurrent(currentVersion: str, repo: str):
    data = get(
        "https://api.github.com/repos/" + str(repo) + "/releases/latest"
    ).json()  # Get latest version data

    try:  # Is valid repo
        if data["message"] == "Not Found":  # Invalid
            raise Exception("Invalid repository")
    except:
        return None
    finally:
        # Try get latest version
        latestVersion = data["name"]
        # Return Data
        if latestVersion == currentVersion:
            return True  # Up to date
        else:
            return False  # Out of date


def getCurrentRelease(repo: str):
    data = get(
        "https://api.github.com/repos/" + str(repo) + "/releases/latest"
    ).json()  # Get latest version data

    try:  # Is valid repo
        if data["message"] == "Not Found":  # Invalid Repo
            raise Exception("Invalid repository")
    except:
        return None
    finally:
        return data["name"]


def getReleaseAge(currentVersion: str, repo: str):
    data = get(
        "https://api.github.com/repos/" + str(repo) + "/releases"
    ).json()  # Get version list

    age = 0

    for x in data:  # Loop through version list
        if str(x["name"]) == currentVersion:
            return age
        else:
            age += 1
