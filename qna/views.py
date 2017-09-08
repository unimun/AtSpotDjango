from django.shortcuts import render

from qna.models import Inquiry
from qna.models import Answer
from accounts.models import Profile

from qna.serializers import InquirySerializer
from qna.serializers import AnswerSerializer
from rest_framework import generics, viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


    def perform_create(self, serializer):
        serializer.save(owner=Profile.objects.get(user=self.request.user))

    @detail_route(renderer_classes=[renderers.JSONRenderer])
    def get_answer(self, request, *args, **kwargs):
        answer = Answer.objects.filter(inquiry=self.get_object()).last()
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def answers_to_inquiry(self, request, *args, **kwargs):
    #     snippet = self.objects.filter()
    #     return Response(snippet.highlighted)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
            serializer.save(owner=Profile.objects.get(user=self.request.user))

    @detail_route(renderer_classes=[renderers.JSONRenderer])
    def answer_to_inquiry(self, request, pk):
        answer = Answer.objects.filter(inquiry=pk).last()
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
