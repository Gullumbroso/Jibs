from services.sessions.Session import Session


class Note(Session):
    def __init__(self, trigger=None, persons=None):
        Session.__init__(self, trigger, persons)
        self.subject = ""
        self.body = ""

    def add_to_subject(self, text):
        self.subject += text

    def add_to_body(self, text):
        self.body += text



