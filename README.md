# Jacob VonTersch 🍊

### Commodity Market Data Tools | Sports Betting Models | Building the Tech Team at Pro Ag

Luverne, Minnesota -> Syracuse -> Professional Ag Marketing.

Applied Data Analytics/Data Science @ the Syracuse iSchool, retired Syracuse Men's Ice Hockey player, and I love taking whatever I'm obsessed with and turning it into a system that actually runs.

Now building technology for commodity markets at Professional Ag Marketing, and models for sports betting on my own time.

---

## MLB Home Run Model 🔒

A production home run prediction system for betting markets. It runs daily and grades every prediction against ground truth the next morning. Private repo, but the numbers are fair game.

| | |
|---|---|
| **Architecture** | XGBoost + regularized logistic blend, Platt-calibrated per side |
| **Features** | 134 engineered, from Statcast 2023-2026 plus weather, ballpark, and market data |
| **Discrimination** | AUC **0.616**, Brier **0.101**, logLoss **0.352** |
| **Top-tier lift** | **27.1%** hit rate against base rate, a **2.13x lift** |
| **Second tier** | **20.4%** hit rate, **1.61x lift** |
| **Validation** | 124-day forward holdout, **26,270** predictions, no lookahead |
| **Track record** | **1,400+** scored predictions in a version-stamped ledger |
| **Delivery** | 13-page research terminal. FastAPI + Next.js, Cloudflare R2 sync, always on. |

**What I'm proudest of is the reporting layer, not the lift.** Every number in the terminal carries the model version that produced it. Stale metrics render an empty state instead of a chart. A headline ROI figure got demoted once I traced it and found only 7 of its 102 picks came from the current model. If I'm putting money behind a number, I need to know exactly where it came from.

**Where it's going.** It started as one market and grew past it. Predictions run daily now. Next up is matchup-level analysis across full slates, a public transparency feed that posts the hit rate regardless of what it says, and a broader player-value model that goes beyond single-game outcomes.

---

## Building a Team

I'm building out the technology function at Professional Ag Marketing from scratch, from the job description through hiring and the engineering standards we work to.

Looking for builders who want real problems. The users are operators making decisions with their own money, so the work has consequences and there is no partial credit for a system that is almost right. Agriculture has plenty of those problems and very few people pointing modern tooling at them.

---

## Public Work

| Project | What it does | Tech |
|---|---|---|
| [Ag Market Predictor](https://github.com/Tersch23/ag-market-predictor) | Cross-market commodity forecasting with an XGBoost engine and offline local-LLM market briefings | Python, XGBoost, Streamlit, Llama.cpp |
| [MLB WAR-162 Forecast](https://github.com/Tersch23/mlb-war162-forecast) | Next-season WAR/162 from prior-season data, leakage-controlled Random Forest at scale | PySpark, MLlib |
| [NFL Leverage Report](https://github.com/Tersch23/NFL-Leverage-Report) | Roster-value opportunities from situational EPA against league average | Python, nflverse, Matplotlib |
| [2025 Playoffs Statcast](https://github.com/Tersch23/mlb-2025-playoffs-statcast) | What separates elite postseason hitters, by quality of contact | R, ggplot2 |
| [NCAA Hoops Dashboard](https://github.com/Tersch23/NCAA-Basketball-Dashboard) | Shot charts, team comparisons, conference standings across the Big 4 | Python, Streamlit, Plotly |
| [Orange Hoops Challenge](https://github.com/Tersch23/Orange_Hoops_Challenge) | Clutch-shot success model, 85% accuracy across 211K shots | Python, scikit-learn, R |

Most of my current work is private. This is the part I can show.

---

## Stack

**Languages** Python · TypeScript · SQL · R · PySpark

**Data** Postgres/Neon · Pandas · NumPy · Parquet · API and report ingestion pipelines

**ML** scikit-learn · XGBoost · calibration and time-series CV · feature engineering · backtesting

**Ship** Next.js · React · FastAPI · Streamlit · Plotly · Tailwind · Railway · Vercel · Cloudflare R2 · Git/GitHub

**AI** Claude Code daily driver · agentic workflows · prompt engineering · local LLMs (Llama 3 via llama.cpp)

---

## Connect

**Jake@professionalagmarketing.com**

[LinkedIn](https://linkedin.com/in/jacobvontersch)
