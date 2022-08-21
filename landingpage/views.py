from collections import Counter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from landingpage.models import *
from landingpage.serializers import *
import random, json

# 질문 페이지
class QuestionView(APIView):
    def get(self, request):
        question_list = list(Question.objects.all())

        random_questions = random.sample(question_list, 9)
        print(random_questions)
        l = []
        for question in random_questions:
            l.append({"question": question.title, "attribute": question.attribute})

        return Response({"data": l}, status=status.HTTP_200_OK)



# 결과 페이지
class ResultView(APIView):
    def post(self, request):
        mbti = ''
        answer = request.data['data']

        # E/I
        if Counter(answer)['E'] >= 2:
            mbti += 'E'
        else:
            mbti += 'I'

        # N/S
        if Counter(answer)['N'] >= 2:
            mbti += 'N'
        else:
            mbti += 'S'

        # F/T
        if Counter(answer)['F'] >= 2:
            mbti += 'F'
        else:
            mbti += 'T'

        result = Result.objects.get(mbti=mbti)
        result_serializer = ResultSerializer(result)

        return Response(result_serializer.data, status=status.HTTP_200_OK)
