from django.urls import path
from scam_report import views

app_name = "scam_report"

urlpatterns = [
    path('predict/email-scam', views.predictEmailScam),
    path ('upload-file', views.upload_file, name="upload"),
]