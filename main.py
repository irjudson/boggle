#
#  Prototype tool for building example stories for the XBRL Warehouse
#
#
import os
import webapp2
from handlers import MainPage

# Grab the debug value based on location (dev_appserver => True, appengine => False)
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Route table pulled out to make things cleaner
routes = [
	(r'/', MainPage),
	(r'/solve', MainPage)
]

# Create the WSGIApplication, hand it routes and debug, later we can sort out the config
app = webapp2.WSGIApplication(routes=routes, debug=debug)