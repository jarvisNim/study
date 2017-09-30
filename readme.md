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

