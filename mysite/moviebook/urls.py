from django.urls import path
from . import views

urlpatterns =[
    path("film_index/", views.FilmIndex.as_view(), name="filmovy_index"),
    path("<int:pk>/film_detail/", views.CurrentFilmview.as_view(), name= "filmovy_detail"),
    path("create_film/", views.CreateFilm.as_view(), name= "novy_film"),
]