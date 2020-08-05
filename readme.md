### Sublime Text 3 Plugins

The plugins are defined as python files. To enable and use a plugin, copy the corresponding file under *Packages/User* directory.

 * MacOS location:   ```~/Library/Application Support/Sublime Text 3/Packages/User```
 * Ubuntu location:  ```~/.config/sublime-text-3/Packages/User```
 * Windows location: ```C:\Users\<user>\AppData\Roaming\Sublime Text 3\Packages\User```

***

To use a plugin, use the ST console (Win/Lin: **< Ctrl + \` >**):

    view.run_command('sort_by_length')
    view.run_command('sort_by_length', {"reverse":True})
    view.run_command('sort_by_length', {"reverse":False})

***

To easily run these commands, they can be added to Context menu (on right click), by adding **Context.sublime-menu** file under *Packages/User* directory.

The commands may also be added to main menu, by adding **Main.sublime-menu** file under *Packages/User* directory.

***

List of available plugins:

 * sort_by_length - sort selected lines by length (ascending and descending)
 * json_one_line - format selected text to a one line text
 * json_pretty - format selected text to a pretty json
 * encode - encode a string to one of the supported types: sha256, sha512, base64
