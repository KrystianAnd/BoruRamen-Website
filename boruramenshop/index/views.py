from django.shortcuts import render
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def menu(request):
    categories = [
        {"name": _("Przystawki"), "anchor": "Przystawki"},
        {"name": _("Dania główne"), "anchor": "Dania_glowne"},
        {"name": _("Ramen"), "anchor": "Ramen"},
        {"name": _("Dodatki"), "anchor": "Dodatki"},
        {"name": _("Desery"), "anchor": "Desery"},
        {"name": _("Napoje"), "anchor": "Napoje"},
        {"name": _("Alkohole"), "anchor": "Alkohole"},
    ]
    return render(request, "menu.html", {"categories": categories})

def PolitykaStrony(request):
    return render(request, 'polityka_strony.html')


def set_language(request):
    lang = request.GET.get('lang') 
    if lang in ['pl', 'en']: 
        request.session['language'] = lang  
        activate(lang) 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 

def robots_txt(request):
    content = """User-agent: *
Disallow: /.git
Disallow: /config
Disallow: /api
Disallow: /wp-content
Disallow: /.env
Disallow: /lib
Disallow: /vendor
Disallow: /admin
Disallow: /core
Disallow: /phpunit
Disallow: /sites
Disallow: /storage
Disallow: /var
Disallow: /administrator
Disallow: /app
Disallow: /laravel
Disallow: /wp-admin
Disallow: /.env.example
Disallow: /test.php
Disallow: /backup
Disallow: /old
Disallow: /public
Disallow: /static
Disallow: /web
Disallow: /.aws
Disallow: /.svn
Disallow: /.dockerignore
Disallow: /.env.dev
Disallow: /.env.local
Disallow: /.env.production
Disallow: /.env.test
Disallow: /.gitignore
Disallow: /.htaccess
Disallow: /.local
Disallow: /.npmrc
Disallow: /.production
Disallow: /.remote
Disallow: /.wp-config.php.swp
Disallow: /admin
Disallow: /api-docs
Disallow: /application.yml
Disallow: /backup.env
Disallow: /backup.sql
Disallow: /config.inc.php
Disallow: /config.old.php
Disallow: /configuration.php~
Disallow: /credentials.env
Disallow: /db.ini
Disallow: /db_backup.sql
Disallow: /debug.php
Disallow: /development.env
Disallow: /Dockerfile
Disallow: /env.backup
Disallow: /info.php
Disallow: /local_settings.py
Disallow: /php.ini
Disallow: /phpinfo.php
Disallow: /phpinfo1.php
Disallow: /phpinfo2.php
Disallow: /prod.env
Disallow: /public
Disallow: /server-status
Disallow: /settings.bak
Disallow: /settings.yaml
Disallow: /stage.env
Disallow: /staging.env
Disallow: /swagger-ui.html
Disallow: /web.config
Disallow: /wp-config-sample.php
Disallow: /wp-config.php
Disallow: /xmlrpc.php
Disallow: /xmlrpc.php?rsd
Disallow: /yarn.lock
Disallow: /apps
Disallow: /assets
Disallow: /bitrix
Disallow: /blog
Disallow: /bootstrap
Disallow: /cgi-bin
Disallow: /cms
Disallow: /cron
Disallow: /cronlab
Disallow: /database
Disallow: /demo
Disallow: /dev
Disallow: /docker
Disallow: /en
Disallow: /exapi
Disallow: /helm
Disallow: /joomla
Disallow: /lab
Disallow: /logs
Disallow: /new
"""
    return HttpResponse(content, content_type="text/plain")
