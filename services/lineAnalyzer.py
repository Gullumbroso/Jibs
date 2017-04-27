import services.dateAnalyzer as da
import services.googleAnalyzer as ga

from enum import Enum


def line_analyzer(line):
    actions, triggers, places, persons, events = ga.google_analyzer(line)
    date = da.date_analyzer(line)

    print("Actions: ", actions)
    print("Triggers: ", triggers)
    print("Places: ", places)
    print("Persons: ", persons)
    print("Time: ", date)
    print("Events: ", events)


if __name__ == '__main__':
    text = "save a meeting tomorrow with Jack Hamilton and Mike at McDonalds"
    # text = "send a mail to me"
    line_analyzer(text)
