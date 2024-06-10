from  django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import StudentViewSet, SemesterViewSet, ProgramViewSet

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('semester', SemesterViewSet)
router.register('program', ProgramViewSet)
urlpatterns = router.urls