=================
proxidize_wrapper
=================


.. image:: https://img.shields.io/pypi/v/proxidize_wrapper.svg
        :target: https://pypi.python.org/pypi/proxidize_wrapper


Wrapper for proxidize android app.

* Free software: MIT license

Install a Proxy Server
======================
Read
`Follow <https://github.com/proxidize/proxidize-android>`__
to host the server.
We would need the http address which is in the format of "IP:PORT:USERNAME:PASSWORD" to use this wrapper.

Features
--------

* Use Proxidize Android app to proxy your internet connection on your PC. Wrapper for it.

How to Use
==========
1. Install the app on your android phone. mentioned above.
2. Install the package:
      pip install ec2_proxy


.. code-block:: python

      from proxidize_wrapper import Proxy

      p = Proxy("IP:PORT:USERNAME:PASSWORD")
      print(p.get_ip())
      p.change_ip()
      print(p.get_ip())

