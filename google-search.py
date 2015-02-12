# available commands
# google_search_selected
# google_search_from_input

import sublime, sublime_plugin
import subprocess, webbrowser

def query(text):
    url = 'http://www.google.com/search?q=' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class GoogleSearchSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)
			
            query(text)

class GoogleSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        query(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass