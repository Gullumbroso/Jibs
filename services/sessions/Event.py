from services.sessions.Session import Session, Triggers


class Event(Session):
    def __init__(self, trigger=Triggers.NONE, persons=None, place=None, time=None, color=None):
        Session.__init__(self, trigger, persons)
        self.subject = ""
        self.place = place
        self.time = time
        self.color = color
        self.attachments = []

    def add_to_subject(self, text):
        self.subject += text

    def set_place(self, place):
        self.place = place

    def set_time(self, time):
        self.time = time

    def set_color(self, color):
        self.color = color

