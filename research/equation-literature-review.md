# Choosing the Risk Equation: Literature Review and Recommendation

This review covers the main published risk formulas and recommends the one to use for the EPQ on disruption at Hormuz, Suez/Red Sea and Malacca. It builds on `research/risk-equation.md` (R = L × S on 1–5 scores, plus a cooperation index C and a process-tracing cause table). It keeps all of that work and adds cooperation to the equation itself.

> **Recommended equation: the Cooperation-Adjusted Chokepoint Risk Index (CCRI)**
>
> $$R = \left(L \times S \times K\right)^{1/3}, \qquad K = 5 - \frac{C}{5}$$
>
> L is likelihood (threat), S is severity (consequence), and K is the **lack of coping capacity** left by weak multilateral cooperation. All three are on 1–5, so R is on 1–5 too. The structure is the INFORM Risk Index's (Marin-Ferrer, Vernaccini and Poljansek, 2017). Section 4 gives the full definition.

---

## 1. What the literature says

### 1.1 ISO 31000 and IEC/ISO 31010: likelihood × consequence

- ISO 31000:2018 defines risk as the **"effect of uncertainty on objectives"**. It says risk is usually expressed through risk sources, events, their **consequences** and their **likelihood** (ISO, 2018).
- IEC 31010:2019 is the companion catalogue of assessment techniques. It does not prescribe a single method; the right technique depends on purpose, the data available and the degree of uncertainty (IEC, 2019). The **consequence/likelihood matrix** is one of its semi-quantitative techniques, and the 1–5 × 1–5 grid that the first version used is the common way to apply it.
- Kaplan and Garrick (1981) set out the idea behind all of these. Risk answers three questions: *what can go wrong, how likely is it, and what are the consequences?*

**Relevance:** this is the justification for "Risk = Likelihood × Severity". The standards say nothing about cooperation, so cooperation could only enter indirectly, through lower L or S.

### 1.2 US DHS/RAND: Risk = Threat × Vulnerability × Consequence

- RAMCAP (Risk Analysis and Management for Critical Asset Protection) is the US critical-infrastructure method. It calculates risk as **the product of consequence, vulnerability and threat** in a seven-step process. Later versions also add resilience and countermeasures (CISA, n.d.).
- RAND's *Estimating Terrorism Risk* (Willis et al., 2005) was written for DHS grant allocation. It recommends defining terrorism risk as **expected annual consequences**. Willis (2007) extends the analysis to resource allocation and risk tolerance.
- **Critiques.** Cox (2008b) lists four problems with the T × V × C product: it ignores **correlations** between the components, the risks it produces cannot be added, its scores cannot be used to allocate defences optimally, and T, V and C are subjective. The National Research Council (2010) found the T/V/C breakdown "reasonable" but said that **simple multiplication is not adequate for terrorism**. An intelligent adversary reacts to defences, so threat is not independent of vulnerability.

**Relevance:** this is the main warning for the EPQ. The Houthis and Somali pirates are adversaries that adapt. When cooperation (convoys, patrols) lowers vulnerability, the threat can move elsewhere or escalate. Note this in the evaluation (see the 2024 strikes example in `risk-equation.md` §4b).

### 1.3 INFORM Risk Index (EU Joint Research Centre)

- INFORM has three dimensions: **Hazard & Exposure**, **Vulnerability**, and **Lack of Coping Capacity**. They are designed as a balance: the hazard side (risk *of what*) is set against the vulnerability and coping side (risk *to what*). Hazard-dependent factors go in Hazard & Exposure. Hazard-independent factors are split between Vulnerability (how strong households are) and Lack of Coping Capacity (how strong institutions are) (JRC DRMKC, n.d.; Marin-Ferrer, Vernaccini and Poljansek, 2017).
- The dimensions are combined **multiplicatively, each raised to the power 1/3**, which is a geometric mean. If any dimension is zero, risk is zero. Inside each dimension, categories are also combined by geometric mean with equal weights, and the index runs from 0 to 10 (Marin-Ferrer, Vernaccini and Poljansek, 2017).
- INFORM keeps coping capacity **separate** from vulnerability because it is designed to guide response by international agencies and donors, which are the actors who can change coping capacity (UN SDG brief on INFORM, JRC 2015).

