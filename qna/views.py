from django.shortcuts import render

from qna.models import Inquiry
from qna.models import Answer
from accounts.models import Profile

from qna.serializers import InquirySerializer
from qna.serializers import AnswerSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def perform_create(self, serializer):
            serializer.save(owner=Profile.objetcs.get(user=self.request.user))

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


# @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     def answers_to_inquiry(self, request, *args, **kwargs):
#         snippet = self.objects.filter()
#         return Response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=Profile.objetcs.get(user=self.request.user))
