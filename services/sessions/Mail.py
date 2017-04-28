from services.sessions.Session import Session


class Mail(Session):
    def __init__(self, trigger=None, persons=None, time=None):
        Session.__init__(self, "mail", trigger, persons)
        self.time = time
        self.subject = ""
        self.body = ""

    def add_to_subject(self, text):
        self.subject += text

    def add_to_body(self, text):
        self.body += text

    def set_time(self, time):
        self.time = time

    def has_time(self):
        return self.time is not None

    def has_subject(self):
        return bool(self.subject)

    def has_body(self):
        return bool(self.body)

    def whats_next(self):
        if not self.has_subject():
            return "subject"

        if not self.has_body():
            return "body"

        if not self.has_persons():
            return "persons"

        if not self.has_time():
            return "time"

        return None

    def is_mandatory_done(self):
        return self.has_persons() and self.has_subjectt() and self.has_body

    def data_I_know(self):
        if self.persons:
            data["persons"] = self.persons
        if self.subject:
            data["subject"] = self.subject
        if self.body:
            data["body"] = self.body
        if self.time:
            data["time"] = self.time

        return data
