#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2010, Mathieu PASQUET <mpa@makina-corpus.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the <ORGANIZATION> nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from restkit import Resource, BasicAuth
import demjson

__docformat__ = 'restructuredtext en'

class e(Exception):pass

def github_req(user, token, fmt='json', suburl=None, method='get'):
    auth = BasicAuth(user, token)
    if not suburl:
        suburl = '/user/show/%s' % user
    url = 'https://github.com/api/v2/%s%s' % (fmt, suburl)
    r = Resource(url, filters=[auth])
    ret = getattr(r, method)().body_string()
    if fmt == 'json':
        ret = demjson.decode(ret)
    return ret

organizations = ['minitage', 'minitage-dependencies', 'minitage', 'minitage-eggs']
def register(user=None,key=None):
    if not user:
        raise e('No user given') 
    if not key:
        raise e('No apikey given')
    for org in organizations:
        # get dev team related repos
        ret = github_req(user, key, suburl='/organizations/%s/teams' % org)
        teams = ret.get('teams', [])
        devid = None
        for t in teams:
            if t.get('name', '') == 'dev':
                devid = t['id']
        if 'repositories' in ret:
            repos = ret['repositories']   
        # get orga
        orga = github_req(user, key, suburl='/organizations/%s' % org)
        # get organization repos
        res = github_req(user, key, suburl='/organizations/%s/public_repositories' % org)
        repos = {}
        if 'repositories' in res:
            repos = dict([(key['name'], key) for key in res['repositories']])
        if devid:
            dev = None
            res = github_req(user, key, suburl='/teams/%s' % devid)
            if 'team' in res:
                dev = res['team']
            if dev:
                res = github_req(user, key, suburl='/teams/%s/repositories' % devid)
                teamrepos = {}
                if 'repositories' in res:
                    teamrepos = dict([(key['name'], key) for key in res['repositories']])
                for r in repos:
                    if not r in teamrepos:
                        repo = repos[r]
                        url = '/teams/%s/repositories?name=%s/%s' % (devid, org, r)        
                        print u"Creating  %s" % (r)
                        res = github_req(user, key, method='post', suburl=url)


# vim:set et sts=4 ts=4 tw=80:

