from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
import services as services

class WhatToDo(APIView):
    def get(self, request):
        # Prepare the graph
        params = request.query_params
        if len(params) != 1:
            return Response("Please enter a url to parse.", status=status.HTTP_204_NO_CONTENT)
        else:
            first_answer = params['firstAnswer']
            session = services.lineAnalyzer.line_analyzer(first_answer)



            response = {
                'article_title': article_title,
                'article_content': article_content,
                'prediction': prediction,
                'confidence': score
            }

            return Response(response, status=status.HTTP_200_OK)
