import ccxt
import numpy as np
from datetime import datetime, timezone


ox = ccxt.okx({
    'proxies': {
        'http': 'socks5h://127.0.0.1:6987',
        'https': 'socks5h://127.0.0.1:6987',
    }
})

# Fetch daily BTC data in batches
all_ohlcv = []
since = ox.parse8601('2023-08-01T00:00:00Z')
end_ts = ox.parse8601('2026-02-22T00:00:00Z')

while since < end_ts:
    batch = ox.fetch_ohlcv('BTC/USDT', '1d', since=since, limit=300)
    if not batch:
        break
    if all_ohlcv:
        last_ts = all_ohlcv[-1][0]
        batch = [c for c in batch if c[0] > last_ts]
    all_ohlcv.extend(batch)
    if len(batch) == 0:
        break
    since = all_ohlcv[-1][0] + 86400000
    dt = datetime.fromtimestamp(
        all_ohlcv[-1][0] / 1000, tz=timezone.utc
    )
    print(f"  Fetched to {dt.strftime('%Y-%m-%d')}, "
          f"total: {len(all_ohlcv)}")

print(f"\nTotal candles: {len(all_ohlcv)}")
d0 = datetime.fromtimestamp(
    all_ohlcv[0][0] / 1000, tz=timezone.utc
)
d1 = datetime.fromtimestamp(
    all_ohlcv[-1][0] / 1000, tz=timezone.utc
)
print(f"From: {d0.strftime('%Y-%m-%d')}")
print(f"To:   {d1.strftime('%Y-%m-%d')}\n")

dates = [
    datetime.fromtimestamp(c[0] / 1000, tz=timezone.utc)
    for c in all_ohlcv
]
closes = np.array([c[4] for c in all_ohlcv])


def calc_ema(data, period):
    ema = np.zeros(len(data))
    ema[0] = data[0]
    mult = 2.0 / (period + 1)
    for i in range(1, len(data)):
        ema[i] = data[i] * mult + ema[i - 1] * (1 - mult)
    return ema


ema50 = calc_ema(closes, 50)
ema200 = calc_ema(closes, 200)

start_date = datetime(2024, 2, 1, tzinfo=timezone.utc)

print("=" * 95)
print("BTC/USDT Market Phases (2024-02 ~ 2026-02)")
print("EMA200 + EMA50 daily trend filter")
print("=" * 95)

phases = []
prev_phase = None

for i in range(len(dates)):
    if dates[i] < start_date:
        continue
    price = closes[i]
    e50 = ema50[i]
    e200 = ema200[i]

    if price > e200 and e50 > e200:
        phase = "BULL"
    elif price < e200 and e50 < e200:
        phase = "BEAR"
    elif price > e200:
        phase = "TURNING_BULL"
    else:
        phase = "TURNING_BEAR"

    if phase != prev_phase:
        phases.append({
            'phase': phase,
            'start': dates[i],
            'start_price': price,
            'end': dates[i],
            'end_price': price,
            'high': price,
            'low': price,
        })
        prev_phase = phase
    else:
        phases[-1]['end'] = dates[i]
        phases[-1]['end_price'] = price
        phases[-1]['high'] = max(phases[-1]['high'], price)
        phases[-1]['low'] = min(phases[-1]['low'], price)

tag_map = {
    "BULL": "UP", "BEAR": "DN",
    "TURNING_BULL": "t+", "TURNING_BEAR": "t-",
}

hdr = (f"{'':>3} {'Phase':<14} {'Start':<12} "
       f"{'End':<12} {'Days':>5} {'Start$':>9} "
       f"{'End$':>9} {'High':>9} {'Low':>9} "
       f"{'Chg':>7}")
sep = "-" * 98


def print_table(title, data):
    print(f"\n{title}")
    print(hdr)
    print(sep)
    for p in data:
        days = (p['end'] - p['start']).days + 1
        chg = ((p['end_price'] - p['start_price'])
               / p['start_price'] * 100)
        tag = tag_map.get(p['phase'], "??")
        print(
            f"{tag:>3} {p['phase']:<14} "
            f"{p['start'].strftime('%Y-%m-%d'):<12} "
            f"{p['end'].strftime('%Y-%m-%d'):<12} "
            f"{days:>5} "
            f"{p['start_price']:>9.0f} "
            f"{p['end_price']:>9.0f} "
            f"{p['high']:>9.0f} "
            f"{p['low']:>9.0f} "
            f"{chg:>+6.1f}%"
        )


print_table("All Phases:", phases)

# Merge transitions < 10 days
major = []
for p in phases:
    days = (p['end'] - p['start']).days + 1
    if days < 10 and major:
        major[-1]['end'] = p['end']
        major[-1]['end_price'] = p['end_price']
        major[-1]['high'] = max(major[-1]['high'], p['high'])
        major[-1]['low'] = min(major[-1]['low'], p['low'])
    else:
        major.append(dict(p))

print()
print("=" * 95)
print_table("Major Phases (short transitions merged):", major)

print(f"\nCurrent: BTC ${closes[-1]:,.0f} | "
      f"EMA50 ${ema50[-1]:,.0f} | "
      f"EMA200 ${ema200[-1]:,.0f} | "
      f"{dates[-1].strftime('%Y-%m-%d')}")
