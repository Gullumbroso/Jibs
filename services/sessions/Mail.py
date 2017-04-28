from services.sessions.Session import Session


class Mail(Session):
    def __init__(self, trigger=None, persons=None, time=None):
        Session.__init__(self, trigger, persons)
        self.time = time
        self.subject = ""
        self.body = ""
        self.attachments = []

    def add_to_subject(self, text):
        self.subject += text

    def add_to_body(self, text):
        self.body += text

    def set_time(self, time):
        self.time = time

