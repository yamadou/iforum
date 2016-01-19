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
from post_db import Post
from helpers import render
from comment_db import Comment
from helpers import is_loggedin

class Post_Page(webapp2.RequestHandler):

    def write_form(self, post_id):
        
        post = Post.get_by_id(int(post_id))
        qry1 = Comment.query()
        cursor = qry1.filter(Comment.post_id == int(post_id))
        username = self.request.cookies.get('username')
        if username:
            render(self, 'post_page.html',
                   post = post,
                   post_id = int(post_id),
                   username = username,
                   cursor = cursor)
        else:
            render(self, 'post_page_2.html',
                   post = post,
                   post_id = int(post_id),
                   cursor = cursor)
      
             
            
       
            

    def get(self, post_id):
        self.increment_num_view(post_id)
        self.write_form(post_id)

    def post(self, post_id):

        comment = self.request.get('comment')
        poster = str(self.request.cookies.get('username'))
        new_comment = Comment.create_new_comment(int(post_id), comment, poster)
        self.increment_num_comment(post_id)
                     
        if (comment and poster and new_comment):
            new_comment.put()
        self.redirect('/')
        

    def increment_num_view(self, post_id):
        post = Post.get_by_id(int(post_id))
        post.views += 1
        post.put()


    def increment_num_comment(self, post_id):
        post = Post.get_by_id(int(post_id))
        post.comments += 1
        post.put()
 
