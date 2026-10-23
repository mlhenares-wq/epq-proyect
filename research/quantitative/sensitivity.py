"""Sensitivity tests for the QCRI (qcri.py).

Reruns every case with different goalposts, weights, indicator sets and
ways of combining L and S, and reports whether the direction of each
comparison (risk up or down) survives. Run: python3 sensitivity.py
"""
from math import log, log10, sqrt
import qcri

BASE = dict(a_max=200, p_max=10.0, d_max=120, P_max=100, F_max=1000, wL=0.5, mean="geo", drop=None)

def score(i, s):
    """Like qcri.score, but with goalposts, weights and indicator set taken from s."""
    def keep(k, v):
        return None if (s["drop"] == k or v is None) else v
    if i.get("closed"):
        L01 = 1.0
    else:
        a, p = keep("A", i["A"]), keep("p", i["p"])
        L01 = qcri.mean([min(1.0, log(1 + a) / log(1 + s["a_max"])) if a is not None else None,
                         min(1.0, max(0.0, log10(p / 0.01) / log10(s["p_max"] / 0.01))) if p is not None else None])
    T, D, P, F = (keep(k, i[k]) for k in ("T", "D", "P", "F"))
    S01 = qcri.mean([T,
                     min(1.0, log(1 + D) / log(1 + s["d_max"])) if D is not None else None,
                     min(1.0, P / s["P_max"]) if P is not None else None,
                     min(1.0, log(1 + F / 100) / log(1 + s["F_max"] / 100)) if F is not None else None])
    L, S = 1 + 4 * L01, 1 + 4 * S01
    R = (L ** s["wL"]) * (S ** (1 - s["wL"])) if s["mean"] == "geo" else s["wL"] * L + (1 - s["wL"]) * S
    return L, S, R

PAIRS = [("Hormuz: Tanker War (1984-88)", "Hormuz: 2026 closure", "Hormuz"),
         ("Suez: 1967-75 closure", "Red Sea: 2023-26 Houthi crisis", "Suez/Red Sea"),
         ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2025", "Malacca peak-2025"),
         ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2026 (Jan-Sep)", "Malacca peak-2026"),
         ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2008", "Malacca peak-2008"),
         ("Malacca: 2025", "Malacca: 2026 (Jan-Sep)", "Malacca 2025-26")]

TESTS = [("Central (as published)", {}),
         ("Attacks goalpost 100 a year", dict(a_max=100)),
         ("Attacks goalpost 400 a year", dict(a_max=400)),
         ("Premium goalpost 5% of hull", dict(p_max=5.0)),
         ("Premium goalpost 20% of hull", dict(p_max=20.0)),
         ("Duration goalpost 5 years", dict(d_max=60)),
         ("Duration goalpost 20 years", dict(d_max=240)),
         ("Brent goalpost +50%", dict(P_max=50)),
         ("Brent goalpost +200%", dict(P_max=200)),
         ("Freight goalpost +500%", dict(F_max=500)),
         ("Freight goalpost +2,000%", dict(F_max=2000)),
         ("Likelihood weighted 2:1", dict(wL=2 / 3)),
         ("Severity weighted 2:1", dict(wL=1 / 3)),
         ("Arithmetic mean of L and S", dict(mean="arith")),
         ("Drop attacks (A)", dict(drop="A")),
         ("Drop premium (p)", dict(drop="p")),
         ("Drop traffic lost (T)", dict(drop="T")),
         ("Drop duration (D)", dict(drop="D")),
         ("Drop Brent (P)", dict(drop="P")),
         ("Drop freight (F)", dict(drop="F"))]

def band(r):
    return qcri.band(r)

if __name__ == "__main__":
    flips = {}
    header = "".join(f"{p[2]:>19}" for p in PAIRS)
    print(f"{'Test':30}{header}")
    for name, change in TESTS:
        s = dict(BASE, **change)
        R = {k: score(v["central"], s)[2] for k, v in qcri.CASES.items()}
        row = ""
        for a, b, label in PAIRS:
            d = R[b] - R[a]
            base = qcri.score(qcri.CASES[b]["central"])[2] - qcri.score(qcri.CASES[a]["central"])[2]
            flipped = (d > 0) != (base > 0)
            if flipped:
                flips.setdefault(label, []).append(name)
            row += f"{R[a]:5.2f}->{R[b]:4.2f} {d:+.2f}{'*' if flipped else ' '}"
        print(f"{name:30}{row}")
    print()
    print("Bands of each period under every test:")
    for k, v in qcri.CASES.items():
        bands = sorted({band(score(v["central"], dict(BASE, **c))[2]) for _, c in TESTS})
        print(f"  {k:46} {', '.join(bands)}")
    print()
    print("Direction flips (* above):", flips if flips else "none")
