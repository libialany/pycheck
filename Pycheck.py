from bs4 import BeautifulSoup
from requests import get
from win10toast import ToastNotifier
import threading, os

def isCurrent(currentVersion:str, repo:str, notify:bool = False, notifyDuration:int = 5):
    def notifyC(title, msg, dur, nVer):
        # The notifier function
        if os.name == "nt":
            ToastNotifier().show_toast(title, msg, duration=dur)
        else:
            t = '-title {!r}'.format(title)
            s = '-subtitle {!r}'.format(nVer)
            m = '-message {!r}'.format(msg)
            os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

    repo = "https://api.github.com/repos/"+ str(repo) + "/releases/latest" # create link adress
    request = get(repo) # Get web data
    data = str(BeautifulSoup(request.text, "html.parser")).split(",") # Get data from github

    # Is valid repo
    if data[0] == '{"message":"Not Found"': # Invalid
        raise Exception("Invalid repository")

    # Get latest version
    latestVersion = None
    for x in data:
        if x.split('"')[1] == "name": # if name of latest update
            latestVersion = x.split('"')[4] # latestVersion = update name
            
    # Return Data
    if latestVersion == None: # If no version was scraped
        raise Exception("Failed to get latest version")
    elif latestVersion == currentVersion: 
        return True # Up to date
    else:
        if notify:
            threading.Thread(target=notifyC, args=("Update Available", "You are on: " + currentVersion + "| Version Available: " + latestVersion, notifyDuration, latestVersion)).start()
        return False # Out of date

def getCurrentVersion(repo:str):
    repo = "https://api.github.com/repos/"+ str(repo) + "/releases/latest" # create link adress
    request = get(repo) # Get web data
    data = str(BeautifulSoup(request.text, "html.parser")).split(",") # Get data from github

    # Is valid repo
    if data[0] == '{"message":"Not Found"': # Invalid
        raise Exception("Invalid repository")

    # Get latest version
    for x in data:
        if x.split('"')[1] == "name": # if name of latest update
            return x.split('"')[4] # latestVersion = update name

