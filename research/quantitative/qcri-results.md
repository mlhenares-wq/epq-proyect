# Quantitative Chokepoint Risk Index (QCRI): results

Script: `qcri.py` (run `python3 qcri.py` to reproduce every number here).

## Equation

Risk is the geometric mean of likelihood and severity, each built from real data:

- **R = √(L × S)**, with L and S on a 1–5 scale (so R is also 1–5)
- **L = 1 + 4 × mean(ℓ_A, ℓ_P)**; a route physically closed to all ships gets L = 5
- **S = 1 + 4 × mean(s_T, s_D, s_P, s_F)**; indicators with no data are left out

| Indicator | Formula (0–1) | Goalposts |
|---|---|---|
| ℓ_A attacks on merchant ships per year (A) | ln(1 + A) / ln(201) | 0 attacks = 0; 200 a year = 1 |
| ℓ_P war-risk premium, % of hull value (p) | log10(p / 0.01) / 3 | 0.01% (normal) = 0; 10% = 1 |
| s_T share of normal traffic lost (T) | T | 0 = none lost; 1 = all lost |
| s_D months of disruption (D) | ln(1 + D) / ln(121) | 0 = none; 120 months (10 years) = 1 |
| s_P rise in Brent, pre-crisis to peak (P, %) | P / 100 | 0% = 0; +100% = 1 |
| s_F rise in the route's freight benchmark (F, %) | ln(1 + F/100) / ln(11) | 0% = 0; +1,000% (11 times) = 1 |

Bands for R: 1.0–1.9 Low · 2.0–2.9 Moderate · 3.0–3.9 High · 4.0–5.0 Very high.

Cooperation check (best case only): K = 5 − C/5 and R_K = (L × S × K)^(1/3). The counterfactual R_cf = (L₂ × S₂ × K₁)^(1/3) shows risk in the later period if cooperation had stayed at its earlier level.

## Inputs (central value; low–high range in brackets)

| Case and period | Attacks/yr (A) | Premium % hull (p) | Traffic lost (T) | Months (D) | Brent rise % (P) | Freight rise % (F) | C |
|---|---|---|---|---|---|---|---|
| Hormuz, Tanker War 1984–88 | 178 (169–181) | 5 (3–7.5) | 0.25 (0.25–0.45) | 53 (53–90) | 6.9 | no data | 9 |
| Hormuz, 2026 closure | 140 (93–200) | 7.5 (5–10) | 0.90 (0.81–0.95) | 7.7 | 65 (65–77) | 1,041 (573–1,041) | 12 |
| Suez, 1967–75 closure | route closed (L = 5) | route closed | 1.0 | 96 | no data (0 in low case) | 100 (left out in high case) | 5 |
| Red Sea, 2023–26 crisis | 100 (87–160) | 1 (0.5–3) | 0.50 (0.42–0.70) | 35 | 6 (4–8) | 246 (115–286) | 13 |
| Malacca, peak (2000 attacks; 2005 insurance) | 75 | 0.4 (left out in low case) | 0 | 0 | 0 | no data | 6 |
| Malacca, 2008 | 8 (2) | not listed (0.01) | 0 | 0 | 0 | no data | 13 |
| Malacca, 2025 | 108 (1) | not listed (0.01) | 0 | 0 | 0 | no data | 15 |
| Malacca, 2026 (Jan–Sep) | 31 (1–42) | not listed (0.01) | 0 | 0 | 0 | no data | 15 |

### Sources of the central inputs

**Hormuz, Tanker War**
- A = 178 ships attacked or damaged in 1987: Lloyd's Shipping Intelligence via UPI, 10 Dec 1987 (B3), corroborated by USNI *Proceedings*, May 1988 (179–181; B2). Range 169 (UN tally, in the same USNI article) to 181.
- p = about 5%, the "Tanker War rate": Lloyd's List, March 2026 (B2). Range 3% hull + 2% cargo (UPI, 15 May 1984, B2) to 7.5% at Kharg (Strauss Center, B2).
- T = 25% fall in Gulf commercial shipping: Strauss Center (B2). High case 45% fall in oil flow, more than 7 to under 4 mb/d: USIP *Iran Primer* (B2, graded here; partly market-driven).
- D = 53 months, from Iraq's March 1984 escalation to the 20 August 1988 ceasefire (derived; UPI, 7 Mar 1984 and 18 Jul 1988, B1–B2). High case 90 months from the first attacks in 1981.
- P = +6.9%, Brent $18.58 (May 1987) to $19.86 (Jul 1987): FRED/EIA (A1).

