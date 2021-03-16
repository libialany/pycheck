# Update-Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Version: 0.2.0](https://img.shields.io/badge/Version-V0.2.0-blue)

## Description

This module allows you to check if the most recent release from a github repo is newer than the version localy on the users PC.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Changelog](#changelog)

## Installation
Currently this module is not available through pypi so you must clone the repo and drag the Pycheck.py file into your project directory. You will also require the beautifulsoup4 module and the win10toast module.

## Usage
To use this module we first need to import the module into our python project.

```py
import pyceck
```

<br/>

Once we have the module imported we can use the isCurrent function to check if there is a new version of the program available based on the name of the most recent github release. In this example the rep (Example/ExampleRepo) has a new version available.

```py
version = "0.1.0" # Current Version of program
repo = "Example/ExampleRepo" # The owner of the repo/the name of the repo

print(pycheck.isCurrent(version, repo))
# Will return False as a bool
```

<br/>
We can also get the name of the latest release.

```py

print(pycheck.getCurrentRelease(repo))
# Will return "0.2.0" as a string.
```

<br/>
We can also get the age of the release. That being the number of new releases since the local version was released.

```py

print(pycheck.getReleaseAge(version, repo))
# Will return 3" as an integer.
```

## Changelog
### V0.3.0
- Removed ability to send notifications
- Optimised Process
- Renamed functions
- You can now get the release age


### V0.2.0
- Added macOS support for notifications
- Added new function to get current version

### V0.1.0
- Can now check local version against github release name
- Added ability to notify
