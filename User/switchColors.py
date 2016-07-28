import sys
import os
import sublime
import sublime_plugin

# PPA_PATH = list()
# PYMAMI = '{0}{1}'.format(*sys.version_info[:2])
# ST_VERSION = 3000 if sublime.version() == '' else int(sublime.version())
# PLUGIN_NAME = "Python PEP8 Autoformat"
# SETTINGS_FILE = 'pep8_autoformat.sublime-settings'

# #-- Cannot use sublime.packages_path() with ST3 because of inconsistency
# #-- of returned path between bootstap time vs running time.
# #pkg_path = os.path.join(sublime.packages_path(), PLUGIN_NAME)
# pkg_path = os.path.abspath(os.path.dirname(__file__))
# libs_path = os.path.join(pkg_path, 'libs')
# PPA_PATH.append(libs_path)

# versionlibs_path = os.path.join(pkg_path, 'libs', 'py' + PYMAMI)
# if os.path.exists(versionlibs_path):
#     PPA_PATH.append(versionlibs_path)

print('SIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVASIVA')
[sys.path.insert(0, p) for p in PPA_PATH if p not in sys.path]

try:
    import ppaautopep8 as autopep8
    import ppaMergeUtils as MergeUtils
except:
    sublime.error_message(
        '{0}: import error: {1}'.format(PLUGIN_NAME, sys.exc_info()[1]))
    raise
