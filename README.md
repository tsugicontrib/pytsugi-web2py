# pytsugi-web2py

Installation
------------

Check this code out into a web2py distro:

    cd web2py/applications/
    git clone https://github.com/tsugiproject/pytsugi-web2py.git tsugi

You cannot use dashes in application names in web2py apparently.

You also need pytsugi available via `pip`.  See the installation
instructions in https://github.com/tsugiproject/pytsugi

Then checkout, install and setup a PHP tsugi instance according to
www.tsugi.org - get the databases all set up.

Where is the Web2Py Code?
-------------------------

Take a look at `controllers/default.py` and see the `launch` function to see
how this app uses `pytsugi`

This is early days so expect a lot of print statements as the code evolves.

Testing
-------

To test, after you have Tsugi set up go to its developer console:

    http://localhost:8888/tsugi/dev

Set the launch url to:

    http://localhost:8000/tsugi/default/launch

And launch.

For now there is lots of output so watch the web2py console.
If you edit the pytsugi module code make sure to restart the
web2py server to force module reload.  I wish
there was a tick box somewhere to say "developer mode" to
override the module caching.

