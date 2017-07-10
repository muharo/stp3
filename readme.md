### Sublime Text 3 Plugins

The plugins are defined as python files. To enable and use a plugin, copy the corresponding file under *Packages/User* directory.

To use a plugin, use the ST console (Win/Lin: **< Ctrl + \` >**):

    view.run_command('sort_by_length')
    view.run_command('sort_by_length', {"reverse":True})
    view.run_command('sort_by_length', {"reverse":False})


To easily run these commands, they can be added to Context menu (on right click), by adding **Context.sublime-menu** file under *Packages/User* directory.

The commands may also be added to main menu, by adding **Main.sublime-menu** file under *Packages/User* directory.
