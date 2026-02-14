from flask import Flask, render_template, request, jsonify

app = Flask(__name__) # Flask 앱 생성

# 데이터를 저장할 리스트 (실제로는 DB 사용)
records = []

@app.route('/') # 메인 페이지
def index():
    """HTML 페이지 렌더링"""
    return render_template('index.html')

@app.route('/api/records', methods=['GET']) # 내역 조회 API
def get_records():
    """모든 거래 내역 반환"""
    return jsonify(records)

@app.route('/api/records', methods=['POST']) # 내역 추가 API
def add_record():
    """수입/지출 추가"""
    data = request.json # 프론트엔드에서 보낸 JSON 데이터
    record = {
        'type' : data['type'],     # '수입' 또는 '지출'
        'amount' : data['amount'], # 금액
        'memo' : data['memo']      # 메모
    }
    records.append(record)
    return jsonify({'success' : True, 'record': record})

@app.route('/api/records/<int:index>', methods=['DELETE']) # 내역 삭제 API
def delete_record(index):
    """특정 내역 삭제"""
    try:
        if 0 <= index < len(records):
            deleted = records.pop(index)
            return jsonify({'success' : True, 'deleted' : deleted})
        return jsonify({'success' : False, 'error' : '잘못된 인덱스'}), 400
    except Exception as e:
        return jsonify({'success' : False, 'error' : str(e)}), 500
    
@app.route('/api/balance', methods=['GET']) # 잔액 조회 API
def get_balance():
    """총 수입, 지출, 잔액 계산"""
    total_income = sum(r['amount'] for r in records if r['type'] == '수입')
    total_expense = sum(r['amount'] for r in records if r['type'] == '지출')
    balance = total_income - total_expense

    return jsonify({
        'total_income' : total_income,
        'total_expense' : total_expense,
        'balance' : balance
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) # 개발 서버 실행 (http://localhost:5000)