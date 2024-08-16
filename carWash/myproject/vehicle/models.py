from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20, unique=True)    #차량 번호 #고유 제약 조건 추가
    model = models.CharField(max_length=50)     #차량 모델
    no = models.IntegerField(default=0)  #NO
    # 다른 필드들...

    def __str__(self):      #객체를 나타낼 때 사용되는 문자열 표현을 정의
        return self.vehicle_number  #vehicle 객체를 호출할 때, vehicle_number 값을 반환된다.
                        # 'A12345'라는 차량번호를 예로 들면 "'A12345'"라는 문자열로 반환시키는 것으로 보인다.
