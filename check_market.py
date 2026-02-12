import ccxt
import numpy as np

ox = ccxt.okx({
    'proxies': {
        'http': 'socks5h://127.0.0.1:6987',
        'https': 'socks5h://127.0.0.1:6987'
    }
})

pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']

print("=" * 70)
print(f"{'交易对':<12} {'现价':>10} {'EMA200':>10} {'位置':>6} {'趋势判断':>10}")
print("=" * 70)

for pair in pairs:
    # Get 250 daily candles to calculate EMA200
    ohlcv = ox.fetch_ohlcv(pair, '1d', limit=250)
    closes = np.array([c[4] for c in ohlcv])
    
    # Calculate EMA200
    ema200 = closes[0]
    multiplier = 2 / (200 + 1)
    for price in closes[1:]:
        ema200 = price * multiplier + ema200 * (1 - multiplier)
    
    # Calculate EMA50
    ema50 = closes[0]
    multiplier50 = 2 / (50 + 1)
    for price in closes[1:]:
        ema50 = price * multiplier50 + ema50 * (1 - multiplier50)
    
    current = closes[-1]
    pct = (current - ema200) / ema200 * 100
    
    if current > ema200 and ema50 > ema200:
        trend = "🟢 牛市"
    elif current < ema200 and ema50 < ema200:
        trend = "🔴 熊市"
    elif current > ema200:
        trend = "🟡 转牛中"
    else:
        trend = "🟠 转熊中"
    
    print(f"{pair:<12} {current:>10.2f} {ema200:>10.2f} {pct:>+5.1f}% {trend:>10}")

print("=" * 70)
print()
print("判断标准:")
print("  🟢 牛市 = 价格 > EMA200 且 EMA50 > EMA200 (策略会做多)")
print("  🔴 熊市 = 价格 < EMA200 且 EMA50 < EMA200 (策略会做空)")
print("  🟡 转牛中 = 价格刚突破EMA200, 但EMA50还没跟上")
print("  🟠 转熊中 = 价格刚跌破EMA200, 但EMA50还在上面")
