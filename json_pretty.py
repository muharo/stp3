import sublime
import sublime_plugin
import json


class JsonPrettyCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        view = self.view
        my_selection = self.view.sel()
        for region in my_selection:

            selected_text = view.substr(region)
            json_object = json.loads(selected_text)
            selected_text = json.dumps(json_object, indent=4, sort_keys=True)

            # Replace selected lines with the sorted ones
            view.replace(edit, region, selected_text)