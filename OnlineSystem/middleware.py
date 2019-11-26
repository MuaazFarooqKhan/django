from django.conf import settings
from bussystem.views import *
from bussystem.models import *
from django.shortcuts import render, redirect, HttpResponse


class TimezoneMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        return None

    def process_request(self, request):
        # print('Middleware executed succesfully\t', request.get_full_path())

        if request.get_full_path() == '127.0.0.1:8000/calladdthings/':
            if not request.session.get('email'):
                return redirect('/')
            else:
                redirect('/calladdthings')
                pass

        if request.get_full_path() == '127.0.0.1:8000/adminprofile/':
            if not request.session.get('email'):
                return redirect('/')
            else:
                return redirect('/adminprofile')
                pass



    def process_response(self, request, response):
        """Let's handle old-style response processing here, as usual."""
        # Do something with response, possibly using request.
        return response

    def __call__(self, request):
        """Handle new-style middleware here."""
        response = self.process_request(request)
        if response is None:
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)
        response = self.process_response(request, response)
        return response