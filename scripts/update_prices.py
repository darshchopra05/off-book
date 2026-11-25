"""Update closing prices in live.json from Yahoo Finance (via yfinance).

Usage: python3 scripts/update_prices.py live.json
Needs: pip install yfinance curl_cffi
Covers the 20 core companies plus every company in "extra".
A price Yahoo can't return keeps its previous entry and date.
"""
import json, sys, datetime, time
import yfinance as yf
from curl_cffi import requests as cr

CORE = "NVDA MSFT AAPL GOOGL AMZN META AVGO TSLA ORCL LLY WMT NFLX XOM COST AMD INTC IBM DELL CRWV NBIS".split()

def main(path):
    L = json.load(open(path))
    px = L.setdefault("px", {})
    tickers = CORE + [t for t in L.get("extra", {}) if t not in CORE]
    s = cr.Session(impersonate="safari")
    ok, failed = [], []
    for t in tickers:
        try:
            tk = yf.Ticker(t, session=s)
            fi = tk.fast_info
            p, prev, mc = fi.last_price, fi.previous_close, fi.market_cap
            if not p or p <= 0:
                raise ValueError("no price")
            pe = None
            try:
                pe = tk.info.get("trailingPE")
            except Exception:
                old = px.get(t) or {}
                if old.get("pe") and old.get("px"):
                    pe = old["pe"] * p / old["px"]
            px[t] = {
                "px": round(float(p), 2),
                "mc": round(float(mc) / 1e9, 1) if mc else (px.get(t) or {}).get("mc"),
                "pe": round(float(pe), 1) if pe and pe > 0 else None,
                "chg": round((p / prev - 1) * 100, 2) if prev else 0,
                "d": datetime.date.today().strftime("%b %-d, %Y"),
            }
            ok.append(t)
        except Exception as e:
            failed.append(f"{t} ({e})")
        time.sleep(0.3)
    json.dump(L, open(path, "w"), indent=1)
    print(f"Updated {len(ok)} of {len(tickers)} prices.")
    if failed:
        print("Kept previous price for:", ", ".join(failed))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "live.json")
