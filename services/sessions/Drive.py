from services.sessions.Session import Session


class Drive(Session):
    def __init__(self, trigger=None, persons=None, file=None):
        Session.__init__(self, "drive", trigger, persons)
        self.file = file
        self.attachments = []

    def add_file(self, file):
        self.file = file





