import os, string, random, logging
import webapp2, json
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from boggle import boggle_search

class MainPage(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = "Logout"
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = "Login"

		gamedata = self.request.get("gamedata")
		word = self.request.get("word")

		print "GAME: %s WORD: %s" % (gamedata, word)

		template_values = {
		'user' : user,
		'url' : url,
		'url_linktext' : url_linktext,
		}		

		path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
		self.response.out.write(template.render(path, template_values))

	def post(self):
		gamedata = self.request.get("gamedata")
		word = self.request.get("word")

		locations = boggle_search(gamedata, word)
		logging.debug("GAME: %s" % gamedata)
		logging.debug("WORD: %s" % word)
		for l in locations:
			logging.debug("LOCATION: ")
			for i in l:
				logging.debug("\t %d %d" % (i[0], i[1]))
		self.response.headers['Content-type'] = 'application/json'
		self.response.out.write(json.dumps(locations))
