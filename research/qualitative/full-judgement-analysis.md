# Risk and Multilateralism at Maritime Chokepoints: A Full Judgement Analysis

Oct 23, 2026 · @Manuela López-Henares

## The overall judgement

Multilateral cooperation reduces the likelihood and severity of chokepoint disruption only to a limited and conditional extent. In none of the three cases was it the main reason risk changed. It did more to limit the harm each incident caused than to stop incidents happening, and how well it worked depended on who was doing the disrupting.

Two independent methods support this. A risk equation built only from measured data, R = √(L × S) on a scale of 1 to 5, shows how likelihood (L), severity (S) and risk (R) changed. Process tracing then tests what caused each change.

| Case study | Risk, earlier → later | What moved | Cooperation score (0–20) | Cooperation's share of the change | Verdict on cooperation |
| --- | --- | --- | --- | --- | --- |
| Strait of Hormuz: Tanker War (1984–88) → 2026 closure | 3.47 → 4.37, High → Very high | Severity; likelihood was already near its maximum | 9 → 12 | 5.7%, the smallest of nine causes | Minor reason |
| Suez and Red Sea: 1967–75 closure → 2023–26 Houthi crisis | 4.47 → 3.39, Very high → High | Both, as a closure gave way to selective attacks | 5 → 13 | 8.5%, partly negative | Minor reason |
| Strait of Malacca: piracy peak (2000–05) → 2025–26 | 1.92 → 1.66 (2025) and 1.52 (2026), Low throughout | Likelihood only; trade was never disrupted | 6 → 15 | 15.8–23.7% of the fall to 2008; information sharing 27.3% and patrols 13.6% of the 2025–26 fall | Major reason among several |

