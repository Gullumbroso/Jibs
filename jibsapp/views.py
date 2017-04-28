from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
import services as services
from services.lineAnalyzer import *

session = None

class FirstAnswer(APIView):
    def get(self, request):
        # Prepare the graph
        params = request.query_params
        if len(params) != 1:
            return Response("Please enter a url to parse.", status=status.HTTP_204_NO_CONTENT)
        else:
            first_answer = params['firstQuestion']
            session = line_analyzer(first_answer)

            response = {
                'type': session.stype,
                'data': session.data_I_know(),
                'next': session.whats_next(),
                'is_done': session.is_mandatory_done()
            }

            return Response(response, status=status.HTTP_200_OK)


class updateData(APIView):
    def get(self, request):
        # Prepare the graph
        params = request.query_params
        if len(params) != 1:
            return Response("Please enter a url to parse.", status=status.HTTP_204_NO_CONTENT)
        else:
            if params['type'] == "content":
                session.add_to_subject(params['answer']['subject'])
                session.add_to_body(params['answer']['body'])

            if params['type'] == "people":
                session.add_person(params['answer'])

            response = {
                'type': session.stype,
                'data': session.data_I_know(),
                'next': session.whats_next(),
                'is_done': session.is_mandatory_done()
            }

            return Response(response, status=status.HTTP_200_OK)
