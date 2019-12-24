from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm


def index(request):
    return render(request, "index.html")


class RegisterView(FormView):  # 클래스 기반 View를 사용해서 코드 단축
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"  # 성공시 해당 url로 이동
