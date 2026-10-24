# A3: Attribution test for the Strait of Malacca (and Singapore Strait)

**Question:** Was multilateral cooperation the MAIN reason risk changed in the Strait of Malacca between the 1999–2005 piracy peak, the fall after 2006, and 2025–26?

**Method:** the Chokepoint Disruption Risk Index in `research/risk-equation.md`: R = L × S, the cooperation index C (0–20) and the Cause Contribution Score with its decision rule.
**Prepared:** 20 October 2026. The data comes from the research files 02, 03, 05, 06, 07, 08, 09, 10, 11 and 15 in this folder, plus 18 targeted web searches. Page fetching was blocked, so web figures were checked only against search-result text. Before you quote a figure, open the page yourself.

---

## 0. Short answer

- **Risk was Low in every snapshot.** Severity scores the minimum of 1 every time: transits *rose* through the whole period and almost all incidents were theft, not attacks that stopped trade. So every change in R comes from likelihood alone.
- **R values:** peak (2000–05) **3.5** → 2008 **1.5** → 2025 **2.5** → 2026 (Jan–Sep) **2.0**. All of these sit in the "Low" band (1–4).
- **Peak to 2008 (ΔR = −2.0, −57%):** the Malacca Strait Patrols and Eyes in the Sky get the largest share (15.8%), **tied with the 2004 tsunami**. Grouping the two multilateral strands together gives 23.7%, which is exactly 1.50 times the tsunami's share. That passes the "main reason" test only on a knife-edge, and it fails if any single score moves by one point. **Verdict: a major reason among several, not the main reason.**
- **2025 to 2026 (ΔR = −0.5):** the largest single cause is **Indonesia's own national police enforcement (36.4%)**, which is not multilateral. Information sharing through ReCAAP, the IMB and ships' CCTV enabled it (27.3%). **Verdict: multilateral cooperation was a major reason among several, working as an enabler.**
- **The awkward fact for the cooperation argument:** the cooperation index was at its *highest* (C = 15) in 2025, the same year the straits recorded the most incidents since ReCAAP records began in 2007.

---

## 1. Data tables for each snapshot

### 1a. A data problem to settle first: which waters, and whose count?

- **IMB vs ReCAAP.** The two bodies count incidents differently. For 2025, for example, the IMB counts 80 in the "Singapore Straits" and ReCAAP counts 108 in the "Straits of Malacca and Singapore" (SOMS) (file 06, items 28–29). Do not put both in one chart. ReCAAP data only starts in 2007, so the peak has to use IMB figures.
- **Malacca Strait proper vs the combined straits.** The 2000–05 peak happened in the Malacca Strait itself, mostly in Indonesian waters (IMB 2003, via Al Jazeera). The 2025 surge happened almost entirely in the **Singapore Strait**: 107 of ReCAAP's 108 incidents, with **1** in the Malacca Strait proper (ReCAAP 2025 annual report, file 06 item 28). The main calculation below uses the **combined shipping route**, because that is the chokepoint ships actually pass through. A "Malacca Strait proper" version is given as a sensitivity test.
- **Disputed figures.** The IMB count for 2004 is given as 37 or 38. Both score 3, so the difference does not matter. One search summary claimed "79 in 2005 to 50 in 2006" for Malacca. Those are actually the IMB's **Indonesia** totals (the ICC release gives Indonesia 94→79 for 2004→05), so **do not use them for Malacca**. The figure of 58 for 2001 that circulates online **could not be verified**, so it is not used.

### 1b. IMB yearly Malacca Strait series (what could be verified)

| Year | Malacca Strait attacks (IMB) | Source |
|---|---|---|
| 1999 | 2 | ICC/IMB press release on the 2000 report: https://iccwbo.org/news-publications/news/piracy-attacks-rise-to-alarming-new-levels-icc-report-reveals/ |
| 2000 | **75** | same |
| 2001 | not verified | no source seen |
| 2002 | 16 | Al Jazeera (2003), quoting IMB: https://www.aljazeera.com/archive/2003/10/200849142236338398.html |
| 2003 | 28 ("almost all in Indonesian waters") | same |
| 2004 | 37 or 38 | NUS/Beckman slides (37); IMB via AFP and Gulf News (38): https://gulfnews.com/business/piracy-declines-sharply-in-malacca-straits-1.224149 |
| 2005 | 12 (one other report says 18) | ICC/IMB release "Iraq declared new piracy hotspot" (Jan 2006): https://iccwbo.org/news-publications/news/iraq-declared-new-piracy-hotspot/ |
| 2006 | 11 | file 02 (IMB via MINDEF/NPR). H1 2006: 3, against 8 in H1 2005: https://iccwbo.org/news-publications/news/decline-in-piracy-attacks-slows-down-says-imb/ |
| 2007 | 7 (3 actual, 4 attempted) | IMB via ProQuest article (search snippet) |
| 2008 | **2** (Malacca); about 8 for Malacca and Singapore combined | IMB 2008 annual report: https://iccwbo.org/news-publications/news/imb-reports-unprecedented-rise-in-maritime-hijackings/ ; combined figure from RSIS: https://rsis.edu.sg/rsis-publication/idss/1176-piracy-in-the-south-china-sea |
| 2009–10 | not verified for Malacca proper | Antara (file 15, I15) gives a trend of 38 (2004) to 0 (2011) |

