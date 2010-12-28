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

__docformat__ = 'restructuredtext en'

from optparse import OptionParser
import os
import sys


import repos
parser = OptionParser()
parser.add_option("-r", "--register-repos", dest="register_repos", action="store_true",
                  help="Register all repos in  [minitage, minitage-dependencies, minitage-eggs] to dev team.", )

def get_user():
    key = os.environ.get('GITHUB_USER', None)
    return key 

def get_apikey():
    key = os.environ.get('GITHUB_KEY', None)
    return key

def main():
    options, args = parser.parse_args()

    if options.register_repos:
        user = get_user()
        key = get_apikey()
        repos.register(user=user, key=key)



# vim:set et sts=4 ts=4 tw=80:

