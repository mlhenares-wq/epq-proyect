# Chokepoint Disruption Risk Index (CDRI)

> **Update:** this is **version 1** (the simple version). The recommended equation is the **CCRI**, $R = (L \times S \times K)^{1/3}$ with $K = 5 - C/5$. It is justified in `equation-literature-review.md` and applied to all three case studies in `ccri-results.md`. The scoring bands below (§2–§3) and the process-tracing method (§4) are still used by version 2.

A method for measuring the **risk of disruption** at a maritime chokepoint, comparing it between two periods, and testing **how much of the change was caused by multilateral cooperation**.

It uses the standard definition of risk from risk management (ISO 31000 and most national risk registers, including the UK's National Risk Register):

> **Risk = Likelihood × Severity**

Your EPQ already has measures for both parts, so the equation reuses them.

---

## 1. The equations

### 1a. Likelihood of disruption (L)

$$
L = \frac{s_{\text{incidents}} + s_{\text{insurance}} + s_{\text{freight}}}{n_L}
$$

| Symbol | Meaning |
|---|---|
| $s_{\text{incidents}}$ | Score 1–5 for the number of recorded attacks, hijackings, robberies or mine strikes per year |
| $s_{\text{insurance}}$ | Score 1–5 for war-risk insurance premiums (as % of hull value per transit) |
| $s_{\text{freight}}$ | Score 1–5 for the rise in freight rates on the route, compared with the level before the disruption |
| $n_L$ | Number of these indicators you have data for (normally 3; use 2 if one is missing for a historical period) |

### 1b. Severity of disruption (S)

$$
S = \frac{s_{\text{trade}} + s_{\text{duration}} + s_{\text{price}}}{n_S}
$$

| Symbol | Meaning |
|---|---|
| $s_{\text{trade}}$ | Score 1–5 for trade reduction (the % fall in transits or tonnage compared with before the disruption) |
| $s_{\text{duration}}$ | Score 1–5 for the length of disruption |
| $s_{\text{price}}$ | Score 1–5 for the rise in prices (Brent crude peak rise, backed up by a general price level estimate where one exists) |
| $n_S$ | Number of these indicators you have data for |

### 1c. Risk (R)

$$
R = L \times S \qquad (1 \le R \le 25)
$$

| R | Risk band |
|---|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–15 | High |
| 16–25 | Very high |

This is the same 5 × 5 matrix that governments and insurers use, so it is easy to justify in your methodology.

### 1d. Change in risk between your two periods

$$
\Delta R = R_{\text{later}} - R_{\text{earlier}} \qquad\qquad \%\Delta R = \frac{\Delta R}{R_{\text{earlier}}} \times 100
$$

A negative $\Delta R$ means the risk fell.

### 1e. Multilateral Cooperation Index (C)

$$
C = c_{\text{frameworks}} + c_{\text{joint ops}} + c_{\text{info sharing}} + c_{\text{response speed}} + c_{\text{enforcement}} \qquad (0 \le C \le 20)
$$

Score each factor 0–4 using the rubric in section 3.

---

## 2. Scoring rubric: likelihood and severity (1–5)

Use the same bands for every case study and every period. This is what makes the three straits comparable.

### Likelihood indicators

| Score | Incidents per year | War-risk premium (% of hull value per transit) | Freight rate rise vs before |
|---|---|---|---|
| 1 | 0–5 | under 0.05% (normal) | under 10% |
| 2 | 6–20 | 0.05–0.2% | 10–50% |
| 3 | 21–50 | 0.2–0.5% | 50–100% |
| 4 | 51–150 | 0.5–1% | 100–200% |
| 5 | over 150 | over 1%, or cover withdrawn / route listed and ships refusing | over 200% |

### Severity indicators

| Score | Trade reduction (fall in transits) | Length of disruption | Price rise (Brent, pre-crisis to peak) |
|---|---|---|---|
| 1 | under 10% | under 1 week | under 10% |
| 2 | 10–30% | 1 week – 1 month | 10–25% |
| 3 | 30–60% | 1–6 months | 25–50% |
| 4 | 60–90% | 6 months – 2 years | 50–100% |
| 5 | over 90% | over 2 years | over 100% |

**Rules for awkward data:**
- Use the **peak year** of each period for incidents and premiums, and the **peak fall** for trade. Say that you did this.
- If two sources disagree (e.g. 37 vs 38 Malacca attacks in 2004, or different ship-tracking counts for Hormuz), score both. If the score is the same, the disagreement does not matter. If it differs, give the range of R.
- Where a figure does not exist for a historical period (for example PortWatch data before 2019), leave the indicator out and reduce $n$. Record this as a limitation.

---

## 3. Scoring rubric: cooperation factors (0–4)

| Score | Formal frameworks | Joint operations | Information sharing | Response speed | Enforcement of laws |
|---|---|---|---|---|---|
| 0 | No agreement covers the route | None | None | No coordinated action at all | Rules ignored, no consequences |
| 1 | General rules only (e.g. UNCLOS) | One or two states acting separately | Ad hoc national warnings | Over 1 year | Rare, symbolic |
| 2 | A specific agreement, few members | Small coalition, limited area or time | A reporting centre exists, slow | 3–12 months | Some arrests or sanctions, patchy |
| 3 | Specific agreement, most key states, some binding | Sustained coalition covering most of the route | Regular advisories to industry | 1–3 months | Regular prosecutions, most ships follow agreed routes |
| 4 | Binding, includes all littoral states and major users | Coordinated, continuous, all key states | Real-time sharing between states and industry | Under 1 month | Consistent enforcement that deters |

Example: response speed scores 1 for the 1967 Suez closure (about 7 years until clearance) and 4 for the 2026 IEA stock release (11 days), but only 2 for the 2026 UK–France mission (still not deployed by October 2026, over 7 months).

---

## 4. Was multilateralism the *main* reason for the change in risk?

The equation shows **how much** risk changed. It cannot show **why** on its own, because many things change between two periods. To test causes, use **process tracing** (George and Bennett, 2005, *Case Studies and Theory Development in the Social Sciences*, MIT Press), which is the standard method for small-number case comparisons.

### 4a. The Cause Contribution Score

For **every possible cause**, i.e. multilateral cooperation plus each alternative factor in your plan (supply chain design, trade concentration, type of threat, technology, connected crises, physical alternatives, regional economic growth, and any case-specific ones such as the 2004 tsunami), score four tests, each 0–2:

| Test | 0 | 1 | 2 |
|---|---|---|---|
| **Change**: did this factor change between the two periods? | No | A little | A lot |
| **Timing**: did the change come *before* the change in risk? | No / after | Roughly the same time | Clearly before |
| **Mechanism**: do sources show *how* it changed L or S? | No evidence | Claimed, no data | Direct evidence (data, official reports) |
| **Counterfactual**: would risk have changed without it? | Yes, anyway | Partly | No, sources say this was decisive |

$$
\text{Contribution}_i = \text{Change}_i + \text{Timing}_i + \text{Mechanism}_i + \text{Counterfactual}_i \qquad (0\text{–}8)
$$

$$
\text{Share}_i = \frac{\text{Contribution}_i}{\sum_j \text{Contribution}_j} \times 100\%
$$

**Decision rule:**
- Multilateralism is **the main reason** if its share is the largest **and** at least 1.5 times the next largest.
- It is **a major reason among several** if it is the largest but by less than 1.5 times, or second within a few points.
- It is **a minor reason** otherwise.

### 4b. Direction check

Also note the **sign** of each cause. Cooperation can *raise* risk. Sources argue that the US-led strikes on the Houthis in 2024 were followed by more attacks, not fewer. Record such a cause with a minus sign and discuss it in your evaluation, because it is exactly the kind of counter-argument examiners reward.

---

## 5. Worked template (fill in from your sources)

| | Period 1 | Period 2 |
|---|---|---|
| Incidents (score) | | |
| Insurance (score) | | |
| Freight (score) | | |
| **L** | | |
| Trade reduction (score) | | |
| Duration (score) | | |
| Price rise (score) | | |
| **S** | | |
| **R = L × S** | | |
| **C** | | |
| **ΔR** | | |
| **ΔC** | | |

Then fill in the cause table:

| Cause | Change | Timing | Mechanism | Counterfactual | Total | Share |
|---|---|---|---|---|---|---|
| Multilateral cooperation | | | | | | |
| Type of threat | | | | | | |
| Physical alternatives | | | | | | |
| Connected crises | | | | | | |
| … | | | | | | |

The completed tables for your three case studies are in `research/multilateralism-attribution.md`.

---

## 6. Limitations to discuss in your evaluation

1. **The bands are a judgement.** Equal weights and the cut-off points are your choice. Test this: double the weight of one indicator and see whether your conclusion changes (a *sensitivity test*). If it does not change, your conclusion is robust.
2. **Likelihood measures also react to severity.** Insurance premiums and freight rates rise both because attacks are more likely and because each attack is costlier. Your plan already notes this; say so here too.
3. **Historical data is thinner.** The 1967–75 and 1980–88 periods have no daily ship-tracking data, so fewer indicators are used ($n < 3$).
4. **Peak versus average.** Using peak values exaggerates short spikes. You could repeat the calculation with yearly averages.
5. **Process tracing scores are qualitative.** They make your reasoning transparent, but two researchers could score them differently. Show your evidence for every score.
6. **Multiplying ordinal scores** (1–5) is standard practice in risk matrices but is not true arithmetic on measured quantities. Use R to rank and compare, not as an exact amount.
