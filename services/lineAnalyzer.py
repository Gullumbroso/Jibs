import services.dateAnalyzer as da
import services.googleAnalyzer as ga

from services.sessions.Mail import *
from services.sessions.Drive import *
from services.sessions.Event import *
from services.sessions.Note import *
from services.sessions.Reminder import *


from enum import Enum


NOUNS_MAIL = ["mail", "e-mail", "email"]
NOUNS_REMINDER = ["reminder", "alarm"]
NOUNS_EVENT = ["event"]
NOUNS_NOTE = ["note", "keep"]
NOUNS_DRIVE = ["drive"]

class Actions(Enum):
    NONE = 0
    MAIL = 1
    REMINDER = 2
    EVENT = 3
    NOTE = 4
    DRIVE = 5


def line_analyzer(line):
    actions, triggers, places, persons, events = ga.google_analyzer(line)
    date = da.date_analyzer(line)

    action = None
    for tup in actions:
        verb, noun = tup
        if verb in ["send"]:
            action = Actions.MAIL
        elif verb in ["upload"]:
            action = Actions.DRIVE
        elif verb in ["save"]:
            if noun in ["event"] or noun in events:
                action = Actions.EVENT
            elif noun in NOUNS_NOTE:
                action = Actions.NOTE
        elif verb in ["write", "create", "set"]:
            if noun in NOUNS_MAIL:
                action = Actions.MAIL
            elif noun in NOUNS_REMINDER:
                action = Actions.REMINDER
            elif noun in NOUNS_EVENT:
                action = Actions.EVENT
        else:
            pass
        break

    if action == Actions.MAIL:
        return Mail(Triggers.NOW, persons, date)
    if action == Actions.DRIVE:
        return Drive(Triggers.NOW, persons)
    if action == Actions.EVENT:
        return Event(Triggers.NOW, persons, places, date, events)
    if Actions == Actions.REMINDER:
        return Reminder(Triggers.TIME, persons, date)
    if action == Actions.NOTE:
        return Note(Triggers.NOW, persons)

    print("ERRORRRRRRRRRRRRRR")
    # print("Actions: ", actions)
    # print("Actions: ", actions[:,1])
    #
    # print("Triggers: ", triggers)
    # print("Places: ", places)
    # print("Persons: ", persons)
    # print("Time: ", date)
    # print("Events: ", events)


if __name__ == '__main__':
    text = "create an event when i receive an e-mail"
    # text = "send a mail to me"
    ses = line_analyzer(text)
    print("end")
