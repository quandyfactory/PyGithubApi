#!/usr/bin/env python

"""
A series of Python functions for interacting with the GitHub API. 
It requires PyYAML http://pyyaml.org/.
Otherwise, save this module somewhere on the Python PATH and you should be good to go.
"""

__version__ = 0.13
__releasedate__ = '2011-03-14'
__author__ = 'Ryan McGreal <ryan@quandyfactory.com>'
__homepage__ = 'http://quandyfactory.com/projects/2/githubapi/'
__copyright__ = '(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html'

try:
    import yaml
except:
    print 'Python yaml library missing. Get it here: http://pyyaml.org/'
    quit() # not much point in going on, is there?

import urllib

def get_last_commit(user='', repo='', proxies = {}):
    """
    Takes a url from the GitHub API for the commits on a repository and returns the latest
    commit date.
    """
    # create url from user and repo
    url = 'http://github.com/api/v2/yaml/commits/list/%s/%s/master' % (user, repo)
    
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
    
