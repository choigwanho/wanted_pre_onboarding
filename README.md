# 요구사항 해결
### 요구사항
- [O] 1. 채용공고 등록 
- [O] 2. 채용공고 수정
- [O] 3. 채용공고 삭제
- [O] 4-1. 채용공고 목록 조회
### 선택사항
- [O] 4-2. 채용공고 검색 기능
- [X] 5. 채용공고 상세 페이지 
- [X] 6. 채용공고 지원 기능
- [O] 로그인
- [O] 회원가입

### 필수 기술요건
- [O] ORM 사용 : Django ORM 사용 (save, delete ..)
- [O] RDBMS 사용 : PostgreSQL 사용

# 1. 프로젝트 셋팅
## 1.1 가상환경 
```
python -m venv myenv
cd myenv
cd Scripts
activate.bat
```

## 1.2 쿠키커터
```
pip install cookiecutter 
cookiecutter https://github.com/pydanny/cookiecutter-django 
```

## 1.3 패키지 설치
```
pip install -r requirements/local.txt
```

## 1.4 프로젝트 구조 파악
- config > settings : db 연동, urls 설정
- recruit > rcruitments, users : 앱 모델, 뷰, 폼, 시리얼라이저, urls 등 작업
- recruit > templates > 앱 이름 : 템플릿
- recruit > static : 정적 리소스 관리
```
C:.
├─config
│  ├─settings
│  │  └─__pycache__
│  └─__pycache__
├─docs
├─locale
├─recruit
│  ├─contrib
│  │  ├─sites
│  │  │  ├─migrations
│  │  │  │  └─__pycache__
│  │  │  └─__pycache__
│  │  └─__pycache__
│  ├─recruitments
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  ├─static
│  │  ├─css
│  │  │  ├─recruitments
│  │  │  └─users
│  │  ├─fonts
│  │  ├─images
│  │  │  └─favicons
│  │  └─js
│  ├─templates
│  │  ├─account
│  │  ├─pages
│  │  ├─recruitments
│  │  └─users
│  ├─users
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  ├─tests
│  │  └─__pycache__
│  ├─utils
│  └─__pycache__
├─requirements
├─utility
└─__pycache__
```


# 2. postgres DB 설치 및 프로젝트 연동
## 2.1 postgres 설치 및 DB 생성
pgAdmin에서 'recruit' Database 생성
![Image](https://i.imgur.com/il2Jr08.png)

## 2.2 settings >  base.py DB 연동 설정
```
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="postgres://{유저명}:{비밀번호}@localhost:{포트번호}/{DB명}",
    ),
}
```

## 2.3 모델 마이그레이션
```
python manage.py makemigrations
python manage.py migrate
```
![Image](https://i.imgur.com/jNTPonO.png)


# 3. 요구사항 분석 및 데이터 모델 생성
## 3.1 테이블 파악
![Image](https://i.imgur.com/I1snt79.png)


## 3.2 앱 및 모델 생성
#### users >  models.py
- Company : User = 1 : N

### recruitments >  models.py
```
django-admin startapp recruitments
```
- Recruitment : User = 1 : N

# 4. 기능 구현
## 로그인
![Image](https://i.imgur.com/NfB7HD5.png)

## 회원가입
![Image](https://i.imgur.com/CIOt359.png)
![Image](https://i.imgur.com/6WA6old.png)
* 옵션 설명
1: 개인회원(default), 0: 관리자, 1 ~ N : 회사

## 채용공고 목록 조회
- 회사/관리자 아이디로 로그인 시 오른쪽 상단 (+) 아이콘 활성화
- (+)을 통해 등록 가능
- 본인이 작성한 글인 경우 수정, 삭제 아이콘 활성화
![Image](https://i.imgur.com/yDPcjLE.png)

## 채용공고 등록
![Image](https://i.imgur.com/Zu6xIKH.png)

## 채용공고 수정
- 개별항목 모두 수정 가능
![Image](https://i.imgur.com/0zydHnG.png)
- 수정 결과
![Image](https://i.imgur.com/VYxmzbo.png)

## 채용공고 삭제
- before
![uploading...](http://i.imgur.com/uploading.png)
- after
![Image](https://i.imgur.com/A5313Yo.png)

## 채용공고 검색
- 내용으로 검색
![Image](https://i.imgur.com/4aoPyQV.png)

# 서버 실행 
```
py manage.py runserver
```

