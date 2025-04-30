# 베이스 이미지 설정
FROM python:3.9-slim

# 환경변수 파일 위치 (RUN 전에)
ENV ENV_FILE_PATH=/app/recloset.env

# 작업 디렉토리 설정
WORKDIR /app 

# 프로젝트 파일을 컨테이너로 복사
COPY . /app  

# 필요한 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 포트 노출
EXPOSE 5000  

# 애플리케이션 실행
CMD ["python", "recloset_llm.py"]
