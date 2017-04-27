from enum import Enum


class Triggers(Enum):
    NONE = 0
    RECEIVE_MAIL = 1
    PLACE = 2
    TIME = 3
    NOW = 4



class Session:
    def __init__(self, trigger, persons):
        self.trigger = trigger
        self.is_ready = False

        if persons is None:
            self.persons = []
        else:
            self.persons = persons

    def add_person(self, person):
        self.persons.append(person)

    def set_trigger(self, trigger):
        self.trigger = trigger
