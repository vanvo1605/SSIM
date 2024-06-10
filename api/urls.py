from  django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import StudentViewSet, SemesterViewSet, ProgramViewSet, EnrollmentViewSet, LecturerViewSet

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('semester', SemesterViewSet)
router.register('program', ProgramViewSet)
router.register('lecturer', LecturerViewSet)
router.register('enrollment', EnrollmentViewSet)
urlpatterns = router.urls