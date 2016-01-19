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

from user_db import Users
from helpers import render
from helpers import set_secure_cookie

class Log_In(webapp2.RequestHandler):

    def write_form(self, err_msg=''):
        render(self, 'log_in.html', err_msg = err_msg)
    
    def get(self):
        self.write_form()


    def post(self):
        username = self.request.get('username')
        pw = self.request.get('password')
            
        if not (username and pw):
            self.write_form(err_msg = 'Username or password is missing.')
        elif not Users.exist_username(username):
            self.write_form(err_msg = 'The username you have entered does not match any account.')
        elif not Users.password_match(pw, Users.get_pwhash(username).password):
            self.write_form(err_msg = 'The password you have entered is incorrect.')
            
        else:
            pw_hash = Users.get_pwhash(username).password
            set_secure_cookie(self, 'username', str(username))
            set_secure_cookie(self, 'password', str(Users.get_pwhash(username).password))
            self.redirect('/')
                 
                
