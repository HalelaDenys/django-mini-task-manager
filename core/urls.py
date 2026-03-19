from django.urls import path

from core.views import LandingPageView

app_name = "core"
urlpatterns = [
    path("", LandingPageView.as_view(), name="landing_page"),
]
