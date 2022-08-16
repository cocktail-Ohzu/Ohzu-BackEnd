from collections import Counter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from landingpage.models import Result
from landingpage.serializers import ResultSerializer


# 결과 페이지
class ResultView(APIView):
    def get(self, request):
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