**Relevance:** this is the model to follow. Multilateral cooperation (frameworks, joint operations, information sharing, response speed, enforcement) is **institutional coping capacity** in INFORM's sense. Giving it its own dimension is what lets its effect be measured separately.

### 1.4 UNDRR and IPCC: risk = hazard × exposure × vulnerability

- IPCC AR5 says risk "results from the interaction of … hazards … with the vulnerability and exposure of human and natural systems". Vulnerability covers sensitivity and **lack of capacity to cope and adapt** (IPCC, 2014).
- The UN terminology adopted under the Sendai Framework (UNGA, 2016) treats disaster risk as a function of **hazard, exposure, vulnerability and capacity**. Exposure is what is located in hazard-prone areas, and capacity has its own definition.
- A common teaching version is **Risk = Hazard × Vulnerability ÷ Capacity** (ADRC, n.d.). It puts capacity in the denominator.

**Relevance:** this framing supports treating cooperation as *capacity*. Exposure (how much trade passes through, and whether there is a bypass) is mostly a fixed property of each strait. EIA (2026) and Bailey and Wellesley (2017) supply it.

### 1.5 IMO Formal Safety Assessment (FSA)

- FSA is the IMO's rule-making risk method. It defines risk as the combination of the **frequency** and the **severity** of consequences. The current guidelines are MSC-MEPC.2/Circ.12/Rev.2, which also require incident data to be checked for reliability and its limitations reported (IMO, 2018).
- The original guidelines (IMO, 2002) used a **logarithmic risk matrix**: a Frequency Index (1–7) plus a Severity Index (1–4) gives a Risk Index, **RI = FI + SI**. Because each step on the scales is a factor of ten, adding indices is the same as multiplying frequency by consequence. Societal risk is shown on **FN curves**, with an ALARP ("as low as reasonably practicable") zone between unacceptable and negligible risk.

**Relevance:** FSA shows that adding log-scaled scores is equivalent to multiplying. The same idea gives the log decomposition in section 5. FN curves need casualty and frequency data that do not exist for 1967 or the 1980s, so they are not practical here.

### 1.6 Maritime-security risk models

- **BMP5** (BIMCO et al., 2018) is the industry guide for the Red Sea, Gulf of Aden and Indian Ocean. It requires a **threat assessment** that feeds a ship-level **risk assessment** before transit. That assessment covers flag-state and insurer requirements, cooperation with military forces, armed guards, and the ship's own characteristics. It stresses that threats are dynamic. Its threat-then-vulnerability-then-mitigation order matches T × V.
- **Bayesian network models.** Pristrom et al. (2016), in *Reliability Engineering & System Safety*, estimate the probability of a ship being hijacked off East Africa. They combine ship characteristics, environmental conditions and **security measures in place** using IMO GISIS data and expert judgement. A 2024 paper in *Maritime Policy & Management* (Fan et al., 2024) links a data-driven Bayesian network to TOPSIS to rank anti-piracy strategies by how much they lower piracy likelihood.

**Relevance:** these models confirm that security measures and cooperation act **on likelihood** as well as on coping capacity. They need ship-level data and software, which is beyond EPQ scope. Cite them to show you know the advanced methods, and explain why a composite index fits your data better.

### 1.7 Chokepoint vulnerability indices and data

- **Chatham House** (Bailey and Wellesley, 2017) mapped 14 chokepoints. They estimate that over half of traded grain passes through at least one, and that over 10% depends on a maritime chokepoint **with no viable alternative route**. They group hazards as weather/climate, security/conflict and institutional.
- **IMF PortWatch** (IMF and University of Oxford, 2023) gives **daily transit calls and estimated trade volumes for 28 chokepoints** from satellite AIS ship-tracking data, using the method of Arslanalp, Koepke and Verschuur (2021). The figures are modelled estimates and **start only in 2019**.
- **Verschuur, Lumma and Hall (2025)** estimate about **USD 192 billion** of trade disrupted at chokepoints each year in expectation. They count **delays, rerouting, insurance premiums and higher freight costs** as economic losses, which supports treating freight rates as a *consequence*.
- **EIA (2026)** names Malacca (about 23 million b/d) and Hormuz (about 21 million b/d) as the two most important oil chokepoints. Hormuz has very limited bypass pipelines; Malacca is the easiest to route around.
- War-risk insurance: additional war-risk premiums are quoted as **% of hull and machinery value** and are required in Joint War Committee "listed areas" (Argus Media, n.d.).

