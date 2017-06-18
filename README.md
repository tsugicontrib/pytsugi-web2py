# pytsugi-web2py

Installation
------------

Check this code out into a web2py distro:

    cd web2py/applications/
    git clone https://github.com/tsugiproject/pytsugi-web2py.git tsugi

You cannot use dashes in application names in web2py apparently.

You also need pytsugi in modules.  Someday this will be in pypi, but for now

    cd modules
    git clone https://github.com/tsugiproject/pytsugi.git

Then checkout and setup a PHP tsugi according to www.tsugi.org - get the databases
all set up.  

Testing
-------

To test, after you have Tsugi set up go to its developer console:

    http://localhost:8888/tsugi/dev

Set the launch url to:

    http://localhost:8000/tsugi/default/launch

And launch.

For now there is lots of output so watch the web2py console.   If you edit the module
code make sure to restart the web2py server to force module reload.  I wish
there was a tick box somewhere to say "developer mode" to override the caching.

