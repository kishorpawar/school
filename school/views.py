from rest_framework.response import Response
from rest_framework import generics
from school.serializers import StudentSerializer
from school.models import Enrolment, Student


class StudentView(generics.ListAPIView):
     serializer_class = StudentSerializer

     def get_queryset(self):
         tid = self.kwargs['tid']
         
         enrolments = Enrolment.objects.filter(cid__tid=tid).values('sid')
         return Student.objects.filter(id__in=enrolments)
         



