from u9botpr.wsgi import application
# import os
# import sys
#
# sys.path.insert(0, os.path.dirname(__file__))
#
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'Hello people!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     resp = '0'
#     response = '\n'.join([message, version, resp])
#     return [response.encode()]
