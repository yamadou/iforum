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
import json
from post_db import Post
from votes_db import Vote

class Post_Upvote_Handler(webapp2.RequestHandler):
    
    def post(self):

        data = json.loads(self.request.body)
        post_id = int(data['postKey'])
        username = self.request.cookies.get('username')
        voted = Vote.voted(post_id, None, username, 'upvote')
        
        if not voted:
            post = Post.get_by_id(post_id)
            post.upvote += 1
            post.put()
            vote = Vote.create_vote(post_id, None, username, 'upvote')
            vote.put()
            self.response.write(json.dumps(({'post': post.to_dict(include=('upvote',
                                                                       'downvote',
                                                                       'title'))})))


        
        
      