**Hormuz, 2026**
- A = 140 a year, annualised from at least 70 commercial ships attacked between 28 Feb and late August: IMO via Seatrade Maritime (C2, graded here). Low case 93 is the actual count to mid-October (70 plus 23 in 1–15 Oct: AFP via Ahram Online, C1, graded here); high case 200 is the October rate.
- p = 7.5% rising towards 10%: Lloyd's List, 11 Mar 2026 (B2); 7.5–10% again in July: S&P Global/Marsh, 22 Jul 2026 (B1).
- T = 0.90, exports through Hormuz below 10% of pre-conflict levels: IEA, 11 Mar 2026 (A1). Range 0.81 (loadings 20 to 3.8 mb/d: IEA *Oil Market Report*, Apr 2026, A2) to 0.95 (transits 129 to 6 a day: UNCTAD, Apr 2026, A1, seen only via a university mirror graded D6).
- D = 7.7 months, 28 Feb to 19 Oct 2026 and continuing (derived).
- P = +65%, Brent $71.36 (27 Feb, FRED, A1) to $118 (31 Mar, EIA, A1). High case +77% to $126.3 in late April (RT and Spanish press, C–D; use with care).
- F = +1,041%, VLCC Gulf–China rate $123,825/day (mid-Dec 2025, Clarksons via Riviera Maritime Media, C2, graded here) to $1,412,594/day (15 Oct 2026, Baltic Exchange via Cyprus Shipping News, C2, graded here); the record path is confirmed by Lloyd's List (B1). Low case +573% from the late-February $210,000.

**Suez, 1967–75**
- Closed to all ships from 5 Jun 1967 to 5 Jun 1975: Time, June 1967 (B2); AP in the Michigan Daily, 6 Jun 1975 (B1). So L = 5, T = 1.0 and D = 96 months.
- F = +100%, tanker rates "doubled" by late July 1967: NYT 23 Jul 1967 quoted by a blog (C3, graded here); US *Minerals Yearbook*: "markedly higher".
- P: no measured oil-price effect of the closure; the 1973–74 price shock came from the October War embargo, a connected crisis.

**Red Sea, 2023–26**
- A = about 100 ships attacked from November 2023 to December 2024: Seatrade Maritime (C2); Lloyd's List counted 99 to early 2026 (B2). Low 87 (to May 2024: South24, C2); high 160 (the Nov 2023–May 2024 rate annualised).
- p = about 1% of hull value: Lloyd's List, Jan 2024 (B2); Insurance Journal/Reuters, Mar 2024 (B2). Low 0.5% (typical 0.4–0.7%: S&P Global, B6, figure not seen directly); high 3% for Saudi-linked tankers (Insurance Journal/Reuters, 25 Sep 2026, B2).
- T = 0.50, Suez trade volume down 50% year on year: IMF PortWatch blog, 7 Mar 2024 (A1). Range 0.42 (UNCTAD, Feb 2024, A1) to 0.70 (UNCTAD *Review of Maritime Transport 2024*, A1).
- D = 35 months, 19 Nov 2023 to Oct 2026, with traffic still below normal (derived).
- P = +6%, Brent about $77 to $80–83: Engine and World Oil, Jan 2024 (C2, graded here; two independent trade sources).
- F = +246%, Drewry WCI Shanghai–Rotterdam to $4,951 by 18 Jan 2024: Drewry WCI (B2), seen via a Hellenic Shipping News repost (D1); cite Drewry.

**Malacca**
- Attacks: 75 (2000) and 2 (2008) in the Malacca Strait: ICC-IMB (A1). About 8 in Malacca and Singapore combined in 2008: RSIS (B2). 108 in the Straits of Malacca and Singapore in 2025, 107 of them in the Singapore Strait and 1 in the Malacca Strait: ReCAAP ISC (A1). 23 by end-September 2026, annualised to 31: ReCAAP via SAFETY4SEA (C2).
- Premium 0.4% of hull value while the strait was a listed area (June 2005–August 2006): Maritime Executive, 6 Jul 2005 (C2, one source). Not listed afterwards: London P&I Club circular 7083 (A2, graded here); JWLA-033 (A1).
- Traffic rose throughout (43,965 transits in 1999, 63,636 in 2004, 102,525 in 2025): Marine Department Malaysia via IALA (B2, graded here) and Seatrade (C2). So T, D and P = 0.

## Indicator values (central case)

