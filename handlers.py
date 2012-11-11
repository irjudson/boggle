import os, string, random, logging
import webapp2, json
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from boggle import boggle_search

class App(webapp2.RequestHandler):

	def get(self):
		path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
		self.response.out.write(open(path).read())

	def post(self):
		gamedata = self.request.get("gamedata")
		word = self.request.get("word")
		locations = boggle_search(gamedata.upper(), word.upper())
		self.response.headers['Content-type'] = 'application/json'
		self.response.out.write(json.dumps(locations))
