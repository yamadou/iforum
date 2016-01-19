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
class Vote(ndb.Model):

    post_id = ndb.IntegerProperty(required = False)
    comment_id = ndb.IntegerProperty(required = False)
    username = ndb.StringProperty(required = True)
    kind_of_vote = ndb.StringProperty(required = True)

    @classmethod
    def create_vote(cls, post_id, comment_id, username, vote):
        return Vote(post_id = post_id,
                    username = username,
                    comment_id = comment_id,
                    kind_of_vote = vote)

    @classmethod
    def voted(cls, post_id, comment_id, username, vote):
        return Vote.query(Vote.username == username,
                          Vote.post_id == post_id,
                          Vote.comment_id == comment_id,
                          Vote.kind_of_vote == vote).get()


    
        
        
