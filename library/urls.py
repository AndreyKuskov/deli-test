from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home_page'),
	path('book/<pk>', views.BookView.as_view(), name='book_inf'),
	path('add/', views.AddBook.as_view(), name='add_book'),
	path('registration/', views.Registration.as_view(), name='registration'),
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)