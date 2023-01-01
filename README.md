# Update-Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Version: 0.3.0](https://img.shields.io/badge/Version-V0.3.0-blue)

## Description

This module allows you to track, compare and view data about the releases from a GitHub Repository.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Changelog](#changelog)

## Installation

Currently, this module is not available through PyPI so you must clone the repo and drag the pycheck folder into your project directory.

## Usage

```
# Imports
import pycheck

# Variables
REPO: str = "example/example"
VERSION: str = "V0.1.0"

# Functions
is_current: bool = pycheck.is_current(VERSION, REPO)
age:int = pycheck.get_release_age(VERSION, REPO)

# Functions that return a release object
release = pycheck.get_current_release(REPO)
releases_list: list = pycheck.get_releases(REPO) # Returns a list of all releases

# The following is a list of variables that
# can be accessed through the release object

release.info: dict
release.tag_name: str
release.name: str
release.age: int
release.is_latest: bool

releases_list: list = pycheck.get_releases(REPO) # Returns a list of all releases

# Release(repo: str, tag_name: str, info_override: dict = None)
# Note that info_override allows you to pass the
# info of a release directly into the object
release_2 = Release(REPO, VERSION)

```

example:

on CLI:

`export git_key=gh..`

create a script main.py on root folder.

```
from Pycheck import is_current,get_release_age,get_current_release,get_releases
print('is_current>\n',is_current('v22.03.2','openwrt/openwrt'))
print('get_release_age>\n',get_release_age('v21.02.3','openwrt/openwrt'))
print('get_current_release>\n',get_current_release('openwrt/openwrt'))
print('get_releases>\n',get_releases('openwrt/openwrt'))
```

run:
`python3 main.py`

## Changelog

### V1.0.0

- Added ability to get all info from a release
- Info can now be accessed from a Class
- Optimised functions
- Added better exception handling

### V0.3.1

- Make the module more pythonic
- Use snake case

### V0.3.0

- Removed ability to send notifications
- Optimised Process
- Renamed functions
- You can now get the release age

### V0.2.0

- Added macOS support for notifications
- Added a new function to get the current version

### V0.1.0

- Can now check the local version against GitHub release name
- Added ability to notify

## License

pycheck is shared under the [MIT license](https://github.com/ThomasLandstra/PyReleaseCheck/blob/main/licence).
