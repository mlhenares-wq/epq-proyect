# Results: the three case studies under both equations

This file applies the recommended **Cooperation-Adjusted Chokepoint Risk Index (CCRI)** from `equation-literature-review.md` to the scores found by the three attribution analyses (`attribution/A1–A3`), and compares it with the simpler **CDRI** (`risk-equation.md`).

$$
\textbf{CCRI:}\quad R = (L \times S \times K)^{1/3}, \qquad K = 5 - \frac{C}{5} \qquad (1 \le R \le 5)
$$

$$
\textbf{CDRI:}\quad R = L \times S \qquad (1 \le R \le 25)
$$

In the CCRI, freight rates are part of **S** (severity), not L. K is "lack of coping capacity": it falls from 5 to 1 as cooperation C rises from 0 to 20.

---

## 1. Inputs (indicator scores from the attribution files)

| Case and period | Incidents | Insurance | Trade | Duration | Price | Freight | **L** | **S** | **C** | **K** |
|---|---|---|---|---|---|---|---|---|---|---|
| Hormuz: Tanker War (1984–88) | 5 | 5 | 2 | 5 | 1 | no data | 5.00 | 2.67 | 9 | 3.20 |
| Hormuz: 2026 closure | 4 | 5 | 5 | 4 | 4 | 5 | 4.50 | 4.50 | 12 | 2.60 |
| Suez: 1967–75 closure | not valid* | 5* | 5 | 5 | 1 | 4 | 5.00 | 3.75 | 5 | 4.00 |
| Red Sea: 2023–26 Houthi crisis | 4 | 4 | 4 | 5 | 1 | 5 | 4.00 | 3.75 | 13 | 2.40 |
| Malacca: peak (2000–05) | 4 | 3 | 1 | 1 | 1 | no data | 3.50 | 1.00 | 6 | 3.80 |
| Malacca: 2008 | 2 | 1 | 1 | 1 | 1 | no data | 1.50 | 1.00 | 13 | 2.40 |
| Malacca: 2025 | 4 | 1 | 1 | 1 | 1 | no data | 2.50 | 1.00 | 15 | 2.00 |
| Malacca: 2026 (Jan–Sep) | 3 | 1 | 1 | 1 | 1 | no data | 2.00 | 1.00 | 15 | 2.00 |

\* **Suez 1967:** the canal was closed by a state, so disruption was certain, not a matter of chance, and "incidents per year" is not a valid measure. L is scored 5 on the insurance indicator using the rubric's top condition ("cover withdrawn / ships refusing the route"), because no ship could use the canal at all. This is a judgement; say so in your methodology.

---

## 2. Results

| Case | Period 1 R | Period 2 R | ΔR | Old CDRI (L×S) | Counterfactual R (C kept at period-1 level) | **Direct effect of extra cooperation** |
|---|---|---|---|---|---|---|
| **Hormuz** | 3.49 High | 3.75 High | **+0.25 (+7%)** | 13.3 → 20.2 (+52%) | 4.02 Very high | −0.27 |
| **Suez / Red Sea** | 4.22 Very high | 3.30 High | **−0.92 (−22%)** | 18.8 → 15.0 (−20%) | 3.91 High | −0.61 |
| **Malacca, peak → 2008** | 2.37 Moderate | 1.53 Low | **−0.84 (−35%)** | 3.5 → 1.5 (−57%) | 1.79 Low | −0.25 |
| **Malacca, 2025 → 2026** | 1.71 Low | 1.59 Low | **−0.12 (−7%)** | 2.5 → 2.0 (−20%) | 1.59 Low | 0.00 (C unchanged) |

Risk bands for the CCRI: 1.0–1.9 Low, 2.0–2.9 Moderate, 3.0–3.9 High, 4.0–5.0 Very high.

### Where the change came from (log decomposition)

| Case | Δln L (likelihood) | Δln S (severity) | Δln K (coping capacity) |
|---|---|---|---|
| Hormuz | −0.105 | **+0.523** | −0.208 |
| Suez / Red Sea | −0.223 | 0.000 | **−0.511** |
| Malacca, peak → 2008 | **−0.847** | 0.000 | −0.460 |
| Malacca, 2025 → 2026 | −0.223 | 0.000 | 0.000 |

