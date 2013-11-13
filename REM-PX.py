import sublime, sublime_plugin

class pxtoremCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():
                # retrieve the settings
                self.settings = sublime.load_settings('REM-PX.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)
                px = s[:-2]
                unit = s[-2:]

                # invalid unit, so just return the string
                if unit != "px":
                    rem = s
                # convert to rem
                else:
                    rem = float(px) / base_rem
                    rem = '{0:g}'.format(rem)
                    rem = str(rem) + 'rem'

                # Replace the selection with transformed text
                view.replace(edit, region, rem)

class remtopxCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():
                # retrieve the settings
                self.settings = sublime.load_settings('REM-PX.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)
                rem = s[:-3]
                unit = s[-3:]

                # invalid unit, so just return the string
                if unit != "rem":
                    px = s
                # convert to rem
                else:
                    px = float(rem) * base_rem
                    px = '{0:g}'.format(px)
                    px = str(px) + 'px'

                # replace the selection with transformed text
                view.replace(edit, region, px)