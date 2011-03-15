﻿# PyGithubApi README

PyGithubApi is a series of Python functions for interacting with the GitHub API.

## Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com][1]
* Homepage: [http://quandyfactory.com/projects/25/pygithubapi][2]
* Repository: [http://github.com/quandyfactory/PyGithubApi][3]

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html][4]

## This Version

* Version: 0.13
* Release Date: 2011-03-14

## Revision History

### Version: 0.13

* Release Date: 2011-03-14
* Changes:
    * Added `try ... except` around yaml import
        

### Version: 0.

* Release Date: 2009-09-28
* Changes:
    * Changed parameters for get_last_commit() from URL to user, repo.


### Version: 0.11

* Release Date: 2009-09-25
* Changes:
    * Added optional proxy support to get_last_commit()

### Version: 0.1

* Release Date: 2009-09-24
* Changes:
    * First Commit

## Requirements

* Python 2.5 or newer (not Python 3)
* PyYAML [http://pyyaml.org/] [5]
* python-markdown or python-markdown2

## Notes

The main purpose of PyGithubApi is so I can write a function for my other projects to check back with GitHub and see if they are the most current version.

Right now it only has one function: get_last_commit(), which takes a URL from the GitHub API for the commits on a repository and returns the latest commit date.

#### Missing Functionality

Every other function that the GitHub API offers.

#### Add a Tutorial

It would be nice to add a tutorial for new users who are not used to it.

[1]: mailto:ryan@quandyfactory.com

[2]: http://quandyfactory.com/projects/25/pygithubapi

[3]: http://github.com/quandyfactory/PyGithubApi

[4]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

[5]: http://pyyaml.org/

