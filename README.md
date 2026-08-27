# Jacob VonTersch 🍊

Data and product at **Professional Ag Marketing**. I build the pipelines, models, and dashboards behind commodity marketing decisions, mostly hogs and grain, where the output is somebody's actual position.

Syracuse iSchool grad, Syracuse Men's Hockey, Luverne MN.

---

## What I'm building

**One data library instead of fifteen spreadsheets.** Pro Ag ran on hand-updated Excel files: one person, one workbook, one commodity, refreshed by hand every week. We replaced that with a real platform. Roughly 20 ingest connectors pull USDA (FAS, AMS/MARS, NASS, PSD), EIA, CME, and Barchart into a single Postgres schema, and a Next.js app renders it live. Crush margins, balance sheets, export commitments, harvest and production, cold storage, cutouts, basis, feeder cattle. Some series backfilled 26 years deep.

**The point isn't the charts, it's what becomes visible.** When every commodity lives in its own workbook, nobody can ask a question that crosses two of them. Once it's all in one schema with consistent dates and units, questions that used to be a two-day research project become a page you open. That's the whole thesis: bring everyone's data together, then see the things you couldn't see.

**Verify against the real report, every time.** Every connector gets checked figure-by-figure against the actual USDA release or the legacy spreadsheet before it ships. That habit has caught real bugs on every source where it got skipped: marketing-year boundary errors, silent release substitutions, a government-shutdown gap masquerading as clean data.

**Fill in what the public data doesn't give you.** The official CME Lean Hog index posts about two days late, so the basis chart was always stale at the tip. I reverse-engineered the index formula from USDA's daily mandatory price reports and reconstructed a provisional value for the missing days. **Mean absolute deviation of $0.0025 against the real index across 95 days.** Never stale again.

**Building the team.** Writing the job description, running the hiring process, and setting the conventions we build on: STATUS-first repos, branch and PR, docs that ship with the change instead of after it.

**Next up.** A forward-looking, packer-grid-aware marketing decision layer for hog producers, which is the piece nobody in that market actually ships. And a contract-position system replacing a twenty-year-old Access database for a grain operation.

Most of this is private. The ideas backlog is considerably longer than my available weekends.

---

## The home run model 🔒

Private repo, private edge. The numbers are fair game.

| | |
|---|---|
| **Architecture** | XGBoost + regularized logistic blend, Platt-calibrated per side |
| **Features** | 134 engineered, from Statcast 2023-2026 plus weather, park, and market data |
| **Discrimination** | AUC **0.616**, Brier **0.101**, logLoss **0.352** |
| **Top-tier lift** | **27.1%** hit rate vs. base rate, a **2.13x lift** |
| **Second tier** | **20.4%** hit rate, **1.61x lift** |
| **Validation** | 124-day forward holdout, **26,270** predictions. No peeking backwards. |
| **Track record** | **1,400+** scored predictions in a version-stamped ledger |
| **Delivery** | 13-page research terminal. FastAPI + Next.js 16, Cloudflare R2 data bridge, always on. |

The part I'm proudest of isn't the lift, it's the audit. I spent two weeks making my own dashboard report worse numbers about itself. Every figure now carries the model version it came from, stale metrics render an empty state instead of a chart, and a headline ROI stat got demoted the moment I traced that only 7 of its 102 picks came from the current model.

A model that flatters you is a model that's lying to you. Mine isn't allowed to.

---

## Featured public work

| Project | What it does | Tech |
|---|---|---|
| [Ag Market Predictor](https://github.com/Tersch23/ag-market-predictor) | Cross-market commodity forecasting with an XGBoost engine and offline local-LLM market briefings | Python, XGBoost, Streamlit, Llama.cpp |
| [MLB WAR-162 Forecast](https://github.com/Tersch23/mlb-war162-forecast) | Next-season WAR/162 from prior-season data, leakage-controlled Random Forest at scale | PySpark, MLlib |
| [NFL Leverage Report](https://github.com/Tersch23/NFL-Leverage-Report) | Roster-value opportunities from situational EPA vs. league average | Python, nflverse, Matplotlib |
| [2025 Playoffs Statcast](https://github.com/Tersch23/mlb-2025-playoffs-statcast) | What separates elite postseason hitters, by quality of contact | R, ggplot2 |
| [NCAA Hoops Dashboard](https://github.com/Tersch23/NCAA-Basketball-Dashboard) | Shot charts, team comparisons, conference standings across the Big 4 | Python, Streamlit, Plotly |
| [Orange Hoops Challenge](https://github.com/Tersch23/Orange_Hoops_Challenge) | Clutch-shot success model, 85% accuracy across 211K shots | Python, scikit-learn, R |

---

## Stack

**Languages** Python · TypeScript · SQL · R · PySpark

**Data** Postgres/Neon · Pandas · NumPy · Parquet · REST + scraped report ingestion · USDA, EIA, CME, Barchart, Statcast

**ML** scikit-learn · XGBoost · calibration and time-series CV · feature engineering · honest backtesting

**Ship** Next.js · React · FastAPI · Streamlit · Plotly · Tailwind · Railway · Vercel · Cloudflare R2 · Git/GitHub

**AI** Claude Code daily driver · agentic workflows · prompt engineering · local LLMs (Llama 3 via llama.cpp)

---

## How I work

- **Ship it, then be honest about it.** Every repo has a STATUS.md that says what's actually true today, including what's broken.
- **A number without provenance is a rumor.** Version-stamp everything.
- **Domain first.** The best feature I've ever engineered came from a producer explaining his kill sheet, not from a hyperparameter sweep.
- **Small validated changes** beat big confident ones.

---

## Connect

[LinkedIn](https://linkedin.com/in/jacobvontersch) · Always up for talking markets, models, or hockey.
