from services.sessions.Session import Session


class Reminder(Session):
    def __init__(self, trigger=None, persons=None, time=None):
        Session.__init__(self, trigger, persons)
        self.text = ""
        self.time = time

    def add_to_text(self, text):
        self.text += text

    def set_time(self, time):
        self.time = time



