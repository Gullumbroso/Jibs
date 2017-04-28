from services.sessions.Session import Session, Triggers


class Event(Session):
    def __init__(self, trigger=Triggers.NONE, persons=None, place=None, time=None, title=None, color=None):
        Session.__init__(self, "event", trigger, persons)
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

    def has_time(self):
        return self.time is not None

    def has_title(self):
        return bool(self.title)

    def has_place(self):
        return bool(self.place)

    def has_color(self):
        return self.color is not None

    def whats_next(self):
        if not self.has_time():
            return "time"

        if not self.has_title():
            return "title"

        if not self.has_place():
            return "place"

        if not self.has_color():
            return "color"

        if not self.has_persons():
            return "persons"

        return None

    def is_mandatory_done(self):
        return self.has_time() and self.has_title()

    def data_I_know(self):
        data = {}
        if self.persons:
            data["persons"] = self.persons
        if self.title:
            data["title"] = self.title
        if self.time:
            data["time"] = self.time
        if self.place:
            data["place"] = self.place
        if self.color:
            data["color"] = self.color

        return data