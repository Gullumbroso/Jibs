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

    def what_missing(self):
        json = {}
        if self.time is None:
            json["time"] = {"Missing": True, "Mandatory": False}
        else:
            json["time"] = {"Missing": False, "Mandatory": False}

        if self.subject == "":
            json["subject"] = {"Missing": True, "Mandatory": True}
        else:
            json["subject"] = {"Missing": False, "Mandatory": True}

        if self.body == "":
            json["body"] = {"Missing": True, "Mandatory": True}
        else:
            json["body"] = {"Missing": False, "Mandatory": True}

        if len(self.persons) == 0:
            json["persons"] = {"Missing": True, "Mandatory": True}
        else:
            json["persons"] = {"Missing": False, "Mandatory": True}