import ccxt
import numpy as np


ox = ccxt.okx({
    'proxies': {
        'http': 'socks5h://127.0.0.1:6987',
        'https': 'socks5h://127.0.0.1:6987',
    }
})

pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']

print("=" * 70)
print(f"{'Pair':<12} {'Price':>10} {'EMA200':>10} {'Pos':>6} {'Trend':>10}")
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
        trend = "Bull"
    elif current < ema200 and ema50 < ema200:
        trend = "Bear"
    elif current > ema200:
        trend = "Turning Bull"
    else:
        trend = "Turning Bear"

    print(f"{pair:<12} {current:>10.2f} {ema200:>10.2f} {pct:>+5.1f}% {trend:>12}")

print("=" * 70)
print()
print("Legend:")
print("  Bull        = Price > EMA200 and EMA50 > EMA200 (go long)")
print("  Bear        = Price < EMA200 and EMA50 < EMA200 (go short)")
print("  Turning Bull = Price just broke above EMA200, EMA50 lagging")
print("  Turning Bear = Price just broke below EMA200, EMA50 still above")