| Case and period | ℓ_A | ℓ_P | s_T | s_D | s_P | s_F |
|---|---|---|---|---|---|---|
| Hormuz, Tanker War | 0.978 | 0.900 | 0.250 | 0.832 | 0.069 | – |
| Hormuz, 2026 | 0.933 | 0.958 | 0.900 | 0.451 | 0.650 | 1.000 |
| Suez, 1967–75 | closed | closed | 1.000 | 0.954 | – | 0.289 |
| Red Sea, 2023–26 | 0.870 | 0.667 | 0.500 | 0.747 | 0.060 | 0.518 |
| Malacca, peak | 0.817 | 0.534 | 0 | 0 | 0 | – |
| Malacca, 2008 | 0.414 | 0 | 0 | 0 | 0 | – |
| Malacca, 2025 | 0.885 | 0 | 0 | 0 | 0 | – |
| Malacca, 2026 | 0.654 | 0 | 0 | 0 | 0 | – |

## Results

| Case and period | L | S | R | Band | R range (low–high inputs) | C | R_K |
|---|---|---|---|---|---|---|---|
| Hormuz, Tanker War | 4.76 | 2.53 | 3.47 | High | 3.41–3.79 | 9 | 3.38 |
| Hormuz, 2026 | 4.78 | 4.00 | 4.37 | Very high | 4.09–4.57 | 12 | 3.68 |
| Suez, 1967–75 | 5.00 | 3.99 | 4.47 | Very high | 4.03–4.95 | 5 | 4.31 |
| Red Sea, 2023–26 | 4.07 | 2.82 | 3.39 | High | 3.11–3.76 | 13 | 3.02 |
| Malacca, peak | 3.70 | 1.00 | 1.92 | Low | 1.92–2.07 | 6 | 2.41 |
| Malacca, 2008 | 1.83 | 1.00 | 1.35 | Low | 1.19–1.35 | 13 | 1.64 |
| Malacca, 2025 | 2.77 | 1.00 | 1.66 | Low | 1.12–1.66 | 15 | 1.77 |
| Malacca, 2026 | 2.31 | 1.00 | 1.52 | Low | 1.12–1.56 | 15 | 1.66 |

## Changes between periods

| Comparison | ΔR | ΔL | ΔS | Ranges separate? | ΔC | Best-case cooperation effect (R_K scale) | Process-tracing share of cooperation |
|---|---|---|---|---|---|---|---|
| Hormuz: Tanker War → 2026 | +0.90 (+26%) | +0.03 | +1.47 | Yes | +3 | −0.26 (risk rose anyway; without the extra cooperation R_K would be 3.94, not 3.68) | 5.7% |
| Suez 1967–75 → Red Sea 2023–26 | −1.07 (−24%) | −0.93 | −1.17 | Yes | +8 | −0.56 (at most 44% of the fall) | 8.5%, mixed sign |
| Malacca peak → 2008 | −0.57 (−30%) | −1.87 | 0 | Yes | +7 | −0.27 (at most 35% of the fall) | 15.8–23.7% |
| Malacca 2025 → 2026 | −0.15 (−9%) | −0.46 | 0 | No (overlap) | 0 | 0 (cooperation did not change) | 13.6% patrols + 27.3% information sharing |

## Likelihood check: insurance-implied vs observed chance of attack

A war-risk premium of p% of hull value implies that insurers expect at most about p chances in 100 of losing the ship on that voyage (less once their profit margin is taken out).

| Case and period | Premium | Insurance-implied (upper bound) | Observed attack rate per transit | Source of the observed rate |
|---|---|---|---|---|
| Tanker War, 1987 | ~5% | 1 in 20 | under 2% (1 in 50 or fewer) | Strauss Center (B2); fewer than 25% of ships hit were sunk or disabled |
| Hormuz, 2026 | 7.5% | 1 in 13 | about 5% (1 in 19) | derived: at least 70 attacks ÷ about 1,330 transits, Mar–Aug 2026 (PortWatch write-ups); an overestimate, since some ships were hit in port |
| Red Sea, 2024 | ~1% | 1 in 100 | about 0.76% (1 in 132); about 4 sunk (1 in 3,300) | derived: about 100 attacks ÷ about 13,200 Suez transits in 2024 (Suez Canal Authority via Ahram Online, D2) |
| Malacca, 2000 / 2005 | 0.4% (2005) | 1 in 250 | 0.13% (1 in 746) in 2000 | derived: 75 attacks ÷ 55,957 transits (IMB; Marine Department Malaysia) |
| Malacca, 2025 | not listed | – | 0.11% (1 in 949), 53% petty theft | derived: 108 incidents ÷ 102,525 transits (ReCAAP; Seatrade) |

In every case the insurance price is 1.3–3 times the observed attack rate: premiums track likelihood but lean high.