### 1.8 Critique of risk matrices (Cox, 2008a)

Cox (2008a) shows that risk matrices have **poor resolution**: very different risks can get the same cell. Their inputs need subjective interpretation, so different users can give **opposite ratings** to the same risks. Matrices should be used "with caution, and only with careful explanations of embedded judgments". IMO FSA has the same weakness: a frequent minor event and a remote catastrophic one can get the same RI.

**Relevance:** R = L × S on 1–5 gives only 14 distinct values between 1 and 25. Values such as 7, 11, 13 and 14 cannot occur at all. Averaging several indicators within each dimension, as here, gives continuous values and reduces the resolution problem. Use R to *compare and rank*, and always show the indicator scores behind it.

### 1.9 Composite-indicator method (OECD/JRC Handbook, 2008)

The Handbook (OECD/JRC, 2008) sets out the construction steps: theoretical framework, data selection, imputation of missing data, **normalisation**, **weighting and aggregation**, and **uncertainty and sensitivity analysis**. Key points:

- **Normalisation** puts indicators on a common scale. Options include min-max, z-scores, and **categorical scales (bands)**. Bands are robust to outliers and rough data but lose detail.
- **Aggregation:** an arithmetic mean is **fully compensatory**, so a low score on one part can cancel a high score on another. A **geometric mean is less compensatory** and always penalises unbalanced profiles (JRC COIN, 2023).
- **Weighting:** equal weights are the most common choice when there is no good reason for anything else. They are still a value judgement, so test them.
- **Sensitivity analysis:** vary the normalisation, weights and aggregation together, and check whether the rankings still hold (Saisana, Saltelli and Tarantola, 2005).

---

## 2. Candidate formulas compared

All candidates use the student's existing 1–5 indicator scores.

| # | Formula | Where it comes from | Pros | Cons |
|---|---|---|---|---|
| **A** | $R = L \times S$ (1–25) | ISO 31000 / IEC 31010 matrix; the current version | Very simple. Widely recognised. Already built. | Cooperation is not in the equation, so its effect can only be argued, not computed. Coarse resolution with gaps (Cox, 2008a). Ordinal scores are multiplied. |
| **B** | $R = T \times V \times C_{\text{onseq}}$ | DHS RAMCAP; RAND (Willis et al., 2005) | Separates threat from vulnerability, which is useful for security threats. Cooperation could lower V. | V has no clean data for 1967 or 1980–88. Ignores how threat and vulnerability affect each other, and an intelligent adversary (Cox, 2008b; NRC, 2010). Cooperation still has no term of its own. Range 1–125 exaggerates differences. |
| **C** | $R = (L \times S \times K)^{1/3}$, $K = 5 - C/5$ | **INFORM** (geometric mean with Lack of Coping Capacity); UNDRR/IPCC "capacity" | Cooperation is its own dimension, so its effect can be isolated exactly with logs or a counterfactual. Uses existing L and S. Stays on the 1–5 scale. Geometric mean is less compensatory (OECD/JRC, 2008). Strong citations. | Assumes cooperation counts as much as threat and severity (equal weights), so this must be tested. Observed L and S already partly reflect cooperation, so the K term measures only the *coping* channel (see §5.3). Needs a cube root. |
| **D** | $R = \dfrac{L \times S}{1 + C/20}$ or $L \times S \times (1 - kC)$ | Teaching formula "H × V ÷ Capacity" (ADRC, n.d.) | Intuitive: more cooperation, less risk. Easy to compute. | The size of the cooperation effect depends on k or on the "1 +", which is arbitrary. Not an established index method. Values are not on the 1–5 scale. Hard to defend to an examiner. |

