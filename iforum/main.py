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
from log_in import Log_In
from log_out import Log_Out
from sign_up import Sign_Up
from post_db import Post
from new_post import New_Post
from post_page import Post_Page
from helpers import is_loggedin
from post_upvote_handler import Post_Upvote_Handler
from post_downvote_handler import Post_Downvote_Handler

# Default front page which will be seen by users who aren't logged in
class HomePage(webapp2.RequestHandler):

    def write_form(self, topic_btn = '/login', link1='/login',
                   text1 ='Log In', status = 'status red',
                   link2 = 'signup', text2 = 'Sign Up', username=''):

        cursor = Post.query()
        render(self, 'home_page.html',
               cursor = cursor,
               status = status, 
               link1 = link1, text1 = text1,
               link2 = link2, text2 = text2,
               username = username,
               new_topic_btn = topic_btn)
        
        
    def get(self):

        user_loggedin = self.request.cookies.get('username') 
        if user_loggedin:
            self.write_form(topic_btn = '/new_post',
                            link1 = '/logout',
                            text1 = 'Log Out',
                            link2 = '/', text2 = '',
                            status = 'status green',
                            username = user_loggedin)
        else:
            self.write_form()
            
        
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/signup', Sign_Up),
    ('/login', Log_In),
    ('/logout', Log_Out),
    ('/new_post', New_Post),
    ('/upvote/', Post_Upvote_Handler),
    ('/downvote/', Post_Downvote_Handler),
    ('/([0-9]+)', Post_Page)
], debug=True)

