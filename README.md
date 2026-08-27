# Jacob VonTersch 🍊

Data and product at **Professional Ag Marketing**. I build the models, pipelines, and dashboards that turn messy market data into decisions people actually make with money on the line — hogs and grain by day, baseball by night.

Syracuse iSchool grad, Syracuse Men's Hockey, Luverne MN. I ship things.

---

## What I'm working on

**Building the tech function at Pro Ag.** Writing the job description, running the hiring process, and setting the engineering conventions we'll build on — STATUS-first repos, branch-and-PR, docs that travel with the change. Going from "the guy who builds tools" to a team that does.

**Production ag analytics.** Shipped the Lean Hog basis engine into our internal data platform: Postgres on Neon, Next.js front end, Railway deploys. Then solved the annoying part — the official CME index posts two days late, so I reverse-engineered the formula from USDA's daily mandatory price reports and reconstructed a provisional index for the missing days. **Mean absolute deviation of $0.0025 against the real index over 95 days.** The chart is never stale again.

**A proprietary MLB home run model** (private — stats below). Live, deployed, and scored every morning against ground truth.

**New builds in flight.** A forward-looking marketing decision layer for hog producers (load-level, packer-grid-aware — the piece nobody in that market actually ships), and a contract-position system replacing a 20-year-old Access database for a grain operation.

Plus a backlog of ideas considerably longer than my available weekends.

---

## The home run model 🔒

Private repo, private edge — but the numbers are fair game.

| | |
|---|---|
| **Architecture** | XGBoost + regularized logistic blend, Platt-calibrated per side |
| **Features** | 134 engineered, from Statcast 2023–2026 + weather + park + market data |
| **Discrimination** | AUC **0.616**, Brier **0.101**, logLoss **0.352** |
| **Top-tier lift** | **27.1%** hit rate vs. base rate — **2.13x lift** |
| **Second tier** | **20.4%** hit rate — **1.61x lift** |
| **Validation** | 124-day forward holdout, **26,270** predictions. No peeking backwards. |
| **Track record** | **1,400+** scored predictions in a version-stamped ledger |
| **Delivery** | 13-page research terminal — FastAPI + Next.js 16, Cloudflare R2 data bridge, always-on |

The thing I'm proudest of isn't the lift, it's the audit. I spent two weeks making my own dashboard report *worse* numbers about itself: every figure now carries the model version it came from, stale metrics render an empty state instead of a chart, and a headline ROI stat got demoted the moment I traced that only 7 of its 102 picks came from the current model.

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

**Data** Postgres/Neon · Pandas · NumPy · dbt · Parquet · pybaseball/Statcast · USDA & CME feeds · Barchart

**ML** scikit-learn · XGBoost · calibration & time-series CV · feature engineering · honest backtesting

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
