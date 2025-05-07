# Recloset-AI-LLM

## 프로젝트 개요

* **프로젝트 명**: Recloset-AI-LLM
* **설명**: AI 기반 손상 인식 및 솔루션 제공 시스템. 이미지 손상 유형 인식 결과를 전달받고, Gemini API를 통해 LLM 기반 텍스트 생성으로 사용자에게 적합한 해결 방법을 안내하는 Flask 서버 애플리케이션.
* **주요 기능**:

  * 이미지 기반 손상 인식 결과를 바탕으로 LLM 기반 텍스트 생성
  * Flask 서버로 사용자 요청 처리
  * Docker를 통한 배포

## 파일 구조 설명

* **Dockerfile**: Docker 이미지를 빌드하기 위한 설정 파일 / Flask 서버 및 필요한 라이브러리 설치
* **README.md**: 프로젝트 소개 및 사용 가이드
* **recloset\_llm.py**: Flask 서버의 메인 코드 / 이미지 인식 및 손상 해결 안내 처리, Gemini API를 통한 LLM 기반 안내 생성
* **recloset\_prompt.txt**: LLM 프롬프트 설정 파일 / Gemini API에 전달할 지시어 텍스트
* **recloset\_solution.xlsx**: 손상 유형별 해결 방법이 정리된 엑셀 파일
* **requirements.txt**: 프로젝트 실행에 필요한 Python 패키지 목록
* **templates/index.html**: 웹 인터페이스 템플릿

## 설치 및 실행 가이드

### Docker 사용

1. Docker 설치 확인:

   ```bash
   docker --version
   ```
2. Docker 이미지 빌드:

   ```bash
   docker build -t recloset-ai-llm .
   ```
3. Docker 컨테이너 실행:

   ```bash
   docker run -d -p 5000:5000 recloset-ai-llm
   ```

### 로컬 실행

1. Python 환경 설정:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. 패키지 설치:

   ```bash
   pip install -r requirements.txt
   ```
3. Flask 서버 실행:

   ```bash
   python recloset_llm.py
   ```

## 사용 방법

1. 웹 브라우저에서 `http://localhost:5000`으로 접속
2. 이미지 업로드를 통해 손상 유형 분석 및 해결 방법 확인
3. 각 손상 유형에 대한 안내는 `recloset_solution.xlsx` 파일의 내용에 기반

## API 엔드포인트

* `/`: 서버 상태 확인 (GET)
* `/process_damage`: 손상 유형 처리 (POST)

  * JSON 요청 예시:

    ```json
    { "damage_type": "1" }
    ```
  * 응답 예시:

    ```json
    { "response": "Gemini API로 생성된 해결 안내 텍스트", "solution": "사전 정의된 손상 해결 방법" }
    ```