**Very important for causation:** the biggest fall, from **75 in 2000 to 16 in 2002 (−79%)**, happened **before any multilateral patrol existed**. MALSINDO began in July 2004.

### 1c. Traffic (for the trade-reduction indicator)

| Year | Ships reporting to the Malacca Strait traffic system (Marine Dept Malaysia) | Source |
|---|---|---|
| 1999 | 43,965 | IALA wiki table: https://www.iala.int/wiki/iwrap/index.php/Malacca_Strait_Traffic_Volume_and_Incident_Rates |
| 2000 | 55,957 | same |
| 2004 | 63,636 | same |
| 2008 | no total found; container-ship transits hit an all-time high of 26,359 | Nippon Maritime Center via search snippet |
| 2024 | about 94,300 (ships over 300 gt; a different series) | Seatrade Maritime: https://www.seatrade-maritime.com/tankers/malacca-strait-vessel-traffic-at-record-levels-in-2025 |
| 2025 | **102,525**, a record | same |

The 1999–2007 and 2024–25 series measure slightly different things, so do not compare their levels directly. **Both rise.** Piracy never reduced traffic.

### 1d. Snapshot A: the peak (period 2000–05, using peak values as the method says)

| Indicator | Raw value | Source (URL) | Score |
|---|---|---|---|
| Incidents (peak year, 2000) | 75 attacks in the Malacca Strait (IMB) | https://iccwbo.org/news-publications/news/piracy-attacks-rise-to-alarming-new-levels-icc-report-reveals/ | **4** (51–150) |
| War-risk premium (peak, mid-2005) | Lloyd's JWC listed the strait in June 2005. Premiums "nearly 0.4% of hull and machinery value", about US$150,000 per port call (Maritime Executive). Other reports say "1% of *cargo* value", and RSIS cites an estimate of about US$5,000 per trip. Ships did **not** stop using the route. | https://maritime-executive.com/article/2005-07-06insurance-rates-for-malacca-strait-tra ; https://rsis.edu.sg/rsis-publication/rsis/769-marine-war-risk-insurance-sho/ | **3** (0.2–0.5% of hull). The JWC "listed" condition for a 5 requires ships to be refusing the route, which did not happen. |
| Freight-rate rise | **No data.** No source shows a piracy-driven freight premium on Malacca routes. | — | left out (n_L = 2) |
| **L** | (4 + 3) / 2 | | **3.5** |
| Trade reduction | **None.** Transits rose from 43,965 (1999) to 55,957 (2000) to 63,636 (2004). | IALA wiki (above) | **1** (<10%) |
| Duration | No closure or sustained slowdown. Each incident delayed one ship for hours. | file 05, 06; IMB | **1** (<1 week) |
| Price rise (Brent) | No oil-price effect can be traced to Malacca piracy. Brent moved for other reasons (the 2003–05 demand boom). | — | **1** |
| **S** | (1 + 1 + 1) / 3 | | **1.0** |
| **R = L × S** | | | **3.5 (Low)** |

*Alternatives:* using **2004 values only** (38 attacks → 3; not yet listed by the JWC → 1) gives L = 2.0 and R = **2.0**. Using **2005 values only** (12 → 2; listed → 3) gives L = 2.5 and R = **2.5**. So the peak R lies between **2.0 and 3.5** depending on the year. The method's peak-values rule gives 3.5.

### 1e. Snapshot B: after cooperation (2008)

| Indicator | Raw value | Source (URL) | Score |
|---|---|---|---|
| Incidents | IMB: 2 in the Malacca Strait; about 8 in Malacca and Singapore combined. Indonesia total: 28, down from 121 in 2003. | https://iccwbo.org/news-publications/news/imb-reports-unprecedented-rise-in-maritime-hijackings/ ; https://rsis.edu.sg/rsis-publication/idss/1176-piracy-in-the-south-china-sea | **2** (combined, 6–20); 1 for Malacca proper |
| War-risk premium | Normal. The JWC delisted the strait from 00:01 BST on 7 Aug 2006 (London P&I Club circular). Ports in north-east Sumatra stayed listed. | https://www.informare.it/news/review/2006/b090806uk.asp ; https://www.londonpandi.com/media/1386/7083.pdf ; https://www.businessinsurance.com/strait-of-malacca-off-high-risk-list/ | **1** |
| Freight | No data | — | left out |
| **L** | (2 + 1) / 2 | | **1.5** (1.0 for Malacca proper) |
| Trade reduction | None. Container transits hit a record of 26,359. | Nippon Maritime Center (search snippet) | **1** |
| Duration | None | — | **1** |
| Price | Brent's 2008 spike was unrelated to Malacca | — | **1** |
| **S** | | | **1.0** |
| **R** | | | **1.5 (Low)** (1.0 for Malacca proper) |

