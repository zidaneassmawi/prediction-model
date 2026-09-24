## Alpaca hourly bars, first look (25 Sep)

- Asked for MSFT hourly, 15-19 Sep. Expected ~28 rows (4 days x 7). Got 64.
- 64 = 4 days x 16 bars. 16 hours = extended session 04:00-20:00 ET.
- Alpaca returns pre-market and after-hours by default. Must filter to
  regular hours (09:30-16:00 ET) to get the 7 bars/day this project assumes.
- Timestamps arrive in UTC (+00:00). First bar 08:00 UTC = 04:00 ET, pre-market.
- Volume confirms it: 04:00 bar 66,347, then 14,298 and 12,333. Extended
  hours are thin and not comparable to regular-hours bars.
- Index is a MultiIndex: (symbol, timestamp).
- Extra columns available: trade_count, vwap.
