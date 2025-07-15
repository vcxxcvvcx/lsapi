# lsapi

패키지 설치 (가능한 최신버전 사용 권장)
pip install ebest

    일부 샘플은 prettytable, cryptography, padas, ta, matplotlib 패키지 필요
    pip install prettytable
    pip install cryptography
    pip install pandas
    pip install ta
    pip install matplotlib

    QT샘플은 PyQt6, qasync 필요
    pip install PyQt6
    pip install qasync


샘플 코드 이용
1. 샘플폴더에 app_keys.py 파일 생성
2. app_keys.py 파일에 아래와 같이 변수 세팅
    appkey = '발급받은 앱Key'
    appsecretkey = '발급받은 앱 비밀Key'
3. 샘플코드 실행

LS-OpenApi DevCenter 실행
python DevCenter.py
    LS증권 OpenApi 모든 요청/실시간 테스트 가능
    테스트베드 기능 포함
    개별 샘플파일 테스트 가능
    PyQt6, qasync, prettytable, cryptography 필요
퍼온것임
