[2017/09/30: 0일차]

1) /var/www 웹서버 www-data 계정  설정
https://blog.xianchoi.kr/268

2) /var/www 웹서버 디렉토리 설정
http://abipictures.tistory.com/m/918

3) django 설정 + uswgi + nginx 연결
http://brownbears.tistory.com/16
http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html




[2017/09/31: 1일차]

4) uwsgi 오류로 (502 Bad Gateway) 설치/삭제/설치 지속 반복 했으나,
   결국 plugin 모듈이 없어서 restart 가 안되었음.
sudo apt-get install uwsgi-plugin-python
* venv 모드를 꼭 잊지말것
** uwsgi 를 venv모드가 아닌 전체모드로 개선 -> uwsgi 기동시 deactivate 할것
*** reboot 시 uwsgi emperor 모드로 기동은 하는데 nginx 와 연동은 안되어
    일단 매뉴얼로 기동하고 추후 다시 보완 필요.

5) githun 동기화

6) /etc/hosts 파일에 www.mirae00.com, mirae00.com, blog, iot 서브도메인 등록

7) nginx.conf 에서 blog, iot 노드 가상서버 설정 및 기동



[2017.10.01: 2일차]

8) postgresql 설치
   sudo su - postgres
   psql
   - db : mirae_db
   - user : miraeuser
   - password : 1234

   - db : blog_db
   - user : bloguser
   - password : 1234

9) django + postgresql 연동 --> www.mirae website
   - settings.py
   - createsuperuser
     . admin, dlalwl00, admin@miraelabs.com, dlalwl00

10) nodejs(express) + mongodb 연동  --> iot.mirae website
   - express, body-parser, mongoose 설치

11) nodejs(express) + postgresql 연동  --> blog.mirae website
   - pg, pgadmin3
 
12) pystagram(django) tutorial 수행 
   *** django 는 기본적으로  One Project, Multi app


[2017.10.02: 3일차]

13) django 설정파일 ( /admin 의 nginx.conf (not uwsgi.ini) 설정 오류로 초기css적용안되어 6시간이상 해멤...)
   - uwsgi, settings.py 쪽 오류로 css 파일을 찾지 못한다고 생각하고 여러가지 설정 바꿔가면 테스트 하였으나, 
     계속 실패.
   - nginx.conf 내 locatio /static 설정값 추가로 path 맞춤.  ^^

14) /blog tutorial 찾음 (pystagram)
http://blog.hannal.com/category/start-with-django-webframework/
   - node.js, express, postgresql 기술 검증

15) /iot tutorial 검색중
   - 후보 1:  아두이노와 node.js 로 연결하여 자율주행
   - 후보 2:  아두이노, 펜마우스, node.js 연결



[2017.10.03: 4일차] 

16) 
