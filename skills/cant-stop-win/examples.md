# Examples - Can't Stop Win

## Example 1: Single Match Prediction

### User Request
```
"predict the Brazil vs Germany match"
```

### Agent Response
```python
from cant_stop_win import Predictor, DataFetcher

# Initialize
predictor = Predictor(model='ensemble')
fetcher = DataFetcher()

# Get latest team data
home_data = fetcher.get_team_data("Brazil")
away_data = fetcher.get_team_data("Germany")

# Generate prediction
prediction = predictor.predict(home_data, away_data)

print(prediction)
```

### Output
```
⚽ BRAZIL vs GERMANY ⚽
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Win Probabilities:
🇧🇷 Brazil: 38.5%
🤝 Draw: 29.2%
🇩🇪 Germany: 32.3%

Expected Score: 2-1 (Brazil)

Over 2.5 Goals: 61%
Both Teams Score: 54%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Key Factors:
✅ Brazil's attacking form (5W-0D-0L in qualifiers)
✅ Neymar's influence in midfield
⚠️ Germany's defensive record improving
❌ Brazil missing starting goalkeeper

Narrative: "A clash of titans with Brazil edging it.
The Maracanazo won't repeat, but expect fireworks
from both sides."
```

---

## Example 2: Tournament Simulation

### User Request
```
"simulate the 2026 World Cup and tell me who wins"
```

### Agent Response
```python
from cant_stop_win import TournamentSimulator, Predictor

# Setup
predictor = Predictor(model='ensemble')
simulator = TournamentSimulator(teams=32, predictor=predictor)

# Run simulation (10,000 times)
results = simulator.simulate_tournament(n_iterations=10000)

# Display results
for team, probs in sorted(results.items(), key=lambda x: -x[1]['champion']):
    print(f"{team}: {probs['champion']:.1%} to win")
```

### Output
```
🏆 WORLD CUP 2026 - WINNER PROBABILITIES 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 🇧🇷 Brazil         18.5%  ████████████
2. 🇫🇷 France         15.2%  ██████████
3. 🇩🇪 Germany        12.8%  ████████
4. 🇦🇷 Argentina       11.4%  ███████
5. 🇪🇸 Spain          9.7%   ██████
6. 🇵🇹 Portugal        7.3%   ████
7. 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England       6.8%   ████
8. 🇳🇱 Netherlands    5.2%   ███
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Based on 10,000 simulations:
"France and Brazil dominate, but England being
England means they'll somehow lose to penalties
in the semifinal. Again."
```

---

## Example 3: Build Prediction Model

### User Request
```
"help me build a model to predict World Cup matches using historical data"
```

### Agent Response

Step 1: Create the data pipeline
```python
import pandas as pd
from cant_stop_win import DataPipeline, WorldCupPredictor

# Step 1: Load historical data
pipeline = DataPipeline()
df = pipeline.load_historical_matches(
    source='kaggle',
    years=range(2002, 2026)
)

# Step 2: Feature engineering
df_features = pipeline.engineer_features(df)

# Step 3: Train model
model = WorldCupPredictor(model_type='xgboost')
model.train(df_features, target='result')

# Step 4: Evaluate
metrics = model.evaluate()
print(f"Accuracy: {metrics['accuracy']:.1%}")
print(f"ROC-AUC: {metrics['roc_auc']:.3f}")
```

Step 2: Make predictions
```python
# Predict Brazil vs Argentina final
prediction = model.predict(
    home_team="Brazil",
    away_team="Argentina",
    context={'stage': 'Final', 'neutral': True}
)

print(f"Argentina wins: {prediction['away_win']:.1%}")
```

---

## Example 4: Pre-Match Analysis

### User Request
```
"give me betting insights for France vs Spain match"
```

### Agent Response
```python
from cant_stop_win import MatchAnalyzer

analyzer = MatchAnalyzer()

# Comprehensive analysis
analysis = analyzer.analyze(
    home="France",
    away="Spain",
    match_type="Knockout"
)

# Display
print(analysis.formatted_report())
```

### Output
```
📊 FRANCE vs SPAIN - MATCH ANALYSIS 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FORM (Last 5 matches):
🇫🇷 France: WWDWW (Home: WWWDW)
🇪🇸 Spain: WDWWW (Away: DWWWL)

HEAD-TO-HEAD (Last 10):
France: 3 wins | Draws: 3 | Spain: 4 wins

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY MATCHUP: Mbappé vs Garcia
- Mbappé: 3 goals in last 2 matches
- Garcia: 2 red cards in career vs France

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PREDICTION:
🇫🇷 France Win: 41%
🤝 Draw: 31%
🇪🇸 Spain Win: 28%

SCORE PREDICTION: 2-1 France

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BETTING INSIGHTS (Educational Only!):

✅ VALUE BET: France to win @ 2.40
   - Implied: 41.7%
   - Our estimate: 41%
   - Verdict: Fair odds

⚠️ CAUTION: Over 2.5 @ 1.85
   - High variance, tight match expected
   - Only bet what you can lose

❌ AVOID: Correct Score 3-0 France
   - Spain's defense too good
   - Would require Mbappé magic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUN FACT:
These teams last met in 2021 Nations League.
France won 2-1. Mbappé scored. Mbappé always scores.
```

