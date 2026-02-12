import aiohttp
import aiohttp_socks
import asyncio

async def test():
    conn = aiohttp_socks.ProxyConnector.from_url('socks5://127.0.0.1:6987')
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(
            'https://www.okx.com/api/v5/public/time',
            timeout=aiohttp.ClientTimeout(total=15)
        ) as resp:
            print(f'OKX API Status: {resp.status}')
            print(await resp.text())

asyncio.run(test())
