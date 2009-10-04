# -*- coding: utf-8 -*-
#
# Copyright 2009 Tobias Rodäbel
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
"""Simple hello world application."""

import google.appengine.ext.webapp
import wsgiref.handlers


class HelloWorldRequestHandler(google.appengine.ext.webapp.RequestHandler):
    """Simple request handler."""

    def get(self):
        """Handles get."""

        self.response.out.write("<html><body>Hello, World!</body></html>")


app = google.appengine.ext.webapp.WSGIApplication([
    ('/.*', HelloWorldRequestHandler),
], debug=True)


def main():
    """The main function."""

    wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
    main()
