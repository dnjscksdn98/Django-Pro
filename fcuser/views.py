from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .forms import LoginForm


def index(request):
    return render(request, "index.html", {"email": request.session.get("user")})


class RegisterView(FormView):  # 클래스 기반 View를 사용해서 코드 단축
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"  # 성공시 해당 url로 이동


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):  # 세션 지정
        self.request.session["user"] = form.email
        return super().form_valid(form)
