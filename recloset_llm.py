from flask import Flask, request, jsonify
import json
import os
import pandas as pd
import google.generativeai as genai
from flask_cors import CORS
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv(dotenv_path=".env")

# 환경 변수에서 API_KEY를 불러오기
api_key = "api-key"

# API 키 설정
genai.configure(api_key=api_key)

# 모델 설정
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
CORS(app, origins=["https://your-frontend-domain.com"])

# xlsx 파일 로딩 (손상 설명 + 해결 방법)
def load_damage_solutions(file_path="recloset_solution.xlsx"):
    df = pd.read_excel(file_path)
    solutions = dict(zip(df['유형'].astype(str), df['해결 방법']))
    descriptions = dict(zip(df['유형'].astype(str), df['손상 설명']))
    return solutions, descriptions

# recloset_prompt.txt 불러오기
def load_prompt_template(file_path="recloset_prompt.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} 파일을 찾을 수 없습니다.")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# JSON 데이터에서 오염 유형에 맞는 해결 방법 가져오기
def get_solution_for_damage_type(damage_type, solutions_data):
    return solutions_data.get(str(damage_type), "해당 오염 유형에 대한 해결 방법을 찾을 수 없습니다.")

@app.route('/process_damage', methods=['POST'])
def process_damage():
    try:
        data = request.get_json()
        damage_type = data.get('damage_type', None)

        if not damage_type or not damage_type.isdigit():
            return jsonify({"error": "Invalid or missing 'damage_type' parameter."}), 400

        damage_type = int(damage_type)

        solutions_data, descriptions_data = load_damage_solutions()
        solution = get_solution_for_damage_type(damage_type, solutions_data)
        damage_description = descriptions_data.get(str(damage_type), "손상 유형을 찾을 수 없습니다.")
        
        # 프롬프트 템플릿 읽기 및 {damage_description} 치환
        prompt_template = load_prompt_template()
        prompt_to_send = prompt_template.replace("{damage_description}", damage_description)

        # Gemini API 호출
        completion = model.generate_content(
            prompt_to_send,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 200
            }
        )

        response_text = completion.text

        # 후처리
        response_text = response_text.strip('"')
        response_text = response_text.replace("\\", "")
        response_text = response_text.replace("\n", " ")
        response_text = response_text.replace("\t", " ")
        response_text = response_text.replace('\"', '')
        response_text = response_text.strip()

        try:
            response_text = json.loads(f'"{response_text}"')
        except json.JSONDecodeError:
            pass

        response_data = {
            "response": response_text,
            "solution": solution
            #object
        }

        return app.response_class(
            response=json.dumps(response_data, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format: JSON parsing failed."}), 400
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "ReCloset LLM API server is running."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

# /process_damage test
# curl -X POST http://127.0.0.1:5000/process_damage \
#    -H "Content-Type: application/json" \
#    -d '{"damage_type": "1"}'
