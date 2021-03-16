from requests import get

def isCurrent(currentVersion:str, repo:str):
    request = get("https://api.github.com/repos/" + str(repo) + "/releases/latest") # Get web data
    data = request.json() # Load the data into a dictionary

    # Is valid repo
    try:
        if data["message"] == "Not Found": # Invalid
            raise Exception("Invalid repository")
    except:
        return None
    finally:
        # Try get latest version
        latestVersion = data["name"]
        # Return Data
        if latestVersion == currentVersion: 
            return True # Up to date
        else:
            return False # Out of date

def getCurrentRelease(repo:str):
    request = get("https://api.github.com/repos/" + str(repo) + "/releases/latest") # Get web data
    data = request.json() # Load the data into a dictionary

    # Is valid repo
    try:
        if data["message"] == "Not Found": # Invalid
            raise Exception("Invalid repository")
    except:
        return None
    finally:
        return data["name"]

def getReleaseAge(currentVersion:str, repo:str):
    request = get("https://api.github.com/repos/" + str(repo) + "/releases") # Get web data
    data = request.json() # Load the data into a dictionary
    age = 0

    for x in data:
        if str(x["name"]) == currentVersion:
            return age
        else:
            age += 1
