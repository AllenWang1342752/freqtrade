import asyncio
import ccxt.async_support as ccxt_async


async def test_async():
    print("=== Testing async CCXT with socks5 proxy ===")
    exchange = ccxt_async.okx({
        'proxies': {
            'http': 'socks5h://127.0.0.1:6987',
            'https': 'socks5h://127.0.0.1:6987',
        },
        'aiohttp_proxy': 'socks5://127.0.0.1:6987',
        'timeout': 30000,
    })
    try:
        time_result = await exchange.fetch_time()
        print(f"Async fetch_time OK: {time_result}")

        print("Trying fetch_tickers...")
        tickers = await exchange.fetch_tickers(params={'instType': 'SPOT'})
        print(f"Async fetch_tickers OK: got {len(tickers)} tickers")
    except Exception as e:
        print(f"Async error: {type(e).__name__}: {e}")
    finally:
        await exchange.close()

asyncio.run(test_async())
