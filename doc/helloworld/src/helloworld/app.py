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

import google.appengine.api.xmpp
import google.appengine.ext.webapp
import google.appengine.ext.webapp.template
import logging
import wsgiref.handlers


class HelloWorldRequestHandler(google.appengine.ext.webapp.RequestHandler):
    """Simple request handler."""

    def get(self):
        """Handles get."""

        index = google.appengine.ext.webapp.template.render('index.html', {})
        self.response.out.write(index)


class XMPPHandler(google.appengine.ext.webapp.RequestHandler):
    """Handles XMPP messages."""

    def post(self):
        """Handles post."""

        message = google.appengine.api.xmpp.Message(self.request.POST)

        logging.info("Received XMPP message: %s" % message.body)

        if message.body[0:5].lower() == 'hello':
             message.reply("Hi, %s!" % message.sender)


class InviteHandler(google.appengine.ext.webapp.RequestHandler):
    """Invites one to a XMPP chat."""

    def post(self):
        """Handles post."""

        jid = self.request.get('jid')
        if google.appengine.api.xmpp.get_presence(jid):
            google.appengine.api.xmpp.send_invite(jid)

        self.redirect('/')


app = google.appengine.ext.webapp.WSGIApplication([
    ('/_ah/xmpp/message/chat/', XMPPHandler),
    ('/invite', InviteHandler),
    ('/.*', HelloWorldRequestHandler),
], debug=True)


def main():
    """The main function."""

    wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
    main()
