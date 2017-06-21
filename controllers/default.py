# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

from gluon.custom_import import track_changes
track_changes(True)

import urllib

import oauth.oauth as oauth
from pytsugi import LTIX

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def launch() : 
    print "Welcome to Launch"
    launch = LTIX.web2py(request, response, db, session)
    if not launch.valid : 
        print "Not Valid"
        if launch.redirecturl is not None :
            print "Redirect to",launch.redirecturl
            redirect(launch.redirecturl)
            return ''
        return launch.detail
    
    print "user id", launch.user.id
    print "instructor", launch.user.instructor()
    print "course id", launch.context.id
    print "course", launch.context.title
    return 'Good Launch <a href="display_form">Continue...</a>'

def display_form():
    launch = LTIX.web2py(request, response, db, session)
    form = FORM('Enter grade:',
              INPUT(_name='grade', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    print "user id", launch.user.id
    if form.process().accepted:
        response.flash = 'form accepted '+str(form.vars.grade)
        launch.result.setGrade(float(form.vars.grade),"Nice work")
        # session.flash = 'form accepted '+str(form.vars.grade)
        # redirect(URL('next'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form, launch=launch)

def next():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
