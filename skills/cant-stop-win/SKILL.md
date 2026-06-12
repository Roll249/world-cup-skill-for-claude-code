---
name: cant-stop-win
description: >-
  World Cup 2026 prediction skill. Predict match outcomes for FIFA World Cup 2026 using historical data, team statistics, player analysis, and ML models. Use when the user wants to predict World Cup matches, build prediction models, analyze teams, or ask "who will win the World Cup 2026?". Supports both AI-powered predictions and code generation for prediction pipelines.
---

# Can't Stop Win - World Cup 2026 Predictor

## What This Skill Does

Predicts World Cup 2026 match outcomes using quantum physics... wait no, just really good data analysis and vibes! 

This skill helps you:
- Predict match outcomes (scores, winners, over/under)
- Build ML prediction models
- Analyze team form and head-to-head records
- Generate betting insights (for educational purposes only!)
- Create beautiful prediction dashboards

## Quick Start

### 1. Gather Match Information

Before predicting, collect:

```
- Two teams playing
- Match date and venue
- Recent form (last 5-10 matches)
- Head-to-head history
- Player availability (injuries, suspensions)
- Tournament context (group stage, knockout)
```

### 2. Data Sources

Use these sources for data:

| Source | What to Get | URL |
|--------|-------------|-----|
| FIFA Official | Rankings, match history | fifa.com |
| Transfermarkt | Squad info, injuries | transfermarkt.com |
| Flashscore | Live scores, form | flashscore.com |
| SofaScore | Detailed stats | sofascore.com |
| WorldFootball | Historical data | worldfootball.net |
| Kaggle | Historical datasets | kaggle.com/datasets |

### 3. Prediction Workflow

```
1. Fetch historical data → 2. Feature engineering → 3. Model prediction → 4. Generate insights
```

#### Step 1: Fetch Data
```python
# See scripts/fetch_data.py for implementation
python scripts/fetch_data.py --teams "Brazil" "Germany" --output match_data.json
```

#### Step 2: Feature Engineering
Key features for prediction:
- FIFA ranking difference
- Goals scored/conceded ratio
- Recent form (weighted average)
- Head-to-head record
- Home/away advantage
- Player quality (Elo ratings)
- Tournament stage factor

#### Step 3: Run Prediction
```python
# See reference.md for model details
python scripts/predict.py --match_data match_data.json --model xgboost
```

### 4. Interpretation

**Prediction Output Format:**
```
Match: Brazil vs Germany
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Win Probability: Brazil 45% | Draw 28% | Germany 27%
Expected Score: 2-1 (Brazil)
Over 2.5 Goals: 68%
Both Teams Score: 55%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Key Factors:
✅ Brazil's home advantage
✅ Germany's defensive issues
⚠️ Missing key midfielder
```

## Common Use Cases

### Predict Single Match
```
User: "Predict Brazil vs Argentina final"
→ Collect team data → Run model → Generate prediction
```

### Build Prediction Dataset
```
User: "I want to build a model to predict World Cup matches"
→ Create data pipeline → Feature engineering guide → Model templates
```

### Analyze Team's Chances
```
User: "How far will England go in the tournament?"
→ Analyze group → Simulate tournament → Probability for each round
```

### Pre-Match Analysis
```
User: "Give me betting insights for France vs Spain"
→ Form analysis → H2H → Key player impact → Value bets
```

## Model Options

| Model | Best For | Complexity |
|-------|----------|------------|
| Logistic Regression | Baseline, interpretable | Low |
| XGBoost/LightGBM | High accuracy | Medium |
| Neural Network | Complex patterns | High |
| Ensemble | Robust predictions | High |

## Output Formats

### For CLI
```
python scripts/predict.py --match "Brazil vs Germany"
```

### For Dashboard
Generate HTML/React prediction dashboard. See examples in reference.

### For Analysis Report
Generate markdown report with:
- Team form charts
- Key statistics comparison
- Win probability breakdown
- Recommended bets

## Additional Resources

- For complete API reference, see [reference.md](reference.md)
- For data collection scripts, see [scripts/](scripts/)
- For prediction examples, see [examples.md](examples.md)

## Tips & Tricks

1. **More data = better predictions** (but diminishing returns after ~10 years)
2. **Home advantage matters!** (worth ~0.4 goals in international football)
3. **Form is temporary, class is permanent** (use weighted averages)
4. **World Cup = high variance** (anything can happen!)
5. **Don't bet your house** (this is for fun!)

---

*Built with ❤️ for football fans who think they know better than the experts*
