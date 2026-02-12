"""测试通过傲盾代理使用 CCXT Pro WebSocket 连接 OKX"""
import asyncio
import ccxt.pro as ccxtpro

async def test_ws_via_proxy():
    """测试 WS 通过 SOCKS5 代理"""
    print("=== 测试: WebSocket 通过 SOCKS5 代理连接 OKX ===")
    exchange = ccxtpro.okx({
        'socksProxy': 'socks5://127.0.0.1:6987',
        'wsProxy': 'socks5://127.0.0.1:6987',
    })
    try:
        # watchOHLCV 会建立 WebSocket 连接
        print("正在通过代理建立 WebSocket 连接...")
        ohlcv = await asyncio.wait_for(
            exchange.watch_ohlcv('BTC/USDT', '1m'),
            timeout=20
        )
        print(f"✅ WebSocket 成功! 收到 {len(ohlcv)} 条 K线数据")
        if ohlcv:
            last = ohlcv[-1]
            print(f"   最新K线: 时间={last[0]}, 开={last[1]}, 高={last[2]}, 低={last[3]}, 收={last[4]}")
    except asyncio.TimeoutError:
        print("❌ 超时 (20s)")
    except Exception as e:
        print(f"❌ 失败: {type(e).__name__}: {e}")
    finally:
        await exchange.close()

async def test_ws_via_http_proxy():
    """测试 WS 通过 HTTP 代理 (如果傲盾也提供 HTTP 代理端口)"""
    print("\n=== 测试: WebSocket 通过 HTTP 代理连接 OKX ===")
    exchange = ccxtpro.okx({
        'httpsProxy': 'http://127.0.0.1:6987',
        'wsProxy': 'http://127.0.0.1:6987',
    })
    try:
        print("正在通过 HTTP 代理建立 WebSocket 连接...")
        ohlcv = await asyncio.wait_for(
            exchange.watch_ohlcv('BTC/USDT', '1m'),
            timeout=15
        )
        print(f"✅ WebSocket 成功! 收到 {len(ohlcv)} 条 K线数据")
    except asyncio.TimeoutError:
        print("❌ 超时 (15s)")
    except Exception as e:
        print(f"❌ 失败: {type(e).__name__}: {e}")
    finally:
        await exchange.close()

async def test_ws_via_socks5h_proxy():
    """测试 WS 通过 socks5h 代理 (DNS 也走代理)"""
    print("\n=== 测试: WebSocket 通过 socks5h 代理连接 OKX ===")
    exchange = ccxtpro.okx({
        'socksProxy': 'socks5h://127.0.0.1:6987',
        'wsProxy': 'socks5h://127.0.0.1:6987',
    })
    try:
        print("正在通过 socks5h 代理建立 WebSocket 连接...")
        ohlcv = await asyncio.wait_for(
            exchange.watch_ohlcv('BTC/USDT', '1m'),
            timeout=15
        )
        print(f"✅ WebSocket 成功! 收到 {len(ohlcv)} 条 K线数据")
    except asyncio.TimeoutError:
        print("❌ 超时 (15s)")
    except Exception as e:
        print(f"❌ 失败: {type(e).__name__}: {e}")
    finally:
        await exchange.close()

async def main():
    await test_ws_via_proxy()
    await test_ws_via_http_proxy()
    await test_ws_via_socks5h_proxy()

if __name__ == '__main__':
    asyncio.run(main())
