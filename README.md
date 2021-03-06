Zim-markdown Branch
===================

This is [Zim Wiki](https://github.com/zim-desktop-wiki/zim-desktop-wiki)
branch/fork with Markdown format support for page content. Note that both
the Markdown format and the original Zim-wiki format are supported
(original format at least for reading, page templates, etc. may be already
updated for Markdown). Which format to use is a per-notebook setting. The
default format remains Zim-wiki. To switch a particular notebook to
Markdown format, settings in notebook's `notebook.zim` config file should
be updated. Below are detailed instructions on doing so.

To create a Markdown notebook:

1. Clone this repository:
`git clone https://github.com/pfalcon/zim-desktop-wiki zim-markdown`
(this will clone into `zim-markdown` directory).
2. Change into `zim-markdown` and run `./zim-debug.sh` (Linux assumed).
Alternatively, run `python3 zim.py --standalone --debug`.
3. In menu, choose File -> Open another notebook...
4. In the "Open Notebook" dialog, press "Add" button.
5. Enter name "MarkdownNotes" for the notebook. Note the filesystem
folder for the notebook (e.g. `~/Notebooks/MarkdownNotes`).
6. Quit Zim.
7. Go to the notebook folder noted above using any file manager.
8. In the folder, there should be file named `notebook.zim`.
9. Open it in any editor.
10. In the file, there should be lines:
```
default_file_format=zim-wiki
default_file_extension=.txt
```
replace them with the following lines:
```
default_file_format=zim_markdown
default_file_extension=.md
```
11. Restart Zim. Open the notebook you modified.
12. For each newly created page, you need to press Ctrl+R for Markdown
formatting to go into effect (a known issue, or a feature, depending
on how you look into it).
13. Type some text, apply some formatting. Go to the notebook folder
and behold that you have e.g. `Home.md` file, which contains Markdown
formatting inside.
14. If you have existing Markdown files, you can just drop them into
the notebook folder, and press Ctrl+R in Zim for it to pick up them
15. Note that not all Markdown formatting is supported as of now, visit
the [bugtracker](https://github.com/pfalcon/zim-desktop-wiki/issues)
to stay in loop of the known issues.



Below is the original Zim README.

---

Zim - A Desktop Wiki Editor
===========================

![zim banner](./website/files/images/invade_your_desktop.png)


Zim is a graphical text editor used to maintain a collection of wiki pages. Each
page can contain links to other pages, simple formatting, and images. Pages are
stored in a folder structure, like in an outliner, and can have attachments.
Creating a new page is as easy as linking to a nonexistent page. All data is
stored in plain text files with wiki formatting. Various plugins provide
additional functionality, like a task list manager, an equation editor, a tray
icon, and support for version control.

![Screenshot](./website/files/screenshots/zim-normal.png)

Zim can be used to:
* Keep an archive of notes
* Keep a daily or weekly journal
* Take notes during meetings or lectures
* Organize task lists
* Draft blog entries and emails
* Do brainstorming


## Installing from a Package

Most Linux distributions include zim in their package repository. On Debian and
Ubuntu, the package is simply called "zim".

Debian/Ubuntu packages and a Windows installer can be found via https://zim-wiki.org/downloads.html

On Mac OS X, zim can be installed from Homebrew using,

```
brew install zim
```

Optionally, you can [create a .app
wrapper](https://github.com/jaap-karssenberg/zim-wiki/wiki/Mac-OSX-App-%28wrapper%29)
for convenience.

## Installing from Source

**NOTE:** You don't need to install zim in order to test it. You should be able to run it
directly from the source directory by calling `./zim.py`. (To run a translated
version from the source, run `./setup.py build_trans`.)


First, you should verify you have the dependencies zim needs. To list all dependencies check `./setup.py --requires`.

You will at least need the following:

* Gtk+ >= 3.18
* python3 >= 3.2
* python3-gi (also known as pygobject, but make sure to have the "gi" based version)
* python3-xdg (optional, but recommended)
* xdg-utils (optional, but recommended)

To verify that zim is working properly on your system, you can run the test suite using `./test.py`. Failures do not have to be critical, but in principle, all tests should pass.

Zim can be installed from source using:

    ./setup.py install

If you are installing Zim from source in a Python virtual environment,
you need to tell Zim where to load necessary data files by
`export XDG_DATA_DIRS=<where-your-virtual-environment-root-folder-is>/share:$XDG_DATA_DIRS`.
Please refer to the `Install Paths` section for more details about the XDG paths.

Most plugins have additional requirements. These are listed in the plugin descriptions.

### Ubuntu

On Ubuntu or other Debian derived systems, the following packages should be installed:

* python3
* gir1.2-gtk-3.0
* python3-gi
* python3-xdg


### Windows

Download, install and update [MSYS2](https://www.msys2.org/) 64-bit by following the instructions on their website.

Open "MSYS2 MSYS" terminal from the Start Menu and install GTK3, Python3 and Python bindings for GTK:

`pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject`

The Windows drive is mounted on `/c`, browse your Windows user folder using:

`cd "/c/Users/$USERNAME"`

You can now run Zim from the MSYS terminal using:

`/mingw64/bin/python3 zim.py`

Or from any Windows terminal using:

`C:\msys64\mingw64\bin\python3.exe zim.py`

For more details see https://www.gtk.org/docs/installations/windows/ and https://pygobject.readthedocs.io/en/latest/getting_started.html.

*Note:* installation of the "msys" environment offers a "32" and a "64" bit
shell. When you installed the "64" packages for Gtk, they will only run from
the "64" shell.


### Mac OS X

You can run zim on Mac if you have the proper dependencies installed.

If you are using Mac Ports packages installing the following ports should work:

TODO: new instructions for Gtk3 / Python3

If you are using [Homebrew package manager](https://brew.sh/), the proper dependencies can be installed using

`brew install python gtk+3 pygobject3`

Once done, install

`brew install zim`

Then run from terminal

`zim`

Or [make a wrapper app](https://github.com/jaap-karssenberg/zim-wiki/wiki/Mac-OSX-App-%28wrapper%29) for Zim so that you can keep it in the launcher and open it as a native Mac OSX app.


### Install Paths

If you install zim in a non-default location, you may need to set the PYTHONPATH environment variable in order for zim to find its python modules. For example, if you installed the modules below "/home/user/lib/zim" you need to set:

    PYTHONPATH=/home/user/lib

Also, zim uses the XDG paths to locate data and config files. If you get an error that zim can not find its data files, for example, if you installed the zim data files to "/home/user/share/zim", you will need to set the data path like this:

    XDG_DATA_DIRS=/home/user/share:/usr/local/share:/usr/share


## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) and [PLUGIN_WRITING](./PLUGIN_WRITING.md)
for information on contributing to the zim source code, translations and
documentation.


## Copyright and License

Zim is an open-source program. This means it can be used and distributed freely
under the conditions of the [license](./LICENSE).

All files in this package, except for those mentioned below, are
copyrighted by Jaap Karssenberg <jaap.karssenberg@gmail.com>

Translations are copyrighted by their respective translators. All translations
that are entered through the launchpad website are distributed under the BSD
license. See the translation files for detailed translator credits.

The following files were included from other sources:
* `zim/inc/xdot.py` - Copyright 2008 Jose Fonseca
* `zim/inc/arithmetic.py` - Copyright 2010, 2011 Patricio Paez
* From the default Gnome icon theme:
  * `pixmaps/task-list.png` (was: `stock_todo.png`)
  * `pixmaps/attachment.png` (was: `mail-attachment.png`)
* From Gtk+ 2.8
  * `pixmaps/link.png` (was: `stock_connect_24.png`)
* `pixmaps/calendar.png` (was: `stock_calendar-view-month.png`)
  Copyright 2007 by Jakub Steiner, released under GPL
  modifications copyright 2009 by Gabriel Hurley
