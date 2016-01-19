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

import re
import webapp2

from user_db import Users
from helpers import render
from helpers import set_secure_cookie
from google.appengine.api import mail


class Sign_Up(webapp2.RequestHandler):

    def write_form(self, fname='', lname='', err_msg='', username='', verify=''):
        render(self, 'new_account.html',
               err_msg = err_msg,
               first_name = fname,
               last_name = lname,
               username = username)
        
    
    def get(self):
        self.write_form()
        

    def post(self):
        fname = self.request.get('first_name')
        lname = self.request.get('last_name')
        username = self.request.get('username')
        email = self.request.get('email')
        pw = self.request.get('password')
        verify = self.request.get('verify')

        if not (fname and lname and username and pw and verify):
            self.write_form(err_msg = 'Required field missing',
                            fname = fname,
                            lname=lname,
                            username=username)     
        

        elif not self.valid_username(username):
            self.write_form(err_msg = 'Username should be at least 4 characters long.',
                            fname = fname,
                            lname = lname)

        elif Users.exist_username(username):
            self.write_form(err_msg = 'This username is already taken.',
                            fname = fname,
                            lname = lname)

        elif not self.valid_password(pw):
            self.write_form(err_msg = 'Password should be at least 6 characters long.',
                            fname = fname,
                            lname = lname,
                            username = username)
            
        elif  pw != verify:
            self.write_form(err_msg = 'Passwords did not match',
                            fname = fname,
                            lname = lname,
                            username = username)
                            
        else:
            pw_hash = Users.make_pw_hash(pw)
            Users.create_new_user(fname, lname, pw_hash, username, email)
            set_secure_cookie(self, 'username', str(username))
            set_secure_cookie(self, 'password', str(pw_hash))
            self.redirect('/')
    
        

    # Password is only valid if it contains at least 6 charaters & if it is only
    # restricted to (does not specifically require any of): uppercase letters,
    # lowercase letters, numbers & any of the special characters(@#$%^&*+)
    def valid_password(self, password):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', password)
 
    # A username should be at least 6 characters long
    def valid_username(self, username):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{4,}', username)
  
