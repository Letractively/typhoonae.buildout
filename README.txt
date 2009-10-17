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
  * Running the cloud out of the box
  * Sending and receiving XMPP messages
  * How to run the guestbook demo application
  * Google's development application server


Copyright and license
---------------------

Copyright 2009 Tobias Rodäbel

This software is released under the Apache License, Version 2.0. You may obtain
a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0


What will be installed
----------------------

The main principles in the design of TyphoonAE are decoupling and statelessness
to provide concurrency, better caching, horizontal scalability and
fault-tolerance. It integrates various open source products.

  * mongoDB - http://www.mongodb.org
  * memcached - http://www.danga.com/memcached/
  * RabbitMQ - http://www.rabbitmq.com
  * ejabberd - http://www.process-one.net/en/ejabberd
  * FastCGI - http://www.fastcgi.com
  * nginx - http://nginx.net/
  * Supervisor - http://supervisord.org
  * Google App Engine SDK 1.2.7 - http://code.google.com/appengine

All these parts will be automatically installed by zc.buildout into an isolated
directory tree on your development machine. If you want to remove the TyphoonAE
environment you just have to delete this single directory.

See http://typhoonae.googlecode.com and
http://code.google.com/p/typhoonae/wiki/GettingStarted for further information.


What is new in this release
---------------------------

  * Updated to Google App Engine SDK 1.2.7
  * Added basic XMPP support
  * Several bugfixes (see http://typhoonae.googlecode.com for details)


Running the cloud out of the box
--------------------------------

Build the whole stack by typing the following commands::

  $ python bootstrap.py
  $ ./bin/buildout

Configure the 'helloworld' application::

  $ ./bin/apptool parts/helloworld/

Run the supervisor daemon which starts and controls all services at once::

  $ ./bin/supervisord

You can access the application using a web browser with the following URL::

  http://localhost:8080/


Sending and receiving XMPP messages
-----------------------------------

Create a new account guest@localhost in your XMPP/Jabber client and add
helloworld@localhost as buddy. Then send 'hello' and the app should answer
immediately.


How to run the guestbook demo application
-----------------------------------------

Shutdown the supervisor by typing::

  $ bin/supervisorctl -c etc/supervisord.conf -u admin -p admin shutdown

Configure the guestbook application::

  $ ./bin/apptool parts/google_appengine/demos/guestbook/

Run the supervisor daemon::

  $ ./bin/supervisord

You can access the guestbook using a web browser with the following URL::

  http://localhost:8080/


Google's development application server
---------------------------------------

You may recognize the dev_appserver script in the bin directory after building
the environment. It's included to check whether your application runs with the
installed original SDK.

It can be used as expected::

  $ bin/dev_appserver parts/helloworld
