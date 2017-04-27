import services.dateAnalyzer as da
import services.googleAnalyzer as ga


def line_analyzer(line):
    actions, triggers, places = ga.google_analyzer(line)
    date = da.date_analyzer(line)

    print("Actions: ", actions)
    print("Triggers: ", triggers)
    print("Places: ", places)
    print("Time: ", date)


if __name__ == '__main__':
    text = "I want to send a mail to friends when i'm in Jerusalem"
    text = "hi"
    line_analyzer(text)
