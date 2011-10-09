# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse

def main_page(request):
	output = '''<html>
        <head><title> %s </title></head>
        <body>
            <h1>%s</h1><p>%s</p>
        </body>
    </html>''' % ('Grosik - NET',
           'Witamy w internetowym systemie zarządzania przedszkolem',
           'Umożliwia on zarządzanie podziałem na grupy, obecnościami i opiekunami dzieci.')
	return HttpResponse(output)


