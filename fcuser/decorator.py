from django.shortcuts import redirect
from .models import Fcuser


def login_required(function):  # 로그인 상태에서만 실행이 가능하도록 하는 데코레이터
    def wrap(request, *args, **kwargs):
        user = request.session.get("user")
        if user is None or not user:
            return redirect("/login/")

        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):  # 관리자 상태에서만 실행이 가능하도록 하는 데코레이터
    def wrap(request, *args, **kwargs):
        user = request.session.get("user")
        if user is None or not user:
            return redirect("/login/")

        user = Fcuser.objects.get(email=user)
        if user.level != "admin":
            return redirect("/")

        return function(request, *args, **kwargs)

    return wrap