- **Against a state that chooses to close a strait, cooperation softens the blow but cannot prevent it.** In 2026 Iran cut Hormuz transits from 129 a day to 6 (UNCTAD, April 2026, A1). The IEA's record 400-million-barrel stock release came within 11 days (IEA, 11 March 2026, A1), yet Brent still rose 65% (FRED, A1; EIA, A1) and the UK–France naval mission still had no ships in the strait seven months later (The National, 6 October 2026, C2). In 1967 Egypt kept the Suez Canal shut for eight years, and the 1974 multinational clearance began only after a political settlement.
- **Against an armed non-state group, cooperation limits harm per attack but can provoke escalation.** About 100 ships were attacked in the Red Sea from November 2023, yet only about four sank (Seatrade Maritime, C2; AP via CP24, 2025, B1). After the US–UK strikes of January 2024, war-risk premiums tripled within a week (Lloyd's List, January 2024, B2). Risk fell mainly because a selective threat, unlike Egypt's closure, let most ships keep moving.
- **Against small-scale crime, cooperation works best, mainly by supporting national enforcement.** Malacca Strait attacks fell from 75 in 2000 to 2 in 2008 (ICC-IMB, 2001, A1; ICC-IMB, 2009, A1), but the steepest fall came before the joint patrols began in July 2004. The 2025–26 fall followed arrests by Indonesian police that used information shared through ReCAAP (ReCAAP ISC Annual Report 2025, A1).

The answer to the EPQ question is therefore **"to a limited and conditional extent"**. Cooperation matters at the margin of severity, and most against criminal threats. The type of threat, how much trade depends on the route and whether ships have another way round decide most of the risk.

## How the judgements are made

Each case is judged in two ways, so that the three straits can be compared fairly and each judgement can be checked against the other: an equation measures how risk changed, and process tracing tests what caused the change.

1. **Likelihood:** how probable was disruption, and why? This looks at who posed the threat, what they wanted and what they could do. It is measured by attacks per year and war-risk insurance premiums.
2. **Severity:** how much harm did disruption cause? It is measured by the share of traffic lost, how long the disruption lasted, and the rise in oil and freight prices. Human cost is discussed in the text but is not part of the equation.
3. **Risk:** the equation combines the two into one score, R = √(L × S), using measured data only (see "The quantitative risk equation" below).
4. **Cooperation:** what did states do together? Five factors are each scored 0–4: formal frameworks, joint operations, information sharing, response speed and enforcement of laws, giving a total, C, out of 20.
5. **Causation:** did cooperation cause the change, or did something else? Each possible cause is scored 0–2 on four tests (change, timing, mechanism and counterfactual), following process tracing (George and Bennett, 2005). A cause's share is its score divided by the total, and cooperation counts as the main reason only if its share is the largest and at least 1.5 times the next.

### How data provenance is shown

Every figure is followed by its source, its date and its Admiralty Code grade, for example (UNCTAD, April 2026, A1). "Graded here" marks a grade given in this analysis with the project rubric rather than taken from the provenance files, and "derived" marks a figure calculated from other cited figures.

| Grade | Producer | Use in this analysis |
| --- | --- | --- |
| A | Completely reliable: peer-reviewed journals, UN agencies, official statistics | Figures that judgements rest on |
| B | Usually reliable: Reuters, AP, Lloyd's List, major think tanks | Figures and main arguments |
| C | Fairly reliable: regional papers, trade press | National perspectives and local detail |
| D | Not usually reliable: state media on their own government | Only as evidence of how a government framed events |

The number after the letter rates the content: 1 means confirmed by independent sources, 2 probably true, 3 possibly true, and 6 cannot be judged. All figures were confirmed from search results rather than full pages, so check each one at its source before quoting it.

## The quantitative risk equation

The equation scores how risky each period was using only measured data that can be checked. Cooperation is deliberately left out of it, so it can test whether cooperation lowered risk instead of assuming that it did. The script `research/quantitative/qcri.py` reproduces every number in this section and the next.

### The formula

Risk (R) is the geometric mean of likelihood (L) and severity (S). Both are scored from 1 (none) to 5 (the most possible), so R also runs from 1 to 5.

```latex
R = \sqrt{L \times S}, \qquad L = 1 + 4 \times \frac{\ell_A + \ell_P}{2}, \qquad S = 1 + 4 \times \frac{s_T + s_D + s_P + s_F}{4}
```

Each small letter is an indicator scored from 0 to 1 against fixed goalposts, set out in the table below. If an indicator has no data for a period, it is left out and the average is taken over the rest. A route closed to every ship gets L = 5, because disruption is certain.

| Indicator | What it measures | Score from 0 to 1 | Goalposts | Why this scale |
| --- | --- | --- | --- | --- |
| ℓ\_A | Attacks on merchant ships per year (A) | ln(1 + A) ÷ ln(201) | 0 attacks scores 0; 200 a year scores 1 | Log scale: the first few attacks change the danger far more than a rise from 150 to 160 |
| ℓ\_P | War-risk insurance premium (p), % of hull value per voyage | log₁₀(p ÷ 0.01) ÷ 3 | 0.01% (peacetime) scores 0; 10% scores 1 | Premiums vary a thousandfold, so each tenfold rise adds a third |
| s\_T | Share of normal traffic lost (T) | T | None lost scores 0; all lost scores 1 | Already a share |
| s\_D | Months of disruption (D) | ln(1 + D) ÷ ln(121) | 0 months scores 0; 120 months (10 years) scores 1 | The first months do the most damage, before trade adapts |
| s\_P | Rise in the Brent oil price, from before the crisis to its peak (P, %) | P ÷ 100 | No rise scores 0; a doubling scores 1 | Straight line, capped at a doubling |
| s\_F | Rise in the route's main freight rate (F, %) | ln(1 + F ÷ 100) ÷ ln(11) | No rise scores 0; an elevenfold rise (+1,000%) scores 1 | Log scale, so one freak spike cannot dominate |

R is read in four bands: 1.0–1.9 Low, 2.0–2.9 Moderate, 3.0–3.9 High and 4.0–5.0 Very high.

Because R multiplies likelihood by severity, a period scores high only if disruption was both likely and harmful. At the Malacca peak, attacks were frequent (L = 3.70) but trade carried on as normal (S = 1.00), so risk was only Low (R = 1.92).

### Worked example: Hormuz in 2026

1. **Attacks:** at least 70 commercial ships were attacked between 28 February and late August (IMO via Seatrade Maritime, 2026, C2), or about 140 a year. So ℓ\_A = ln(141) ÷ ln(201) = 0.933.
2. **Insurance:** war-risk cover reached 7.5% of hull value (Lloyd's List, 11 March 2026, B2). So ℓ\_P = log₁₀(750) ÷ 3 = 0.958.
3. **Likelihood:** L = 1 + 4 × (0.933 + 0.958) ÷ 2 = 4.78.
4. **Severity:** exports through the strait fell below 10% of normal, so T = 0.90 (IEA, 11 March 2026, A1). By 19 October the disruption had lasted 7.7 months, so s\_D = ln(8.7) ÷ ln(121) = 0.451. Brent rose 65%, from $71.36 to $118 (FRED, A1; EIA, A1), so s\_P = 0.650. The VLCC Gulf–China freight rate rose about 1,040% (Clarksons via Riviera Maritime Media, C2; Baltic Exchange via Cyprus Shipping News, C2), which passes the goalpost, so s\_F = 1.
5. **Severity score:** S = 1 + 4 × (0.900 + 0.451 + 0.650 + 1.000) ÷ 4 = 4.00.
6. **Risk:** R = √(4.78 × 4.00) = 4.37, which is Very high.

### Why this form

- **Likelihood times consequence.** ISO 31000, the international risk-management standard, describes risk in terms of the likelihood of an event and its consequences. National risk registers, such as the UK's, score risks the same way.
- **Geometric mean.** Taking the square root of the product keeps R on the same 1–5 scale as its parts. As in the EU's INFORM Risk Index (Marin-Ferrer, Vernaccini and Poljansek, 2017), a high score on one side cannot hide a low score on the other.
- **Fixed goalposts and averaging.** Rescaling each indicator between fixed goalposts and averaging several of them follows the OECD/JRC *Handbook on Constructing Composite Indicators* (2008). Because the goalposts are fixed, rather than set by the highest and lowest of these eight periods, a new period can be scored without changing the others.
- **Measured indicators, not guesses.** Building each score from several measured indicators, instead of one banded judgement, answers Cox's (2008) warning that simple risk matrices can rank risks wrongly.
- **Cooperation kept out.** An earlier version, the CCRI, multiplied in a third term for lack of coping capacity, K = 5 − C ÷ 5, where C is the 0–20 cooperation score. That builds in the assumption that cooperation lowers risk, so it cannot test it. K is now used only for a generous check on the most cooperation could have done (see the next section).

### Limits of the equation

- **Judgement calls.** The goalposts and the equal weights are judgements. The sensitivity tests in the next section change each one.
- **Overlap between likelihood and severity.** Insurers raise premiums both when attacks become more likely and when each attack costs more.
- **Gaps in the data.** There is no freight index for the Tanker War and no war-risk premium for 1967, so those scores rest on fewer indicators.
- **Every incident counts the same.** A theft of scrap metal from a barge weighs as much as a missile strike. This matters most at Malacca, where most incidents in 2025 were petty thefts.
- **Prevented harm is invisible.** The equation measures harm that happened, so it cannot see attacks that patrols deterred.
- **Unfinished crises.** Both 2026 crises are still going on, so their duration scores, and therefore their severity, will rise.

## Quantitative results

Risk rose at Hormuz, from High (3.47) to Very high (4.37). It fell at Suez and the Red Sea, from Very high (4.47) to High (3.39). At Malacca it fell from 1.92 at the piracy peak to 1.66 in 2025 and 1.52 in 2026, staying in the Low band throughout. Almost all of the Hormuz rise came from severity, while every Malacca change came from likelihood.

&#91;embedded content: research/quantitative/qcri.py, central inputs for all eight periods; dashed curves mark the band boundaries R = 2, 3 and 4\]

The Hormuz arrow is almost vertical because attacks and insurance were near their maximum in both wars; what changed was how much harm each war did to trade and prices. The Malacca points all sit on the floor of the map because traffic through the strait grew in every period.

### How certain each score is

Each period was rerun with the lowest and the highest credible value of every input.

| Case and period | Band | R with the lowest and highest inputs | Main uncertainty |
| --- | --- | --- | --- |
| Hormuz: Tanker War, 1984–88 | High | 3.41–3.79 | Duration (53 months from 1984, or 90 from 1981); no freight index |
| Hormuz: 2026 closure | Very high | 4.09–4.57 | Attack count (93–200 a year); the crisis is still going on |
| Suez: 1967–75 closure | Very high | 4.03–4.95 | No oil-price or premium data; the freight rise comes from one press report |
| Red Sea: 2023–26 Houthi crisis | High | 3.11–3.76 | Premiums (0.5–3%) and traffic lost (42–70%) |
| Malacca: piracy peak, 2000–05 | Low | 1.92–2.07 | One source for the 0.4% premium |
| Malacca: 2008 | Low | 1.19–1.35 | 2 attacks in the Malacca Strait (IMB) or about 8 in both straits (RSIS) |
| Malacca: 2025 | Low | 1.12–1.66 | Area: 1 incident in the Malacca Strait, 108 including the Singapore Strait |
| Malacca: 2026 (January–September) | Low | 1.12–1.56 | Area, as for 2025; only nine months of data |

### Inputs and their sources

**Hormuz**

| Indicator | Tanker War, 1984–88 | 2026 closure |
| --- | --- | --- |
| Attacks a year (A) | 178 ships attacked or damaged in 1987 (Lloyd's Shipping Intelligence via UPI, 10 Dec 1987, B3; 179–181 in USNI *Proceedings*, May 1988, B2) | About 140: at least 70 between 28 February and late August (IMO via Seatrade Maritime, 2026, C2) |
| Premium (p) | About 5% of hull value, the "Tanker War rate" (Lloyd's List, March 2026, B2) | 7.5%, rising towards 10% (Lloyd's List, 11 March 2026, B2; S&P Global/Marsh, 22 July 2026, B1) |
| Traffic lost (T) | 25% fall in Gulf commercial shipping (Strauss Center, n.d., B2) | 90%: exports below 10% of normal (IEA, 11 March 2026, A1) |
| Months (D) | 53, from Iraq's escalation in March 1984 to the ceasefire of 20 August 1988 (derived; UPI, 1984 and 1988, B1–B2) | 7.7, from 28 February to 19 October 2026 and continuing (derived) |
| Brent rise (P) | 6.9%: $18.58 to $19.86, May–July 1987 (FRED/EIA, A1) | 65%: $71.36 on 27 February to $118 on 31 March (FRED, A1; EIA, A1) |
| Freight rise (F) | No data | 1,041%: VLCC Gulf–China from $123,825 to $1,412,594 a day (Clarksons via Riviera Maritime Media, C2; Baltic Exchange via Cyprus Shipping News, 15 October 2026, C2) |

**Suez and the Red Sea**

| Indicator | 1967–75 closure | 2023–26 Houthi crisis |
| --- | --- | --- |
| Attacks a year (A) | Not used: the canal was closed to all ships from 5 June 1967 to 5 June 1975, so L = 5 (Time, June 1967, B2; AP in the Michigan Daily, 6 June 1975, B1) | About 100 ships attacked, November 2023 to December 2024 (Seatrade Maritime, C2; Lloyd's List counted 99 by early 2026, B2) |
| Premium (p) | Not used (canal closed) | About 1% of hull value (Lloyd's List, January 2024, B2; Insurance Journal/Reuters, March 2024, B2) |
| Traffic lost (T) | 100% | 50%: Suez trade volume down by half year on year (IMF PortWatch blog, 7 March 2024, A1) |
| Months (D) | 96 | 35, from 19 November 2023 to October 2026 (derived) |
| Brent rise (P) | No measured effect: the 1973–74 price shock came from the October War embargo | 6%: about $77 to $80–83 (Engine and World Oil, January 2024, C2) |
| Freight rise (F) | 100%: tanker rates "doubled" by late July 1967 (NYT, 23 July 1967, quoted by a blog, C3) | 246%: Drewry World Container Index, Shanghai–Rotterdam, to $4,951 by 18 January 2024 (Drewry, B2) |

**Malacca**

| Indicator | Piracy peak, 2000–05 | 2008 | 2025 | 2026 (January–September) |
| --- | --- | --- | --- | --- |
| Attacks a year (A) | 75 in 2000, Malacca Strait (ICC-IMB, 2001, A1) | About 8 in both straits (RSIS, B2); 2 in the Malacca Strait (ICC-IMB, 2009, A1) | 108 in both straits, 107 of them in the Singapore Strait (ReCAAP ISC Annual Report 2025, A1) | 23 to September, about 31 a year (ReCAAP via SAFETY4SEA, October 2026, C2) |
| Premium (p) | 0.4% of hull value while the strait was a listed war-risk area, June 2005 to August 2006 (Maritime Executive, 6 July 2005, C2) | Not listed: delisted on 7 August 2006 (London P&I Club circular via inforMARE, 2006, C1) | Not listed (Joint War Committee, JWLA-033, 2026, A1) | Not listed (same) |
| Traffic lost, months and Brent rise | None: transits rose from 43,965 in 1999 to 63,636 in 2004 (Marine Department Malaysia via IALA, B2) | None | None: a record 102,525 transits (Seatrade Maritime, 2026, C2) | None |
| Freight rise (F) | No data | No data | No data | No data |

### Changes between periods

| Comparison | Change in R | Change in L | Change in S | Low–high ranges separate? |
| --- | --- | --- | --- | --- |
| Hormuz: Tanker War → 2026 | +0.90 (+26%) | +0.03 | +1.47 | Yes |
| Suez 1967–75 → Red Sea 2023–26 | −1.07 (−24%) | −0.93 | −1.17 | Yes |
| Malacca: peak → 2025 | −0.26 (−14%) | −0.93 | 0 | Yes |
| Malacca: peak → 2026 | −0.40 (−21%) | −1.39 | 0 | Yes |
| Malacca: peak → 2008 | −0.57 (−30%) | −1.87 | 0 | Yes |
| Malacca: 2025 → 2026 | −0.15 (−9%) | −0.46 | 0 | No, so this change is not robust |

- **Hormuz.** Likelihood was near its ceiling in both wars, so the whole rise came from severity. In the 1980s Gulf shipping fell by a quarter and Brent barely moved (+7%). In 2026 nine-tenths of exports stopped, Brent rose 65% and VLCC freight rates rose elevenfold.
- **Suez and the Red Sea.** Both parts fell. A canal closed to every ship for eight years became a selective threat that each shipowner could choose to face or avoid, and about half of Suez trade carried on.
- **Malacca.** Severity never left its floor, because traffic grew in every period, so every change comes from likelihood. The fall from the peak to 2025 comes from insurance: the strait was a listed war-risk area in 2005 but not in 2025. On attack counts alone, 2025 (108 incidents in both straits) was above the 2000 peak (75 in the Malacca Strait).

### Does insurance agree with the attack rate?

A war-risk premium is the insurance market's own estimate of likelihood. A premium of p% of hull value means insurers expect at most about p losses per 100 voyages, and fewer once their margin is taken out. Comparing it with the observed attack rate checks the two likelihood indicators against each other.

| Case and period | Premium (% of hull value) | Insurers' implied chance of loss (upper bound) | Observed attacks per transit | Source of the observed rate |
| --- | --- | --- | --- | --- |
| Hormuz: Tanker War, 1987 | About 5% | 1 in 20 | Under 2% (1 in 50 or fewer) | Strauss Center (B2); fewer than a quarter of the ships hit were sunk or disabled |
| Hormuz: 2026 | 7.5% | 1 in 13 | About 5% (1 in 19) | Derived: at least 70 attacks ÷ about 1,330 transits, March–August 2026 (IMF PortWatch write-ups); an overestimate, since some ships were hit in port |
| Red Sea: 2024 | About 1% | 1 in 100 | About 0.76% (1 in 132); about 4 sunk (1 in 3,300) | Derived: about 100 attacks ÷ about 13,200 Suez transits in 2024 (Suez Canal Authority via Ahram Online, D2) |
| Malacca: peak | 0.4% (2005) | 1 in 250 | 0.13% in 2000 (1 in 746) | Derived: 75 attacks ÷ 55,957 transits (ICC-IMB, A1; Marine Department Malaysia, B2) |
| Malacca: 2025 | Not listed | – | 0.11% (1 in 949) | Derived: 108 incidents ÷ 102,525 transits (ReCAAP ISC, A1; Seatrade Maritime, C2) |

Wherever there was a premium, it was between 1.3 and 3 times the observed attack rate. Premiums therefore track likelihood but lean high, because insurers add a margin and also price in the cost of each attack. This is the overlap between likelihood and severity noted above.

### What cooperation could have done at most

The K term asks how much lower each later period's risk would be if, as the INFORM index assumes, every point of cooperation adds coping capacity. It keeps the later likelihood and severity but swaps in the earlier cooperation score.

```latex
R_K = \left(L \times S \times K\right)^{1/3}, \qquad K = 5 - \frac{C}{5}, \qquad R_{cf} = \left(L_2 \times S_2 \times K_1\right)^{1/3}
```

Because it assumes that cooperation always helps, this is a generous upper estimate, not proof.

| Comparison | Cooperation score, C (0–20) | R\_K, earlier → later | Later R\_K without the extra cooperation | Generous cooperation effect | Cooperation's share in process tracing |
| --- | --- | --- | --- | --- | --- |
| Hormuz: Tanker War → 2026 | 9 → 12 | 3.38 → 3.68 | 3.94 | −0.26, but risk still rose | 5.7% |
| Suez 1967–75 → Red Sea 2023–26 | 5 → 13 | 4.31 → 3.02 | 3.58 | −0.56 (44% of the fall) | 8.5%, partly negative |
| Malacca: peak → 2025 | 6 → 15 | 2.41 → 1.77 | 2.19 | −0.42 (65% of the fall) | Not tested separately |
| Malacca: peak → 2026 | 6 → 15 | 2.41 → 1.66 | 2.06 | −0.40 (53% of the fall) | Not tested separately |
| Malacca: peak → 2008 | 6 → 13 | 2.41 → 1.64 | 1.91 | −0.27 (35% of the fall) | 15.8–23.7% |
| Malacca: 2025 → 2026 | 15 → 15 | 1.77 → 1.66 | 1.66 | None (cooperation did not change) | 13.6% patrols, 27.3% information sharing |

Even on this generous reading, cooperation could not stop risk rising at Hormuz. At Suez and Malacca it could account for 35–65% of the fall in R\_K, but those shares are inflated: K is built from the cooperation score, so part of each fall is the assumption itself. Process tracing, which does not assume that cooperation helps, gives cooperation 5.7–23.7% of each change. Cooperation's real effect therefore lies somewhere between the two, and both methods give Hormuz the smallest effect.

### Sensitivity tests

The direction of every main change survives 19 other versions of the equation, with one exception at Malacca (`research/quantitative/sensitivity.py`). Each test changes one thing: one goalpost halved or doubled, likelihood or severity weighted two to one, an ordinary average of L and S instead of the geometric mean, or one indicator left out.

| Comparison | Central change in R | Range across the 19 tests | Does the direction ever reverse? |
| --- | --- | --- | --- |
| Hormuz: Tanker War → 2026 | +0.90 | +0.57 (without Brent) to +1.80 (without duration) | No |
| Suez 1967–75 → Red Sea 2023–26 | −1.07 | −0.77 (without Brent) to −1.61 (without freight) | No |
| Malacca: peak → 2025 | −0.26 | +0.06 (without insurance) to −0.77 (without attacks) | Yes, once: without insurance, risk rises slightly |
| Malacca: peak → 2026 | −0.40 | −0.16 (without insurance) to −0.77 (without attacks) | No |
| Malacca: peak → 2008 | −0.57 | −0.32 (severity weighted 2:1) to −0.94 (ordinary average) | No |
| Malacca: 2025 → 2026 | −0.15 | 0.00 (without attacks) to −0.23 | No, but the low–high ranges overlap |

The bands are just as stable. Hormuz in 2026 and Suez in 1967–75 stay Very high in every test, and the Red Sea stays High. The Tanker War drops to Moderate only if duration is left out. The Malacca peak and Malacca 2025 reach Moderate in a few tests, which shows how close Malacca sits to the line between Low and Moderate. The banded version used in earlier drafts, the CCRI, gives the same direction in every comparison. The very first version, the CDRI, scored the closed canal's likelihood as 4 rather than 5 and so found almost no change at Suez (14.7 to 14.4 on its 1–25 scale). Even with that lower score for 1967, the QCRI still shows a fall of 0.61.

The one reversal matters for the Malacca verdict. Without the insurance indicator, risk in 2025 (2.13) sits just above the peak (2.07). The Straits of Malacca and Singapore together had 108 incidents in 2025 (ReCAAP ISC Annual Report 2025, A1), against 75 in the Malacca Strait alone in 2000 (ICC-IMB, 2001, A1). Two facts still point to a real fall. First, 107 of the 108 incidents were in the Singapore Strait; with the 1 incident in the Malacca Strait itself, R is 1.12. Second, no incident anywhere in Asia in 2025 reached ReCAAP's most serious category, and 53% were petty theft (ReCAAP ISC Annual Report 2025, A1). The safer claim is that Malacca risk stayed Low throughout, and that the type and place of crime changed more than the danger to trade did.

## Strait of Hormuz: the Tanker War (1980–88) vs the 2026 closure

Multilateral cooperation at Hormuz grew between the two periods, but it only softened severity at the margin and left likelihood unchanged. On the project's 1–5 risk index (QCRI), R rose from 3.47 to 4.37, up 26%, and almost all of that rise came from severity. The main reason was the type of threat: in 2026 a state at war chose closure, and no coalition could reverse that choice.

### Likelihood

In the 1980s two belligerents raided each other's trade, but neither sought to close the strait. Iraq escalated attacks on neutral ships in March 1984 under a declared blockade of Iranian ports (UPI, 7 Mar 1984, B2). It made about two-thirds of the attacks on more than 450 ships (The National, 2020, C1).

Iran retaliated against Kuwaiti and Saudi trade (UPI, 15 May 1984, B2), but it needed Hormuz for its own oil exports. A mine blamed on Iran holed the reflagged tanker Bridgeton on the first US convoy (UPI, 24 Jul 1987, B1). Later, a missile believed to be an Iranian Silkworm hit the Sea Isle City (UPI, 16 Oct 1987, B1).

In 2026 the threat came from one state at war: the US and Israel struck Iran on 28 February (Congressional Research Service, 2026, B2). Iran declared the strait closed and used it as a bargaining tool, tying reopening to seven conditions (The National, 4 Oct 2026, C1). Its new strait authority charged permit fees of up to $2m a voyage (Raman, War on the Rocks, 2026, C3).

Each new closure order cut traffic: on 21 June, daily transits fell from 26 to 5 (Kpler via Reuters/gCaptain, 22 Jun 2026, B1). Iran's means had also grown, with stocks of mines, missiles and small boats above Tanker War levels (Talmadge, 2008, A2).

The International Maritime Organization (IMO) reported the central lanes unusable because of mines (IMO, n.d., A2). Yet the US military said a drone and a missile, not a mine, struck the El Gaia (Arab News, 2026, C3, graded here).

In 1987 Lloyd's counted 178 ships attacked or damaged (UPI, 10 Dec 1987, B3); a naval journal gives 179–181 (USNI Proceedings, May 1988, B2). In 2026 at least 70 commercial ships were attacked by late August (IMO via Seatrade Maritime, Aug 2026, C2, graded here). Another 23 attacks came in 1–15 October, almost double the monthly average (AFP via Ahram Online, Oct 2026, C1, graded here).

Yearly attacks were similar: 178 in 1987 against about 140 in 2026, scaling up the August count. The index therefore puts likelihood near its ceiling of 5 in both periods: L is 4.76 for the Tanker War and 4.78 for 2026. Higher war-risk premiums in 2026 offset the slightly lower attack rate.

With both near the ceiling, L barely separates the periods, so an insurance check helps. A war-risk premium of p% of hull value implies that insurers expect at most p losses per 100 voyages. The Tanker War rate of about 5% (Lloyd's List, 11 Mar 2026, B2) thus implied up to 1 loss in 20.

Quotes reached 7.5–10% in 2026 (S&P Global/Marsh, 22 Jul 2026, B1); at 7.5%, that implies up to 1 loss in 13. The Strauss Center puts the 1980s peak at Kharg Island higher, at 7.5% (Strauss Center, n.d., B2). Observed hit rates were lower: under 2% of ships in the 1980s (Strauss Center, n.d., B2) and about 5% in 2026.

The 2026 rate divides at least 70 attacks by about 1,330 transits from PortWatch write-ups (GlobalMilitary.net and World Monitor, 2026, D3, graded here). That overstates the risk, since some ships were hit in port, yet a 2026 voyage was probably still more dangerous than one in 1987. In both periods premiums ran above observed rates, so they tracked likelihood but leaned high.

### Severity

In the 1980s, Gulf commercial shipping fell by about 25% (Strauss Center, n.d., B2). Oil flow through the strait fell from over 7 to under 4 million barrels a day (mb/d) (USIP Iran Primer, n.d., B2, graded here). That fall was partly market-driven.

By 10 March 2026, by contrast, exports through Hormuz had fallen below 10% of pre-conflict levels (IEA, 11 Mar 2026, A1). Daily transits fell from 129 to 6 (UNCTAD, Apr 2026, A1, seen only via a university mirror graded D6). The World Bank called it the largest oil supply shock on record (World Bank, Apr 2026, A2).

Recovery is disputed: Kpler data put early-October crude flows at about 74% of pre-war (Iran International, 8 Oct 2026, C1). Another Kpler reading had exports about 40% below normal in the week to 12 October (CNBC, 14 Oct 2026, B1).

Duration is the one measure on which the Tanker War was worse. Attacks on neutral shipping ran for 53 months, until the ceasefire of 20 August 1988 (UPI, 18 Jul 1988, B1). The 2026 closure has lasted 7.7 months and continues, but it nearly stopped the flow rather than slowing it.

Prices show the sharpest contrast: Brent crude rose only 6.9%, from $18.58 in May 1987 to $19.86 in July (FRED, 1987, A1). In 2026 it rose 65%, from $71.36 on 27 February (FRED, 2026, A1) to $118 on 31 March (EIA, 2026, A1).

No freight data were found for the 1980s. The Gulf–China supertanker rate was $123,825 a day in mid-December 2025 (Clarksons via Riviera Maritime Media, Dec 2025, C2, graded here). By 15 October 2026 it was $1,412,594, up 1,041% (Baltic Exchange via Cyprus Shipping News, 15 Oct 2026, C2, graded here).

Lloyd's List confirms the record run (Lloyd's List, 2 Mar 2026, B1). Insurance also became a heavy cost, as underwriters cancelled Gulf war cover from 5 March (S&P Global, 6 Mar 2026, B2). New quotes meant over $10m in premium for one supertanker trip (Lloyd's List, 11 Mar 2026, B2).

In 1984, seven-day cover for Kharg Island doubled from 0.75% to 1.5% of hull value (UPI, 15 May 1984, B2). Marine insurers lost over $500m between September 1980 and March 1984 (UPI, 9 Mar 1984, B2). By May 2026, lost Gulf oil output had passed 1bn barrels (IEA Oil Market Report, May 2026, A2).

Human costs were higher in the 1980s, though counts differ widely. They run from 116 seafarers killed in 1984–87 (USNI Proceedings, May 1988, B2) to over 400 (Navias and Hooton, 1996, A2). By 15 October 2026 the IMO counted 24 seafarers dead (AFP via Ahram Online, Oct 2026, C1, graded here).

The index captures this gap: S rose from 2.53 to 4.00. Traffic lost scores 0.900 against 0.250 and the price rise 0.650 against 0.069, while only duration is lower in 2026 (0.451 against 0.832). Freight adds a full 1.000 for 2026 but is missing for the 1980s, so the scores are not perfectly like for like.

### The five cooperation factors

Scores (0–4, higher is stronger) come from the project's attribution test.

| Factor | Tanker War: score (0–4) and evidence | 2026: score (0–4) and evidence | Effect on likelihood | Effect on severity |
| --- | --- | --- | --- | --- |
| Formal frameworks | Score 2. Resolution 598 deplored attacks on shipping (UNSC, 20 Jul 1987, A1). Reflagging was a bilateral US–Kuwait deal (UPI, 21 Jul 1987, B1). | Score 3. Resolution 2817 passed 13–0 (UNSC, 11 Mar 2026, A1). An escort draft was vetoed (Greek UN Mission, 7 Apr 2026, B1). | None in either period. | Slight: Resolution 598 framed the 1988 ceasefire. |
| Joint operations | Score 2. US convoys ran from July 1987 (UPI, 23 Jul 1987, B1). Five European navies sent minesweepers (UPI, 11 Aug 1987, B1). | Score 2. The UK–France mission was undeployed in October (The National, 6 Oct 2026, C2). The US claimed its escorts reached 22% of normal traffic (gCaptain, 15 Oct 2026, C2). | Worse in 1987, as convoys drew mines; none in 2026. | Slight: some escorted cargoes moved. |
| Information sharing | Score 1. With no shared air picture, USS Vincennes downed an Iranian airliner (UPI, 4 Jul 1988, B1). | Score 3. JMIC issued shared threat levels (JMIC via Seatrade, 2026, B2). US and tracker counts clashed: about 1,000 transits against 650 (gCaptain/Bloomberg, 5 Jun 2026, B2). | None. | Worse in 1988; any 2026 saving in lives is unmeasured. |
| Response speed | Score 2. The first convoy came over four months after a US offer (Washington Post, 28 Mar 1987, B2). | Score 3. The IEA release was agreed in 11 days (IEA, 11 Mar 2026, A1). A US-backed $40bn reinsurance facility existed by 6 April (Insurance Journal, 6 Apr 2026, C2). | None. | Slight in 2026, through prices and insurance cover. |
| Enforcement | Score 2. Praying Mantis hit Iran's navy (UPI, 18 Apr 1988, B2), but Iraqi attacks went on (UPI, 14 May 1988, B2). | Score 1. Resolution 2817 authorised no force (UNSC, 11 Mar 2026, A1). | None from multilateral action. | None from multilateral action. |
| Total (out of 20) | 9 | 12 | None overall. | Slight overall. |

**Formal frameworks:** Iran accepted Resolution 598 only a year after it passed (UPI, 18 Jul 1988, B1), while attacks peaked in between. In 2026 Resolution 2817 condemned the closure, yet Iran kept setting its own conditions for reopening (The National, 4 Oct 2026, C1). Frameworks did nothing to likelihood in either period and reduced severity only slightly, by framing the 1988 ceasefire once Iran chose peace.

**Joint operations:** five European navies sent minesweepers in 1987 but cleared "only a few dozen mines" (UPI, 2 Apr 1989, B2). In 2026 the US military claimed about 30 escorted transits a day, even as attacks hit a new high (gCaptain, 15 Oct 2026, C2). Joint operations made likelihood worse in 1987, when convoys drew mines and missiles, and eased severity only slightly in either period.

**Information sharing:** with no shared air picture, USS Vincennes shot down an Iranian airliner in 1988, killing 290 (UPI, 4 Jul 1988, B1). In 2026 the Joint Maritime Information Center gave all ships a common threat rating (JMIC via Seatrade, 2026, B2). Its absence made 1988 worse, but its presence in 2026 did not reduce likelihood, and any saving in lives is unmeasured.

**Response speed:** the first convoy sailed in July 1987, over four months after the US offered escorts (Washington Post, 28 Mar 1987, B2). In 2026 the International Energy Agency's 32 members agreed a record 400-million-barrel release in 11 days (IEA, 11 Mar 2026, A1). Speed trimmed severity at the margin but not likelihood; even so, Brent hit $100 the next day (CNBC, 12 Mar 2026, B1).

**Enforcement:** US strikes crippled Iran's navy four days after a US frigate was mined (NHHC, Apr 2018, B1, graded here). In 2026 Resolution 2817 authorised no force, and the IMO condemned tolls with no means to stop them (Foreign Policy, 26 Mar 2026, B2). Multilateral enforcement did nothing in either period; the only coercion with any effect was unilateral US force in 1988.

### Other explanations

Process tracing gives cooperation 5.7% of the causal weight, the smallest share of nine causes.

**Type of threat (15.1%):** a state choosing closure is far harder to counter than two belligerents raiding trade. Chatham House judged that the strait cannot be opened by force (Chatham House, 1 May 2026, B2). This largest share explains why more cooperation did not lower risk.

**Trade concentration (13.2%):** about 20 mb/d, roughly 25% of seaborne oil, used the strait before the war (IEA, 11 Mar 2026, A1). The 1984 flow was over 7 mb/d (USIP Iran Primer, n.d., B2, graded here); an estimated 12% share of world demand is unverified. So the same closure caused a far bigger shock, and concentration clearly outweighs cooperation.

**US role (13.2%):** the US escorted convoys as a neutral protector in 1987–88 (UPI, 23 Jul 1987, B1), but was a belligerent in 2026. Its blockade of Iranian ports from 13 April (Atlantic Council, 2026, B2) preceded Iran's re-closure on 18 April (Al Jazeera, 11 Jun 2026, C2). A belligerent's escorts invite attack, so this factor outweighs cooperation, though it overlaps with the type of threat.

**Pipelines and oil surplus (11.3% each):** bypass lines could carry about 9 of the 20 mb/d (Al Jazeera, 27 Mar 2026, B2). Bordoff and O'Sullivan credit pre-war oversupply and pipelines, not navies, for the milder-than-feared outcome (Foreign Affairs, 14 Aug 2026, B2). Both cushioned severity more than cooperation did, though the bypasses themselves proved vulnerable.

**Technology (11.3%):** mines mattered in both periods, so the new element in 2026 was cheap drones and precision missiles. Drones shut Saudi Arabia's East–West bypass pipeline on 13 September (Saudi Gazette, Sep 2026, C1). Technology raised the ceiling on disruption but did not cause closure, so it outweighs cooperation but not threat type.

**Shale (9.4%):** though a net oil exporter, the US faced the same global price shock (Brookings, 2026, B2). Shale changed who is exposed, not the world price, so it explains little of the change. Even so, the test gives it more weight than cooperation.

### What the numbers show

Risk rose by 0.90, and the low–high ranges (3.41–3.79 and 4.09–4.57) do not overlap, so the result is robust. Almost all of the rise is in severity: S rose by 1.47 and L by only 0.03. Cooperation rose by 3 points, from 9 to 12 out of 20.

The best-case check gives cooperation full credit: without the extra 3 points, adjusted 2026 risk would be 3.94, not 3.68. That −0.26 is real but small, because adjusted risk still rose from 3.38 to 3.68. Cooperation pushed the right way, but far too weakly to offset the rise.

### Judgement

Multilateral cooperation did not reduce the likelihood of disruption at Hormuz, and it reduced severity only at the margin. Likelihood stayed near the maximum in both periods because attackers' choices, not coalitions, set the pace of attacks. The 2026 rise in cooperation came from stocks, insurance and information, not navies, and these cushioned prices rather than reopening the strait.

The main cause of the change was the type of threat: a state at war chose closure, which escorts could not reverse. It leads the attribution test at 15.1%, but only narrowly, so trade concentration and the US role (13.2% each) share the explanation. The best counter-argument, that the IEA release capped prices, is plausible but unmeasured, and Brent still rose 65% (FRED, 2026, A1; EIA, 2026, A1).

Confidence is moderate. The verdict survives every sensitivity test: generous scoring lifts cooperation only to 10.7%, and the risk ranges never overlap. However, most evidence comes from search snippets, the 1980s lack freight data, the crisis continues and several factors overlap.

## Suez Canal and Red Sea: the 1967–75 closure vs the 2023–26 Houthi crisis

Multilateral cooperation did little to reduce the likelihood of disruption on the Suez–Red Sea route and only modestly reduced its severity. On the project's 1–5 risk index, risk (R) fell from 4.47 in 1967–75 to 3.39 in 2023–26, a 24% fall. The main reason was the type of threat: a state shut the canal in 1967, but a non-state group attacked only selected ships.

### Likelihood

In June 1967 Egypt closed the canal itself, leaving it "blocked at both ends by scuttled Egyptian ships" (Time, 1967, B2). Disruption was certain rather than a matter of chance, so the index gives the closed route the maximum likelihood, L = 5.00. No ships passed, so there were no attacks to count and no war-risk premiums (extra insurance per voyage) to price.

From November 2023 a non-state armed group, the Houthis, attacked selected ships instead of closing the route (UN Security Council, 2024, A1). Cheap military technology and their position on the Bab el-Mandeb gave them the means (Arellanes, 2025, A2). About 100 ships were attacked from November 2023 to December 2024 (Seatrade, 2025, C2).

Other counts give 87 ships by May 2024 (South24, 2024, C2) and 99 attacks by early 2026 (Container News citing Lloyd's List, 2026, C2). Attacks fell 84% in 2025 (ACLED, 2025, B2), but the Houthis declared a blockade on Saudi shipping on 20 July 2026 (AP, 2026, B1). Saudi-linked tankers then paid premiums of about 3% at Yanbu and up to 7% at Jizan (Insurance Journal/Reuters, 2026, B2).

The index builds likelihood from attacks per year and the war-risk premium. With about 100 attacks a year and a premium of about 1% of the ship's value, L is 4.07 (Lloyd's List, 2024, B2). L fell by 0.93 because ships could choose to sail, and most passed safely.

An insurance check supports this: a 1% premium implies insurers expected at most 1 loss in 100 voyages. In 2024 about 0.76% of transits were attacked (1 in 132): about 100 attacks against about 13,200 transits (Ahram Online, 2025, D2). Only about 4 ships sank, 1 in 3,300 transits (AP via CP24, 2025, B1, graded here).

Across the index, premiums run 1.3–3 times the observed attack rate: they track likelihood but lean high.

### Severity

In 1966 the canal carried 237m tons of cargo, about 15% of world seaborne trade (CIA, 1967, B2, graded here). From June 1967 that fell to zero for eight years (Time, 1967, B2; AP, 1975, B1). In 2023–26 the loss was partial: Suez trade volume fell about 50% year on year in early 2024 (IMF, 2024, A1).

Annual transits halved, from about 26,400 in 2023 to about 13,200 in 2024 (Ahram Online, 2025, D2). Because that is Egyptian state media, UNCTAD's figures are a useful check. UNCTAD found transits down 42% from their peak by February and tonnage down 70% by mid-2024 (UNCTAD, 2024, A1; UNCTAD RMT, 2024, A1).

The closure lasted 96 months, from 5 June 1967 to 5 June 1975 (AP, 1975, B1). The Houthi crisis, which began on 19 November 2023, had lasted 35 months by October 2026 (UN Security Council, 2024, A1). Even 100 days after the last 2025 attack, Suez transits were still about 60% below 2023 (Container News citing BIMCO, 2026, C2).

Tanker rates "doubled" by late July 1967 (NYT via The Gamming blog, 1967, C3, graded here). The US Bureau of Mines called them "markedly higher" (US Minerals Yearbook, 1968, A2, graded here). In 2023–24 the Drewry container index for Shanghai–Rotterdam rose 246%, to $4,951 per 40-ft container by 18 January 2024 (Drewry WCI, 2024, B2).

The sources give no measured oil-price effect for 1967; the 1973–74 shock came from the October War embargo (Time, 1973, B3). In 2023–24 Brent rose only about 6%, from about $77 to $80–83 a barrel (Engine and World Oil, 2024, C2, graded here). In an escalation scenario, the ECB put the extra euro-area inflation at only about 0.25 percentage points (ECB, 2024, A2).

A UN study put Egypt's lost tolls in 1967–75 at $250m a year (AP, 2021, B1). In 2023–26 canal revenue fell from $10.25bn in 2023 to $3.99bn in 2024 (Egypt Today, 2025, D2; Ahram Online, 2025, D2). Both are state media repeating the Canal Authority; Reuters reported Sisi's claim of about $7bn lost (Reuters via CNBC Africa, 2024, B2).

The IMF put the loss nearer $6bn (Al Jazeera citing the IMF, 2025, B2). For 1967–75, a UN estimate put the total cost to the world at about $10bn (Time, 1975, B3). UNCTAD's 1973 study assessed these costs (UNCTAD, 1973, A3), but Abrahamson's review that year called its estimates exaggerated (Abrahamson, 1973, C3, graded here).

Feyrer finds that distance cut trade only about half as much as standard estimates suggest (Feyrer, 2021, A2). CEPII finds a smaller effect still, so the size of the 1967 trade shock is contested (CEPII, 2016, B2).

In 1967, 15 ships were trapped for eight years, 14 in the Great Bitter Lake (Time, 1969, B2). A later report counted 16 ships (Time, 1974, B4). In 2023–26 ships could divert rather than be trapped, but four were sunk (AP via CP24, 2025, B1, graded here).

Seafarer deaths to July 2025 range from 6 (Iran International, 2025, C3, graded here) to 8 (Dawn, 2025, C3, graded here). Diverted ships went round the Cape of Good Hope, adding more than 10 days to deliveries (IMF, 2024, A1). Cape arrivals rose 89% by mid-2024 (UNCTAD RMT, 2024, A1).

Severity averages traffic lost, duration, freight and, where data exist, oil prices; S fell from 3.99 to 2.82. Traffic lost fell from all to half of normal, and duration from 96 to 35 months, outweighing a sharper freight rise. So 1967–75 was worse for trade, duration and stranded crews, while 2023–26 was worse for freight, insurance and lives.

### The five cooperation factors

| Factor | 1967–75: score (0–4) and evidence | 2023–26: score (0–4) and evidence | Effect on likelihood | Effect on severity |
| --- | --- | --- | --- | --- |
| Formal frameworks | Score 1. Resolution 242 affirmed free navigation but had no enforcement (UN Security Council, 1967, A1). | Score 2. Resolution 2722 passed 11–0–4 (UN Security Council, 2024, A1). EU decisions created Aspides (Council of the EU, 2024–26, A1). Egypt did not publicly join Prosperity Guardian (Mada Masr, 2023, C1). | None. The canal stayed shut, and attacks went on. | Small. Frameworks gave legitimacy, not protection. |
| Joint operations | Score 2. US, UK and French units cleared the canal from April 1974 (CTF-65, 1975, B1). Ten wrecks were raised (Boyd, 1976, B2). | Score 3. Prosperity Guardian began in December 2023 (CNN, 2023, B1). Aspides escorted over 720 ships by August 2026 (EEAS via Lovguiden, 2026, B2, graded here). Atalanta was widened into parts of the Red Sea (Council of the EU, 2024, A1). ECFR calls the European missions "fragmented and under-resourced" (ECFR, 2026, B2). | Little. The patrols did not deter the Houthis (Forces News citing IISS, 2024–25, C2). | Large once politics allowed: clearance ended the closure in 1975. The naval operation "successfully prevented the loss of civilian lives" (Forces News citing IISS, 2024–25, C2). |
| Information sharing | Score 1. UN observers reported on the ceasefire, not on shipping (UN S/8053/Add.4, 1967, A2, graded here). | Score 3. Aspides issued threat alerts (ANSA, 2026, B2). Its mandate added sharing with Interpol and the IMO (Council of the EU, 2024–26, A1). | Little. Alerts did not change Houthi intent. | Some. Owners could judge the risk and divert. |
| Response speed | Score 1. Clearance began about seven years after the closure (CTF-65, 1975, B1). | Score 3. Prosperity Guardian came 29 days after the first attack (CNN, 2023, B1). Aspides launched about three months after it (Council of the EU, 2024–26, A1). | None. Maersk had paused before the coalition formed (gCaptain, 2024, C1). | Small. Help arrived faster once attacks began. |
| Enforcement | Score 0. Nothing forced Egypt to reopen, and Israeli ships were still barred in 1975 (UPI, 1975, B2). | Score 2. US and UK strikes hit about 60 targets in January 2024 (CSIS, 2024, B2). Djibouti refused US strikes from its base (gCaptain, undated, C2). | Raised it. Premiums tripled within a week of the strikes (Lloyd's List, 2024, B2). | Little. Attacks resumed, and two ships sank in July 2025 (Bloomberg, 2025, B1). |
| Total (out of 20) | 5 | 13 (range 12–14) | Little overall | Some, mainly lower harm per attack |

**Formal frameworks:** Resolution 242 affirmed "freedom of navigation through international waterways", yet the canal stayed closed until 1975 (UN Security Council, 1967, A1). Resolution 2722 condemned the attacks, but coastal Eritrea says "no force substitutes the littoral states" (UN Security Council, 2024, A1; Shabait, 2025, D3). Frameworks gave legitimacy in both periods but, without enforcement or regional support, changed neither likelihood nor severity.

**Joint operations:** The 1974 clearance began only after the January 1974 disengagement agreement (Egypt and Israel, 1974, A1). Spain declined Prosperity Guardian and Aspides (Última Hora, 2023, C1; The Objective, 2024, C1), though it leads Atalanta (Council of the EU, 2024, A1). Joint operations cut harm per attack and, once politics allowed, ended the closure, but they did not deter attacks.

**Information sharing:** In 1967 UN observers, 43 at 9 posts, reported on the ceasefire rather than shipping (UN S/8053/Add.4, 1967, A2, graded here). In 2023–26 Aspides issued threat alerts to shipping, helping owners judge when to divert (ANSA, 2026, B2). Better information probably lowered harm per attack, but it gave owners reasons to avoid the route, not to return.

**Response speed:** Clearance began seven years late, then took eight months once Nixon's letter settled the politics (Nixon, 1974, A2; CTF-65, 1975, B1). Prosperity Guardian came 29 days after the first attack, yet Maersk had already paused Red Sea transits (CNN, 2023, B1; gCaptain, 2024, C1). Speed helped the response but not the outcome, because owners had decided before the navies arrived.

**Enforcement:** After the January 2024 strikes on about 60 targets, premiums tripled within a week (CSIS, 2024, B2; Lloyd's List, 2024, B2). The 2025 truce was a bilateral US–Houthi deal brokered by Oman, not multilateral cooperation (CBS News, 2025, B1). Enforcement raised insured risk in the short term and did not stop attacks, so its sign is negative or mixed.

### Other explanations

Process tracing scores how well each of eight causes fits the evidence; cooperation takes 8.5%, with a mixed sign. A mixed sign means it pushed risk down in some ways and up in others. Five other causes each take a larger share.

The type of threat scores 17.0%, twice cooperation's share: a state closure stops every ship, but a selective threat lets each owner decide. In late 2025 container-ship transits were 86% below 2023, but product tankers only 19% (Container News citing BIMCO, 2026, C2). Selectivity, not naval protection, explains why the trade loss was partial, so this is the main cause.

Connected crises score 17.0%, because attacks paused with Gaza ceasefires and restarted when fighting resumed (Times of Israel and Al Jazeera, 2025, B2). The 2026 Hormuz war made Saudi Arabia export through the Red Sea, which the Houthis then blockaded (CSIS, 2026, B2; AP, 2026, B1). These crises switched attacks on and off, which navies could not do, so they outweigh cooperation.

Technology scores 14.9%: cheap drones gave a local militia reach, and a drone boat sank the Tutor (Al Jazeera, 2024, B1). Larger ships cut the other way: supertankers sailing round the Cape made the 1975 reopening an "anti-climax" (Samuelson, 1975, C2). Technology outweighs cooperation, raising likelihood but lowering severity.

Supply-chain adaptation scores 14.9%: carriers added ships to keep port calls steady on the Cape route (Yap and Yang, 2024, A2). Transport-chain costs to Europe rose only 3–13% (Bedoya-Maya and others, 2025, A2). Industry, not navies, limited the cost of diversion, so this factor also outweighs cooperation.

Physical alternatives score 12.8%; the Cape existed in both periods, but the SUMED pipeline opened only in 1977 (SUMED, undated, B2, graded here). In 2026 some Saudi crude moved through SUMED around the blockade (Lloyd's List Intelligence, 2026, B2). SUMED lowered severity only at the margin, but alternatives together still outweigh cooperation.

Cargo mix (8.5%) and the bilateral 2025 truce (6.4%) complete the eight causes. Cooperation therefore ties for sixth place, with half the share of the two leading causes.

### What the numbers show

Risk fell by 1.07 points, from 4.47 to 3.39 (−24%), and the ranges (4.03–4.95 and 3.11–3.76) do not overlap. Both parts fell: likelihood by 0.93 (5.00 to 4.07) and severity by 1.17 (3.99 to 2.82). Over the same period the cooperation score rose by 8 points, from 5 to 13 out of 20.

A version of the index that lets more cooperation lower risk shows risk falling from 4.31 to 3.02. Assuming cooperation always helps, it explains at most 0.56 points of that fall, or 44%. Process tracing gives cooperation only 8.5%, with a mixed sign, so 44% is a ceiling, not an estimate.

### Judgement

Cooperation barely reduced the likelihood of disruption: Resolution 242 left the canal shut, and attacks in 2023–26 followed Gaza, not navies. It reduced severity more, by limiting deaths per attack (Forces News citing IISS, 2024–25, C2). The 1974 clearance did end the closure, but only after the disengagement deal, so cooperation followed politics (Egypt and Israel, 1974, A1).

The main cause was the type of threat: a state closure is certain and total, but selective attacks are probable and partial. Connected crises, technology and industry adaptation come next. Cooperation was a minor cause, at 8.5% with a mixed sign.

The strongest counter-argument is that the index counts trade, not lives, so it undervalues the escorts. That is fair, yet Tallis argues the US Navy won its battles but failed to bring traffic back (Tallis, 2025, C2). Overall, multilateral cooperation reduced disruption at this chokepoint only to a limited extent, mainly by lowering harm per attack.

Confidence is moderate: the fall in risk is robust because the ranges do not overlap, but the 1967 data are thin. There are no 1967 premiums, the freight figure is second-hand, Egypt's figures are state media, and the crisis is not over. Most figures were seen only in search snippets, and the process-tracing scores rest on judgement.

## Strait of Malacca: the piracy peak (1999–2005), the fall to 2008, and 2025–26

Multilateral cooperation was a major reason among several for the fall in risk in the Strait of Malacca, but not the main one. On the project's 1–5 Quantitative Chokepoint Risk Index (QCRI), risk (R) fell from 1.92 at the piracy peak to 1.66 in 2025 and 1.52 in 2026, and it was lowest in 2008, at 1.35.

Risk stayed in the Low band throughout, and only likelihood moved: severity stayed at its minimum because piracy never slowed trade. The fall from 2025 to 2026 is within the margin of error.

### Likelihood

The International Maritime Bureau (IMB), a shipowner-backed watchdog, counts attacks in the Malacca Strait itself; they rose sharply in 2000, then collapsed.

| Year | IMB attacks, Malacca Strait | Source |
| --- | --- | --- |
| 1999 | 2 | ICC-IMB, 2001, A1 |
| 2000 | 75 | ICC-IMB, 2001, A1 |
| 2002 | 16 | Al Jazeera, 2003, B2, graded here |
| 2004 | 38 (37 in another count) | ICC-IMB, Jan 2006, A1 (38); Beckman, 2012, B2 (37) |
| 2005 | 12 | ICC-IMB, Jan 2006, A1 |
| 2008 | 2 | ICC-IMB, 2009, A1 |

ReCAAP, an intergovernmental body, counted 108 incidents in the Malacca and Singapore straits in 2025, the most since 2007 (ReCAAP, Jan 2026, A1). Only 1 incident was in the Malacca Strait; the other 107 were in the Singapore Strait (ReCAAP, Jan 2026, A1).

The surge reversed: 21 incidents in the first half of 2026, down 74% on 80 a year earlier (ReCAAP, Jul 2026, A1). By September the total was 23 incidents, about 31 a year, with 1 in the Malacca Strait (SAFETY4SEA, 2026, C2).

These counts are not like for like: the peak sat in the Malacca Strait, the recent surge in the Singapore Strait. The IMB, which draws areas differently, counted 80 incidents in the "Singapore Straits" in 2025, against ReCAAP's 107 (ICC-IMB, 2026, A2). For 2008 the index uses about 8 incidents in both straits (RSIS, n.d., B2); its low case uses Malacca's 2 attacks.

The type of crime also matters. In 2025 no Asian incident reached CAT 1, the most serious level, and 53% were CAT 4 petty theft (ReCAAP, Jan 2026, A1). These shares cover all of Asia, and most cases were night thefts in which often nothing was taken (PortNews, 2026, C2).

Insurance offers a second check. The 0.4% war-risk premium of 2005 (Maritime Executive, 2005, C2) implied at most a 1-in-250 chance of losing a ship per voyage. In 2000, 75 attacks among 55,957 transits gave an observed rate of 0.13%, or 1 in 746 (IALA, n.d., B2, graded here).

So the premium tracked likelihood but leaned high, at about three times the attack rate. By 2005, when it applied, attacks had already fallen to 12. The 2025 rate was roughly similar to 2000, at 0.11% of transits (derived), yet the strait stayed unlisted (LMA JWC, 2026, A1).

On the project's scale, likelihood (L) moved from 3.70 at the peak to 1.83 in 2008, 2.77 in 2025 and 2.31 in 2026.

### Severity

Severity (S) was minimal in every period: S = 1.00 at the peak, in 2008, 2025 and 2026. Traffic grew from 43,965 transits in 1999 to 63,636 in 2004 (IALA, n.d., B2, graded here). A record 102,525 ships passed in 2025, on a different count that also shows growth (Seatrade, 2026, C2).

ReCAAP said the 2025 rise "does not indicate a corresponding increase in threat to maritime trade" (Free Malaysia Today, 2026, C1). The only measurable cost came from insurers, after Lloyd's Joint War Committee (JWC) listed the strait on 20 June 2005 (RSIS, 2005, B2).

Premiums reached nearly 0.4% of hull value, about US$150,000 per port call (Maritime Executive, 2005, C2). The better-graded RSIS put the cost far lower, at about US$5,000 per trip (RSIS, 2006, B2). The listing ended on 7 August 2006 (London P&I Club circular via inforMARE, 2006, C1), and ships never abandoned the route.

Crews still suffered harm. In 2025 the IMB recorded 14 crew taken hostage in the Singapore Straits, and guns in 27 incidents worldwide (ICC-IMB, 2026, A2). Robbers increasingly carried metal rods or improvised weapons (RSIS, 2025, B2).

The equation gives the floor value because all three measured indicators (traffic lost, months of disruption and oil-price rise) were zero. Freight had no data, so S = 1 + 4 × 0 = 1.00. The index therefore measures disruption to trade and cannot register harm to crews.

Because R = √(L × S), risk equals √L throughout, so cooperation could lower risk only by lowering likelihood.

### The five cooperation factors

Each factor is scored 0–4, so the cooperation index C runs from 0 to 20.

| Factor | Peak (2000–05): score | 2008: score | 2025–26: score | Effect on likelihood | Effect on severity |
| --- | --- | --- | --- | --- | --- |
| Formal frameworks | 1 in 2000, 2 by 2005: no regional pact, then MALSINDO; ReCAAP agreed in November 2004 (ReCAAP Agreement, 2004, A1) | 3: ReCAAP in force from 4 September 2006 (ReCAAP Agreement, 2004, A1) | 3: ReCAAP and the Malacca Straits Patrol (MSP) continue, but Malaysia and Indonesia stay outside ReCAAP (Poonnawatt, 2023, A2) | Small: arrived after most of the fall | None: S stays at 1.00 |
| Joint operations | 1, then 2: MALSINDO (Malaysia–Singapore–Indonesia) sea patrols from 20 July 2004 (YaleGlobal, 2004, B1). Eyes in the Sky air patrols from 13 September 2005 (MINDEF, 2005, B1) | 3: sea and air patrols, seven flights a week (Business Insurance, 2006, C1); Thailand full member from 18 September 2008 (MINDEF, 2008, B1) | 3: MSP plus Indonesia–Malaysia patrols (Koran Jakarta, 2025, C2) | Moderate: helped end the war-risk listing, unproven on attacks | None |
| Information sharing | 2, then 2: only the industry-run IMB reporting centre (ICC-IMB, 2001, A1) | 3: ReCAAP centre opened in Singapore on 29 November 2006 (Today, 2006, C1) | 4: real-time alerts, Information Fusion Centre, ships' CCTV (MINDEF, 2025, B2) | Weak at first; key enabler of the 2025 arrests | None |
| Response speed | 1, then 1: MALSINDO came about four years after the 2000 surge | 2: hotline (YaleGlobal, 2004, B1) and ReCAAP centre in place, but untested | 2: alert on 3 February 2025 (ReCAAP, 2025, A1), arrests only in July | Slow: both surges ran for months or years | None |
| Enforcement of laws | 1, then 2: rare; Indonesian operations in 2005 (Gulf News, 2006, C3) | 2: at most 1.47% of piracies worldwide prosecuted internationally (Kontorovich and Art, 2010, A2) | 3: 11 arrests in the Riau Islands (Maritime Executive, 2025, C1) | Largest in 2025–26, but by national police | None |
| Total C (0–20) | 6, then 9 | 13 | 15 | C rose in both intervals, but L fell, then rose | None |

Formal frameworks: the US plan for a Regional Maritime Security Initiative (RMSI) failed over sovereignty, but ReCAAP's looser model lasted (Poonnawatt, 2023, A2). In 2004 Malaysia insisted that security "should not be an excuse to compromise on sovereignty" (The Straits Times, 2004, C1). Frameworks lasted because they respected sovereignty, but they arrived too late to explain the fall and bound no state to act.

Joint operations: Eyes in the Sky flew about 8 sorties a week against about 70 needed, in daytime only (Marine Policy, 2026, A3). Yet the JWC refused to delist in January 2006 (Business Times, 2006, C2), relenting only after reviewing the patrols (Business Insurance, 2006, C1). These operations were a real but modest cause: they changed how insurers saw the strait more than how often pirates struck.

Information sharing: in 2025 Singapore cited the MSP and its own Information Fusion Centre, linked to 58 countries (MINDEF, 2025, B2). The 2025 arrests used ships' CCTV footage (ReCAAP, Jan 2026, A1) and tips from the public and the IMB (Maritime Executive, 2025, C1). Sharing did little at the peak but became cooperation's strongest tool in 2025, working through national police rather than replacing them.

Response speed: sovereignty and border disputes (Johnson and Valencia, 2005, A2) delayed the first patrols until about four years after the 2000 surge. A rise in robberies was reported in 2023 (Lowy Interpreter, 2023, B2), but arrests came only in July 2025 (Maritime Executive, 2025, C1). Slow response is cooperation's clearest weakness: both surges ran for months or years before decisive action.

Enforcement: on 9 July 2025, Indonesian police in the Riau Islands arrested 8 robbers at sea, 11 in all (Maritime Executive, 2025, C1). Singapore Strait robberies then fell from 14 in July to 2 in August and 1 in September (MINDEF, 2025, B2). Enforcement was decisive in 2025–26, but it was national police work, which counts as cooperation only under a broad definition.

### Other explanations

The steepest fall came before any joint patrol existed. Attacks fell 79%, from 75 in 2000 (ICC-IMB, 2001, A1) to 16 in 2002 (Al Jazeera, 2003, B2, graded here). MALSINDO began only in July 2004 (YaleGlobal, 2004, B1), so other forces started the decline.

Each cause has a process-tracing share, scored on change, timing, mechanism and counterfactual; shares are for peak to 2008 unless stated.

An IMB official said the 2004 tsunami "seems to have really succeeded where the joint patrols could not" (Al Jazeera, 2005, B2). The pause was brief: the IMB still counted 8 attacks in the first half of 2005 (ICC-IMB half-year release, 2006, A1). Process tracing gives the tsunami 15.8%, tied with the patrols for the largest share.

The Aceh peace deal followed on 15 August 2005 (Peace Accords Matrix, n.d., B1, graded here). One report links it to the 2005 fall (Gulf News, 2006, C3), but the deal came after most of the drop. It probably explains why attacks stayed low rather than why they fell, and scores 13.2%.

Indonesian poverty fell from about 23–24% in 1999 to about 13% in 2010 (SMERU, n.d., B2, graded here). Yet Indonesian incidents rose from 15 in 2009 to 106 in 2013 while the economy grew (CIMSEC, 2014, C2). The economy remains a plausible background cause, scoring 13.2%, but that counter-example weakens it.

The ISPS Code brought new ship-security rules from 1 July 2004, but the IMB saw "no dramatic decline in attacks" afterwards (ICC-IMB, 2004–05, A1). Its share is 7.9%. Industry precautions score 18.2% for 2025–26, and ReCAAP's director credited them alongside enforcement (Splash247, 2026, C1).

National enforcement fits both changes: the IMB linked the 2005 drop to Indonesian patrols in Indonesian waters (Gulf News, 2006, C3). It scores 13.2% for peak to 2008 and 36.4% for 2025 to 2026, the largest single share there. Even so, two or three gangs were still active in January 2026 (Seatrade, Jan 2026, C2, graded here).

Connected crises score 0% for peak to 2008 and only 4.5% for 2025 to 2026. One report links part of the 2025 rise to Red Sea diversions (Malay Mail, 2025, C1), but no other source confirms it.

The 2026 Hormuz closure cut Malacca's oil flow from 23.2 to 16.6 million barrels a day (EIA, 2026, A1; Kompas, 2026, C2). The index leaves this out of severity, because it was imported from another chokepoint and crime had already fallen.

Market pressure from the listing scores 13.2%: Eyes in the Sky began about three months after it (MINDEF, 2005, B1). The listing also feeds the likelihood score, so it must not be counted twice.

### What the numbers show

The main comparison is the peak against today: R fell by 0.26 (−14%) to 2025 and 0.40 (−21%) to 2026. All of it came through likelihood (ΔL −0.93 and −1.39; ΔS 0), and the ranges do not overlap, so the fall is robust.

The area caveat matters, because the peak's 75 attacks cover the Malacca Strait only (ICC-IMB, 2001, A1). The 108 of 2025 cover both straits, and 107 were in the Singapore Strait (ReCAAP, Jan 2026, A1). Counting only the Malacca Strait, with 1 incident, gives R = 1.12 in 2025 and 2026, a fall of 0.80 from the peak.

Peak to 2008 is the window that tests the joint patrols: R fell by a robust 0.57 (−30%), all through likelihood (ΔL −1.87).

A generous check assumes every point of cooperation lowers risk. Its adjusted score falls from 2.41 to 1.77 (2025) and 1.66 (2026), against 2.19 and 2.06 with peak-level cooperation. That credits cooperation with −0.42 and −0.40, or 65% and 53% of the adjusted fall; for peak to 2008, −0.27, or 35%.

These shares are inflated, because the check builds its cooperation term from the cooperation score itself. Process tracing, which gives multilateral cooperation 15.8–23.7% of the peak-to-2008 fall, is the real test of cause.

The latest change, 2025 to 2026, is a fall of only 0.15, and the ranges overlap, so it is not robust. Cooperation did not change, with C at 15 in both years, so the fall points to national enforcement.

### Judgement

Multilateral cooperation was a major reason among several, not the main reason, for lower risk in the Strait of Malacca. The steepest fall came before any joint patrol, and the 2025 surge happened when cooperation was at its strongest (C = 15). Process tracing gives the patrols 15.8%, tied with the tsunami; adding ReCAAP makes 23.7%, exactly 1.5 times the tsunami's share.

That meets the project's "main reason" rule only on a knife-edge: lowering one score by a point breaks it. Cooperation's clearest effects were on insurers, who delisted the strait after reviewing the patrols, and on the information behind the 2025 arrests. It did nothing for severity, because severity never rose above its floor.

The strongest counter-argument is definitional: MALSINDO was designed so that each navy patrols its own waters (YaleGlobal, 2004, B1). The coastal states would accept nothing else: Indonesia called their own frameworks the only way to manage the straits (Oegroseno, 2008, B2). If those national patrols count as cooperation, the share rises to 36.8%, 2.3 times the next cause, making it the main reason.

But the 2000–02 fall happened with no coordination, and the 2025 surge grew inside the same system. Cooperation is therefore best seen as a necessary condition for keeping risk low: it locked in a fall that other forces started.

Confidence is moderate. The direction of change is secure, because the IMB series is A1 data and the fall from the peak survives every range tested.

The size of cooperation's role is less certain: the IMB and ReCAAP count different areas, and the premium rests on one C2 source. Many web figures were also checked only against search results, and the causal shares are judgements that shift with how causes are grouped.

## Why cooperation worked in some cases and not others

The more the disrupter is a state with political aims, the less cooperation explains. Only at Malacca does cooperation match the largest rival cause, and nowhere does the amount of cooperation predict the level of risk.

&#91;embedded content: Process-tracing shares from the three attribution analyses (research/attribution/A1–A3); Red Sea type of threat ties with connected crises at 17.0%\]

Four differences explain the pattern.

- **Who controls the water.** At Malacca the coastal states were willing partners and policed their own waters; Indonesia and Malaysia rejected outside patrols in 2004 but ran their own. At Hormuz and in 1967 the disrupter was itself a coastal state, and in the Red Sea littoral states such as Egypt, Eritrea and Djibouti stayed out of the coalitions.
- **What the threat wants.** Pirates want profit, so patrols, arrests and higher risk deter them. Iran in 2026 and the Houthis wanted political leverage, so the costs that cooperation imposes did not change their decisions.
- **What cooperation can reach.** Information sharing and insurance support cut the cost of each incident in every case. Only enforcement on land, as in the Riau Islands arrests of July 2025 (Maritime Executive, 2025, C1), removed the threat at its source.
- **Whether ships have another way round.** Severity depends on alternatives as much as on defence. The Cape of Good Hope kept trade moving in both Suez crises, while bypass pipelines can carry only about 9 mb/d of the roughly 20 mb/d that normally passes Hormuz (Al Jazeera, 27 March 2026, B2). That gap is why the 2026 closure did so much more harm than the Houthi attacks.

### Cooperation compared factor by factor

| Factor (each scored 0–4) | Tanker War, 1984–88 | Hormuz, 2026 | Suez, 1967–75 | Red Sea, 2023–26 | Malacca peak, 2000 | Malacca, 2025–26 |
| --- | --- | --- | --- | --- | --- | --- |
| Formal frameworks | 2 | 3 | 1 | 2 | 1 | 3 |
| Joint operations | 2 | 2 | 2 | 3 | 1 | 3 |
| Information sharing | 1 | 3 | 1 | 3 | 2 | 4 |
| Response speed | 2 | 3 | 1 | 3 | 1 | 2 |
| Enforcement | 2 | 1 | 0 | 2 | 1 | 3 |
| Total, C (out of 20) | 9 | 12 | 5 | 13 | 6 | 15 |

The scores are the project's own, with the reasoning and evidence in the attribution files (research/attribution/A1–A3) and in each case section above.

- **Information sharing grew most.** It rose by 2 points at every strait, from ad hoc warnings to shared threat ratings and alert centres (JMIC, ReCAAP and the EU's Aspides alerts). It is the one factor that improved everywhere, which fits its role in cutting harm per incident in every case.
- **Joint operations and enforcement did not grow at Hormuz.** Joint operations stayed at 2 and enforcement fell from 2 to 1. In 1987 Operation Earnest Will was escorting tankers about seven months after Kuwait asked for help. In 2026 the UK–France mission still had no ships in the strait on 6 October (The National, 6 October 2026, C2), and US-led escorts managed only about 30 transits a day, 22% of normal (CENTCOM via gCaptain, 15 October 2026, C2).
- **Enforcement mattered most when it was national.** The factor most closely tied to falling likelihood was enforcement, but the decisive cases, Indonesia's operations in 2005 and its arrests in 2025, were national police and navy work supported by shared information.

### Where cooperation acted

| Type of cooperation | Example | What it changed | Evidence of effect |
| --- | --- | --- | --- |
| Emergency oil stocks | IEA release of 400 million barrels, March 2026 (IEA, 11 March 2026, A1) | Severity: prices | Brent still closed above $100 the day after the announcement (CNBC, 12 March 2026, B1); the release cushioned prices but did not prevent the shock |
| Escorts and air defence | Prosperity Guardian and Aspides, 2023–26 | Severity: harm per attack | About four ships sank out of about 100 attacked (AP via CP24, 2025, B1); escorts "prevented the loss of civilian lives" but did not deter attacks (Forces News citing IISS, 2024–25, C2) |
| Joint patrols | MALSINDO from 2004 and Eyes in the Sky from 2005 | Likelihood, through insurers | The Joint War Committee delisted the strait only after reviewing the patrols (Business Insurance, 2006, C1) |
| Information sharing | ReCAAP alerts and ships' CCTV, 2025 | Likelihood, through national arrests | Singapore Strait robberies fell from 14 in July 2025 to 1 in September after the arrests (MINDEF, 2025, B2) |
| Military strikes | US–UK strikes on about 60 Houthi targets, January 2024 (CSIS, 2024, B2) | Intended to cut likelihood | War-risk premiums tripled within a week (Lloyd's List, January 2024, B2), and attacks continued |
| Legal frameworks | UN resolutions 242 (1967), 598 (1987) and 2722 (2024) | Neither directly | They gave legitimacy, but none was enforced at sea (UN Security Council, A1) |

Cooperation worked mainly on severity: it cushioned prices, protected crews and kept insurance available. Where it lowered likelihood, it did so indirectly, through insurers at Malacca in 2006 and through national police in 2025. It never deterred a state or an armed group with political aims.

### Does more cooperation mean less risk?

Cooperation rose in all three cases, by 3, 8 and 9 points, but risk rose at Hormuz and fell at the other two. The largest rise in cooperation, at Malacca (+9), came with the smallest fall in risk (−0.26 to 2025), partly because Malacca risk started low. Within Malacca, cooperation was at its strongest in 2025 (C = 15), the year with the most incidents in the Straits of Malacca and Singapore since 2007 (ReCAAP ISC Annual Report 2025, A1). The amount of cooperation therefore does not predict the level of risk, whereas the type of threat does.

## Counter-arguments

Seven counter-arguments deserve weight. One could change the Malacca verdict and another weakens the Malacca measurement; the others refine the judgement without reversing it.

| Counter-argument | Strongest evidence | How far it changes the judgement |
| --- | --- | --- |
| **"Multilateral" is defined too narrowly.** MALSINDO was designed for each navy to patrol its own waters, so national enforcement is part of the cooperative system. | The Malacca Strait Patrols were launched on 20 July 2004 (YaleGlobal, 2004, B1; MINDEF, B1). The Indonesian police arrests of 9 July 2025 (Maritime Executive, 2025, C1) followed ReCAAP information sharing. | **Large for Malacca.** Counting national patrols as cooperation lifts its share from about 24% to 37%, 2.3 times the next cause, so it would become the main reason. It does not change Hormuz or the Red Sea. |
| **The measures miss lives and ships saved.** The equation counts trade disrupted, not harm prevented. | Of about 100 ships attacked in the Red Sea, about four sank (AP via CP24, 2025, B1). Navies shot down large numbers of missiles and drones. | **Moderate.** Cooperation reduced the harm per attack, which supports "severity at the margin". It did not bring traffic back: Suez transits were still about 60% down 100 days after the attacks stopped (Container News citing BIMCO, 2026, C2). |
| **Cooperation prevented worse outcomes that the data cannot show.** Without the IEA release and the escorts, prices and losses would have been higher. | The IEA's 400-million-barrel release came within 11 days (IEA, 11 March 2026, A1). On the generous check, Hormuz risk would have been 3.94 instead of 3.68 without the extra cooperation. | **Moderate.** The point is fair, since no equation can measure prevented harm. But even the generous check cannot stop the Hormuz rise, and Brent still closed above $100 the day after the release (CNBC, 12 March 2026, B1). |
| **Cooperation ended the 1967 closure.** The 1974 clearance by US, British and French units physically reopened the canal. | Clearance ran from 11 April to 15 December 1974 (CTF-65 Final Report, B1), and the canal reopened on 5 June 1975 (Boyd, USNI *Proceedings*, 1976, B2). | **Small.** Clearance began only after Egypt's political decision following the 1973 war, so cooperation followed politics rather than causing the reopening. |
| **The equation is built to find that cooperation does little, because cooperation is left out of it.** | R uses only measured likelihood and severity, while the earlier CCRI multiplied in a cooperation term. | **Small.** Leaving cooperation out is what allows the equation to test it. When cooperation is put back in on the most generous terms, the Hormuz rise remains, and process tracing still ranks cooperation below other causes at Hormuz and Suez. |
| **Malacca risk did not really fall: the 2025 surge matched the peak.** | There were 108 incidents in the Straits of Malacca and Singapore in 2025 (ReCAAP ISC Annual Report 2025, A1), against 75 in the Malacca Strait in 2000 (ICC-IMB, 2001, A1). Without the insurance indicator, measured risk rises slightly. | **Moderate for Malacca.** It weakens the claim that risk fell from the peak to 2025. But 107 of the 108 incidents were in the Singapore Strait, the Malacca Strait itself had 1, and most incidents across Asia were petty theft. |
| **Cooperation moves threats rather than removing them.** | Off Somalia, naval patrols pushed attacks out of the guarded corridor and into the open ocean (Shortland and Vothknecht, 2011, A2). | **Strengthens the judgement.** It shows why cooperation lowers local likelihood without removing the threat, which fits the 2025 surge in the Singapore Strait. |

Two further limits apply to all three cases. First, cooperation and threat interact: patrols and strikes change what attackers do, so effects cannot be read off one period (National Research Council, 2010, A1). Second, both 2026 crises are still going on, so their severity may rise further.

## Evaluation of the evidence and the method

The overall pattern is robust, but individual figures are less certain than their two decimal places suggest. The main weakness lies in how the sources were reached, not in who produced them.

### Strengths

- **The same tests in every case.** Each case is judged on the same questions, with the same equation and the same causal tests, so the three straits can be compared fairly.
- **Two independent strands that agree.** The equation measures risk without assuming anything about cooperation, while process tracing tests causes without using the equation. Both give cooperation its smallest effect at Hormuz.
- **Strong producers.** Most figures the judgements rest on come from A- or B-graded producers: UN agencies and the IMF, the IEA, official price series (FRED and the EIA), the two piracy watchdogs (ICC-IMB and ReCAAP), Lloyd's List, Reuters and AP.
- **Checks that cross-confirm.** Insurance prices and observed attack rates are independent measures of likelihood, and they agree within a factor of 3 in every case. The direction of every main change also survives 19 versions of the equation and the full low–high range of the inputs, with the single Malacca exception explained above.

### Weaknesses of the evidence

1. **Snippets, not full texts.** The research environment blocked direct access to most web pages, so most figures were confirmed from search-result text rather than the full document. For this reason, credibility is graded no better than 2 unless independent sources agree. Each figure should be checked at its source before it is quoted.
2. **Thinner history.** There is no daily ship-tracking data before 2019, no war-risk premium for 1967 and no freight index for the Tanker War. The historical periods therefore rest on fewer indicators and lean more on newspapers of the time, such as Time, UPI and AP.
3. **Producers with an interest.** Egypt's canal figures come from the Suez Canal Authority via state-linked Egyptian media (Ahram Online, D2). The war-risk areas are set by an insurance market that profits from wide listings. Navies and governments report their own successes, such as escort numbers.
4. **Counts that conflict.** Sources disagree on the Malacca attacks in 2004 (37 or 38), the deaths on the Eternity C (3 or 4), the end of the 1974 canal clearance (15 or 20 December) and the dates of the Hormuz re-closures in 2026.
5. **Different definitions.** The IMB and ReCAAP draw the Singapore Strait differently, and some sources count attempted attacks while others count only actual ones. This is why the Malacca comparison is shown both ways.
6. **Missing outlets.** The NYT, the Guardian, the BBC, the FT, El País and The Economist could not be searched, so other papers from the same countries stand in for them.

### Weaknesses of the method

1. **The equation.** Its goalposts and equal weights are choices, likelihood and severity overlap through insurance prices, and every incident counts the same. Most inputs are peak values, so R describes each crisis at its worst, not on average. It cannot see harm that cooperation prevented.
2. **The cooperation score.** The five factors are each scored 0–4 by judgement. The scores are reasoned and recorded in the attribution files, but another researcher could reasonably score a factor one point higher or lower.
3. **Process tracing.** The four tests are also scored by judgement, and the shares depend on which causes are listed, since a cause left off the list cannot be credited. The rule that cooperation is the main reason only if its share is the largest and at least 1.5 times the next is a convention, not a law.
4. **Cooperation follows risk.** Navies deploy when attacks rise, so cooperation and risk move together even when one does not cause the other. Attackers also adapt: patrols can push attacks elsewhere rather than end them.
5. **Three cases.** Three straits cannot prove a general law. The explanation by type of threat fits all three, but it would need testing on other cases, such as Somali piracy in the Gulf of Aden.

### What would change the verdict

- **A wider definition of cooperation.** If each navy patrolling its own waters within MALSINDO counts as cooperation, cooperation becomes the main reason at Malacca: its share rises to 36.8%, 2.3 times the next cause.
- **The Malacca measurement.** Without the insurance indicator, measured risk rises slightly from the peak to 2025 (2.07 to 2.13, both just inside Moderate). Counting the Malacca Strait alone makes the fall three times larger (−0.80). The finding that Malacca risk stayed low holds either way, but the size and even the direction of the change from the peak to 2025 depend on the measure.
- **The end of the 2026 crises.** If a multilateral agreement reopens Hormuz or ends the Red Sea attacks, cooperation's share in those cases would have to be scored again.
- **Full-text checks.** Opening the A- and B-graded sources could move individual figures. Given the sensitivity tests, the directions of change would hold unless a figure moved well outside its low–high range.

## Conclusion

Multilateral cooperation reduces the likelihood and severity of chokepoint disruption only to a limited and conditional extent. Its effect is real but secondary, and it depends on the type of threat.

**Risk did not follow cooperation.** Measured from data alone, risk rose at Hormuz (3.47 to 4.37) and fell at Suez and the Red Sea (4.47 to 3.39) and at Malacca (1.92 to 1.66 in 2025 and 1.52 in 2026), even though cooperation increased in all three cases. Even on the generous assumption that every point of cooperation lowers risk, the extra cooperation could not have stopped the Hormuz rise. Process tracing, which tests causes directly, gives cooperation between 5.7% and 23.7% of each change.

**On likelihood, cooperation rarely decides the outcome.** At Hormuz likelihood was near its maximum in both periods: 178–181 ships were hit in 1987 (Lloyd's Shipping Intelligence via UPI, 1987, B3; USNI *Proceedings*, 1988, B2), and Iran chose to close the strait in 2026. In the Red Sea, attacks rose after the coalition formed and fell after the bilateral US–Houthi truce of 2025. Only at Malacca did likelihood fall alongside cooperation, and even there the 2004 tsunami, the Aceh peace deal and national enforcement share the credit.

**On severity, cooperation matters at the margin.** The IEA stock release, the Red Sea escorts, information sharing through JMIC and ReCAAP, and coordinated insurance backing all cushioned the damage. The clearest single case of cooperation lowering a measured cost came in August 2006, when the Lloyd's Joint War Committee lifted the Malacca war-risk listing after reviewing the joint patrols (London P&I Club circular via inforMARE, 2006, C1; Business Insurance, 2006, C1).

**The decisive variable is the type of threat.** Cooperation is strongest against diffuse criminal threats in the waters of willing coastal states, where it supports national police. It is weakest against a state, or an armed group backed by one, that has political reasons to disrupt trade and accepts the costs. Two further conditions decide how much harm follows: how much trade depends on the route, and whether ships have another way round.

**Confidence: moderate.** The pattern holds across three cases and eight periods, the two methods agree, and the direction of change survives 19 versions of the equation. Two findings are fragile. Counting national patrols as cooperation makes it the main reason at Malacca, and the fall in Malacca risk from the peak to 2025 depends on the insurance indicator and on which waters are counted. The main weaknesses are thin historical data, figures taken from search results rather than full texts, and two crises that have not yet ended.

## Sources for the data cited

Every source cited above, with its full reference, a link and its Admiralty Code grade (letter for the producer, number for the content). Sources are grouped by the case they concern; those used in the cross-case sections appear under the case they describe. "Graded here" marks a grade given in this analysis with the project rubric. Figures marked "derived", and all risk-index, cooperation and process-tracing values, are the project's own calculations (research/quantitative/qcri.py and research/attribution/A1–A3), so they carry no grade.

### Method

- Cox, L. A. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. [link](https://doi.org/10.1111/j.1539-6924.2008.01030.x) — Grade A2 (graded here)
- George, A. L. and Bennett, A. (2005). *Case Studies and Theory Development in the Social Sciences*. MIT Press. [link](https://scholar.google.com/scholar?q=George+Bennett+2005+Case+Studies+and+Theory+Development+in+the+Social+Sciences) — Grade A2 (graded here)
- ISO (2018). *ISO 31000:2018 Risk management: Guidelines*. International Organization for Standardization. [link](https://www.iso.org/standard/65694.html) — Grade A2 (graded here)
- Marin-Ferrer, M., Vernaccini, L. and Poljansek, K. (2017). *Index for Risk Management INFORM: Concept and Methodology, Version 2017*. European Commission JRC. [link](https://doi.org/10.2760/094023) — Grade A2 (graded here)
- National Research Council (2010). *Review of the Department of Homeland Security's Approach to Risk Analysis*. National Academies Press. [link](https://doi.org/10.17226/12972) — Grade A1
- OECD/JRC (2008). *Handbook on Constructing Composite Indicators: Methodology and User Guide*. OECD Publishing. [link](https://www.oecd.org/sdd/42495745.pdf) — Grade A2 (graded here)
- Saisana, M., Saltelli, A. and Tarantola, S. (2005). Uncertainty and sensitivity analysis techniques as tools for the quality assessment of composite indicators. *Journal of the Royal Statistical Society: Series A*, 168(2), 307–323. [link](https://doi.org/10.1111/j.1467-985X.2005.00350.x) — Grade A2 (graded here)
- Shortland, A. and Vothknecht, M. (2011). Combating "maritime terrorism" off the coast of Somalia. *European Journal of Political Economy*, 27(S1). [link](https://doi.org/10.1016/j.ejpoleco.2011.03.004) — Grade A2

### Strait of Hormuz

- AFP via Ahram Online (2026). Report on Hormuz attacks in 1–15 October and seafarer deaths (title not recorded). Ahram Online. [link](https://english.ahram.org.eg/News/580023.aspx) — Grade C1 (graded here)
- Al Jazeera (2026). Iran shuts Hormuz strait: But wasn't it already closed? Al Jazeera. [link](https://www.aljazeera.com/news/2026/6/11/iran-shuts-hormuz-strait-but-wasnt-it-already-closed) — Grade C2
- Al Jazeera (2026). Saudi, UAE, Iraq: Can three pipelines help oil escape Strait of Hormuz? Al Jazeera. [link](https://www.aljazeera.com/economy/2026/3/27/saudi-uae-iraq-can-three-pipelines-help-oil-escape-strait-of-hormuz) — Grade B2
- Arab News (2026). Report quoting CENTCOM on the attack on the El Gaia (title not recorded). Arab News. [link](https://www.arabnews.com/node/2651361) — Grade C3 (graded here)
- Atlantic Council (2026). The crisis in the Strait of Hormuz is a heavy blow to the deteriorating maritime order. Atlantic Council issue brief. [link](https://www.atlanticcouncil.org/in-depth-research-reports/issue-brief/the-crisis-in-the-strait-of-hormuz-is-a-heavy-blow-to-the-deteriorating-maritime-order/) — Grade B2
- Bordoff, J. and O'Sullivan, M.L. (2026). The Long Shadow of the Iran Shock. Foreign Affairs, 14 August. [link](https://www.foreignaffairs.com/iran/long-shadow-iran-shock) — Grade B2
- Brookings Institution (2026). From chokepoint to crisis: the Strait of Hormuz and global oil markets. Brookings. [link](https://www.brookings.edu/articles/from-chokepoint-to-crisis-the-strait-of-hormuz-and-global-oil-markets/) — Grade B2
- Chatham House (2026). A naval coalition in the Strait of Hormuz should learn these lessons. Chatham House Expert Comment, 1 May. [link](https://www.chathamhouse.org/2026/05/naval-coalition-strait-hormuz-should-learn-these-lessons) — Grade B2
- CNBC (2026). Brent oil closes at $100 after Iran's new supreme leader says Strait of Hormuz must remain closed. CNBC, 12 March. [link](https://www.cnbc.com/2026/03/12/oil-prices-jump-iea-record-reserve-release-markets-doubt-relief.html) — Grade B1
- CNBC (2026). Container ship sinks in Strait of Hormuz as Iran steps up attacks. CNBC, 14 October. [link](https://www.cnbc.com/2026/10/14/container-ship-sinks-strait-hormuz-as-iran-war-attacks.html) — Grade B1
- Congressional Research Service (2026). Report R45281 (Iran conflict background). US Congress. [link](https://www.congress.gov/crs-product/R45281) — Grade B2
- Cyprus Shipping News (2026). VLCCs climbing the record charts (Baltic Exchange weekly data, 15 October). Cyprus Shipping News. [link](https://cyprusshippingnews.com/2026/10/15/vlccs-climbing-the-record-charts/) — Grade C2 (graded here)
- FRED / US Energy Information Administration (1987). Brent crude oil spot price, monthly (MCOILBRENTEU). Federal Reserve Bank of St Louis. [link](https://fred.stlouisfed.org/data/MCOILBRENTEU) — Grade A1
- FRED / US Energy Information Administration (2026). Brent crude oil spot price, weekly (27 February 2026). Federal Reserve Bank of St Louis. [link](https://fred.stlouisfed.org/graph/?g=4Nmx) — Grade A1
- Foreign Policy (2026). Iran Puts "Toll Booth" in Strait of Hormuz, Charging Fees for Ships' Safe Passage. Foreign Policy, 26 March. [link](https://foreignpolicy.com/2026/03/26/iran-strait-hormuz-war-tolls-shipping/) — Grade B2
- gCaptain (2026). By the Numbers: U.S. Claims Control of Hormuz as Ship Attacks Hit New High. gCaptain, 15 October. [link](https://gcaptain.com/by-the-numbers-u-s-claims-control-of-hormuz-as-ship-attacks-hit-new-high/) — Grade C2
- gCaptain / Bloomberg (2026). U.S. counts far more Hormuz ship transits than commercial tracking data shows. gCaptain, 5 June. [link](https://gcaptain.com/u-s-counts-far-more-hormuz-ship-transits-than-commercial-tracking-data-shows/) — Grade B2
- GlobalMilitary.net (2026). Strait of Hormuz transits 2026 (write-up of IMF PortWatch data). GlobalMilitary.net. [link](https://www.globalmilitary.net/conflicts/strait-of-hormuz/transits/2026/) — Grade D3 (graded here)
- Governments of Greece and the UAE (2026). Statements on the vetoed Hormuz draft resolution (Greek explanation of vote, 7 April). Greek Mission to the UN. [link](https://greeceforunsc.mfa.gr/wp-content/uploads/2026/04/GRC_Res.-on-the-Strait-of-Hormuz-EoV-April-7th.pdf) — Grade B1
- Insurance Journal (2026). US doubles Hormuz reinsurance guarantees to $40 billion with new partners. Insurance Journal, 6 April. [link](https://www.insurancejournal.com/news/international/2026/04/06/864586.htm) — Grade C2
- International Energy Agency (2026). IEA Member countries to carry out largest ever oil stock release amid market disruptions from Middle East conflict. IEA press release, 11 March. [link](https://www.iea.org/news/iea-member-countries-to-carry-out-largest-ever-oil-stock-release-amid-market-disruptions-from-middle-east-conflict/) — Grade A1
- International Energy Agency (2026). Oil Market Report, May 2026. IEA. [link](https://www.iea.org/reports/oil-market-report-may-2026) — Grade A2
- International Maritime Organization (n.d.). Middle East / Strait of Hormuz hot-topic page. IMO. [link](https://www.imo.org/en/mediacentre/hottopics/pages/middle-east-strait-of-hormuz.aspx) — Grade A2
- Iran International (2026). Hormuz traffic falls to lowest in more than two months. Iran International, 8 October. [link](https://www.iranintl.com/en/202610085164) — Grade C1
- Joint Maritime Information Center (2025–26). JMIC Advisory Notes and threat levels. JMIC / UKMTO via Seatrade Maritime. [link](https://www.seatrade-maritime.com/security/jmic-raises-strait-of-hormuz-threat-level-to-severe) — Grade B2
- Lloyd's List (2026). Crude tanker rates in unchartered territory; VLCC index tops $420K. Lloyd's List, c. 2 March. [link](https://www.lloydslist.com/LL1156492/Crude-tanker-rates-in-unchartered-territory-VLCC-index-tops-420K) — Grade B1
- Lloyd's List (2026). Gulf war risk premiums topping double-digit millions of dollars per trip. Lloyd's List, c. 11 March. [link](https://www.lloydslist.com/LL1156586/Gulf-war-risk-premiums-topping-double-digit-millions-of-dollars-per-trip) — Grade B2
- Navias, M.S. and Hooton, E.R. (1996). Tanker Wars: The Assault on Merchant Shipping during the Iran–Iraq Conflict, 1980–1988. I.B. Tauris (reviewed in Iranian Studies). [link](https://www.cambridge.org/core/journals/iranian-studies/article/abs/tanker-wars-the-assault-on-merchant-shipping-during-the-iraniraq-conflict-19801988-martin-s-navias-and-e-r-horton-london-and-new-york-ib-tauris-publishers-1996-ix-244-pp-including-appendix-notes-index-of-ships-and-general-index-cloth/555128C86253A41B2A6257F098EC20C2) — Grade A2
- O'Rourke, R. (1988). The Tanker War. US Naval Institute Proceedings 114(5), May. [link](https://www.usni.org/magazines/proceedings/1988/may/tanker-war) — Grade B2
- Raman, S. \[attribution unconfirmed\] (2026). The Toll Booth at the Throat of World Trade. War on the Rocks. [link](https://warontherocks.com/the-toll-booth-at-the-throat-of-world-trade/) — Grade C3
- Riviera Maritime Media (2025). Sanctions squeeze supports spot strength (Clarksons VLCC data, mid-December). Riviera Maritime Media. [link](https://www.rivieramm.com/news-content-hub/sanctions-squeeze-supports-spot-strength-87160) — Grade C2 (graded here)
- Robert S. Strauss Center, University of Texas (n.d.). Strait of Hormuz – Insurance Market. Strauss Center for International Security and Law. [link](https://www.strausscenter.org/?p=1968) — Grade B2
- Robert S. Strauss Center, University of Texas (n.d.). Strait of Hormuz – Tanker War. Strauss Center for International Security and Law. [link](https://www.strausscenter.org/strait-of-hormuz-tanker-war/) — Grade B2
- S&P Global (2026). Marine insurers seek solutions as Gulf shipping threats evolve. S&P Global Commodity Insights, 6 March. [link](https://www.spglobal.com/energy/en/news-research/latest-news/refined-products/030626-marine-insurers-seek-solutions-as-gulf-shipping-threats-evolve) — Grade B2
- S&P Global (2026). Middle East shipping insurance costs rise on Hormuz risks: Marsh. S&P Global Commodity Insights, 22 July. [link](https://www.spglobal.com/energy/en/news-research/latest-news/shipping/072226-middle-east-shipping-insurance-costs-rise-on-hormuz-risks-marsh) — Grade B1
- Saudi Gazette (2026). Saudi Arabia shuts East-West oil pipeline after multiple attacks. Saudi Gazette, c. 13 September. [link](https://saudigazette.com.sa/article/664495/saudi-arabia/saudi-arabia-shuts-east-west-oil-pipeline-after-multiple-attacks) — Grade C1
- Seatrade Maritime (2026). Iran war at six months: 6,000 seafarers still stranded in the Gulf (IMO figures). Seatrade Maritime News. [link](https://www.seatrade-maritime.com/security/iran-war-at-six-months-6-000-seafarers-still-stranded-in-the-gulf) — Grade C2 (graded here)
- Shanghai University of Finance and Economics (2026). Academic Newsletter copy of UNCTAD Hormuz material (page not found). SUFE Academic Newsletter. [link](https://academicnewsletter.sufe.edu.cn/info/462104) — Grade D6
- Talmadge, C. (2008). Closing Time: Assessing the Iranian Threat to the Strait of Hormuz. International Security 33(1), pp. 82–117. [link](https://www.belfercenter.org/publication/closing-time-assessing-iranian-threat-strait-hormuz) — Grade A2
- Tan, F. / Reuters (2026). Shipping slows after Iran says it has again shut the Strait of Hormuz (Kpler data). gCaptain, 22 June. [link](https://gcaptain.com/shipping-slows-after-iran-says-it-has-again-shut-the-strait-of-hormuz/) — Grade B1
- The National (2020). Iraq-Iran war: a legacy of carnage that shaped the Middle East for 40 years. The National (Abu Dhabi). [link](https://www.thenationalnews.com/world/iraq-iran-war-a-legacy-of-carnage-that-shaped-the-middle-east-for-40-years-1.1081287) — Grade C1
- The National (2026). French warships "ready to go now" for Gulf deployment, says admiral. The National, 6 October. [link](https://www.thenationalnews.com/news/europe/2026/10/06/french-warships-ready-to-go-now-for-gulf-deployment-says-admiral/) — Grade C2
- The National (2026). Iran says Strait of Hormuz will not reopen until seven conditions are met. The National, 4 October. [link](https://www.thenationalnews.com/news/gulf/2026/10/04/iran-says-strait-of-hormuz-will-not-reopen-until-its-conditions-are-met/) — Grade C1
- UN Security Council (1987). Resolution 598 (1987). UN Digital Library, 20 July. [link](https://digitallibrary.un.org/record/137345) — Grade A1
- UN Security Council (2026). Resolution 2817. Security Council Report, 11 March. [link](https://www.securitycouncilreport.org/un-documents/document/s-res-2817.php) — Grade A1
- UNCTAD (2026). Strait of Hormuz Disruptions: Growth and Financial Implications (April rapid assessment; transit figures seen only via the SUFE mirror). UN Trade and Development. [link](https://unctad.org/system/files/official-document/osginf2026d2_en.pdf) — Grade A1
- United States Institute of Peace (n.d.). U.S.-Iran Showdown in the Gulf — Déjà vu? The Iran Primer. [link](https://iranprimer.usip.org/node/6146) — Grade B2 (graded here)
- UPI (1984). The Iran-Iraq war in the Persian Gulf has cost marine insurers. UPI Archives, 9 March. [link](https://www.upi.com/Archives/1984/03/09/The-Iran-Iraq-war-in-the-Persian-Gulf-has-cost/3441276045960/) — Grade B2
- UPI (1984). Two cargo ships, one British and one Turkish, attacked. UPI Archives, 7 March. [link](https://www.upi.com/Archives/1984/03/07/Two-cargo-ships-one-British-and-one-Turkish/3365447483600) — Grade B2
- UPI (1984). Attack on Persian Gulf tanker "dangerous escalation". UPI Archives, 15 May. [link](https://www.upi.com/Archives/1984/05/15/Attack-on-Persian-Gulf-tanker-dangerous-escalation/6583453441600/) — Grade B2
- UPI (1987). Kuwaiti tankers reflagged with Stars and Stripes. UPI Archives, 21 July. [link](https://www.upi.com/Archives/1987/07/21/Kuwaiti-tankers-reflagged-with-Stars-and-Stripes/5770553838400/) — Grade B1
- UPI (1987). First Earnest Will convoy reports (US warships escorted two reflagged Kuwaiti tankers). UPI Archives, 22–23 July. [link](https://www.upi.com/Archives/1987/07/23/US-warships-escorted-two-reflagged-Kuwaiti-tankers-up-the/9564554011200/) — Grade B1
- UPI (1987). The supertanker Bridgeton hit an underwater mine Friday morning. UPI Archives, 24 July. [link](https://www.upi.com/Archives/1987/07/24/The-supertanker-Bridgeton-hit-an-underwater-mine-Friday-morning/4397554097600/) — Grade B1
- UPI (1987). Britain, France sending mine sweepers to Persian, Oman gulfs. UPI Archives, 11 August. [link](https://www.upi.com/Archives/1987/08/11/Britain-France-sending-mine-sweepers-to-Persian-Oman-gulfs/5251555652800/) — Grade B1
- UPI (1987). A missile believed to be an Iranian-fired Silkworm hit the Sea Isle City. UPI Archives, 16 October. [link](https://www.upi.com/Archives/1987/10/16/A-missile-believed-to-be-an-Iranian-fired-Silkworm-slammed/3846561355200/) — Grade B1
- UPI (1987). Tanker sinks in Persian Gulf (Lloyd's counts of ships attacked). UPI Archives, 10 December. [link](https://www.upi.com/Archives/1987/12/10/Tanker-sinks-in-Persian-Gulf/8340566110800/) — Grade B3
- UPI (1988). U.S. forces destroyed two Iranian oil platforms. UPI Archives, 18 April. [link](https://www.upi.com/Archives/1988/04/18/US-forces-destroyed-two-Iranian-oil-platforms-in-the/6703577339200/) — Grade B2
- UPI (1988). Iraqi jets attacked four tankers anchored at an Iranian terminal. UPI Archives, 14 May. [link](https://www.upi.com/Archives/1988/05/14/Iraqi-jets-attacked-four-tankers-anchored-at-an-Iranian/9675579585600/) — Grade B2
- UPI (1988). President Reagan said downing of Iranian airliner was "understandable accident". UPI Archives, 4 July. [link](https://www.upi.com/Archives/1988/07/04/President-Reagan-said-downing-of-Iranian-airliner-was-understandable-accident/3452583992000/) — Grade B1
- UPI (1988). Iran accepts unconditional cease-fire. UPI Archives, 18 July. [link](https://www.upi.com/Archives/1988/07/18/Iran-accepts-unconditional-cease-fire/6562585201600) — Grade B1
- UPI (1989). Four U.S. warships withdraw from Persian Gulf. UPI Archives, 2 April. [link](https://www.upi.com/amp/Archives/1989/04/02/Four-US-warships-withdraw-from-Persian-Gulf/9819607496400) — Grade B2
- US Energy Information Administration (2026). Today in Energy: Brent's first-quarter rise. EIA. [link](https://www.eia.gov/todayinenergy/detail.php?id=67424) — Grade A2
- US Naval History and Heritage Command (2018). H-Gram 018: 30th Anniversary of Operation Praying Mantis. NHHC Director's Corner, April. [link](https://history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-018.html) — Grade B1 (graded here)
- Washington Post (1987). Kuwait rejects U.S. offer of Gulf tanker escorts. The Washington Post, 28 March. [link](https://www.washingtonpost.com/archive/politics/1987/03/28/kuwait-rejects-us-offer-of-gulf-tanker-escorts/2d0b325d-845a-43f0-8d7c-3bd110d6186c/) — Grade B2
- World Bank (2026). Commodity Markets Outlook, April 2026 (seen via Kitco). World Bank. [link](https://www.kitco.com/news/off-the-wire/2026-04-28/world-bank-forecasts-24-surge-energy-prices-2026-due-middle-east-war) — Grade A2
- World Monitor (2026). Strait of Hormuz transit report, July 2026 (write-up of IMF PortWatch data). World Monitor. [link](https://www.worldmonitor.app/research/strait-of-hormuz-transit-report-2026-07/) — Grade D3 (graded here)

### Suez Canal and Red Sea

- Abrahamson, B. J. (1973). \[Critical review of the UNCTAD estimates of the costs of the Suez Canal closure\]. TRID record. [link](https://trid.trb.org/View/10346) — Grade C3 (graded here)
- ACLED (2025). Regional power struggles fuel simmering tensions across Red Sea. ACLED. [link](https://acleddata.com/report/regional-power-struggles-fuel-simmering-tensions-across-red-sea) — Grade B2
- Ahram Online (2025). Suez Canal revenues plummet to $4 bln in 2024 amid Red Sea tensions: SCA chairman. Ahram Online. [link](https://english.ahram.org.eg/News/537710.aspx) — Grade D2
- Al Jazeera (2024). Greek-owned Tutor believed to have sunk a week after Houthi missile attack. Al Jazeera. [link](https://www.aljazeera.com/news/2024/6/19/greek-owned-tutor-believed-to-have-sunk-a-week-after-houthi-missile-attack) — Grade B1
- ANSA (2026). Kallas: "Attacchi degli Houthi inaccettabili, Aspides innalza l'allerta". ANSA. [link](https://www.ansa.it/europa/notizie/rubriche/altrenews/2026/09/18/-kallas-attacchi-degli-houthi-inaccettabili-aspides-innalza-lallerta-_3b2d7ec1-5b02-4ee5-8862-18206cd51620.html) — Grade B2
- Arellanes Arellanes, J. (2025). Los hutíes en el entramado geopolítico de Medio Oriente: la Crisis del Mar Rojo como disrupción de la seguridad marítima internacional. Revista Mexicana de Ciencias Políticas y Sociales 70(255). [link](https://www.revistas.unam.mx/index.php/rmcpys/article/view/93957) — Grade A2
- Associated Press (1975). \[Sadat reopens the Suez Canal\]. The Michigan Daily. [link](https://digital.bentley.umich.edu/midaily/mdp.39015071754639/265) — Grade B1
- Associated Press (2021). Not only grounded ships: A look at past crises that closed Suez. Times of Israel. [link](https://www.timesofisrael.com/not-only-grounded-ships-a-look-at-past-crises-that-closed-suez/) — Grade B1
- Associated Press (2025). At least 4 presumed dead, 11 missing after Houthi rebels sink ship in Red Sea, EU naval mission says. CP24. [link](https://www.cp24.com/news/world/2025/07/11/at-least-4-presumed-dead-11-missing-after-houthi-rebels-sink-ship-in-red-sea-eu-naval-mission-says/) — Grade B1 (graded here)
- Associated Press (2026). Yemen's Iranian-backed Houthis say they will block Saudi shipping at Red Sea gateway. ABC News. [link](https://abcnews.com/International/wireStory/yemens-houthis-announce-maritime-embargo-saudi-arabia-134912678) — Grade B1
- Bedoya-Maya, F. and others (2025). Container port competitiveness amid disruptions: insights from the European maritime network during the Red Sea crisis. Journal of Transport Geography 128. [link](https://doi.org/10.1016/j.jtrangeo.2025.104304) — Grade A2
- Bloomberg (2025). Houthi attacks in Red Sea sink two cargo ships, leave three dead. Bloomberg. [link](https://www.bloomberg.com/news/articles/2025-07-07/houthis-say-they-hit-red-sea-ship-in-first-attack-this-year) — Grade B1
- Boyd, J. H., Jr. (1976). Nimrod Spar: Clearing the Suez Canal. Proceedings (US Naval Institute) 102/2/876. [link](https://www.usni.org/magazines/proceedings/1976/february/nimrod-spar-clearing-suez-canal) — Grade B2
- CBS News (2025). Trump says U.S. will stop bombing Houthis after group "capitulated". CBS News. [link](https://www.cbsnews.com/amp/news/trump-houthis-ceasefire-bombing-over-capitulated) — Grade B1
- CEPII (2016). Trade costs and the Suez and Panama Canals, Working Paper 2016-29. CEPII. [link](https://www.cepii.fr/PDF_PUB/wp/2016/wp2016-29.pdf) — Grade B2
- CIA (1967). \[Briefing note on the Suez Canal, August 1967\]. CIA Reading Room. [link](https://www.cia.gov/readingroom/print/409837) — Grade B2 (graded here)
- CNN (2023). Austin announces US-led security operation focusing on Red Sea, Gulf of Aden after Houthi attacks on commercial shipping. KTVZ / CNN. [link](https://ktvz.com/politics/cnn-us-politics/2023/12/18/austin-announces-us-led-security-operation-focusing-on-red-sea-gulf-of-aden-after-houthi-attacks-on-commercial-shipping/) — Grade B1
- Commander Task Force 65 (1975). CTF Sixty-Five Final Report: Suez Canal Clearance Operations Nimbus Star, Nimbus Moon, Nimrod Spar. DTIC AD-A010 261. [link](https://apps.dtic.mil/sti/pdfs/ADA010261.pdf) — Grade B1
- Container News (2026). Suez Canal traffic still 60% below pre-attack levels 100 days on (BIMCO data; Lloyd's List attack count). Container News. [link](https://container-news.com/suez-canal-traffic-still-60-below-pre-attack-levels-100-days-on) — Grade C2
- Council of the EU (2024). Decision (CFSP) 2024/3186 amending Decision 2008/851/CFSP (Operation ATALANTA). EUR-Lex. [link](https://eur-lex.europa.eu/eli/dec/2024/3186/oj) — Grade A1
- Council of the EU (2024–26). Decisions (CFSP) 2024/583, 2024/632, 2025/334 and 2026/439 on EUNAVFOR ASPIDES. EUR-Lex. [link](https://eur-lex.europa.eu/eli/dec/2024/583/oj/eng) — Grade A1
- CSIS (2024). The Global Economic Consequences of the Attacks on Red Sea Shipping Lanes. Center for Strategic and International Studies. [link](https://www.csis.org/analysis/global-economic-consequences-attacks-red-sea-shipping-lanes) — Grade B2
- CSIS (2026). The Houthis Enter the Iran War and Everything Gets Worse. Center for Strategic and International Studies. [link](https://www.csis.org/analysis/houthis-enter-iran-war-and-everything-gets-worse) — Grade B2
- Dawn (2025). Death toll from Houthi attack on ship in Red Sea rises to 4: report. Dawn. [link](https://www.dawn.com/news/1923694/death-toll-from-houthi-attack-on-ship-in-red-sea-rises-to-4-report) — Grade C3 (graded here)
- Drewry (2024). World Container Index, release of 18 January 2024. Drewry. [link](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry) — Grade B2
- ECB (2024). Staff macroeconomic projections, March 2024 (Box 3). European Central Bank. [link](https://www.ecb.europa.eu/press/projections/html/ecb.projections202403_ecbstaff~f2f2d34d5a.en.html) — Grade A2
- ECFR (2026). The strait and narrow: Yemen, the Red Sea and Europe's path forward. European Council on Foreign Relations. [link](https://ecfr.eu/article/the-strait-and-narrow-yemen-the-red-sea-and-europes-path-forward/) — Grade B2
- EEAS (2026). \[EUNAVFOR Aspides ship-protection figures to August 2026\], reposted by Lovguiden. Lovguiden.dk. [link](https://lovguiden.dk/en/det-offentlige/eu-udenrigstjenesten/2026-08-24-eunavfor-aspides-har-eskorteret-over-2390-skibe-i-roedt-hav) — Grade B2 (graded here)
- Egypt and Israel (1974). Agreement on Disengagement of Forces (Kilometre 101), annexed to UN document S/11198. United Nations (UNISPAL). [link](https://www.un.org/unispal/document/auto-insert-181723) — Grade A1
- Egypt Today (2025). Egypt's Suez Canal revenues go down by 61% to $3.9 billion in 2024 due to Red Sea tensions. Egypt Today. [link](https://www.egypttoday.com/Article/3/139635/Egypt%E2%80%99s-Suez-Canal-revenues-go-down-by-61-to-3) — Grade D2
- Engine (2024). Brent moves higher amid rising attacks in the Red Sea. Engine. [link](https://engine.online/news/brent-moves-higher-amid-rising-attacks-in-the-red-sea-585e) — Grade C2 (graded here)
- Feyrer, J. (2021). Distance, trade, and income – The 1967 to 1975 closing of the Suez Canal as a natural experiment. Journal of Development Economics 153, 102708. [link](https://doi.org/10.1016/j.jdeveco.2021.102708) — Grade A2
- Forces News (2024–25). Red Sea trade declines, Houthis grow strength despite Western airstrikes (citing IISS). Forces News. [link](https://www.forcesnews.com/middle-east/red-sea-trade-declines-houthis-grow-strength-despite-western-airstrikes) — Grade C2
- gCaptain (2024). Maersk halts Red Sea voyages "until further notice". gCaptain. [link](https://gcaptain.com/maersk-pausing-red-sea-transits-until-further-notice/) — Grade C1
- gCaptain (undated). How tiny Djibouti said no to the U.S. over Houthi Red Sea attacks. gCaptain. [link](https://gcaptain.com/how-tiny-djibouti-said-no-to-the-u-s-over-houthi-red-sea-attacks/) — Grade C2
- IMF (2024). Red Sea attacks disrupt global trade. IMF Blog (Chart of the Week). [link](https://www.imf.org/Blogs/Articles/2024/03/07/Red-Sea-Attacks-Disrupt-Global-Trade) — Grade A1
- Iran International (2025). \[Report on deaths in Houthi attacks on shipping, 8 July 2025\]. Iran International. [link](https://cdn.iranintl.news/en/202507081358) — Grade C3 (graded here)
- Lloyd's List (2024). Red Sea war risk rates see huge jump in wake of Yemen airstrikes. Lloyd's List. [link](https://www.lloydslist.com/LL1147965/Red-Sea-war-risk-rates-see-huge-jump-in-wake-of-Yemen-airstrikes) — Grade B2
- Lloyd's List Intelligence (2026). Red Sea Brief: 6 August 2026. Lloyd's List Intelligence blog. [link](https://www.lloydslistintelligence.com/resources/blog/red-sea-brief-6-august-2026) — Grade B2
- Mada Masr (2023). US to assemble international maritime security force to protect shipping lines after Houthi attacks. Mada Masr. [link](https://www.madamasr.com/en/2023/12/19/news/u/shipping-lines-reroute-traffic-away-from-suez-canal-due-to-houthi-attacks-us-assembles-international-maritime-security-force/) — Grade C1
- New York Times (1967), quoted by The Gamming blog (2014). How the closure of the Suez Canal changed the world. The Gamming. [link](https://thegamming.org/2014/08/31/how-the-closure-of-the-suez-canal-changed-the-world/) — Grade C3 (graded here)
- Nixon, R. (1974). Letter from President Nixon to Egyptian President Sadat, 17 January 1974 (FRUS 1969–1976, vol. XXVI, doc. 13). Office of the Historian, US Department of State. [link](https://history.state.gov/historicaldocuments/frus1969-76v26/d13) — Grade A2
- Reuters (2024). Egypt's Sisi says regional challenges cost Egypt around $7 bln of Suez Canal revenues in 2024. CNBC Africa. [link](https://cnbcafrica.com/wire/655389) — Grade B2
- Reuters (2026). Saudi oil export strategy hits new hurdle as Red Sea insurance costs soar. Insurance Journal. [link](https://www.insurancejournal.com/news/international/2026/09/25/886769.htm) — Grade B2
- Samuelson, M. (1975). Suez Canal. The Spectator, 7 June, p. 11. [link](https://archive.spectator.co.uk/article/7th-june-1975/11/suez-canal) — Grade C2
- Seatrade Maritime News (2025). Eternity C sinks after Houthi attack in Red Sea, death toll rises. Seatrade Maritime. [link](https://www.seatrade-maritime.com/security/eternity-c-red-sea-attack-death-toll-rises-as-ship-reported-sunk) — Grade C2
- Shabait (2025). "No force substitutes the littoral states of the Red Sea": President Isaias Afwerki. Shabait (Eritrea). [link](https://shabait.com/2025/11/12/no-force-substitutes-the-littoral-states-of-the-red-sea-president-isaias-afwerki/) — Grade D3
- South24 (2024). \[Report counting 87 commercial ships targeted, November 2023 to May 2024\]. South24 Center. [link](https://south24.net/news/newse.php?nid=4019) — Grade C2
- SUMED (undated). \[Company history page: pipeline opened in 1977\]. SUMED website. [link](https://www.sumed.org/?p=history) — Grade B2 (graded here)
- Tallis, J. (2025). How the Biden Administration Won Tactically but Failed Strategically in the Red Sea. War on the Rocks. [link](https://warontherocks.com/2025/04/how-the-biden-administration-won-tactically-but-failed-strategically-in-the-red-sea/) — Grade C2
- The Objective (2024). Aspides: la misión de la UE en el mar Rojo. The Objective. [link](https://theobjective.com/internacional/2024-01-31/aspides-mision-ue-mar-rojo/) — Grade C1
- Time (1967). Middle East: The Quickest War. Time. [link](https://time.com/archive/6890621/middle-east-the-quickest-war/) — Grade B2
- Time (1969). World: The Suez Canal's Bleak Centennial. Time. [link](https://time.com/archive/6635732/world-the-suez-canals-bleak-centennial/) — Grade B2
- Time (1973). Middle East: The War of the Day of Judgment. Time. [link](https://time.com/archive/6841881/middle-east-the-war-of-the-day-of-judgment/) — Grade B3
- Time (1974). The World: Clean Sweep of the Canal. Time. [link](https://time.com/archive/6876758/the-world-clean-sweep-of-the-canal/) — Grade B4
- Time (1975). The World: Suez: The Seas Rejoined. Time. [link](https://time.com/archive/6846859/the-world-suez-the-seas-rejoined/) — Grade B3
- Times of Israel / AP and Al Jazeera (2025). Yemen's Houthis signal they've stopped attacks on Israel and Red Sea shipping (also reports the IMF estimate of Suez revenue lost). Times of Israel; Al Jazeera. [link](https://www.timesofisrael.com/yemens-houthis-signal-theyve-stopped-attacks-on-israel-and-red-sea-shipping/amp/) — Grade B2
- Última Hora (2023). España descarta participar en la operación para velar por la seguridad del mar Rojo. Última Hora. [link](https://www.ultimahora.es/noticias/nacional/2023/12/19/2071283/espana-descarta-participar-operacion-para-velar-por-seguridad-mar-rojo.html) — Grade C1
- UN Secretary-General (1967). \[Supplementary report S/8053/Add.4 on UN observers along the Suez Canal\]. United Nations Digital Library. [link](https://digitallibrary.un.org/record/520138/files/S_8053_Add.4-EN.pdf) — Grade A2 (graded here)
- UN Security Council (1967). Resolution 242 (1967), S/RES/242. United Nations Digital Library. [link](https://digitallibrary.un.org/record/90717) — Grade A1
- UN Security Council (2024). Resolution 2722 (2024), S/RES/2722. United Nations Digital Library. [link](https://digitallibrary.un.org/record/4033392/files/S_RES_2722_%282024%29-EN.pdf) — Grade A1
- UNCTAD (2024). Navigating Troubled Waters: Impact to Global Trade of Disruption of Shipping Routes in the Red Sea, Black Sea and Panama Canal. UNCTAD Rapid Assessment. [link](https://unctad.org/publication/navigating-troubled-waters-impact-global-trade-disruption-shipping-routes-red-sea-black) — Grade A1
- UNCTAD (2024). Review of Maritime Transport 2024. UNCTAD. [link](https://unctad.org/publication/review-maritime-transport-2024) — Grade A1
- UNCTAD Secretariat (1973). Economic Effects of the Closure of the Suez Canal (TD/B/C.4/104). UNCTAD (TRID record). [link](https://trid.trb.org/View/15787) — Grade A3
- UPI (1975). Foreign Affairs: Peace in the Middle East, Conflict in Ireland, Death of Franco \[audio review\]. United Press International. [link](https://www.upi.com/Archives/Audio/1975/Foreign-Affaris-Peace-in-the-Middle-East-Conflict-in-Ireland-Death-of-Franco/) — Grade B2
- US Bureau of Mines (1968). Minerals Yearbook \[tanker rates "markedly higher" in 1967\]. US Bureau of Mines. [link](https://search.library.wisc.edu/digital/AGFCCUKXF4SS2G8F/text/ARC63O7UBJVOPV8E) — Grade A2 (graded here)
- World Oil (2024). Brent oil hits $80 following U.S. airstrikes against Yemen's Houthis. World Oil. [link](https://worldoil.com/news/2024/1/12/brent-oil-hits-80-following-u-s-airstrikes-against-yemen-s-houthis/) — Grade C2 (graded here)
- Yap, W. Y. and Yang, D. (2024). Geopolitical tension and shipping network disruption: analysis of the Red Sea crisis on container port calls. Journal of Transport Geography 121. [link](https://doi.org/10.1016/j.jtrangeo.2024.104004) — Grade A2

### Strait of Malacca

- Al Jazeera (2003). \[Report quoting IMB piracy figures, October 2003\]. Al Jazeera. [link](https://www.aljazeera.com/archive/2003/10/200849142236338398.html) — Grade B2 (graded here)
- Al Jazeera (2005). Piracy disappears in tsunami's wake. Al Jazeera. [link](https://www.aljazeera.com/amp/news/2005/2/1/piracy-disappears-in-tsunamis-wake) — Grade B2
- Beckman, R. (2012). Piracy and Armed Robbery Against Ships in Southeast Asia (presentation slides). Centre for International Law, National University of Singapore. [link](https://cil.nus.edu.sg/wp-content/uploads/2012/03/Beckman-Piracy-in-SE-Asia-CIL-NCSB-SOA-exchange.pdf) — Grade B2
- Business Insurance (2006). Strait of Malacca off high-risk list. Business Insurance. [link](https://www.businessinsurance.com/strait-of-malacca-off-high-risk-list/) — Grade C1
- The Business Times (2006). Malacca Strait stays on Lloyd's Joint War Committee risk list (20 January 2006). The Business Times, via NewspaperSG. [link](https://eresources.nlb.gov.sg/newspapers/digitised/issue/biztimes20060120-1) — Grade C2
- CIMSEC (c. 2014). It's the economy: exploring Indonesia's piracy problem. CIMSEC (naval-affairs forum). [link](https://cimsec.org/economy-stupid-exploring-indonesias-piracy-problem/) — Grade C2
- U.S. Energy Information Administration (EIA) (2026). World Oil Transit Chokepoints (updated 3 March 2026). EIA. [link](https://www.eia.gov/international/content/analysis/special_topics/World_Oil_Transit_Chokepoints) — Grade A1
- Free Malaysia Today (2026). 75% increase in piracy, robbery cases in Straits of Melaka, S'pore. Free Malaysia Today. [link](https://www.freemalaysiatoday.com/category/nation/2026/01/10/75-increase-in-piracy-robbery-cases-in-straits-of-melaka-spore) — Grade C1
- Gulf News (c. 2006). Piracy declines sharply in Malacca Straits. Gulf News. [link](https://gulfnews.com/business/piracy-declines-sharply-in-malacca-straits-1.224149) — Grade C3
- IALA (n.d.). Malacca Strait Traffic Volume and Incident Rates (Marine Department Malaysia data). IALA IWRAP wiki. [link](https://www.iala.int/wiki/iwrap/index.php/Malacca_Strait_Traffic_Volume_and_Incident_Rates) — Grade B2 (graded here)
- ICC International Maritime Bureau (ICC-IMB) (2001). Piracy attacks rise to alarming new levels, ICC report reveals. ICC press release. [link](https://iccwbo.org/news-publications/news/piracy-attacks-rise-to-alarming-new-levels-icc-report-reveals/) — Grade A1
- ICC International Maritime Bureau (ICC-IMB) (2004–05). IMB says security threats remain, despite new safety measures. ICC press release. [link](https://iccwbo.org/news-publications/news/imb-says-security-threats-remain-despite-new-safety-measures/) — Grade A1
- ICC International Maritime Bureau (ICC-IMB) (2006). Iraq declared new piracy hotspot (31 January 2006, IMB 2005 annual figures). ICC press release. [link](https://iccwbo.org/news-publications/news/iraq-declared-new-piracy-hotspot/) — Grade A1
- ICC International Maritime Bureau (ICC-IMB) (2006). Decline in piracy attacks slows down, says IMB (half-year release, January–June 2006 figures). ICC press release. [link](https://iccwbo.org/news-publications/news/decline-in-piracy-attacks-slows-down-says-imb/) — Grade A1
- ICC International Maritime Bureau (ICC-IMB) (2009). IMB reports unprecedented rise in maritime hijackings (IMB 2008 annual figures). ICC press release. [link](https://iccwbo.org/news-publications/news/imb-reports-unprecedented-rise-in-maritime-hijackings/) — Grade A1
- ICC International Maritime Bureau (ICC-IMB) (2026). Piracy and Armed Robbery Against Ships: Report for 2025. ICC-IMB. [link](https://iccwbo.org/news-publications/report/global-maritime-piracy-and-armed-robbery-increased-in-2025/) — Grade A2
- inforMARE (2006). Lloyd's Joint War Committee removes the Malacca Strait from its listed areas. inforMARE. [link](https://www.informare.it/news/review/2006/b090806uk.asp) — Grade C1
- Johnson, D. and Valencia, M. (eds) (2005). Piracy in Southeast Asia: Status, Issues, and Responses. ISEAS / IIAS (book). [link](https://bookshop.iseas.edu.sg/publication/744) — Grade A2
- Kompas (2026). Arus minyak di Selat Malaka turun tajam, apa dampaknya ke Indonesia? (Oil flow in the Malacca Strait drops sharply). Kompas. [link](https://money.kompas.com/read/2026/08/19/145051526/arus-minyak-di-selat-malaka-turun-tajam-apa-dampaknya-ke-indonesia) — Grade C2
- Kontorovich, E. and Art, S. (2010). An empirical examination of universal jurisdiction for piracy. American Journal of International Law, 104. [link](https://scholarlycommons.law.northwestern.edu/facultyworkingpapers/38) — Grade A2
- Koran Jakarta (2025). Bakamla RI dan APMM Malaysia gelar rendezvous di Selat Malaka (Indonesian and Malaysian coastguards meet in the strait). Koran Jakarta. [link](https://koran-jakarta.com/2025-09-20/bakamla-ri-dan-apmm-malaysia-gelar-rendezvous-di-selat-malaka) — Grade C2
- Lloyd's Market Association Joint War Committee (LMA JWC) (2026). Listed Areas, circular JWLA-033 (3 March 2026). LMA. [link](https://lmalloyds.com/wp-content/uploads/2026/03/JWLA-033_Iran.pdf) — Grade A1
- London P&I Club (2006). Circular 7083 on the JWC delisting of the Malacca Strait. London P&I Club. [link](https://www.londonpandi.com/media/1386/7083.pdf) — Grade C1 (seen via inforMARE, as graded in provenance P05-07 #47)
- Thư Nguyễn Hoàng Anh (2023). Sea robbery in the Singapore Strait. The Interpreter (Lowy Institute). [link](https://www.lowyinstitute.org/the-interpreter/sea-robbery-singapore-strait) — Grade B2
- Malay Mail (2025). Piracy in Strait of Malacca, Singapore Strait surges nearly fourfold in 2025, says anti-piracy watchdog. Malay Mail. [link](https://www.malaymail.com/news/malaysia/2025/08/26/piracy-in-strait-of-malacca-singapore-strait-surges-nearly-fourfold-in-2025-says-anti-piracy-watchdog/188915) — Grade C1
- &#91;Author unknown\] (2026). Complexities of governance and sovereignty in maritime security. Marine Policy, vol. 187. [link](https://www.sciencedirect.com/science/article/pii/S0308597X26000369) — Grade A3
- The Maritime Executive (2005). \[Insurance rates for Malacca Strait transits\] (6 July 2005). The Maritime Executive. [link](https://maritime-executive.com/article/2005-07-06insurance-rates-for-malacca-strait-tra) — Grade C2
- The Maritime Executive (2025). Indonesian police bust pirate gang in Riau Islands. The Maritime Executive. [link](https://www.maritime-executive.com/article/indonesian-police-bust-pirate-gang-in-riau-islands) — Grade C1
- Ministry of Defence, Singapore (MINDEF) (2005). Joint news release: launch of Eyes in the Sky (EiS) initiative. National Archives of Singapore. [link](https://www.nas.gov.sg/archivesonline/data/pdfdoc/20050913984.htm) — Grade B1
- Ministry of Defence, Singapore (MINDEF) (2008). Thailand joins Malacca Straits Patrols. National Archives of Singapore. [link](https://www.nas.gov.sg/archivesonline/data/pdfdoc/20080918989.htm) — Grade B1
- Ministry of Defence, Singapore / Republic of Singapore Navy (MINDEF) (2025). Reply to media query on increase in piracy in Singapore waters. MINDEF. [link](https://www.mindef.gov.sg/news-and-events/latest-releases/13oct25-mq/) — Grade B2
- Oegroseno, A.H. / Ministry of Foreign Affairs, Indonesia (2008). Presentation on the Straits of Malacca and Singapore to the UN Open-ended Informal Consultative Process on Oceans and the Law of the Sea. UN Division for Ocean Affairs and the Law of the Sea. [link](https://static.un.org/depts/los/consultative_process/documents/9_oegroseno_presentation.pdf) — Grade B2
- Peace Accords Matrix (n.d.). Disarmament: MoU between the Government of the Republic of Indonesia and the Free Aceh Movement. Peace Accords Matrix (University of Notre Dame). [link](https://peaceaccords.nd.edu/provision/disarmament-mou-between-the-government-of-the-republic-of-indonesia-and-the-free-aceh-movement) — Grade B1 (graded here)
- Poonnawatt, K. (2023). Multilateral cooperation against maritime piracy in the Straits of Malacca: from the RMSI to ReCAAP. Marine Policy, vol. 152, article 105628. [link](https://www.sciencedirect.com/science/article/abs/pii/S0308597X23001550) — Grade A2
- PortNews (2026). Piracy and sea robbery in Malacca-Singapore Straits hit 19-year high in 2025, ReCAAP says. PortNews. [link](https://en.portnews.ru/news/386610/) — Grade C2
- ReCAAP member states (2004). Regional Cooperation Agreement on Combating Piracy and Armed Robbery against Ships in Asia (ReCAAP Agreement). NUS Centre for International Law treaty database. [link](https://cil.nus.edu.sg/databasecil/2004-regional-cooperation-agreement-on-combating-piracy-and-armed-robbery-against-ships-in-asia-3/) — Grade A1
- ReCAAP ISC (2025). Incident Alert 01/2025: sea robbery incidents in the Singapore Strait (3 February 2025). ReCAAP Information Sharing Centre. [link](<https://www.recaap.org/resources/ck/files/alerts/2025/ReCAAP%20ISC%20IA%2001-2025%20Sea%20robbery%20Incidents%20in%20the%20Singapore%20Strait%20(3%20Feb%202025).pdf>) — Grade A1
- ReCAAP ISC (2026). Piracy and Armed Robbery against Ships in Asia: Annual Report 2025 and press release (January 2026). ReCAAP Information Sharing Centre. [link](https://recaap.org/resources/ck/files/reports/annual/ReCAAP%20ISC%20Annual%20Report%202025.pdf) — Grade A1
- ReCAAP ISC (2026). Piracy and Armed Robbery against Ships in Asia: Half Yearly Report, January–June 2026 (July 2026). ReCAAP Information Sharing Centre. [link](https://www.recaap.org/resources/ck/files/reports/half-year/ReCAAP%20ISC%20Half%20Yearly%20Report%202026.pdf) — Grade A1
- RSIS (n.d.). Piracy in the South China Sea (IDSS publication 1176). S. Rajaratnam School of International Studies, Nanyang Technological University. [link](https://rsis.edu.sg/rsis-publication/idss/1176-piracy-in-the-south-china-sea) — Grade B2
- RSIS (2005). Malacca Straits: a war risk? (Commentary CO05057). S. Rajaratnam School of International Studies, Nanyang Technological University. [link](https://rsis.edu.sg/rsis-publication/rsis/718-malacca-straits-a-war-risk/) — Grade B2
- RSIS (2006). Marine war risk insurance (commentary). S. Rajaratnam School of International Studies, Nanyang Technological University. [link](https://rsis.edu.sg/rsis-publication/rsis/769-marine-war-risk-insurance-sho/) — Grade B2
- RSIS (2025). Anti-Piracy and Sea Robbery Conference 2025 (event report). S. Rajaratnam School of International Studies, Nanyang Technological University. [link](https://rsis.edu.sg/rsis-event-article/rsis/anti-piracy-and-sea-robbery-conference-2025/) — Grade B2
- SAFETY4SEA (2026). ReCAAP ISC Q3: 58% drop in Asian piracy and armed robbery incidents. SAFETY4SEA. [link](https://safety4sea.com/recaap-isc-q3-58-drop-in-asian-piracy-and-armed-robbery-incidents/) — Grade C2
- Seatrade Maritime (2026). Malacca Strait vessel traffic at record levels in 2025. Seatrade Maritime. [link](https://www.seatrade-maritime.com/tankers/malacca-strait-vessel-traffic-at-record-levels-in-2025) — Grade C2
- Seatrade Maritime (2026). 2 or 3 ship robbery groups remain active in Singapore Strait (January 2026). Seatrade Maritime. [link](https://www.seatrade-maritime.com/security/2-or-3-ship-robbery-groups-remain-active-in-singapore-strait) — Grade C2 (graded here)
- SMERU Research Institute (n.d.). \[Indonesian poverty data, 1999–2010\]. SMERU. [link](https://smeru.or.id/en/node/1147) — Grade B2 (graded here)
- Splash247 (2026). Singapore Strait crackdown sends Asian sea robberies to seven-year low. Splash247. [link](https://splash247.com/singapore-strait-crackdown-sends-asian-sea-robberies-to-seven-year-low/) — Grade C1
- The Straits Times (2004). Malaysia rules out direct foreign policing of the strait (28 April 2004). The Straits Times, via NewspaperSG. [link](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes20040428-1) — Grade C1
- Today (2006). ReCAAP Information Sharing Centre launched (30 November 2006). Today (Singapore), via NewspaperSG. [link](https://eresources.nlb.gov.sg/newspapers/digitised/issue/today20061130-2) — Grade C1
- YaleGlobal Online (2004). Indonesia, Malaysia, Singapore launch coordinated patrol of Malacca Strait. YaleGlobal Online. [link](https://archive-yaleglobal.yale.edu/node/47391) — Grade B1
