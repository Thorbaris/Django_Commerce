from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("login", views.login_view, name= "login"),
    path("logout", views.logout_view, name= "logout"),
    path("register", views.register, name= "register"),
    path("products/<str:entry>", views.entry, name= "entry"),
    path("search", views.search, name= "search"),
    path("publish", views.publish, name= "publish"),
    path("categories/<str:catid>", views.categoria, name= "categoria"),
    path("watchlist", views.watchlist, name= "watchlist")
]
