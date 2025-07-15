import asyncio
import ebest
from common import *
from app_keys import appkey, appsecretkey # app_keys.py 파일에 appkey, appsecretkey 변수를 정의하고 사용하세요

async def sample(api):
    request = {
        't1102InBlock': {
            'shcode': '005930', # 삼성전자
        }
    }
    response = await api.request('t1102', request)
    if not response: return print(f'요청실패: {api.last_message}')
    
    print_table(response.body['t1102OutBlock'])
    

async def main():
    api=ebest.OpenApi()
    if not await api.login(appkey, appsecretkey):
        return print(f'연결실패: {api.last_message}')
    await sample(api)
    await api.close()

if __name__ == '__main__':
    asyncio.run(main())
