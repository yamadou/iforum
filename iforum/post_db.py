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

from google.appengine.ext import ndb

# Databse
class Post(ndb.Model):
    
    title = ndb.StringProperty(required = True)
    description = ndb.TextProperty(required = True)
    poster = ndb.StringProperty(required = True)
    posted = ndb.DateProperty(auto_now_add = True)
    comments = ndb.IntegerProperty(required = True, default = 0)
    views = ndb.IntegerProperty(required = True, default = 0)
    upvote = ndb.IntegerProperty(required = True, default = 0)
    downvote = ndb.IntegerProperty(required = True, default = 0)


    @classmethod
    def create_new_post(cls, title, descrip, poster):
        return Post(title = title,
                    description = descrip,
                    poster = poster)
