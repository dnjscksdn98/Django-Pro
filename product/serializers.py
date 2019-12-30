from rest_framework import serializers
from .models import Product

# serializer : api를 만들때 form이 하던 역할을 해줌


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product  # 사용할 모델 지정
        fields = "__all__"  # 선택한 모델의 모든 필드들을 자동으로 가져옴
