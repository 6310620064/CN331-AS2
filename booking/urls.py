from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject_id>', views.subject, name='subject'),
    path('<subject_id>/enrollment', views.enrollment, name='enrollment'),
    path('enroll_list', views.enroll_list, name='enroll_list'),
    path('<subject_id>/unenrollment', views.unenrollment, name='unenrollment'), 
]