---

## Example 5: Group Stage Analysis

### User Request
```
"analyze Group G: Brazil, Switzerland, Cameroon, Serbia"
```

### Agent Response
```python
from cant_stop_win import GroupAnalyzer

analyzer = GroupAnalyzer()

results = analyzer.simulate_group(
    teams=["Brazil", "Switzerland", "Cameroon", "Serbia"],
    iterations=10000
)

print(results.formatted_table())
```

### Output
```
🌎 GROUP G - PROBABILITIES 🌎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        | Qualify | Runners Up | 3rd | 4th
━━━━━━━━━|━━━━━━━━━|━━━━━━━━━━━━|═════|═════
🇧🇷 Brazil   |  82.3%  |   12.1%   | 4.5%| 1.1%
🇨🇭 Switz.  |  54.2%  |   28.7%   |12.4%| 4.7%
🇷🇸 Serbia  |  35.1%  |   32.8%   |18.2%|13.9%
🇨🇲 Cameroon|  28.4%  |   26.4%   |24.9%|20.3%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MATCH PREDICTIONS:

Brazil vs Switzerland (Opening):
→ 2-0 Brazil (68% confidence)

Cameroon vs Serbia (Opening):
→ 1-1 Draw (45% confidence)

Brazil vs Cameroon:
→ 3-1 Brazil

Serbia vs Switzerland (Decider):
→ 2-1 Switzerland (go through)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DRAMATIC SCENARIO:
"If Cameroon beats Brazil (8% chance) and Serbia
beats Switzerland (35%), we're looking at a
three-way tie on 6 points. Chaos ensues.
God bless VAR."
```

---

## Example 6: Real-Time Prediction Update

### User Request
```
"Messi just got injured in warm-up! Update prediction"
```

### Agent Response
```python
# Update player availability
predictor.update_context(
    team="Argentina",
    changes={
        "messi_injured": True,
        "injury_severity": "muscle strain",
        "expected_comeback": "quarter-final (if they make it)"
    }
)

# Regenerate predictions for remaining matches
for opponent in ["Group Stage opponents"]:
    new_pred = predictor.predict("Argentina", opponent)
    print(f"vs {opponent}: {new_pred['argentina_win']:.1%} (was {old_preds[opponent']:.1%})")
```

### Output
```
⚠️ PREDICTION UPDATE ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🇦🇷 ARGENTINA - INJURY SHOCK 🇦🇷

Messi's Injury: Muscle strain, ~2 weeks out

Updated Win Probabilities:

vs Mexico:     52% (was 61%) ▼ 9pp
vs Poland:    48% (was 57%) ▼ 9pp  
vs Saudi:     78% (was 89%) ▼11pp

Knockout Impact:
QFs: 31% (was 44%) ▼ 13pp
SFs: 18% (was 28%) ▼ 10pp
Final:  8% (was 15%) ▼  7pp

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Narrative: "Messi's injury changes everything.
Di Maria must step up. Or it's penalties.
Argentina always has penalties."
```

---

## Example 7: Building Your Own Pipeline

### User Request
```
"build a complete prediction pipeline with my own data"
```

### Agent Response

Creating `my_prediction_pipeline.py`:

```python
"""
World Cup Prediction Pipeline
============================
Your data + Our models = Better predictions (maybe)
"""

from cant_stop_win import (
    DataLoader,
    FeatureEngineer,
    ModelTrainer,
    Predictor,
    Visualizer
)
import pandas as pd

# 1. LOAD YOUR DATA
loader = DataLoader()

# Option A: Use our data
matches = loader.load_standard_dataset()

# Option B: Load your own CSV
# matches = loader.load_csv("my_matches.csv")

# 2. ENGINEER FEATURES
engineer = FeatureEngineer()

features = [
    'fifa_ranking_diff',
    'weighted_form',
    'goals_scored_avg',
    'goals_conceded_avg',
    'h2h_record',
    'home_advantage',
    'xg_differential',
    'tournament_stage_factor',
    'days_since_last_match',
    'players_available_ratio'
]

df = engineer.create_features(matches, features)

# 3. TRAIN MODEL
trainer = ModelTrainer()

# Split data (tournament-aware)
trainer.split_tournament_wise(df, test_tournaments=[2022])

# Train multiple models
models = trainer.train_ensemble(['xgboost', 'lightgbm', 'logistic'])

# 4. EVALUATE
metrics = trainer.evaluate(models)
print(f"Best Model: {metrics['best_model']}")
print(f"Accuracy: {metrics['accuracy']:.1%}")
print(f"Log Loss: {metrics['log_loss']:.3f}")

# 5. PREDICT!
predictor = Predictor(models=models)

for match in upcoming_matches:
    result = predictor.predict(match['home'], match['away'])
    print(f"{match['home']} vs {match['away']}: {result['prediction']}")

# 6. VISUALIZE
viz = Visualizer()

# Plot feature importance
viz.plot_feature_importance(models['xgboost'], features)

# Plot model comparison
viz.plot_model_comparison(metrics)

# Plot tournament simulation
viz.plot_tournament_probs(simulator.results)
```

---

*More examples coming as the World Cup approaches!*
