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

#Database
class Comment(ndb.Model):

    post_id = ndb.IntegerProperty(required = True)
    comment = ndb.TextProperty(required = True)
    poster = ndb.StringProperty(required = True)
    commented = ndb.DateProperty(auto_now_add = True)
    

    @classmethod
    def create_new_comment(cls, post_id, comment, poster):
        return Comment(post_id = post_id,
                    comment = comment,
                    poster = poster)
        
