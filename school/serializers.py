from rest_framework import serializers
from school.models import Student

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.StringRelatedField()
    class Meta:
        model = Student
        fields = ('name',)