### 1f. Snapshot C: now (2025 peak year, and the 2026 fall)

| Indicator | Raw value | Source (URL) | Score |
|---|---|---|---|
| Incidents, 2025 | ReCAAP: **108** in SOMS (+74% on 62 in 2024), the highest since 2007. 107 were in the Singapore Strait and 1 in the Malacca Strait. None were CAT 1 (most serious) and 53% were CAT 4 (petty theft). IMB: 80 in the "Singapore Straits". | https://www.recaap.org/resources/ck/files/news/2026/Press%20release%20-%20ReCAAP%20ISC%20annual%20report%20(2025)%20-FINAL.pdf ; https://iccwbo.org/news-publications/report/global-maritime-piracy-and-armed-robbery-increased-in-2025/ | **4** with either count (51–150); 1 for Malacca proper |
| Incidents, 2026 (Jan–Sep) | ReCAAP: 21 in H1 2026 (−74% on 80 in H1 2025); 22 by 14 July; **23** by end of September (22 in the Singapore Strait, 1 in the Malacca Strait). Annualised, that is about 31. IMB Q1 2026: 8 in the Singapore Straits, against 31 in Q1 2025. | https://www.recaap.org/resources/ck/files/reports/half-year/ReCAAP%20ISC%20Half%20Yearly%20Report%202026.pdf ; https://safety4sea.com/recaap-isc-q3-58-drop-in-asian-piracy-and-armed-robbery-incidents/ ; https://maritime-executive.com/article/piracy-falls-to-lowest-levels-in-35-years-during-first-quarter-of-2026 | **3** (21–50) |
| War-risk premium | Not on the JWC Listed Areas. The 2026 JWC changes (JWLA-033) cover the Gulf and Red Sea only. No source reports a Malacca or Singapore premium; S&P notes insurance rates are "typically not in public domain". | file 06 item 42; https://www.spglobal.com/platts/en/market-insights/latest-news/shipping/011821-asia-piracy-incidents-hit-5-year-high-in-2020-shipping-insurance-rates-firm | **1** |
| Freight | No piracy-driven freight data. Asia–Europe rates in 2024–26 were driven by the Red Sea and Hormuz, not by Malacca crime, so they are not counted. | — | left out |
| **L (2025)** | (4 + 1) / 2 | | **2.5** |
| **L (2026)** | (3 + 1) / 2 | | **2.0** |
| Trade reduction | None. Transits hit a record of 102,525 in 2025 (+8.7%). ReCAAP says the rise "does not indicate a corresponding increase in threat to maritime trade". Oil flows fell in Q2 2026 (23.2 → 16.6 mb/d), but because Hormuz was closed, not because of crime. | Seatrade (above); file 15 M19, I20 | **1** |
| Duration | No disruption to traffic | — | **1** |
| Price | Brent rose sharply in 2026 because of Hormuz, not Malacca | — | **1** |
| **S** | | | **1.0** |
| **R (2025)** | | | **2.5 (Low)** |
| **R (2026)** | | | **2.0 (Low)** |

### 1g. Summary of R and ΔR

| | Peak (2000–05) | 2008 | 2025 | 2026 (Jan–Sep) |
|---|---|---|---|---|
| Incidents score | 4 | 2 | 4 | 3 |
| Insurance score | 3 | 1 | 1 | 1 |
| Freight | n/a | n/a | n/a | n/a |
| **L** | **3.5** | **1.5** | **2.5** | **2.0** |
| Trade / Duration / Price | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 1 / 1 |
| **S** | **1.0** | **1.0** | **1.0** | **1.0** |
| **R** | **3.5** | **1.5** | **2.5** | **2.0** |
| Band | Low | Low | Low | Low |
| **C** (section 2) | 6 (2000) / 9 (2005) | 13 | 15 | 15 |

| Change | ΔR | %ΔR |
|---|---|---|
| Peak → 2008 | **−2.0** | −57% |
| 2008 → 2025 | **+1.0** | +67% |
| 2025 → 2026 | **−0.5** | −20% |
| Peak → 2026 | **−1.5** | −43% |

### 1h. Sensitivity tests

