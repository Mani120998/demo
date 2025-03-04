from django.shortcuts import render
from rest_framework.decorators import api_view
from TestApp.models import student
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def studententry(request):
    name = request.data['name']
    standard = request.data['standard']
    section = request.data['section']
    grade = request.data['grade']
    student.objects.create(studentname=name,standard=standard,section=section,grade=grade)
    return Response('success')

