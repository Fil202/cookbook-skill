from mycroft import MycroftSkill, intent_file_handler


class Cookbook(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cookbook.intent')
    def handle_cookbook(self, message):
        self.speak_dialog('cookbook')


def create_skill():
    return Cookbook()

