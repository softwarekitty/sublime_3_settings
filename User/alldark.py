import sublime, sublime_plugin, os, sys, re

#note, commentjson lib is just one regex - strips comments
#this is fragile and should not strip comments, using temporarily
#a better version would parse using antlr or similar and preserve
#comments and json order.  most subl packages seem to behave
#badly by stripping comments and re-organizing the order
#this plugin will have to do that for now.
#good opportunity for a popular project: subl_settings_parser

#named users_path bc moving this file would change this logic!
users_path = os.path.abspath(os.path.dirname(__file__))
parsing_library_path = os.path.join(users_path,"libs/commentjson")
sys.path.append(parsing_library_path)
import commentjson

class AlldarkCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        for fileName in os.listdir(users_path):
            if fileName.endswith(".sublime-settings"):
                print("running alldark on settings file: " + fileName)

                with open (os.path.join(users_path,fileName), "r+") as setup:
                    try:
                        setupObject = commentjson.load(setup)
                        self.setToDark(setupObject, fileName)
                    except:
                        # todo - maybe pass out message? could come from elsewhere
                        print("json parsing error in file: "+fileName)


    def setToDark(self, setupJson, setting_filename):
        if "color_scheme" not in setupJson:
            print("no color scheme found in file: " +setting_filename)
        elif "color_scheme_dark" not in setupJson:
            print("no dark color scheme found")
        else:
            print("setting color scheme to contents of color_scheme_dark")
            setupJson["color_scheme"] = setupJson["color_scheme_dark"]
            with open (os.path.join(users_path,setting_filename), "w") as setup:
                    commentjson.dump(setupJson,setup, indent=4, sort_keys=True)
