from enum import Enum


class Triggers(Enum):
    NONE = 0
    RECEIVE_MAIL = 1
    PLACE = 2
    TIME = 3
    NOW = 4


class Session:
    def __init__(self, stype, trigger, persons):
        self.stype = stype
        self.trigger = trigger

        if persons is None:
            self.persons = []
        else:
            self.persons = persons

    def add_person(self, person):
        self.persons.append(person)

    def set_trigger(self, trigger):
        self.trigger = trigger

    def has_persons(self):
        return bool(self.persons)
