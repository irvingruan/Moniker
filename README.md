Moniker
=========================================

Written by Irving Y. Ruan <[irvingruan@gmail.com](mailto:irvingruan@gmail.com)>

About
-----

Moniker is a simple Python utility that finds all files and folders in the first 
level of a given path and does mass-(un)capitalization editing of their 
respective names. This was built primarily for people who want to change the 
capitalization naming model for a given directory, especially if it contains a 
large number of (un)capitalized files and folders.

Moniker currently only runs on *nix systems and requires Python 2.x or higher.

Usage
-----

Simply run:

`./Moniker.py -p [path] -c [case]`

For example:

`./Moniker.py -p /Users/irving/Documents/ -c Upper`

And Moniker will take care of the rest by properly capitalizing the first letter 
of folders and directories in the specified path.

Help
-----

For help with using Moniker, run:

`./Moniker.py --help`

Legal
-----

Moniker is Copyright (c) 2012 Irving Ruan and is BSD licensed. The full text of 
the license can be found in LICENSE.