SublimeLinter-contrib-selene
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-selene.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-selene)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [selene](https://kampfkarren.github.io/selene/). It will be used with files that have the “lua” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `selene` is installed on your system. Follow the instructions [here](https://kampfkarren.github.io/selene/cli/installation.html) if you have not installed it yet. 

In order for `selene` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

The recommended way of configuring `selene` is using [selene.toml](https://kampfkarren.github.io/selene/cli/std.html)