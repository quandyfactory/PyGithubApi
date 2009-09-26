"""
A series of Python functions for interacting with the GitHub API. 
Save this module somewhere on the Python PATH and you should be good to go.
"""

#!/usr/bin/env python

__version__ = 0.11
__releasedate__ = '2009-09-25'
__author__ = 'Ryan McGreal <ryan@quandyfactory.com>'
__homepage__ = 'http://quandyfactory.com/projects/2/githubapi/'
__copyright__ = '(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html'

import yaml
import urllib

def get_last_commit(url, proxies = {}):
    """
    Takes a url from the GitHub API for the commits on a repository and returns the latest
    commit date.
    """
    # page contains the downloaded object
    
    try:
        page = urllib.urlopen(url, proxies=proxies)
    except URLError:
        return URLError

    # content contains the contents of the page
    content = page.read()
    # code is the content converted to a yaml hash
    code = yaml.load(content)
    # commits is the value of the 'commits' key in code
    commits = code['commits']
    # last_commit is a hash of details from the latest commit
    last_commit = commits[0]
    # cdate is the YYYY-MM-DD of the last commit
    cdate = last_commit['committed_date'][:10]
    return cdate
    
