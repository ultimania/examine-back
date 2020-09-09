from rest_framework import serializers

from exam.models import *


class ExamSerializer(serializers.ModelSerializer):
    questions = serializers.CharField(required=False)
    answers = serializers.CharField(required=False)

    class Meta:
        model = ExamTr
        fields = (
            'id',
            'volume',
            'scope',
            'year',
            'questions',
            'answers',
        )


class QuestionSerializer(serializers.ModelSerializer):
    select5  = serializers.CharField(required=False)
    select6  = serializers.CharField(required=False)
    select7  = serializers.CharField(required=False)
    select8  = serializers.CharField(required=False)
    select9  = serializers.CharField(required=False)
    select10 = serializers.CharField(required=False)

    class Meta:
        model = QuestionTr
        fields = (
            'id',
            'text',
            'exam_class',
            'year',
            'select1',
            'select2',
            'select3',
            'select4',
            'select5',
            'select6',
            'select7',
            'select8',
            'select9',
            'select10',
            'explanation',
        )
