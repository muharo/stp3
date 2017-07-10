import sublime
import sublime_plugin

class SortLinesLengthReverseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		mysel = self.view.sel()
		for region in mysel:
			lines = []
			line_regions = self.view.split_by_newlines(region)
			for line in line_regions:
				lines.append(self.view.substr(line))
			lines.sort(key = len, reverse = True)
			txt = '\n'.join(str(e) for e in lines)
			self.view.replace(edit,region,txt)
