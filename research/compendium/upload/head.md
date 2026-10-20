# EPQ Research Compendium: Multilateral Cooperation and Chokepoint Disruption

20 October 2026 · Manuela López-Henares · Live version: https://claude.ai/code/artifact/502ddf95-6214-4efa-8ccf-8c8bfaf06e76

## Headline findings

Multilateral cooperation was not the main reason disruption risk changed in any of the three case studies. It softened severity at the margin, and how well it worked depended on the type of threat.

| Case study | Risk (CCRI, 1–5), earlier → later | Cooperation index (0–20) | Cooperation's share of the change | Verdict |
| --- | --- | --- | --- | --- |
| Strait of Hormuz (Tanker War 1984–88 vs 2026 closure) | 3.49 → 3.75 (rose) | 9 → 12 | 5.7%, the smallest of nine causes | Minor reason |
| Suez / Red Sea (1967–75 closure vs 2023–26 Houthi crisis) | 4.22 → 3.30 (fell) | 5 → 13 | 8.5%, partly negative | Minor reason |
| Strait of Malacca (2000–05 peak vs 2008) | 2.37 → 1.53 (fell) | 6 → 13 | 15.8–23.7% | Major reason among several |

- **Hormuz:** risk rose by 7% even though cooperation increased. Iran's own decision to close the strait, the concentration of about 20 million barrels a day through it, and the change in the US role mattered more. The IEA's 400-million-barrel stock release and the JMIC information centre softened the rise.
- **Suez / Red Sea:** risk fell because a non-state group cannot shut a canal the way Egypt did in 1967, so the type of threat explains most of the change. The January 2024 strikes on the Houthis were followed by a tripling of war-risk premiums, so some cooperation made things worse.
- **Malacca:** the joint patrols tie with the 2004 tsunami as the largest cause of the fall in attacks. The steepest fall (75 to 16 attacks, 2000–02) came before any joint patrol. Cooperation becomes the main reason only if each navy's patrols in its own waters count as cooperation.

**Thesis this evidence supports:** cooperation works best against small-scale criminal threats, where it supports national enforcement. It works least against states (Iran, Egypt) and armed groups (the Houthis), whose decisions drive both likelihood and severity.

## Method

Risk is measured with the Cooperation-Adjusted Chokepoint Risk Index (CCRI), built on the structure of the EU's INFORM Risk Index, and causes are tested with process tracing.

```latex
R = \left(L \times S \times K\right)^{1/3}, \qquad K = 5 - \frac{C}{5}, \qquad 1 \le R \le 5
```

| Term | Meaning | Indicators (each scored 1–5 on fixed bands) |
| --- | --- | --- |
| L | Likelihood of disruption | Incidents per year; war-risk insurance premium (% of hull value) |
| S | Severity of disruption | Fall in transits; length of disruption; Brent price rise; freight-rate rise |
| C | Multilateral cooperation index (0–20) | Formal frameworks, joint operations, information sharing, response speed, enforcement (each 0–4) |
| K | Lack of coping capacity | 5 with no cooperation, falling to 1 at full cooperation |
| R | Risk | 1.0–1.9 Low, 2.0–2.9 Moderate, 3.0–3.9 High, 4.0–5.0 Very high |

**Why this equation:** risk as likelihood × consequence follows ISO 31000. The geometric mean with a coping-capacity term follows INFORM (Marin-Ferrer, Vernaccini and Poljansek, 2017). Banded scores and a sensitivity test follow the OECD/JRC (2008) handbook on composite indicators, and averaging several indicators answers Cox's (2008) critique of plain risk matrices. The simpler version 1, R = L × S on a 1–25 scale, gives the same verdicts.

**Separating cooperation's effect:** the counterfactual keeps the later L and S but uses the earlier K, which shows what risk would have been without the extra cooperation. The K term assumes that cooperation lowers risk, so it gives the best case for cooperation, not proof.

**Testing causes (process tracing):** each possible cause is scored 0–2 on four tests (George and Bennett, 2005): change, timing, mechanism and counterfactual. A cause's share is its score divided by the total. Cooperation is the main reason only if its share is the largest and at least 1.5 times the next.

**Grading sources:** every source has an Admiralty Code grade (NATO AJP-2.1). The letter rates the producer: A completely reliable, B usually reliable, C fairly reliable, D not usually reliable, E unreliable, F cannot be judged. The number rates the content: 1 confirmed, 2 probably true, 3 possibly true, 4 doubtful, 5 improbable, 6 cannot be judged.

## Results

Risk rose at Hormuz and fell at Suez and Malacca. In every case, the counterfactual shows that extra cooperation lowered risk by no more than 0.61 points.

| Case | Earlier R | Later R | Later R if cooperation had not increased |
| --- | --- | --- | --- |
| Hormuz: Tanker War → 2026 | 3.49 | 3.75 | 4.02 |
| Suez/Red Sea: 1967–75 → 2023–26 | 4.22 | 3.30 | 3.91 |
| Malacca: peak 2000–05 → 2008 | 2.37 | 1.53 | 1.79 |
| Malacca: 2025 → 2026 | 1.71 | 1.59 | 1.59 |

| Case and period | L | S | C | K |
| --- | --- | --- | --- | --- |
| Hormuz: Tanker War 1984–88 | 5.00 | 2.67 | 9 | 3.20 |
| Hormuz: 2026 closure | 4.50 | 4.50 | 12 | 2.60 |
| Suez: 1967–75 closure | 5.00 | 3.75 | 5 | 4.00 |
| Red Sea: 2023–26 Houthi crisis | 4.00 | 3.75 | 13 | 2.40 |
| Malacca: peak 2000–05 | 3.50 | 1.00 | 6 | 3.80 |
| Malacca: 2008 | 1.50 | 1.00 | 13 | 2.40 |
| Malacca: 2025 | 2.50 | 1.00 | 15 | 2.00 |
| Malacca: 2026 (Jan–Sep) | 2.00 | 1.00 | 15 | 2.00 |

| Case | Largest causes (share) | Cooperation's share |
| --- | --- | --- |
| Hormuz | Type of threat 15.1%; trade concentration 13.2%; US unilateral role 13.2% | 5.7% |
| Suez / Red Sea | Type of threat 17.0%; connected crises 17.0%; technology 14.9% | 8.5% (sign mixed) |
| Malacca, peak → 2008 | Joint patrols 15.8% = 2004 tsunami 15.8%; national enforcement, Aceh peace, economy, Lloyd's listing 13.2% each | 15.8–23.7% |
| Malacca, 2025 → 2026 | Indonesian police enforcement 36.4%; ReCAAP information sharing 27.3% | 13.6% (patrols) + 27.3% (information) |

| Sensitivity test | Result | Verdict changes? |
| --- | --- | --- |
| Version 1 equation (R = L × S) | Same direction in every case | No |
| Suez 1967 likelihood scored 4 instead of 5 | Risk falls by 0.61 instead of 0.92 | No |
| Drop the 2026 Hormuz freight score | Later risk 3.70 instead of 3.75 | No |
| Malacca Strait alone, without the Singapore Strait | 2025 and 2026 risk 1.26 | No |
| Count national patrols as cooperation at Malacca | Cooperation share 36.8%, 2.3 times the next cause | **Yes** |

