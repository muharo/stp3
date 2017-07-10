import sublime
import sublime_plugin

class SortByLengthCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		mysel = self.view.sel()
		for region in mysel:
			lines = []

			# Split selected text into lines
			line_regions = self.view.split_by_newlines(region)

			# Put the lines into an array to easily sort it
			for line in line_regions:
				lines.append(self.view.substr(line))

			# Check if reverse argument is defined, otherwise use default (False)
			try:
				args['reverse']
			except KeyError:
				args['reverse'] = False

			# Sort lines (elements of 'lines' array)
			lines.sort(key = len, reverse = args['reverse'])

			# Merge array elements into a single string
			txt = '\n'.join(str(e) for e in lines)

			# Replace selected lines with the sorted ones
			self.view.replace(edit,region,txt)
