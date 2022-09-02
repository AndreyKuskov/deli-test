from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddNewBookForm, RegistrationForm
from .models import Book
import typing as tp


class HomeView(ListView):
    model = Book
    template_name: str = 'library/home.html'

class BookView(DetailView):
    model = Book
    template_name: str = 'library/book.html'

class AddBook(LoginRequiredMixin, CreateView):
    form_class = AddNewBookForm
    template_name: str = 'library/add_new_book.html'
    success_url: tp.Optional[str] = '/'
    login_url = '/login/'

    def post(self, request: HttpRequest, *args: tp.Any, **kwargs: tp.Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        response = JsonResponse({"error": "Проверьте введенные данные!"})
        response.status_code = 403
        return response

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddBook, self).form_valid(form)

class Registration(CreateView):
    template_name: str = 'library/registration.html'
    form_class = RegistrationForm
    success_url: tp.Optional[str] = '/'

    def post(self, request: HttpRequest, *args: tp.Any, **kwargs: tp.Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        response = JsonResponse({
            "error": "Не получилось зарегистрировать пользователя! Проверьте введенные данные!"
            })
        response.status_code = 403
        return response

class Login(LoginView):
    template_name: str = 'library/login.html'

    def post(self, request: HttpRequest, *args: tp.Any, **kwargs: tp.Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        response = JsonResponse({"error": "Проверьте введенные данные!"})
        response.status_code = 403
        return response

class Logout(LogoutView):
    next_page: tp.Optional[str] = '/'