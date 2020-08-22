from django.conf.urls import url
from AwardWinningFilmsAPI import views

urlpatterns = [
    url(r'^api/films/count$', views.total_films)
]