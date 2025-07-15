import asyncio
import ebest
from app_keys import appkey, appsecretkey

async def login_and_return_api():
    api = ebest.OpenApi()
    success = await api.login(appkey, appsecretkey)
    if not success:
        print(f'❌ 로그인 실패: {api.last_message}')
        return None
    print(f'✅ 로그인 성공 - 접속 서버: {"모의투자" if api.is_simulation else "실투자"}')
    return api

# 테스트 실행 전용
if __name__ == '__main__':
    async def main():
        api = await login_and_return_api()
        if api: await api.close()
    asyncio.run(main())
