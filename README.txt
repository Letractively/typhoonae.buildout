==============================
TyphoonAE - Typhoon App Engine
==============================

The TyphoonAE project aims at providing a full-featured and productive serving
environment to run Google App Engine (Python) applications. It delivers the
parts for building your own scalable App Engine while staying compatible with
Google's API.


Contents
========

  * Copyright and License
  * What is new in this release
  * What will be installed
  * Before you install
  * Running all services out of the box
  * How to run the guestbook demo application
  * Using the MySQL backed Datastore
  * How to configere BDBDatastore as alternate Datastore
  * How to configure your Jabber client to send and receive XMPP messages
  * Google's development application server
  * Contact


Copyright and License
=====================

Copyright 2009, 2010 Tobias Rodäbel

This software is released under the Apache License, Version 2.0. You may obtain
a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Google App Engine is a trademark of Google Inc.


What is new in this release
===========================

  * Support for Google App Engine SDK 1.4.1
  * Various bugfixes

Visit http://code.google.com/p/typhoonae/wiki/ReleaseNotes to get a more
detailed overview of the changes.


What will be installed
======================

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
  * Google App Engine SDK 1.4.0 - http://code.google.com/appengine
  and ...
  * TyphoonAE 0.2.0 - http://pypi.python.org/pypi/typhoonae/0.2.0

All these parts will be automatically installed by zc.buildout into an isolated
directory tree on your development machine. If you want to remove the TyphoonAE
environment you just have to delete this single directory.

See http://code.google.com/p/typhoonae/wiki/GettingStarted for further
information.


Before you install
==================

Python Interpreter
------------------

It is possible to run TyphoonAE's Python parts with Python 2.5.x and 2.6.x, but
it is recommended to use a version which is supported by the Google App Engine
SDK. See http://code.google.com/intl/de/appengine/docs/python/overview.html for
further information.

We recommend to install TyphoonAE into a virtualenv in order to obtain
isolation from any 'system' packages you've got installed in your Python
version. If you are using OS X it is not recommended to use the system's
Python. Here is how to build your own suitable Python.

Google App Engine SDK
---------------------

You don't have to install the Google App Engine SDK, because zc.buildout will
install it for you.

Other Requirements
------------------

Most of the required libraries and programs will be installed by zc.buildout.

The buildout needs Python and the tools contained in /bin and /usr/bin of a
standard installation of the Linux operating environment. You should ensure
that these directories are on your PATH and following programs can be found::

  * Python 2.5.2+ (3.x is not supported!)
  * gcc and g++
  * make
  * JAVA
  * locally installed sendmail (if you want to send emails)
  * Erlang
  * MySQL (if you want to use it as alternate Datastore backend)

On Debian Lenny you will need to have the following packages installed::

  * libmysql++-dev
  * libncurses5-dev
  * libssl-dev
  * python-dev
  * python-setuptools
  * libexpat-dev (libexpat1-dev)
  * gettext
  * erlang-nox and erlang-dev

The Images API uses the Python Imaging Library to transform images. TyphoonAE's
buildout does not set up PIL for you. You'll need to download the PIL module
and install it. For instance, on Debian use apt-get to install the
python-imaging package.


Running all services out of the box
===================================

Build the whole stack by typing the following commands::

  $ python bootstrap.py
  $ ./bin/buildout

Configure the 'helloworld' application::

  $ ./bin/apptool parts/helloworld/

Run the supervisor daemon which starts and controls all services at once::

  $ ./bin/supervisord

You can access the application using a web browser with the following URL::

  http://localhost:8080/


How to run the guestbook demo application
=========================================

Shutdown the supervisor by typing::

  $ bin/supervisorctl shutdown

Configure the guestbook application::

  $ ./bin/apptool parts/google_appengine/demos/guestbook/

Run the supervisor daemon::

  $ ./bin/supervisord

You can access the guestbook using a web browser with the following URL::

  http://localhost:8080/


Using the MySQL backed Datastore
================================

With TyphoonAE you can use a MySQL server as alternate Datastore backend. Since
we don't include MySQL in our buildout configuration, you have to install it
manually.

Configure the MySQL Datastore by typing::

  $ bin/apptool --datastore=mysql parts/google_appengine/demos/guestbook/

There are a number of special command line options to configure a different
host or custom authentication credentials. Use the --help option for further
information.


How to configere BDBDatastore as alternate Datastore
====================================================

BDBDatastore is an alternate Datastore backend for App Engine, implemented
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


How to configure your Jabber client to send and receive XMPP messages
=====================================================================

  * Create a Jabber account guest@<your.domain> where host
    is the machine on which you're running the server.
  * The password can be any desired password but must not be empty.
  * Your Jabber client should use port 5222 (no SSL).
  * Send an invitation to your newly created account.


Google's development application server
=======================================

You may recognize the dev_appserver script in the bin directory after building
the environment. It's included to check whether your application runs with the
installed original SDK.

It can be used as expected::

  $ bin/dev_appserver parts/helloworld


Contact
=======

If you have any further questions, please do not hesitate to visit the Google
Group for TyphoonAE http://groups.google.com/group/typhoonae.

Please use http://code.google.com/p/typhoonae/issues/list to report bugs.
