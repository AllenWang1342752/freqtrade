"""Analyze BTC market phases (bull/bear) over the past 2 years using daily data."""

import pandas as pd


# Load local BTC daily data
df = pd.read_feather(r"user_data\data\okx\BTC_USDT-1d.feather")
df["date"] = pd.to_datetime(df["date"], utc=True)
df = df.sort_values("date").reset_index(drop=True)

print(f"Data range: {df['date'].min().strftime('%Y-%m-%d')} ~ {df['date'].max().strftime('%Y-%m-%d')}")
print(f"Total daily candles: {len(df)}")
print()

# Use daily data directly
daily = df.set_index("date")

# Calculate key EMAs on daily
daily["ema50"] = daily["close"].ewm(span=50, adjust=False).mean()
daily["ema200"] = daily["close"].ewm(span=200, adjust=False).mean()

# Determine bull/bear: price > EMA200 = bull, price < EMA200 = bear
daily["trend"] = "bull"
daily.loc[daily["close"] < daily["ema200"], "trend"] = "bear"

# Find phase transitions
daily["prev_trend"] = daily["trend"].shift(1)
daily["phase_change"] = daily["trend"] != daily["prev_trend"]

# Extract phases
phases = []
current_phase_start = daily.index[0]
current_trend = daily["trend"].iloc[0]

for date, row in daily.iterrows():
    if row["phase_change"] and not pd.isna(row["prev_trend"]):
        phases.append({
            "trend": current_trend,
            "start": current_phase_start,
            "end": date - pd.Timedelta(days=1),
            "duration_days": (date - current_phase_start).days,
        })
        current_phase_start = date
        current_trend = row["trend"]

# Add the last phase
phases.append({
    "trend": current_trend,
    "start": current_phase_start,
    "end": daily.index[-1],
    "duration_days": (daily.index[-1] - current_phase_start).days,
})

# Filter out very short phases (< 7 days) as noise, merge them
merged_phases = []
for p in phases:
    if p["duration_days"] < 7 and merged_phases:
        # Too short, merge with previous
        merged_phases[-1]["end"] = p["end"]
        merged_phases[-1]["duration_days"] = (
            merged_phases[-1]["end"] - merged_phases[-1]["start"]
        ).days
    else:
        merged_phases.append(p)

# Add price info
for p in merged_phases:
    mask = (daily.index >= p["start"]) & (daily.index <= p["end"])
    subset = daily.loc[mask]
    if len(subset) > 0:
        p["start_price"] = subset["close"].iloc[0]
        p["end_price"] = subset["close"].iloc[-1]
        p["high"] = subset["high"].max()
        p["low"] = subset["low"].min()
        p["change_pct"] = (p["end_price"] / p["start_price"] - 1) * 100

print("=" * 95)
print("BTC/USDT Market Phases (2024-02 ~ 2026-02)")
print("Method: Daily close vs EMA200, phases < 7 days merged as noise")
print("=" * 95)
print()
print(f"{'#':<4} {'Trend':<6} {'Start':<12} {'End':<12} {'Days':>5} "
      f"{'Start$':>10} {'End$':>10} {'High$':>10} {'Low$':>10} {'Change':>8}")
print("-" * 95)

for i, p in enumerate(merged_phases, 1):
    trend_label = "BULL" if p["trend"] == "bull" else "BEAR"
    print(f"  {i:<3} {trend_label:<6} "
          f"{p['start'].strftime('%Y-%m-%d'):<12} {p['end'].strftime('%Y-%m-%d'):<12} "
          f"{p['duration_days']:>5} "
          f"{p['start_price']:>10,.0f} {p['end_price']:>10,.0f} "
          f"{p['high']:>10,.0f} {p['low']:>10,.0f} "
          f"{p['change_pct']:>+7.1f}%")

print()
print("=" * 95)
print("SUMMARY:")
bull_days = sum(p["duration_days"] for p in merged_phases if p["trend"] == "bull")
bear_days = sum(p["duration_days"] for p in merged_phases if p["trend"] == "bear")
total_days = bull_days + bear_days
print(f"  Total period : {merged_phases[0]['start'].strftime('%Y-%m-%d')} ~ "
      f"{merged_phases[-1]['end'].strftime('%Y-%m-%d')} ({total_days} days)")
print(f"  Bull days    : {bull_days} days ({bull_days/total_days*100:.1f}%)")
print(f"  Bear days    : {bear_days} days ({bear_days/total_days*100:.1f}%)")
print(f"  Current trend: {'BULL' if merged_phases[-1]['trend'] == 'bull' else 'BEAR'}")
print(f"  Current phase: started {merged_phases[-1]['start'].strftime('%Y-%m-%d')} "
      f"({merged_phases[-1]['duration_days']} days ago)")
print()

# Key price milestones
print("KEY PRICES:")
print(f"  2-year high  : ${daily['high'].max():,.0f}")
print(f"  2-year low   : ${daily['low'].min():,.0f}")
print(f"  Current price: ${daily['close'].iloc[-1]:,.0f}")
print(f"  EMA200 now   : ${daily['ema200'].iloc[-1]:,.0f}")
print(f"  EMA50  now   : ${daily['ema50'].iloc[-1]:,.0f}")
