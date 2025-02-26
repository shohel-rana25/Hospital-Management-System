from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views


router =DefaultRouter()
router.register('doctor', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('specialization', views.SpecializationViewset)
router.register('review', views.ReviewViewset)
router.register('available_time', views.AvailableTimeViewset)

urlpatterns = [
    path('', include(router.urls)),
]