(Shares are only meaningful when all three move the same way. For Hormuz they do not, so read each column separately.)

---

## 3. How to read this: an important warning about the K term

**The K term assumes that more cooperation means less risk.** It does not test this assumption. It builds it in. That is why the CCRI shows cooperation "lowering" risk in every case where C rose, including Suez and the Red Sea, where the evidence in `attribution/A2` shows the January 2024 strikes *tripled* insurance premiums.

So the two parts of the method answer different questions:

| Part | Question it answers | What it shows here |
|---|---|---|
| **K term (counterfactual)** | *If* cooperation works as coping capacity is assumed to, how much would it have reduced risk? | An **upper bound**: at most −0.27 (Hormuz), −0.61 (Red Sea), −0.25 (Malacca) |
| **Observed L and S** | What actually happened to likelihood and severity? | Hormuz: severity **rose** sharply despite more cooperation. Red Sea: likelihood fell a little and severity stayed the same. Malacca: likelihood fell sharply |
| **Process tracing (cause table)** | *Why* did L and S change? | Cooperation was a **minor** cause at Hormuz (5.7%) and the Red Sea (8.5%), and a **major cause among several** at Malacca (15.8–23.7%) |

**Use the CCRI to measure risk and to give the best case for cooperation. Use the process-tracing table to judge whether cooperation actually caused the change.** Saying this explicitly in your evaluation shows the examiner that you understand the limits of your own model.

---

## 4. Does the new equation change the verdicts?

**No. The verdicts from the attribution analyses still stand.**

1. **Hormuz: cooperation was a minor reason.** Even giving cooperation the full benefit of the K term, risk still **rose** (+7%), because severity jumped (Δln S = +0.52, the largest single movement in any case). Without the extra cooperation, R would have been 4.02 (Very high) instead of 3.75 (High), so cooperation softened the rise but could not stop it. The process tracing credits Iran's choice to close the strait, trade concentration and the changed US role.
2. **Suez / Red Sea: cooperation was a minor reason, and the K term overstates it.** Under the CCRI, most of the fall comes from K, which is only the model's assumption. In the observed data, severity did not change at all (Δln S = 0) and likelihood fell only a little, mainly because a non-state actor cannot close a canal the way a state can (type of threat).
3. **Malacca: cooperation was a major reason among several.** The fall in likelihood (Δln L = −0.85) is the largest real improvement in any case. The process tracing splits credit between the joint patrols, the 2004 tsunami, the Aceh peace deal and national enforcement. The 2025 → 2026 fall happened with **no change in C at all**, which is consistent with the finding that national (Indonesian) enforcement drove it.

### Overall conclusion supported by both equations

> **Multilateral cooperation reduces the severity and cost of chokepoint disruption at the margin, but it was not the main reason risk changed in any of the three cases. Its effect depends on the type of threat. It worked best against small-scale criminal threats (Malacca piracy), where it supported national enforcement. It worked least against states (Iran in 2026, Egypt in 1967) and armed groups (the Houthis), whose decisions drove both the likelihood and the severity of disruption.**

---

## 5. Sensitivity checks run

| Test | Result | Verdict changes? |
|---|---|---|
| CDRI instead of CCRI | Same direction in every case | No |
| Suez 1967: L = 4 instead of 5 | R₁ = 3.91, ΔR = −0.61 | No |
| Hormuz: drop 2026 freight (no Tanker War equivalent) | S₂ = 4.33, R₂ = 3.70 | No |
| Malacca: Malacca Strait only (not Singapore Strait) | 2025 and 2026 L = 1, R = 1.26 | No; strengthens "fell after cooperation" |
| Count national enforcement as cooperation (Malacca) | Cooperation share 36.8%, 2.3× the next cause | **Yes: Malacca becomes "main reason"**. Discuss this as the strongest counter-argument |

---

## 6. Caveats

- All indicator scores come from the attribution files, which built them from search-result snippets. Check every figure against the original source before you use it; see the provenance grades in `provenance/`.
- The 2026 Hormuz and Red Sea crises are still going on, so duration scores may rise.
- Equal weights are a choice (INFORM default; OECD/JRC 2008). The literature review (§6) gives the full 8-test sensitivity procedure.
