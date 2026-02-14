// script.js - 프론트엔드 로직

// 페이지 로드 시 데이터 불러오기
window.addEventListener('load', () => {
    loadRecords();
    updateBalance();
});

// 거래 내역 불러오기
async function loadRecords() {
    try {
        const response = await fetch('/api/records');
        const records = await response.json();

        const recordsList = document.getElementById('recordsList');
        recordsList.innerHTML = '';

        if (records.length == 0) {
            recordsList.innerHTML = '<li class="empty-message">거래 내역이 없습니다.</li>';
            return;
        }

        records.forEach((record, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <div class="record-info">
                  <span class="record-type ${record.type === '수입' ? 'income' : 'expense'}">${record.type}</span>
                  <strong>${record.amount.toLocaleString()}원</strong> - ${record.memo}
              </div>
              <button class="delete-btn" onclick="deleteRecord(${index})">삭제</button>
         `;
         recordsList.appendChild(li);
        });
    } catch (error) {
            console.error('내역 불러오기 실패:', error);
    }
}

// 거래 추가
async function addRecord() {
    const type = document.getElementById('type').value;
    const amount = parseInt(document.getElementById('amount').value);
    const memo = document.getElementById('memo').value;

    if (!amount || amount <= 0) {
        alert('올바른 금액을 입력해주세요.');
        return;
    }

    if (!memo.trim()) {
        alert('내용을 입력해주세요');
        return;
    }

    try {
        const response = await fetch('/api/records', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({type, amount, memo})
        });

        const result = await response.json();

        if (result.success) {
            // 입력 필드 초기화
            document.getElementById('amount').value = '';
            document.getElementById('memo').value = '';

            // 목록 새로고침
            loadRecords();
            updateBalance();
        }
    } catch (error) {
        console.error('추가 실패: ', error);
        alert('추가에 실패했습니다.');
    }
}

// 거래 삭제
async function deleteRecord(index) {
    if (!confirm('정말 삭제하시겠습니까?')) {
        return;
    }

    try {
        const response = await fetch(`/api/records/${index}`, {
            method: 'DELETE'
        });

        const result  = await response.json();

        if (result.success) {
            loadRecords();
            updateBalance();
        }
    } catch (error) {
        console.error('삭제 실패: ', error);
        alert('삭제에 실패했씁니다.');
    }
}

// 잔액 업데이트
async function updateBalance() {
    try {
        const response = await fetch('/api/balance');
        const data = await response.json();
        
        console.log('잔액 데이터:', data);  // 디버깅용 추가
    
        document.getElementById('totalIncome').textContent = `${data.total_income.toLocaleString()}원`;        
        document.getElementById('totalExpense').textContent = `${data.total_expense.toLocaleString()}원`;        
        document.getElementById('balance').textContent = `${data.balance.toLocaleString()}원`;        
    } catch (error) {
        console.error('잔액 조회 실패:', error);
    }
}