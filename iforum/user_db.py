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

from google.appengine.ext import db
from webapp2_extras.security import generate_password_hash
from webapp2_extras.security import check_password_hash

# Databse
class Users(db.Model):

    first_name = db.StringProperty(required = True)
    last_name = db.StringProperty(required = True)
    username = db.EmailProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def exist_username(cls, username):
        return Users.all().filter('username =', username).get()


    # This class creates a new user, store it in the database
    # and returns the password_hash
    @classmethod
    def create_new_user(cls, fname, lname, pw_hash, username, email):
        user = Users(first_name = fname,
                     last_name = lname,
                     username = username,
                     email = email,
                     password = pw_hash)
        user.put()
        return pw_hash

    @classmethod
    def make_pw_hash(self, pw):
        return generate_password_hash(pw, method='sha1', length=22)
        

    @classmethod
    def get_pwhash(cls, username):
        return Users.all().filter('username =', username).get()
    
    @classmethod
    def password_match(cls, password, pwhash):
        return check_password_hash(password, pwhash)

