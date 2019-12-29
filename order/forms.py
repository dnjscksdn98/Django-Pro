from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser


class OrderForm(forms.Form):
    # 1. 객체 생성시 상품 상세보기 페이지로부터 request를 전달받음, request에 접근하기 위해서(session에 접근하기 위해)
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={"required": "수량을 입력해주세요."},
        label="수량"
    )
    product = forms.IntegerField(
        error_messages={"required": "상품을 고르세요."},
        label="상품",
        widget=forms.HiddenInput  # 사용자한테는 실제로 보이지 않게
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product = cleaned_data.get("product")

        if not (quantity and product):
            self.add_error("quantity", "값이 없습니다.")
            self.add_error("product", "값이 없습니다.")
