==========
Bow Bakery
==========

Django powered HTML5 app running the site thebowbakery.com.

It's code and design was created by my wife (Jerra) and myself (Rob Madole).

The source code is available for review.  See LICENSE.rst for full rights
regarding its use.

==========
Developing
==========

The site uses zc.buildout, so you bootstrap it like so ::

    python bootstrap.py --distribute

Then run the buildout::

    ./bin/buildout

We are also using django-grappelli, and that takes an extra argument on the
command line. ::

    ./bin/django runserver 0.0.0.0:8000 --adminmedia=ext/grappelli/media