**Choice: Candidate C.** It is the only candidate that (i) is a published, peer-reviewed index structure in active use (INFORM, used by UN agencies and the EU), (ii) gives cooperation its own term, and (iii) stays compatible with the student's existing L and S scores. With C held constant, it ranks cases in exactly the same order as A (both rise with L × S). Existing results therefore do not change; the new formula adds a cooperation term on top.

---

## 3. Why cooperation counts as "coping capacity"

INFORM's Lack of Coping Capacity covers **institutional** strength: disaster-risk-reduction programmes, governance and the capacity to respond and recover (Marin-Ferrer, Vernaccini and Poljansek, 2017). The five cooperation factors map onto it directly:

| Student's cooperation factor | Coping-capacity role (INFORM / UNDRR language) |
|---|---|
| Formal frameworks | Institutional and governance capacity, before any crisis (preparedness) |
| Joint operations | Capacity to protect exposed assets (response) |
| Information sharing | Early warning |
| Response speed | Emergency response capacity |
| Enforcement of laws | Rule of law and deterrence (institutional) |

---

## 4. Full definition of the recommended equation (CCRI)

### 4.1 Equation

$$
\boxed{R = \left(L \times S \times K\right)^{1/3}} \qquad 1 \le R \le 5
$$

$$
L = \frac{s_{\text{incidents}} + s_{\text{insurance}}}{n_L}, \qquad
S = \frac{s_{\text{trade}} + s_{\text{duration}} + s_{\text{price}} + s_{\text{freight}}}{n_S}, \qquad
K = 5 - \frac{C}{5}
$$

$$
C = c_{\text{frameworks}} + c_{\text{joint ops}} + c_{\text{info}} + c_{\text{speed}} + c_{\text{enforcement}} \qquad (0 \le C \le 20)
$$

### 4.2 Variables mapped to the student's measures

