from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from .models import Fcuser
from .forms import RegisterForm
from .forms import LoginForm


def index(request):
    return render(request, "index.html", {"email": request.session.get("user")})


class RegisterView(FormView):  # 클래스 기반 View를 사용해서 코드 단축
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"  # 성공시 해당 url로 이동

    # 유효성 검사와 모델 저장 작업을 분리
    # 유효성 검사가 끝난후에 실행
    # form.data.get()
    def form_valid(self, form):
        fcuser = Fcuser(email=form.data.get("email"),
                        password=make_password(form.data.get("password")),
                        level="user")
        fcuser.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):  # 세션 지정
        self.request.session["user"] = form.data.get("email")

        return super().form_valid(form)


def logout(request):
    if "user" in request.session:
        del request.session["user"]

    return redirect("/")
