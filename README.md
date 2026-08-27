# Jacob VonTersch 🍊

### Athlete turned analyst. I build models for the things I can't stop thinking about.

Luverne, Minnesota to Syracuse to Professional Ag Marketing. Applied Data Analytics out of the Syracuse iSchool, 69 games on the blue line for the Orange, and a habit of taking whatever I'm obsessed with and turning it into a system that actually runs.

---

## The path

I grew up in Luverne playing football and hockey, wearing 23 on defense. Hockey is what got me to Syracuse and what taught me most of what I know about work: you don't get a good shift because you felt like it, you get it because you put in the reps nobody watched. Three seasons, 69 games, a Senior Day in March 2026, and a degree in Applied Data Analytics two months later.

Sports is also where the analytical side started. Watching a game, you're already doing it: reading matchups, weighing tendencies, deciding what a situation is actually worth. I just kept going until it was code.

Now I'm at Professional Ag Marketing, building technology for commodity markets. Same instinct, higher stakes, real money on the other side of the screen.

---

## Sports betting, and the model I'm proudest of 🔒

I built an MLB home run prediction system. It started as a bet on a single market inefficiency and turned into the most serious thing I've made. It runs every day, in production, and grades itself against ground truth every morning.

The repo is private. The numbers aren't.

| | |
|---|---|
| **Architecture** | XGBoost + regularized logistic blend, Platt-calibrated per side |
| **Features** | 134 engineered, from Statcast 2023-2026 plus weather, ballpark, and market data |
| **Discrimination** | AUC **0.616**, Brier **0.101**, logLoss **0.352** |
| **Top-tier lift** | **27.1%** hit rate against base rate, a **2.13x lift** |
| **Second tier** | **20.4%** hit rate, **1.61x lift** |
| **Validation** | 124-day forward holdout, **26,270** predictions. No peeking backwards. |
| **Track record** | **1,400+** scored predictions in a version-stamped ledger |
| **Delivery** | 13-page live research terminal. FastAPI + Next.js, Cloudflare R2 sync, always on. |

**Why I'm proud of it isn't the lift.** Anybody can build a model that looks good. I spent two weeks building the thing that tells me when mine doesn't. Every number on that dashboard now carries the model version that produced it. Stale metrics render an empty state instead of a chart. A headline ROI stat got demoted the day I traced it and found only 7 of its 102 picks came from the current model.

That's the discipline the whole thing rests on. A model that flatters you is lying to you, and if I'm going to put money behind a number I need to know exactly where it came from. Betting is what forced that standard, because the market tells you the truth whether you want it or not.

**Where it's going.** It outgrew its origin. It's not one market or one day of the week anymore, it runs daily and the product is bigger than the angle it started from. Next is team and matchup level analysis on real slates, a public-facing transparency feed that posts the hit rate whether it's good or bad, and eventually a broader player-value model that goes past single-game outcomes. The long version is a general sports prediction platform. The short version is that I'm not done.

---

## The team I'm assembling

At Pro Ag I'm building out the technology function from scratch: writing the job description, running the hiring process, and setting the engineering conventions we'll be living with for years.

I'm not hiring people to maintain dashboards. I want builders who want real problems, the unglamorous kind with actual consequences, where the users are operators making decisions with their own money and there's no partial credit for a system that's almost right. Agriculture is full of those problems and short on people pointing modern tooling at them. That's the whole opportunity.

The conventions I'm setting: a STATUS doc that says what's actually true today including what's broken, branch and PR by default, docs that ship with the change instead of after it, and verify against the real source before you trust your own output.

---

## Public work

| Project | What it does | Tech |
|---|---|---|
| [Ag Market Predictor](https://github.com/Tersch23/ag-market-predictor) | Cross-market commodity forecasting with an XGBoost engine and offline local-LLM market briefings | Python, XGBoost, Streamlit, Llama.cpp |
| [MLB WAR-162 Forecast](https://github.com/Tersch23/mlb-war162-forecast) | Next-season WAR/162 from prior-season data, leakage-controlled Random Forest at scale | PySpark, MLlib |
| [NFL Leverage Report](https://github.com/Tersch23/NFL-Leverage-Report) | Roster-value opportunities from situational EPA against league average | Python, nflverse, Matplotlib |
| [2025 Playoffs Statcast](https://github.com/Tersch23/mlb-2025-playoffs-statcast) | What separates elite postseason hitters, by quality of contact | R, ggplot2 |
| [NCAA Hoops Dashboard](https://github.com/Tersch23/NCAA-Basketball-Dashboard) | Shot charts, team comparisons, conference standings across the Big 4 | Python, Streamlit, Plotly |
| [Orange Hoops Challenge](https://github.com/Tersch23/Orange_Hoops_Challenge) | Clutch-shot success model, 85% accuracy across 211K shots | Python, scikit-learn, R |

Most of what I build now is private. The public stuff is the part I can show.

---

## Stack

**Languages** Python · TypeScript · SQL · R · PySpark

**Data** Postgres/Neon · Pandas · NumPy · Parquet · pipeline and connector work against messy public data

**ML** scikit-learn · XGBoost · calibration and time-series CV · feature engineering · honest backtesting

**Ship** Next.js · React · FastAPI · Streamlit · Plotly · Tailwind · Railway · Vercel · Cloudflare R2 · Git/GitHub

**AI** Claude Code daily driver · agentic workflows · prompt engineering · local LLMs (Llama 3 via llama.cpp)

---

## How I think about it

- **Reps beat talent.** Same as hockey. The model got good because it ran every single day and got graded every single morning.
- **A number without provenance is a rumor.** Version-stamp everything.
- **Be your own toughest audit.** If your dashboard has never made you feel worse, it isn't measuring anything.
- **Small validated changes** beat big confident ones.

---

## Connect

**Jake@professionalagmarketing.com**

[LinkedIn](https://linkedin.com/in/jacobvontersch)
