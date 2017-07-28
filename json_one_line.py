import sublime
import sublime_plugin

class JsonOneLineCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		mysel = self.view.sel()
		for region in mysel:

			selected_text = view.substr(region)
			selected_text = selected_text.replace('\n', ' ').replace('\r', '')
			selected_text = ' '.join(selected_text.split())

			# Replace selected lines with the sorted ones
			view.replace(edit,region,selected_text)
