from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from exam.models import *
from .serializers import *
from django.core import serializers

import beeprint
import json


class ExamViewSet(viewsets.ModelViewSet):
    queryset = ExamTr.objects.all()
    serializer_class = ExamSerializer

    def create(self, request):
        cp = request.data.copy()
        cp['year'] = request.data['year'] + '-01-01'
        volume = int(cp['volume'])

        # generate questions
        # questions = serializers.serialize("json", QuestionTr.objects.order_by('?')[:volume])
        questions = QuestionTr.objects.order_by('?')[:volume].values()
        question_ids = list(questions.values_list('id', flat=True))
        cp['questions'] = str(question_ids)

        beeprint.pp(cp)
        serializer = self.get_serializer(data=cp)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        exam_id = serializer.data["id"]

        # Update ExamTr for questions field
        # s = ExamTr.objects.filter(id=exam_id).first()
        # s.questions = question_ids
        # s.save()

        # Serialize Response Data
        response_data = {
            "questions" : list(questions),
            "exam" : serializer.data,
        }
        # beeprint.pp(response_data)

        headers = self.get_success_headers(exam_id)     
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers, content_type='application/json')

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionTr.objects.all()
    serializer_class = QuestionSerializer
