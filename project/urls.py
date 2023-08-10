from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),

]
