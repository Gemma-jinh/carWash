from django import forms    #폼 클래스는 HTML 폼과 그에 연결된 데이터 처리 로직을 관리하는 데 사용
                            #폼을 사용하면 사용자 입력을 쉽게 수집, 검증, 저장할 수 있다.
                            #'forms'를 통해 Django의 기본 폼 클래스 및 필드들을 사용할 수 있다.

class UploadFileForm(forms.Form):   #파일 업로드 폼을 정의. 파일을 서버로 업로드 할 수 있게 한다.
    file = forms.FileField()    #FileField: HTML의 <input type="file">요소에 해당. 파일 업로드 처리 기능
                                #forms.FileField(): 파일 업로드 관련 유효성 검사 자동 처리