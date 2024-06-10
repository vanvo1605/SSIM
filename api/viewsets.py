from rest_framework import viewsets
from .models import Student, Semester, Program
from .serializers import StudentSerializer, SemesterSerializer, ProgramSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
