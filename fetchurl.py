# Very simple command to retrieve the contents of a URL and put it inside a
# new buffer
#
# Created by Chris Baumbauer <cab@cabnetworks.net>

import sublime, sublime_plugin
import urllib

class FetchurlCommand(sublime_plugin.TextCommand):
	def performFetch(self, url):
		r = urllib.request.urlopen(url)
		content = r.read().decode("UTF-8")

		nv = self.view.window().new_file()
		nv.run_command("append", {"characters": content})

	def run(self, edit):
		self.view.window().show_input_panel("URL", "http://", self.performFetch, None, None)