1. **Malacca Strait proper only** (no Singapore Strait): R = 3.5 → 1.0 → 1.0 → 1.0. On this measure, the present-day "surge" disappears and the fall since the peak looks complete.
2. **Double weight on incidents:** L = 3.67 / 1.67 / 3.0 / 2.33. This makes 2025 look almost as risky as the peak. The reason is that the rubric counts a theft of engine spares the same as a hijacking (Bateman, RSIS 2014: https://rsis.edu.sg/rsis-publication/idss/piracy-in-southeast-asia-the-current-situation/). A severity-weighted count would fix this, for example using ReCAAP's CAT 1–4 categories: there were no CAT 1 incidents in 2025, while the 2000s had hijackings and kidnappings.
3. **Duration read as "length of the elevated-threat period"** rather than "length of traffic disruption": the peak would score 5 (more than 2 years, 1999–2005) and S would rise to 2.33, so R_peak = 8.2 (Moderate). That reading measures how long the threat lasted, not how badly it disrupted shipping. It is not recommended, but you can mention it in your evaluation.
4. **No snapshot leaves the Low band** under the recommended scoring. The conclusion "Malacca was never a severe disruption" is therefore robust.

---

## 2. Cooperation index C for each snapshot

| Factor | 2000 (peak) | 2005 (peak + first cooperation) | 2008 | 2025–26 |
|---|---|---|---|---|
| Formal frameworks | **1**: UNCLOS only; no regional anti-piracy agreement | **2**: MALSINDO (July 2004) and EiS (Sept 2005) are specific but cover only 3–4 states. ReCAAP was signed in Nov 2004 but not yet in force. | **3**: ReCAAP in force (4 Sept 2006, ISC opened 29 Nov 2006); MSP framework, with Thailand a full member from Sept 2008. But Malaysia and Indonesia are **not** ReCAAP parties. | **3**: ReCAAP has 21 parties (Japan MOFA, Nov 2025), and the MSP continues. Malaysia and Indonesia are still outside ReCAAP, and none of it is binding on enforcement. |
| Joint operations | **1**: states acting separately (IMB 2000: Malaysian police stepped up patrols, yet attacks rose to 75) | **2**: *coordinated*, not joint, patrols. Each navy stays in its own waters, with no cross-border hot pursuit (The Diplomat 2015). EiS flew about 8 sorties a week against an estimated 70 needed, in daytime only (Marine Policy 2026). | **3**: sustained sea and air patrols covering most of the route, but still not continuous or joint | **3**: MSP plus the Indonesia–Malaysia Patkor Malindo patrols (Antara 2025; Koran Jakarta, Sept 2025). Robberies still tripled in the eastbound lane despite this. |
| Information sharing | **2**: the IMB Piracy Reporting Centre in Kuala Lumpur existed, but it is an industry body and gave no state-to-state sharing | **2**: IMB plus the MSP hotline | **3**: ReCAAP ISC gives regular reports and advisories to industry | **4**: real-time ReCAAP alerts (Incident Alert 01/2025, 3 Feb 2025), weekly reports, Singapore's Information Fusion Centre, and ships' CCTV passed to Indonesian police (ReCAAP 2025 press release; MINDEF 13 Oct 2025) |
| Response speed | **1**: no coordinated response for more than 4 years after the 1999–2000 surge | **1**: MALSINDO came about 4.5 years after the 2000 surge. EiS took from Sept to Dec 2005 even to agree its procedures (StrategyPage). | **2**: the mechanisms (hotline, ISC) exist, but there was no test case. Scored on the mechanism's capability. | **2**: the surge began in Q4 2024 (27 incidents, against 7 in Q4 2023). Alerts went out in Feb 2025; the decisive arrests came on 9 July 2025, about 7–9 months later. |
| Enforcement of laws | **1**: rare. The IMB said attacks would not fall "unless Indonesia took serious action". | **2**: national Indonesian operations in 2005, and Malaysia's MMEA (operational 30 Nov 2005). Patchy. | **2**: the evidence on prosecutions is thin. Kontorovich & Art (2010): at most 1.47% of punishable piracies were prosecuted internationally. | **3**: Indonesian Riau Islands police arrested 11 gang members in July 2025, with more arrests in August. Singapore Strait robberies fell from 14 in July to 2 in August and 1 in September (MINDEF). Two or three gangs were still active (Seatrade, Jan 2026). |
| **C (0–20)** | **6** | **9** | **13** | **15** |

**ΔC:** 2000→2008 = **+7**. 2008→2025 = **+2**. **Cooperation rose in both intervals, but risk fell in the first and rose in the second.** That alone shows cooperation cannot be a sufficient explanation of the risk trend.

---

## 3. Cause Contribution tables

Scoring: Change, Timing, Mechanism and Counterfactual, each 0–2, giving a total of 0–8.

### 3a. Main change: peak → 2008 (ΔR = −2.0)

| Cause | Multi-lateral? | Change | Timing | Mechanism | Counterfactual | **Total** | **Share** | Sign |
|---|---|---|---|---|---|---|---|---|
| MSP / MALSINDO sea patrols + Eyes in the Sky | Yes | 2 | 1 | 2 | 1 | **6** | **15.8%** | − (lowers risk) |
| ReCAAP information sharing | Yes | 2 | 0 | 1 | 0 | **3** | **7.9%** | − |
| Coastal-state national enforcement (Indonesian navy/police, Malaysia's MMEA) | **No** | 2 | 1 | 1 | 1 | **5** | **13.2%** | − |
| 2004 tsunami | No | 2 | 2 | 1 | 1 | **6** | **15.8%** | − |
| 2005 Aceh peace deal (Helsinki MoU) | No | 2 | 1 | 1 | 1 | **5** | **13.2%** | − |
| Indonesia's economy / poverty | No | 1 | 2 | 1 | 1 | **5** | **13.2%** | − |
| Lloyd's JWC listing (market pressure) | No (private market) | 2 | 1 | 1 | 1 | **5** | **13.2%** | ± (raised L in 2005, then pushed states to act) |
| Technology (AIS, ISPS Code July 2004, ship security) | No (IMO rules) | 2 | 1 | 0 | 0 | **3** | **7.9%** | − (weak) |
| Connected crises (Red Sea 2024–25) | — | 0 | 0 | 0 | 0 | **0** | **0%** | not relevant to this interval |
| **Sum** | | | | | | **38** | **100%** | |

**Evidence for each score**

- **MSP/MALSINDO + EiS.** *Change 2:* from no regional patrols to year-round coordinated patrols (from 20 July 2004; 5–7 ships per navy) and air patrols (from 13 Sept 2005; sources: YaleGlobal, VOA, MINDEF/NAS). *Timing 1:* the patrols came before the 2004→05 fall (38→12) but **after** the 2000→02 fall (75→16). *Mechanism 2:* the JWC delisted the strait after its consultant reviewed the littoral states' measures, including seven EiS sorties a week (Business Insurance, 2006). That is documented evidence on the insurance indicator, which is half of L. On incidents there is only a claim (RMAF in The Star, 2008: "Eye in the Sky shows results"). *Counterfactual 1:* incidents were already falling before the patrols began. On the other hand, the JWC had refused delisting in January 2006 despite lobbying (Business Times, 20 Jan 2006), and acted only after the patrols were assessed. So the patrols were probably decisive for the insurance score but not for incidents. Against this: Marine Policy (2026) says EiS flew about 8 of the 70 sorties needed, in daytime only, while pirates attacked at night.
- **ReCAAP.** *Change 2:* a new treaty, with its Information Sharing Centre opened on 29 Nov 2006. *Timing 0:* by then the strait was already down to 11–12 attacks a year and had been delisted (Aug 2006). *Mechanism 1:* the Hostis humani generis paper (2023) credits information sharing for a fall of about 75%, but gives no Malacca-specific causal data. *Counterfactual 0:* most of the risk had already fallen.
- **National enforcement.** *Change 2:* Indonesian navy operations in 2005; Malaysia's MMEA started operating on 30 Nov 2005 (Daily Star 2005; Sejarah journal). *Timing 1:* about the same time as the fall. *Mechanism 1:* the IMB director linked the late-2005 drop to Indonesian patrols on its side of the strait (Malaysiakini/Gulf News, file 07 Debate 1b). This is a claim without data. *Counterfactual 1:* almost all attacks were in Indonesian waters (IMB 2003), so Indonesian action was necessary. But Malaysia's 2000 patrols did not stop the 2000 surge.
- **2004 tsunami.** *Change 2:* it devastated Aceh's coast. *Timing 2:* 26 Dec 2004, clearly before the 2005 fall. *Mechanism 1:* the IMB's Noel Choong reported no attacks in the weeks after; "The tsunami seems to have really succeeded where the joint patrols could not" (Al Jazeera, 1 Feb 2005). This is a claim with a few weeks of data. *Counterfactual 1:* the effect was temporary. Attacks and ransom kidnappings resumed by March 2005 (ORF, "The sea muggers are back").
- **Aceh peace deal.** *Change 2:* the conflict ended (Helsinki MoU, 15 Aug 2005). *Timing 1:* the incident fall was largely in H1 2005 (8 in H1 2005, 3 in H1 2006), so the deal explains why incidents *stayed* low rather than why they fell. *Mechanism 1:* GAM was suspected in ransom kidnappings in the northern strait (IMB 2001; owners' belief in 2005), and one report links the fall off Belawan to the deal. The search found **no source that establishes the causal link**. *Counterfactual 1:* partly.
- **Indonesia's economy and poverty.** *Change 1:* poverty went from about 23–24% in 1999 (JICA; SMERU) to about 13% by 2010 (SMERU). The 2004 and 2008 values were **not verified**. *Timing 2:* recovery began in 1999–2000, before the 2000→02 fall in incidents. The surge from 2 to 75 attacks in 1999–2000 directly followed the Asian financial crisis. *Mechanism 1:* argued by CIMSEC ("inherently an economic problem"), but not measured for Malacca. *Counterfactual 1:* weakened by the rise in Indonesian incidents from 15 (2009) to 106 (2013), which happened while the economy was growing.
- **Lloyd's JWC listing.** *Change 2:* listed in June 2005 and delisted on 7 Aug 2006. *Timing 1:* the listing came after MALSINDO and after most of the incident fall, but before EiS (Sept 2005) and the extra patrols. *Mechanism 1:* states reacted angrily and quickly. Malaysian ministers said costs would hit ports and consumers (Malaysiakini 2005; FP, "Lloyd's curse"), and the "cooperation" that followed was partly aimed at getting delisted. *Counterfactual 1:* partly; it sped up EiS. **Caution: circularity.** The premium is both an *indicator* of L and a *cause* here, so do not count it twice in your argument.
- **Technology / ISPS.** *Change 2:* the ISPS Code took effect on 1 July 2004 and AIS was phased in. *Timing 1:* about the same time. *Mechanism 0:* the IMB said its statistics showed "no dramatic decline in attacks" since ISPS took effect (ICC release, 2004–05). *Counterfactual 0.*

**Decision rule, peak → 2008**

- **Strands kept separate (as the brief asks):** MSP/EiS (15.8%) **ties** with the tsunami (15.8%). It is not the largest alone, so → **"a major reason among several."**
- **Both multilateral strands added together:** 9/38 = **23.7%** against the tsunami's 15.8%. The ratio is **1.50**, exactly on the threshold.
  - Lower the MSP Mechanism score to 1 (incident evidence only): 8/37 = 21.6% against 16.2% gives a ratio of **1.33**, so it **fails**.
  - Group the two Aceh shocks together (tsunami plus peace deal, which worked through the same channel of removing pirate and GAM bases): 28.9% > 23.7%, so multilateralism is **not even the largest**.
- **Verdict: a major reason among several.** It reaches "main reason" only under the most favourable aggregation and scoring.

### 3b. Secondary change: 2025 → 2026 (ΔR = −0.5; incidents −74%)

| Cause | Multilateral? | Change | Timing | Mechanism | Counterfactual | **Total** | **Share** |
|---|---|---|---|---|---|---|---|
| MSP / EiS / coordinated patrols | Yes | 1 | 1 | 1 | 0 | **3** | **13.6%** |
| ReCAAP / IMB / IFC information sharing | Yes | 1 | 2 | 2 | 1 | **6** | **27.3%** |
| Coastal-state national enforcement (Indonesian Riau Islands police) | **No** | 2 | 2 | 2 | 2 | **8** | **36.4%** |
| Technology / industry measures (CCTV, watchkeeping, BMP) | No | 1 | 1 | 1 | 1 | **4** | **18.2%** |
| Connected crises (Red Sea 2024–25 traffic; Hormuz 2026 reducing oil flows) | No | 1 | 0 | 0 | 0 | **1** | **4.5%** |
| Indonesia's economy / poverty | No | 0 | 0 | 0 | 0 | **0** | 0% |
| Tsunami / Aceh / JWC | No | 0 | 0 | 0 | 0 | **0** | 0% |
| **Sum** | | | | | | **22** | 100% |

**Evidence**

- **National enforcement:** the Riau Islands water police arrested a gang on 9 July 2025 in the Phillip Channel: 8 at sea and 3 on land. The gang had been active since 2017 and picked ships slowing to 5 knots or less (Maritime Executive; Seatrade). Robberies then fell from 14 in July to 2 in August and 1 in September (MINDEF, 13 Oct 2025). ReCAAP and Singapore's MPA credit the arrests directly. This is direct evidence and a decisive counterfactual.
- **Information sharing:** the patrol was launched after tips from the public and from the IMB (Maritime Executive). ReCAAP says the arrests used CCTV footage supplied by ships (ReCAAP 2025 press release). Alerts had gone out since 3 Feb 2025. This is a real mechanism, but it worked *through* national police.
- **Patrols:** the Singapore and Indonesian navies jointly foiled one robbery attempt (Baird Maritime), and Patkor Malindo continued. But ReCAAP gives the credit to "law enforcement by the littoral states", not to the MSP.
- **Industry measures:** ReCAAP's executive director credits "preventive measures by the shipping industry" alongside enforcement (Splash247, July 2026).
- **Connected crises:** Malay Mail (Aug 2025) reports that analysts linked *part of the 2025 rise* to extra traffic diverted by the Red Sea crisis. This is second-hand, and no other source confirms it. The search found **no source** linking the 2026 fall to the Hormuz-driven drop in oil flows. The timing is also wrong: incidents fell from August 2025, and Hormuz closed in 2026.

**Decision rule, 2025 → 2026:** strands kept separate, national enforcement is the largest (36.4%) and ReCAAP information sharing is second (27.3%). Added together, the multilateral strands reach 40.9%, against 36.4% for national enforcement, a ratio of 1.12. **Verdict: a major reason among several, working as an enabler of national enforcement, not the main reason.**

### 3c. The rise in between (2008 → 2025, ΔR = +1.0)

This interval was not formally scored, because the task did not ask for it. Still, it matters for the argument: **C rose from 13 to 15 while R rose by 67%.** The rise came from opportunistic gangs in the Riau Islands targeting slow ships in the eastbound lane, and possibly from more traffic (+8.7% in 2025). Existing patrols and ReCAAP did not prevent it (Panneerselvam & Ramkumar 2023; Lowy Interpreter 2023). This is the strongest evidence that cooperation *by itself* does not control likelihood. In Mukundan's words for the IMB, the problem returns "when it goes off the agenda".

---

## 4. Verdict and the strongest counter-argument

### Verdict

On this evidence, **multilateral cooperation was not the main reason risk changed in the Strait of Malacca. It was a major reason among several.** First, the index shows that risk was **Low in every snapshot** (R = 3.5 → 1.5 → 2.5 → 2.0). Severity never rose above the minimum, because traffic grew throughout and the incidents were mostly theft. So "risk changed" here really means "likelihood changed", and only modestly. Second, the timing does not fit a cooperation-led story. The steepest fall in attacks (75 → 16, 2000–02) came **before** any multilateral patrol. The 2005 drop coincided with the tsunami, Indonesian national operations and the Aceh peace process. ReCAAP opened only after most of the fall had happened. Third, cooperation's clearest, best-documented effect was on **insurers' view of risk**: the JWC delisted the strait in August 2006 after assessing the patrols. That cut one of the two likelihood indicators from 3 to 1. Fourth, in 2025, with cooperation at its highest level ever (C = 15), the straits saw a record 108 incidents. The 2026 fall was driven mainly by **national** Indonesian policing, supported by shared information. The fair conclusion is that cooperation in Malacca **reinforced and locked in** a fall started by other forces, and **gave national enforcement the information it needed**. It did not cause the fall on its own.

### Strongest counter-argument

The split between "multilateral" and "national" enforcement is **artificial for Malacca**. MALSINDO was designed as *coordinated* patrols in which each navy polices its own waters. So Indonesia patrolling its sector in 2005, or Indonesian police acting on IMB and ReCAAP tips and ships' CCTV in 2025, **is** the cooperative system working as intended. The RMSI row also shows that littoral states would accept no other form. If national enforcement inside the MSP framework is counted as cooperation, the multilateral share for peak → 2008 becomes (6+3+5)/38 = **36.8%**. That is **2.3 times** the tsunami's share, which meets the "main reason" rule. Persistence supports this view. The tsunami's effect was gone by March 2005, yet attacks in the Malacca Strait proper stayed in single figures from 2007 until today (1 in 2025). That looks like a lasting, institutional cause, not a one-off shock. **Rebuttal to use:** the 2000–02 fall happened with no coordination at all. Malaysia's 2000 patrols did not stop the 2000 surge. And the 2025 surge happened inside the same "working" system. So coordination is better described as a **necessary condition for keeping risk low** than as the main cause of the changes.

---

## 5. Limitations specific to this case

1. **Changes in where incidents happen and how they are counted.** The peak happened in the Malacca Strait; the present-day incidents happen in the Singapore Strait. The IMB and ReCAAP count differently.
2. **There is no freight data for any snapshot**, so L rests on only 2 indicators. The insurance figure for 2005 is a trade-press estimate (0.4% of hull), and it conflicts with the RSIS estimate of about US$5,000 per trip.
3. **The incident rubric ignores how serious each incident is.** It counts petty theft the same as a hijacking, which inflates 2025.
4. **Under-reporting.** The IMB says "more than 50 percent of cases normally go unreported" (ICC 2006). Reporting itself may have risen with ReCAAP, which would bias the counts *against* cooperation in the later periods.
5. **Unverified items:** the IMB Malacca figures for 2001 and 2009–10, Indonesian poverty for 2004 and 2008, and the exact date and content of the 2005 London P&I circular (a search snippet dated a circular 7 Aug 2005 saying transit-only voyages needed no declaration from 1 Sept 2005, but file 05 has the 2006 delisting circular 7083; check both).
6. **Process-tracing scores are judgements.** The "main reason" verdict changes depending on how the causes are grouped (section 3a). Report this openly.

---

## 6. Key sources used

1. ICC-IMB (2001) 'Piracy attacks rise to alarming new levels, ICC report reveals' [press release]. https://iccwbo.org/news-publications/news/piracy-attacks-rise-to-alarming-new-levels-icc-report-reveals/ (2000: 75 Malacca attacks; 1999: 2)
2. ICC-IMB (2006) 'Iraq declared new piracy hotspot' [2005 annual report release]. https://iccwbo.org/news-publications/news/iraq-declared-new-piracy-hotspot/ (Malacca 38 → 12; Indonesia 94 → 79)
3. ICC-IMB (2009) 'IMB reports unprecedented rise in maritime hijackings' [2008 annual report]. https://iccwbo.org/news-publications/news/imb-reports-unprecedented-rise-in-maritime-hijackings/ (Malacca 2 in 2008; Indonesia 28)
4. Al Jazeera (2005) 'Piracy disappears in tsunami's wake', 1 Feb. https://www.aljazeera.com/amp/news/2005/2/1/piracy-disappears-in-tsunamis-wake
5. Maritime Executive (2005) insurance rates for Malacca transits, 6 July. https://maritime-executive.com/article/2005-07-06insurance-rates-for-malacca-strait-tra
6. Business Insurance (2006) 'Strait of Malacca off high-risk list'. https://www.businessinsurance.com/strait-of-malacca-off-high-risk-list/ ; London P&I Club circular: https://www.londonpandi.com/media/1386/7083.pdf
7. MINDEF Singapore (2005) 'Launch of Eyes in the Sky' (joint release). https://www.nas.gov.sg/archivesonline/data/pdfdoc/20050913984.htm ; MINDEF (2016) MSP 10 years: https://www.mindef.gov.sg/news-and-events/latest-releases/2016apr21-news-releases-01782/
8. 'Complexities of governance and sovereignty in maritime security' (2026) *Marine Policy*. https://www.sciencedirect.com/science/article/pii/S0308597X26000369 (EiS: about 8 of 70 needed sorties)
9. ReCAAP ISC (2026) Annual Report 2025 press release. https://www.recaap.org/resources/ck/files/news/2026/Press%20release%20-%20ReCAAP%20ISC%20annual%20report%20(2025)%20-FINAL.pdf ; Half-Yearly Report 2026: https://www.recaap.org/resources/ck/files/reports/half-year/ReCAAP%20ISC%20Half%20Yearly%20Report%202026.pdf
10. Safety4Sea (2026) 'ReCAAP ISC Q3: 58% drop…'. https://safety4sea.com/recaap-isc-q3-58-drop-in-asian-piracy-and-armed-robbery-incidents/
11. MINDEF Singapore (2025) 'Reply to media query on increase in piracy in Singapore waters', 13 Oct. https://www.mindef.gov.sg/news-and-events/latest-releases/13oct25-mq/
12. Maritime Executive (2025) 'Indonesian police bust pirate gang in Riau Islands'. https://www.maritime-executive.com/article/indonesian-police-bust-pirate-gang-in-riau-islands ; Seatrade (2026) '2 or 3 ship robbery groups remain active'. https://www.seatrade-maritime.com/security/2-or-3-ship-robbery-groups-remain-active-in-singapore-strait
13. IALA wiki, Malacca Strait traffic volume (Marine Dept Malaysia data). https://www.iala.int/wiki/iwrap/index.php/Malacca_Strait_Traffic_Volume_and_Incident_Rates ; Seatrade (2026) record 102,525 transits: https://www.seatrade-maritime.com/tankers/malacca-strait-vessel-traffic-at-record-levels-in-2025
14. Bateman, S. (2014) 'Piracy in Southeast Asia: the current situation', RSIS. https://rsis.edu.sg/rsis-publication/idss/piracy-in-southeast-asia-the-current-situation/
15. CIMSEC (c.2014) 'It's the economy: exploring Indonesia's piracy problem'. https://cimsec.org/economy-stupid-exploring-indonesias-piracy-problem/ ; SMERU poverty data: https://smeru.or.id/en/node/1147
16. ICC-IMB, 'IMB says security threats remain, despite new safety measures' (ISPS). https://iccwbo.org/news-publications/news/imb-says-security-threats-remain-despite-new-safety-measures/
17. The Diplomat (2015) 'Piracy in the Malacca Strait: can ASEAN respond?'. https://thediplomat.com/2015/07/piracy-in-the-malacca-strait-can-asean-respond/
