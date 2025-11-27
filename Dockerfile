# 1. 베이스 이미지 가져오기 (가장 기본이 되는 웹 서버인 nginx를 사용)
FROM nginx:latest

# 2. 내가 만든 index.html 파일을 컨테이너 내부의 웹 서버 경로로 복사하기
COPY index.html /usr/share/nginx/html/index.html