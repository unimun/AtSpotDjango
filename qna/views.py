from django.shortcuts import render

from qna.models import Inquiry
from qna.models import Answer

from qna.serializers import InquirySerializer
from qna.serializers import AnswerSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)