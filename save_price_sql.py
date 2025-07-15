import asyncio
import pymysql
from ebest import OpenApi
from app_keys import appkey, appsecretkey

# MySQL 연결 정보
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '****',  # ← 본인 비밀번호로 변경
    'database': 'stock_data',
    'charset': 'utf8mb4'
}

# DB 저장 함수
def save_snapshot(data):
    try:
        sign = data['sign']  # "1": 상승, "2": 보합, "3": 하락
        change = int(data['change'])

        # 등락 부호 반영
        if sign == "1":
            change_amt = change
        elif sign == "3":
            change_amt = -change
        else:
            change_amt = 0

        with pymysql.connect(**MYSQL_CONFIG) as conn:
            with conn.cursor() as cur:
                sql = """
                INSERT INTO stock_price_snapshot (
                    shcode, hname, price, change_amt, change_pct, volume
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """
                cur.execute(sql, (
                    data['shcode'],
                    data['hname'],
                    int(data['price']),
                    change_amt,
                    float(data['diff']),
                    int(data['volume'])
                ))
            conn.commit()
        print(f"✅ 저장 완료: {data['hname']} {data['price']}원, 거래량 {data['volume']}")
    except Exception as e:
        print(f"❌ DB 저장 실패: {e}")


# API 요청 및 처리
async def fetch_and_save():
    api = OpenApi()
    if not await api.login(appkey, appsecretkey):
        print(f"❌ 로그인 실패: {api.last_message}")
        return

    request = {
        't1102InBlock': {
            'shcode': '005930'  # 삼성전자
        }
    }
    response = await api.request('t1102', request)
    if not response:
        print(f"❌ 데이터 요청 실패: {api.last_message}")
    else:
        data = response.body['t1102OutBlock']
        save_snapshot(data)

    await api.close()

if __name__ == '__main__':
    asyncio.run(fetch_and_save())
