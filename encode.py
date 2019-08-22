import sublime
import sublime_plugin
import hashlib
import base64


class EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        view = self.view
        my_selection = self.view.sel()

        for region in my_selection:

            if region.empty():
                region = view.word(region)

            selected_text = view.substr(region).encode('utf-8')
            encoded_text = selected_text

            if args['enc_alg'] == "sha256":
                encode = hashlib.sha256()
                encode.update(selected_text)
                encoded_text = encode.hexdigest()
            elif args['enc_alg'] == "sha512":
                encode = hashlib.sha512()
                encode.update(selected_text)
                encoded_text = encode.hexdigest()
            elif args['enc_alg'] == "base64":
                encoded_text = base64.b64encode(selected_text).decode('utf-8')
            else:
                print("Unknown encryption alg")

            view.replace(edit, region, encoded_text)
