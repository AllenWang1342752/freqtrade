import asyncio
import ccxt.async_support as ccxt_async
import time


async def test_direct():
    print("=== Test 1: Direct connection (no proxy) ===")
    exchange = ccxt_async.okx({'timeout': 15000})
    try:
        t0 = time.time()
        result = await exchange.fetch_time()
        print(f"Direct OK! Time: {result}, took {time.time()-t0:.2f}s")
    except Exception as e:
        print(f"Direct FAILED: {type(e).__name__}: {e}")
    finally:
        await exchange.close()


async def test_proxy():
    print("\n=== Test 2: Via SOCKS5 proxy ===")
    exchange = ccxt_async.okx({
        'aiohttp_proxy': 'socks5://127.0.0.1:6987',
        'timeout': 15000,
    })
    try:
        t0 = time.time()
        result = await exchange.fetch_time()
        print(f"Proxy OK! Time: {result}, took {time.time()-t0:.2f}s")
    except Exception as e:
        print(f"Proxy FAILED: {type(e).__name__}: {e}")
    finally:
        await exchange.close()

asyncio.run(test_direct())
asyncio.run(test_proxy())
