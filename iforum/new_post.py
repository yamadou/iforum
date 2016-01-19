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

import webapp2
from helpers import render
from post_db import Post

class New_Post(webapp2.RequestHandler):

    def write_form(self, title='', description=''):
        username = self.request.cookies.get('username')
        render(self, 'new_post.html',
               title = title,
               description = description,
               username = username)
            
        
    def get(self):
        self.write_form()

    def post(self):
        title = self.request.get('title')
        description = self.request.get('description')
        poster = self.request.cookies.get('username')

        if not (title and description):
            self.write_form(title = title,
                            description = description)

        else:
             post = Post.create_new_post(title, description, poster)
             post.put()
             self.redirect('/')
            
        
