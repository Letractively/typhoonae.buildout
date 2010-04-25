==============================
TyphoonAE - Typhoon App Engine
==============================

The TyphoonAE project aims at providing a full-featured and productive serving
environment to run Google App Engine (Python) applications. It delivers the
parts for building your own scalable App Engine while staying compatible with
Google's API.


Contents
--------

  * Copyright and license
  * What will be installed
  * What is new in this release
  * Running all services out of the box
  * How to configure your Jabber client to send and receive XMPP messages
  * How to run the guestbook demo application
  * How to configere BDBDatastore as alternate datastore
  * Google's development application server
  * Contact and bug reports


Copyright and license
---------------------

Copyright 2009, 2010 Tobias Rodäbel

This software is released under the Apache License, Version 2.0. You may obtain
a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0


What will be installed
----------------------

The main principles in the design of TyphoonAE are decoupling and statelessness
to provide concurrency, better caching, horizontal scalability and
fault-tolerance. It integrates various open source products.

  * mongoDB - http://www.mongodb.org
  * BDBDatastore - http://arachnid.github.com/bdbdatastore
  * memcached - http://www.danga.com/memcached/
  * RabbitMQ - http://www.rabbitmq.com
  * ejabberd - http://www.process-one.net/en/ejabberd
  * tornado - http://www.tornadoweb.org
  * FastCGI - http://www.fastcgi.com
  * nginx - http://nginx.net/
  * Supervisor - http://supervisord.org
  * Google App Engine SDK 1.3.3 - http://code.google.com/appengine
  and ...
  * TyphoonAE 0.1.4 - http://pypi.python.org/pypi/typhoonae/0.1.4

All these parts will be automatically installed by zc.buildout into an isolated
directory tree on your development machine. If you want to remove the TyphoonAE
environment you just have to delete this single directory.

See http://code.google.com/p/typhoonae/wiki/GettingStarted for further
information.


What is new in this release
---------------------------

  * Support for Google App Engine SDK 1.3.3.
  * Uses up-to-date versions of memcached, MongoDB and ejabberd.
  * Several bugfixes.

Visit http://code.google.com/p/typhoonae/wiki/ReleaseNotes to get a more
detailed overview of the changes.


Running all services out of the box
-----------------------------------

Build the whole stack by typing the following commands::

  $ python bootstrap.py
  $ ./bin/buildout

Configure the 'helloworld' application::

  $ ./bin/apptool parts/helloworld/

Run the supervisor daemon which starts and controls all services at once::

  $ ./bin/supervisord

You can access the application using a web browser with the following URL::

  http://<your.domain>:8080/


How to configure your Jabber client to send and receive XMPP messages
---------------------------------------------------------------------

  * Create a Jabber account guest@<your.domain> where host
    is the machine on which you're running the server.
  * The password can be any desired password but must not be empty.
  * Your Jabber client should use port 5222 (no SSL).
  * Send an invitation to your newly created account.


How to run the guestbook demo application
-----------------------------------------

Shutdown the supervisor by typing::

  $ bin/supervisorctl -c etc/supervisord.conf -u admin -p admin shutdown

Configure the guestbook application::

  $ ./bin/apptool parts/google_appengine/demos/guestbook/

Run the supervisor daemon::

  $ ./bin/supervisord

You can access the guestbook using a web browser with the following URL::

  http://<your.domain>:8080/


How to configere BDBDatastore as alternate datastore
----------------------------------------------------

BDBDatastore is an alternate datastore backend for App Engine, implemented
using BDB JE. It requires JAVA installed in your machine.

Use apptool to enable BDBDatastore::

  $ bin/apptool --datastore=bdbdatastore parts/google_appengine/demos/guestbook/

Don't forget to create the index.yaml file::

  $ cat > parts/google_appengine/demos/guestbook/index.yaml
  indexes:

  - kind: Greeting
    properties:
    - name: date
      direction: desc
  <ctrl-c>

Then run the supervisor daemon by typing::

  $ bin/supervisord


Google's development application server
---------------------------------------

You may recognize the dev_appserver script in the bin directory after building
the environment. It's included to check whether your application runs with the
installed original SDK.

It can be used as expected::

  $ bin/dev_appserver parts/helloworld


Contact and bug reports
-----------------------

If you have any further questions, please do not hesitate to visit the Google
Group for TyphoonAE http://groups.google.com/group/typhoonae.

Please use http://code.google.com/p/typhoonae/issues/list to report bugs.
