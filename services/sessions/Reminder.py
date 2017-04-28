from services.sessions.Session import Session


class Reminder(Session):
    def __init__(self, trigger=None, persons=None):
        Session.__init__(self, trigger, persons)
        self.text = ""

    def add_to_text(self, text):
        self.text += text


