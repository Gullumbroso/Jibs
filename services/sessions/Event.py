from services.sessions.Session import Session, Triggers


class Event(Session):
    def __init__(self, trigger=Triggers.NONE, persons=None, place=None, time=None, title=None, color=None):
        Session.__init__(self, trigger, persons)
        self.title = title
        self.place = place
        self.time = time
        self.color = color

    def add_to_title(self, text):
        self.title += text

    def set_place(self, place):
        self.place = place

    def set_time(self, time):
        self.time = time

    def set_color(self, color):
        self.color = color

