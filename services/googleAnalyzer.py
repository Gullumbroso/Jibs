# Imports the Google Cloud client library
from google.cloud import language
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

credentials = GoogleCredentials.get_application_default()

service = build('compute', 'v1', credentials=credentials)


# Instantiates a client
language_client = language.Client()


def google_analyzer(line):
    document = language_client.document_from_text(line)
    annotations = document.annotate_text(include_sentiment=False)

    # ACTION & TRIGGERS:
    num_words = len(annotations.tokens)
    edges = [[] for i in range(num_words)]

    for i in range(num_words):
        edges[int(annotations.tokens[i].edge_index)].append(i)

    actions = []
    triggers = []
    # for token in annotations.tokens:
    for i in range(num_words):
        token = annotations.tokens[i]
        if token.part_of_speech == "VERB":
            for e in edges[i]:
                if annotations.tokens[e].part_of_speech == "NOUN":
                    actions.append((token.text_content, annotations.tokens[e].text_content))


        # print('         text_content: %s' % (token.text_content,))
        # print('         text_begin : %s' % (token.text_begin ,))
        # print('         part_of_speech : %s' % (token.part_of_speech ,))
        # print('         edge_index : %s' % (token.edge_index  ,))
        # print('         edge_label : %s' % (token.edge_label ,))
        # print('         lemma : %s' % (token.lemma ,))
        # print("=========================================================")



    # PLACE
    places = []
    persons = []
    events = []
    for entity in annotations.entities:
        if entity.entity_type in ["ORGANIZATION", "LOCATION"]:
            places.append(entity.name)
        elif entity.entity_type in ["PERSON"]:
            persons.append(entity.name)
        elif entity.entity_type in ["EVENT"]:
            events.append(entity.name)

    return actions, triggers, places, persons, events


if __name__ == '__main__':
    google_analyzer('i want to send an e-mail when i arrive to my home')
