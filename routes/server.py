from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PORTONE_API_SECRET = 'YOUR_PORTONE_API_SECRET'  # 포트원 콘솔에서 발급받은 API 시크릿

@app.route('/payment/complete', methods=['POST'])
def payment_complete():
    data = request.json
    payment_id = data.get('paymentId')
    order_id = data.get('orderId')  # 필요에 따라 주문 ID를 사용

    try:
        # 1. 포트원 결제내역 단건조회 API 호출
        headers = {'Authorization': f'PortOne {PORTONE_API_SECRET}'}
        payment_response = requests.get(f'https://api.portone.io/payments/{payment_id}', headers=headers)

        if payment_response.status_code != 200:
            return jsonify({'error': 'Payment verification failed'}), 400

        payment = payment_response.json()

        # 2. 고객사 내부 주문 데이터의 가격과 실제 지불된 금액을 비교
        # 이 부분은 실제로 주문 데이터를 가져오는 로직을 구현해야 합니다.
        order = {'amount': 1000}  # 예시용 데이터
        if order['amount'] == payment['amount']['total']:
            if payment['status'] == 'VIRTUAL_ACCOUNT_ISSUED':
                # 가상 계좌 발급 처리
                pass
            elif payment['status'] == 'PAID':
                # 결제 완료 처리
                pass
            return jsonify({'status': 'success'})
        else:
            return jsonify({'error': 'Payment amount mismatch'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400
