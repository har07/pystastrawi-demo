#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import json
import webapp2
import logging

from template_base import Handler
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class IndexHandler(Handler):
    def get(self):
        self.render("index.html")


class StemmingHandler(Handler):
    def post(self):
        data = json.loads(self.request.body)
        text = data['text'].encode('utf8')

        # create stemmer
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        # stemming process
        output   = stemmer.stem(text)

        self.response.out.write(json.dumps({'output': output}))


app = webapp2.WSGIApplication([
    ('/stem/', StemmingHandler)
    , ('/', IndexHandler)
], debug=True)
