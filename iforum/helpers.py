#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname('_file_'), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render(self, template, **kw):
    t = jinja_env.get_template(template)
    page = t.render(**kw)
    self.response.write(page)

def set_secure_cookie(self, name, val):
        self.response.headers.add_header('Set-Cookie', '%s=%s' % (name, val))


def is_loggedin(self):
    username = self.request.cookies.get('username')
    if username:
        return True
    else:
        return False
    
