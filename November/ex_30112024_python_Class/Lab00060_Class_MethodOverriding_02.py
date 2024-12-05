# MethodOverriding Real time examples
class OldBrowser:
    def start_browse(self):
        print("IE Browser starts")

    def stop_browser(self):
        print("IE Browser is closing")


class Chrome(OldBrowser):
    def start_browse(self):
        super().start_browse() #Here Super() means it will call parent method
        print("Better Chrome Browser is starting ")

    def stop_browser(self):
        print("Better Chrome Browser is stopping")



# object creation
obj_ref = Chrome()
obj_ref.start_browse()
obj_ref.stop_browser()
