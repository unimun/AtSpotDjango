from rest_framework import serializers  
from qna.models import Inquiry
from qna.models import Answer


class InquirySerializer(serializers.ModelSerializer):  
    class Meta:
        model = Inquiry
        fields = ('id', 'contents', 'point', 'created_on', 'owner')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'owner', 'inquiry', 'image')