| Dimension | INFORM equivalent | Indicator (student's measure) | Normalisation | Source |
|---|---|---|---|---|
| **L** Likelihood / threat | Hazard | $s_{\text{incidents}}$: attacks, hijackings, robberies or mine strikes per year | Banded 1–5 (rubric in `risk-equation.md` §2) | IMB, ReCAAP, UKMTO |
| | | $s_{\text{insurance}}$: war-risk premium, % of hull value | Banded 1–5 | Insurance press, JWC listed areas |
| **S** Severity / consequence | Exposure × impact | $s_{\text{trade}}$: % fall in transits or tonnage | Banded 1–5 | PortWatch (2019 onward), Suez Canal Authority, EIA |
| | | $s_{\text{duration}}$: length of disruption | Banded 1–5 | Historical sources |
| | | $s_{\text{price}}$: Brent rise, pre-crisis to peak | Banded 1–5 | EIA, IEA |
| | | $s_{\text{freight}}$: freight-rate rise | Banded 1–5 | Drewry, Freightos, Baltic indices |
| **K** Lack of coping capacity | Lack of Coping Capacity | 5 cooperation factors scored 0–4 → C (0–20) | Linear: $K = 5 - C/5$ | Treaties, coalition records, IEA |

**Change from version 1: freight rates move from L to S.** Freight rates are an economic *consequence* of disruption: Verschuur, Lumma and Hall (2025) count higher freight costs as losses. Moving them also deals with limitation 2 in `risk-equation.md`, that likelihood measures react to severity. Insurance stays in L because it is the market's price for the chance of loss. Keeping freight in L is one of the sensitivity tests in §6.

**How K maps C:** C = 0 (no cooperation) gives K = 5 (no coping capacity); C = 20 gives K = 1. K never reaches 0, because even perfect cooperation cannot remove all risk. This also stops R collapsing to zero, a known feature of geometric means (INFORM gives zero risk if any dimension is zero).

### 4.3 Normalisation: why bands, with min-max as a check

- **Primary method: banded 1–5 scores** (categorical scaling in OECD/JRC, 2008). Reasons: (a) historical data is patchy and often approximate, such as "about 7 years" or "37 or 38 attacks", and a band absorbs that uncertainty; (b) the indicators span several orders of magnitude (incidents 0–300+, premiums 0.05%–2%), and bands of roughly doubling width act like a log scale, as the IMO FSA indices do; (c) bands are easy for an examiner to check.
- **Check: min-max scaled to 1–5** across all case-periods: $x' = 1 + 4\,\dfrac{x - x_{\min}}{x_{\max} - x_{\min}}$. Take logs of incidents first, $\ln(1 + \text{incidents})$, so that one extreme year (for example Somalia 2010) does not squash everything else. Use this only for indicators that have numbers in every period.

### 4.4 Weighting and its justification

- **Between dimensions:** equal weights (each exponent 1/3), as in INFORM. There is no agreed basis for ranking threat, consequence and coping capacity above one another. The OECD/JRC Handbook treats equal weighting as the default in that case, provided it is tested.
- **Within dimensions:** a simple average of whichever indicators exist ($n_L$, $n_S$). This lets a period with missing data still be scored without inventing values. Record every missing indicator as a limitation.
- **Within C:** equal 0–4 scores for the five factors, so every factor carries the same weight.
- **Aggregation:** arithmetic averaging *within* a dimension is fine, because the indicators measure the same thing and can substitute for each other. Geometric aggregation *between* dimensions means strong cooperation cannot fully cancel a severe threat (JRC COIN, 2023).

### 4.5 Risk bands for R

| R | Band |
|---|---|
| 1.0–1.9 | Low |
| 2.0–2.9 | Moderate |
| 3.0–3.9 | High |
| 4.0–5.0 | Very high |

---

## 5. Isolating the effect of cooperation

### 5.1 Counterfactual method

Compute risk in the later period as if cooperation had stayed at its earlier level:

$$
R_{\text{cf}} = \left(L_2 \times S_2 \times K_1\right)^{1/3}
\qquad
\text{Direct cooperation effect} = R_2 - R_{\text{cf}}
$$

A negative value means cooperation lowered risk.

### 5.2 Exact log decomposition (no leftover term)

Because R is a geometric mean, taking natural logs turns the product into a sum:

$$
\ln R = \tfrac{1}{3}\left(\ln L + \ln S + \ln K\right)
\;\Rightarrow\;
\Delta \ln R = \tfrac{1}{3}\left(\Delta\ln L + \Delta\ln S + \Delta\ln K\right)
$$

$$
\text{Share}_K = \frac{\Delta \ln K}{\Delta\ln L + \Delta\ln S + \Delta\ln K}
$$

The same applies to L and S. The shares add up to exactly 100%, and the result agrees with §5.1, because $R_2 / R_{\text{cf}} = (K_2/K_1)^{1/3}$. This is the same "adding logs = multiplying" idea as the IMO FSA risk index. (Shares are only meaningful when all three components move in the same direction. If they move in opposite directions, report each Δln separately.)

### 5.3 Direct and indirect channels: link to process tracing

Observed L and S **already include some of cooperation's effect**. Convoys reduce incidents, which lowers L, and coordinated stock releases cap price rises, which lowers S. Share_K measures only the **direct (coping) channel**. To get the **total** contribution of cooperation:

$$
\text{Total cooperation share} = \text{Share}_K + p_L \cdot \text{Share}_L + p_S \cdot \text{Share}_S
$$

Here $p_L$ and $p_S$ are the shares of the change in L and S that the **process-tracing cause table** (`risk-equation.md` §4) attributes to cooperation. This joins the equation and the qualitative method into one result, and it answers the NRC (2010) point that threat and defences interact.

### 5.4 Worked example (ILLUSTRATIVE NUMBERS ONLY: not real data for any strait)

| | Period 1 (illustrative) | Period 2 (illustrative) |
|---|---|---|
| $s_{\text{incidents}}$ | 4 | 2 |
| $s_{\text{insurance}}$ | 3 | 2 |
| **L** | (4+3)/2 = **3.50** | (2+2)/2 = **2.00** |
| $s_{\text{trade}}$ | 3 | 2 |
| $s_{\text{duration}}$ | 4 | 2 |
| $s_{\text{price}}$ | 2 | 1 |
| $s_{\text{freight}}$ | 3 | 2 |
| **S** | 12/4 = **3.00** | 7/4 = **1.75** |
| **C** (0–20) | 6 | 13 |
| **K = 5 − C/5** | **3.80** | **2.40** |
| **R = (L·S·K)^(1/3)** | (3.5 × 3.0 × 3.8)^(1/3) = 39.9^(1/3) = **3.42 (High)** | (2.0 × 1.75 × 2.4)^(1/3) = 8.4^(1/3) = **2.03 (Moderate)** |
| *Old R = L × S, for comparison* | *10.5* | *3.5* |

- **Total change:** ΔR = 2.03 − 3.42 = **−1.39** (−41%).
- **Counterfactual:** $R_{\text{cf}} = (2.0 \times 1.75 \times 3.8)^{1/3} = 13.3^{1/3} = 2.37$. Direct cooperation effect = 2.03 − 2.37 = **−0.34**. Without the rise in cooperation, R would have been 2.37 rather than 2.03.
- **Log decomposition:** Δln L = ln(2.0/3.5) = −0.560; Δln S = ln(1.75/3.0) = −0.539; Δln K = ln(2.4/3.8) = −0.460; sum = −1.558. Shares: **L 36%, S 35%, K (cooperation, direct) 29%**.
- **Adding process tracing** (illustrative): if the cause table credits cooperation with $p_L$ = 50% of the fall in L (for example joint patrols) and $p_S$ = 20% of the fall in S, then the total cooperation share = 29% + 0.5 × 36% + 0.2 × 35% = **54%**. Under the decision rule in `risk-equation.md` §4a, compare this with the shares of the other causes.

---

## 6. Sensitivity-test procedure

Following OECD/JRC (2008) and Saisana, Saltelli and Tarantola (2005), recompute R₁, R₂, ΔR and the total cooperation share under each variant. Record the results in one table.

| Test | Variant | Illustrative result (example above) |
|---|---|---|
| 1. Weights | Double each dimension in turn: exponents (½, ¼, ¼), (¼, ½, ¼), (¼, ¼, ½) | Share_K = 22%, 22%, 46%; R still falls from High to Moderate |
| 2. Aggregation | Arithmetic mean (L + S + K)/3 in place of the geometric mean | R: 3.43 → 2.05; R_cf 2.52 |
| 3. Freight placement | Freight back in L (as in version 1) | R: 3.36 → 2.00; R_cf 2.33 |
| 4. Normalisation | Min-max (log incidents) in place of bands, where every period has numeric data | Fill in from your data |
| 5. Disputed data | Score both values where sources disagree (for example 37 vs 38 attacks), and shift any borderline score up or down one band | Report the range of R |
| 6. Leave one out | Drop each indicator in turn (matches the $n<3$ situation for 1967 and the 1980s) | Fill in |
| 7. Peak vs average | Use yearly averages in place of peak values | Fill in |
| 8. K mapping | $K = 5 - C/5$ against $K = 1 + 4(1 - C/20)^2$ (diminishing returns to cooperation) | Fill in |

**Decision rule.** A conclusion is **robust** if it holds in at least 6 of the 8 tests. That covers the sign of ΔR, the order of the three chokepoints, and whether cooperation has the largest share. If test 1 (weighting K at ½) changes the answer, say so clearly: it means the conclusion depends on how much weight you give cooperation.

---

## 7. Limitations to state in the evaluation

1. **Ordinal arithmetic.** Banded scores are not true measurements. R is for ranking and comparing, not an exact quantity (Cox, 2008a).
2. **Intelligent adversaries.** Threat reacts to defences, so L and K are not independent (Cox, 2008b; NRC, 2010). The 2024 Red Sea strikes are an example.
3. **Equal weighting is a value judgement.** Test 1 in §6 checks it.
4. **Double counting.** Cooperation also acts through L and S. §5.3 deals with this; don't add the K effect to an L-based effect that the cause table already attributes to cooperation.
5. **Data gaps.** PortWatch data starts in 2019 and IMO GISIS data is not consistent before the 1990s, so fewer indicators are available for the historical periods.
6. **Exposure is held fixed.** Each strait's structural exposure (EIA oil volumes, bypass options) is the same in both periods, so it cancels out in comparisons within one strait. For comparisons *between* straits, mention it qualitatively, or add an optional exposure score to S.

---

## 8. References (Harvard)

ADRC (Asian Disaster Reduction Center) (n.d.) *Chapter 2, Section 2.1* [PDF]. Available at: https://www.adrc.asia/publications/LWR/LWR_pdf/Chapter%202%20Section%202_1.pdf (Accessed: 20 October 2026).

Argus Media (n.d.) *Explainer: war risk insurance and AWRP*. Available at: https://www.argusmedia.com/en/news-and-insights/latest-market-news/2795769-explainer-war-risk-insurance-and-awrp (Accessed: 20 October 2026).

Arslanalp, S., Koepke, R. and Verschuur, J. (2021) *Tracking Trade from Space: An Application to Pacific Island Countries*. IMF Working Paper WP/21/225. Washington, DC: International Monetary Fund.

Bailey, R. and Wellesley, L. (2017) *Chokepoints and Vulnerabilities in Global Food Trade*. Chatham House Report. London: Royal Institute of International Affairs. Available at: https://www.chathamhouse.org/about-us/our-departments-and-programmes/environment-and-society-centre/chokepoints-and (Accessed: 20 October 2026).

BIMCO, ICS, IGP&I Clubs, INTERTANKO and OCIMF (2018) *BMP5: Best Management Practices to Deter Piracy and Enhance Maritime Security in the Red Sea, Gulf of Aden, Indian Ocean and Arabian Sea*. Edinburgh: Witherby Publishing Group. Available at: https://wwwcdn.imo.org/localresources/en/OurWork/Security/Documents/BMP5%20small.pdf (Accessed: 20 October 2026).

CISA (Cybersecurity and Infrastructure Security Agency) (n.d.) *Risk Analysis and Management for Critical Asset Protection (RAMCAP)*. Available at: https://www.cisa.gov/mts-resilience-resources/risk-analysis-and-management-critical-asset-protection-ramcap (Accessed: 20 October 2026).

Cox, L.A. (2008a) 'What's wrong with risk matrices?', *Risk Analysis*, 28(2), pp. 497–512. doi:10.1111/j.1539-6924.2008.01030.x.

Cox, L.A. (2008b) 'Some limitations of "Risk = Threat × Vulnerability × Consequence" for risk analysis of terrorist attacks', *Risk Analysis*, 28(6), pp. 1749–1761.

EIA (U.S. Energy Information Administration) (2026) *World Oil Transit Chokepoints*. Last updated 3 March 2026. Available at: https://www.eia.gov/international/content/analysis/special_topics/World_Oil_Transit_Chokepoints (Accessed: 20 October 2026).

Fan, H., Lu, J., Chang, Z. and Ji, Y. (2024) [Bayesian network-based TOPSIS framework for dynamic control of maritime piracy risk], *Maritime Policy & Management*, 51(7), pp. 1582–1601. Available at: https://ideas.repec.org/a/taf/marpmg/v51y2024i7p1582-1601.html (Accessed: 20 October 2026). *Note: the search confirmed the authors, journal, volume, pages and subject; copy the exact article title and authors' initials from the RePEc page before submitting.*

George, A.L. and Bennett, A. (2005) *Case Studies and Theory Development in the Social Sciences*. Cambridge, MA: MIT Press. *(Carried over from `risk-equation.md`; not re-checked in this review.)*

IEC (International Electrotechnical Commission) (2019) *IEC 31010:2019 Risk management — Risk assessment techniques*. 2nd edn. Geneva: IEC.

IMF and University of Oxford (2023) *PortWatch* [online platform]. Described in: Environmental Change Institute, University of Oxford (2023) *IMF and University of Oxford launch PortWatch platform to monitor and simulate trade disruptions*. Available at: https://www.eci.ox.ac.uk/news/imf-and-university-oxford-launch-portwatch-platform-monitor-and-simulate-trade-disruptions (Accessed: 20 October 2026).

IMO (International Maritime Organization) (2002) *Guidelines for Formal Safety Assessment (FSA) for use in the IMO rule-making process*. MSC/Circ.1023–MEPC/Circ.392. London: IMO.

IMO (International Maritime Organization) (2018) *Revised Guidelines for Formal Safety Assessment (FSA) for use in the IMO rule-making process*. MSC-MEPC.2/Circ.12/Rev.2, 9 April. London: IMO.

IPCC (2014) 'Summary for policymakers', in Field, C.B., Barros, V.R., Dokken, D.J., Mach, K.J., Mastrandrea, M.D. et al. (eds.) *Climate Change 2014: Impacts, Adaptation, and Vulnerability. Part A: Global and Sectoral Aspects. Contribution of Working Group II to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge and New York: Cambridge University Press, pp. 1–32.

ISO (International Organization for Standardization) (2018) *ISO 31000:2018 Risk management — Guidelines*. Geneva: ISO.

JRC COIN (Joint Research Centre Competence Centre on Composite Indicators and Scoreboards) (2023) *Step 6: Aggregation* [training slides]. European Commission. Available at: https://knowledge4policy.ec.europa.eu/sites/default/files/COIN_2023_Step%206.%20Aggregation.pdf (Accessed: 20 October 2026).

JRC DRMKC (Joint Research Centre Disaster Risk Management Knowledge Centre) (n.d.) *INFORM Risk: Methodology*. European Commission. Available at: https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/Methodology (Accessed: 20 October 2026).

Kaplan, S. and Garrick, B.J. (1981) 'On the quantitative definition of risk', *Risk Analysis*, 1(1).

Marin-Ferrer, M., Vernaccini, L. and Poljansek, K. (2017) *Index for Risk Management INFORM: Concept and Methodology, Version 2017*. EUR 28655 EN. Luxembourg: Publications Office of the European Union. doi:10.2760/094023.

National Research Council (2010) *Review of the Department of Homeland Security's Approach to Risk Analysis*. Washington, DC: The National Academies Press. doi:10.17226/12972.

OECD/JRC (Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A. and Giovannini, E.) (2008) *Handbook on Constructing Composite Indicators: Methodology and User Guide*. Paris: OECD Publishing. ISBN 978-92-64-04345-9.

Pristrom, S., Yang, Z., Wang, J. and Yan, X. (2016) 'A novel flexible model for piracy and robbery assessment of merchant ship operations', *Reliability Engineering & System Safety*, 155, pp. 196–211.

Saisana, M., Saltelli, A. and Tarantola, S. (2005) 'Uncertainty and sensitivity analysis techniques as tools for the quality assessment of composite indicators', *Journal of the Royal Statistical Society: Series A*, 168(2), pp. 307–323. doi:10.1111/j.1467-985X.2005.00350.x.

UNGA (United Nations General Assembly) (2016) *Report of the open-ended intergovernmental expert working group on indicators and terminology relating to disaster risk reduction*. A/71/644, 1 December. New York: United Nations.

Verschuur, J., Lumma, J. and Hall, J.W. (2025) 'Systemic impacts of disruptions at maritime chokepoints', *Nature Communications*, 16, 10421. doi:10.1038/s41467-025-65403-w.

Willis, H.H. (2007) 'Guiding resource allocations based on terrorism risk', *Risk Analysis*, 27(3), pp. 597–606. doi:10.1111/j.1539-6924.2007.00909.x.

Willis, H.H., Morral, A.R., Kelly, T.K. and Medby, J.J. (2005) *Estimating Terrorism Risk*. MG-388. Santa Monica, CA: RAND Corporation. doi:10.7249/MG388.

### Notes on verification

- Every reference above appeared in web-search results during this review (October 2026), except George and Bennett (2005), which was carried over from the existing file.
- Search results confirmed bibliographic details and abstract-level content, not always the full text. Two points are attributed with care:
  - The T × V × C product is attributed to RAMCAP (CISA), the NRC (2010) and Cox (2008b). The search confirmed only that Willis et al. (2005) define risk as expected annual consequences.
  - The FI + SI risk-index matrix is attributed to the 2002 IMO guidelines on the basis of secondary sources.
- Before final submission, check page numbers and exact titles against the originals. This applies especially to Fan et al. (2024) and to the page range of Kaplan and Garrick (1981).
