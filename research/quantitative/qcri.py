"""Quantitative Chokepoint Risk Index (QCRI).

Risk = sqrt(L x S), where L (likelihood) and S (severity) are each built from
real data, normalised to 0-1 against fixed goalposts and rescaled to 1-5.
Run:  python3 qcri.py   (prints the tables used in the judgement analysis)

Every input below names its source and Admiralty grade. "None" = no data,
so that indicator is left out and the others are averaged.
"""
from math import log, log10, sqrt

# ---------- indicator formulas (0 to 1) ----------
def l_attacks(a):            # attacks on merchant ships per year; 200/yr = 1
    return min(1.0, log(1 + a) / log(201))

def l_premium(p):            # war-risk premium, % of hull value; 0.01% = 0, 10% = 1
    return min(1.0, max(0.0, log10(p / 0.01) / 3))

def s_trade(t):              # fraction of normal traffic lost (0-1)
    return t

def s_duration(d):           # months of disruption; 120 months (10 years) = 1
    return min(1.0, log(1 + d) / log(121))

def s_price(p):              # % rise in Brent, pre-crisis to peak; +100% = 1
    return min(1.0, p / 100)

def s_freight(f):            # % rise in the route's freight benchmark; +1,000% = 1
    return min(1.0, log(1 + f / 100) / log(11))

def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs)

def score(i):
    """Return L, S on 1-5 and R = sqrt(L x S)."""
    if i.get("closed"):      # route physically closed: disruption certain
        L01 = 1.0
    else:
        L01 = mean([l_attacks(i["A"]) if i["A"] is not None else None,
                    l_premium(i["p"]) if i["p"] is not None else None])
    S01 = mean([s_trade(i["T"]) if i["T"] is not None else None,
                s_duration(i["D"]) if i["D"] is not None else None,
                s_price(i["P"]) if i["P"] is not None else None,
                s_freight(i["F"]) if i["F"] is not None else None])
    L, S = 1 + 4 * L01, 1 + 4 * S01
    return L, S, sqrt(L * S)

def coop(L, S, C):           # best-case check: cooperation as coping capacity
    K = 5 - C / 5
    return (L * S * K) ** (1 / 3)

# ---------- inputs: central, low, high ----------
# A attacks/yr | p premium % hull | T traffic lost | D months | P Brent % | F freight % | C cooperation 0-20
CASES = {
 "Hormuz: Tanker War (1984-88)": dict(C=9,
   central=dict(A=178, p=5.0, T=0.25, D=53, P=6.9, F=None),
   low=dict(A=169, p=3.0, T=0.25, D=53, P=6.9, F=None),
   high=dict(A=181, p=7.5, T=0.45, D=90, P=6.9, F=None)),
 "Hormuz: 2026 closure": dict(C=12,
   central=dict(A=140, p=7.5, T=0.90, D=7.7, P=65, F=1041),
   low=dict(A=93, p=5.0, T=0.81, D=7.7, P=65, F=573),
   high=dict(A=200, p=10.0, T=0.95, D=7.7, P=77, F=1041)),
 "Suez: 1967-75 closure": dict(C=5,
   central=dict(closed=True, A=None, p=None, T=1.0, D=96, P=None, F=100),
   low=dict(closed=True, A=None, p=None, T=1.0, D=96, P=0, F=100),
   high=dict(closed=True, A=None, p=None, T=1.0, D=96, P=None, F=None)),
 "Red Sea: 2023-26 Houthi crisis": dict(C=13,
   central=dict(A=100, p=1.0, T=0.50, D=35, P=6, F=246),
   low=dict(A=87, p=0.5, T=0.42, D=35, P=4, F=115),
   high=dict(A=160, p=3.0, T=0.70, D=35, P=8, F=286)),
 "Malacca: peak (2000 attacks, 2005 insurance)": dict(C=6,
   central=dict(A=75, p=0.4, T=0, D=0, P=0, F=None),
   low=dict(A=75, p=None, T=0, D=0, P=0, F=None),
   high=dict(A=75, p=0.4, T=0, D=0, P=0, F=None)),
 "Malacca: 2008": dict(C=13,
   central=dict(A=8, p=0.01, T=0, D=0, P=0, F=None),
   low=dict(A=2, p=0.01, T=0, D=0, P=0, F=None),
   high=dict(A=8, p=0.01, T=0, D=0, P=0, F=None)),
 "Malacca: 2025": dict(C=15,
   central=dict(A=108, p=0.01, T=0, D=0, P=0, F=None),
   low=dict(A=1, p=0.01, T=0, D=0, P=0, F=None),
   high=dict(A=108, p=0.01, T=0, D=0, P=0, F=None)),
 "Malacca: 2026 (Jan-Sep)": dict(C=15,
   central=dict(A=31, p=0.01, T=0, D=0, P=0, F=None),
   low=dict(A=1, p=0.01, T=0, D=0, P=0, F=None),
   high=dict(A=42, p=0.01, T=0, D=0, P=0, F=None)),
}

def band(r):
    return "Low" if r < 2 else "Moderate" if r < 3 else "High" if r < 4 else "Very high"

if __name__ == "__main__":
    res = {}
    print(f"{'Case':46} {'L':>5} {'S':>5} {'R':>5}  band       R range      R_coop")
    for name, c in CASES.items():
        L, S, R = score(c["central"])
        lo = score(c["low"])[2]; hi = score(c["high"])[2]
        rk = coop(L, S, c["C"])
        res[name] = (L, S, R, lo, hi, c["C"], rk)
        print(f"{name:46} {L:5.2f} {S:5.2f} {R:5.2f}  {band(R):9}  {min(lo,hi):.2f}-{max(lo,hi):.2f}   {rk:.2f}")
    print()
    pairs = [("Hormuz: Tanker War (1984-88)", "Hormuz: 2026 closure"),
             ("Suez: 1967-75 closure", "Red Sea: 2023-26 Houthi crisis"),
             ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2025"),
             ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2026 (Jan-Sep)"),
             ("Malacca: peak (2000 attacks, 2005 insurance)", "Malacca: 2008"),
             ("Malacca: 2025", "Malacca: 2026 (Jan-Sep)")]
    for a, b in pairs:
        L1, S1, R1, *_ , C1, _ = res[a]; L2, S2, R2, *_ , C2, _ = res[b]
        K1 = 5 - C1 / 5; K2 = 5 - C2 / 5
        rk1 = (L1 * S1 * K1) ** (1/3); rk2 = (L2 * S2 * K2) ** (1/3); rcf = (L2 * S2 * K1) ** (1/3)
        share = ("cooperation unchanged" if C1 == C2 else "R_K rose" if rk2 >= rk1
                 else f"{(rk2 - rcf) / (rk2 - rk1) * 100:.0f}% of R_K change")
        print(f"{a[:28]:28} -> {b[:28]:28} dR={R2-R1:+.2f} ({(R2-R1)/R1*100:+.0f}%)  "
              f"dL={L2-L1:+.2f} dS={S2-S1:+.2f} dC={C2-C1:+d}  "
              f"R_K {rk1:.2f}->{rk2:.2f} (cf {rcf:.2f}); coop best-case effect={rk2-rcf:+.2f} ({share})")
