from django.shortcuts import render

import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vehicle
from .forms import UploadFileForm
#파일을 업로드, Excel 파일을 처리하여 데이터를 데이터베이스에 저장
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']

            try:
                # pandas를 사용하여 Excel 파일을 읽어온다.
                df = pd.read_excel(excel_file, skiprows=5)  #데이터를 6번째 행부터 읽어오기(인덱스는 
                # 0부터 시작하므로 skiprow=5로 저장)

                # DataFrame의 각 행을 Vehicle 객체로 변환하여 저장.
                for _, row in df.iterrows():    # df의 각 행을 반복하면서 처리
                    #df.iterrow(): DataFrame의 행들을 순차적으로 반환하는 반복자. 각 반복에서는 '(index, row)'튜플 반환
                    #'_'는 index를 받지만 사용하지 않겠다는 의미로, Python에서는 관례적으로 사용하지 않는 변수에 '_'를
                    #할당한다고 한다. 'row'는 실제 데이터가 있는 행을 나타내는 'Series' 객체
                    no_value = row['NO']    #현재 행에서 'NO'열에 해당하는 값을 가져온다. 
                    #'세차 제외'가 입력된 행은 무시
                    if isinstance(no_value, str) and '세차 제외' in no_value:
                        #if isinstance(no_value, str): no_value가 문자열 타입인지 확인
                        #'세차 제외' in no_value: no_value 문자열에 세차 제외라는 텍스트가 포함되어 있는지 확인
                        # 두 조건이 모두 참('True')인 경우, 해당 행은 세차 제외라고 표시된 데이터로 간주
                        continue # 해당 행은 건너뛰고 다음 행으로 이동

                    Vehicle.objects.create(
                        
                        no=row['NO'],
                        vehicle_number=row['차량번호'],
                        model=row['차 종']
                        
                        # 추가적인 필드들...
                        
                    )
                messages.success(request, '파일이 성공적으로 업로드되었습니다.')
            except Exception as e:
                messages.error(request, f'파일 처리 중 오류가 발생했습니다: {e}')

            return redirect('upload_file')

    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})
