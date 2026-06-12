# Can't Stop Win - Reference Documentation

## Table of Contents

1. [Data Sources](#data-sources)
2. [Feature Engineering](#feature-engineering)
3. [ML Models](#ml-models)
4. [API Reference](#api-reference)
5. [Tournament Simulation](#tournament-simulation)

---

## Data Sources

### Official FIFA Data

```python
# FIFA World Rankings API
import requests

def get_fifa_ranking(team):
    url = f"https://www.fifa.com/api/ranking/{team.replace(' ', '-')}"
    response = requests.get(url)
    return response.json()
```

### Historical Match Data

| Dataset | Description | Link |
|---------|-------------|------|
| World Cup Matches 1930-2022 | All World Cup matches | Kaggle |
| International Matches 1872-2024 | All international matches | Kaggle |
| FIFA World Rankings | Monthly rankings since 1992 | Kaggle |
| Player Stats | Individual player data | Transfermarkt |

### Key APIs

```python
# Football-Data API (requires key)
FOOTBALL_API_KEY = "your_api_key"
BASE_URL = "https://api.football-data.com/v4"

def get_match_data(match_id):
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    return requests.get(f"{BASE_URL}/matches/{match_id}", headers=headers)

# API-Football (alternative)
def get_team_form(team_id, days=180):
    url = f"https://v3.football.api-sports.io/teams/statistics"
    params = {"team": team_id, "last": 10}
    return requests.get(url, headers=headers, params=params)
```

---

## Feature Engineering

### Core Features

```python
import pandas as pd
import numpy as np

def engineer_features(home_team, away_team, match_data):
    """
    Generate features for match prediction.
    """
    features = {}
    
    # Ranking features
    features['ranking_diff'] = home_team.fifa_rank - away_team.fifa_rank
    features['ranking_points_diff'] = home_team.fifa_points - away_team.fifa_points
    
    # Form features (weighted: recent matches weighted more)
    features['home_form'] = calculate_weighted_form(home_team.recent_results, decay=0.85)
    features['away_form'] = calculate_weighted_form(away_team.recent_results, decay=0.85)
    features['form_diff'] = features['home_form'] - features['away_form']
    
    # Goal statistics
    features['home_avg_scored'] = home_team.avg_goals_scored
    features['home_avg_conceded'] = home_team.avg_goals_conceded
    features['away_avg_scored'] = away_team.avg_goals_scored
    features['away_avg_conceded'] = away_team.avg_goals_conceded
    
    # Expected goals (xG) differential
    features['home_xg_diff'] = home_team.avg_xg - home_team.avg_xga
    features['away_xg_diff'] = away_team.avg_xg - away_team.avg_xga
    
    # Head-to-head
    features['h2h_home_wins'] = h2h_stats['home_wins']
    features['h2h_away_wins'] = h2h_stats['away_wins']
    features['h2h_draws'] = h2h_stats['draws']
    
    # Home advantage (historically ~0.4 goals)
    features['home_advantage'] = 0.4
    
    # Tournament context
    features['is_knockout'] = match_data.get('stage') in ['R16', 'QF', 'SF', 'F']
    features['is_final'] = match_data.get('stage') == 'F'
    
    return features

def calculate_weighted_form(results, decay=0.85):
    """
    Calculate weighted form over recent matches.
    Recent match has weight 1, previous has weight decay, etc.
    """
    form = 0
    total_weight = 0
    for i, result in enumerate(results):
        weight = decay ** i
        form += weight * result_to_score(result)  # W=1, D=0.5, L=0
        total_weight += weight
    return form / total_weight if total_weight > 0 else 0

def result_to_score(result):
    """Convert match result to numerical score."""
    return {'W': 1.0, 'D': 0.5, 'L': 0.0}.get(result, 0.5)
```

### Advanced Features

```python
# Elo Rating System
ELO_INITIAL = 1500
ELO_K_FACTOR = 32

def calculate_elo_ratings(matches_df):
    """
    Calculate Elo ratings for all teams.
    """
    elo_ratings = {team: ELO_INITIAL for team in matches_df['team'].unique()}
    
    for _, match in matches_df.iterrows():
        home_team = match['home_team']
        away_team = match['away_team']
        
        # Expected score
        E_home = 1 / (1 + 10 ** ((elo_ratings[away_team] - elo_ratings[home_team]) / 400))
        E_away = 1 - E_home
        
        # Actual score
        if match['home_goals'] > match['away_goals']:
            S_home, S_away = 1, 0
        elif match['home_goals'] < match['away_goals']:
            S_home, S_away = 0, 1
        else:
            S_home, S_away = 0.5, 0.5
        
        # Update ratings
        elo_ratings[home_team] += ELO_K_FACTOR * (S_home - E_home)
        elo_ratings[away_team] += ELO_K_FACTOR * (S_away - E_away)
    
    return elo_ratings

# Expected Goals (xG) Features
def calculate_xg_features(team, last_n_matches=10):
    """
    Calculate xG-based features for a team.
    """
    matches = team.recent_matches[-last_n_matches:]
    
    total_xg = sum(m.xg_for if m.team == team.name else m.xg_against for m in matches)
    total_xga = sum(m.xg_against if m.team == team.name else m.xg_for for m in matches)
    
    return {
        'avg_xg': total_xg / len(matches) if matches else 1.0,
        'avg_xga': total_xga / len(matches) if matches else 1.0,
        'xg_diff': (total_xg - total_xga) / len(matches) if matches else 0
    }
```

---

## ML Models

### Model Comparison

| Model | Pros | Cons | Best Use Case |
|-------|------|------|---------------|
| Logistic Regression | Interpretable, fast | May miss non-linear patterns | Baseline, betting odds |
| XGBoost | High accuracy, handles missing data | Requires tuning | Production predictions |
| LightGBM | Fastest, good with large data | Less interpretable | Real-time predictions |
| Neural Network | Captures complex patterns | Needs lots of data | Ensemble component |
| Random Forest | Robust, handles outliers | Slow with many trees | Ensemble component |

### XGBoost Implementation

```python
import xgboost as xgb
from sklearn.model_selection import train_test_split

class WorldCupPredictor:
    def __init__(self):
        self.model = xgb.XGBClassifier(
            n_estimators=500,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            objective='multi:softmax',
            num_class=3,  # Win, Draw, Loss
            random_state=42
        )
    
    def train(self, X, y):
        """Train the model."""
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            early_stopping_rounds=50,
            verbose=False
        )
    
    def predict_proba(self, features):
        """Predict win/draw/loss probabilities."""
        return self.model.predict_proba([features])[0]
    
    def predict_score(self, features):
        """Predict expected score using Poisson model."""
        home_xg = self._calculate_xg(features, is_home=True)
        away_xg = self._calculate_xg(features, is_home=False)
        
        return self._poisson_predict(home_xg, away_xg)
    
    def _calculate_xg(self, features, is_home):
        """Calculate expected goals."""
        base_xg = 1.3  # Average World Cup xG
        ranking_adj = features['ranking_diff'] * 0.02 if is_home else -features['ranking_diff'] * 0.02
        form_adj = features['home_form'] * 0.3 if is_home else features['away_form'] * 0.3
        home_adj = 0.4 if is_home else -0.4
        
        return base_xg + ranking_adj + form_adj + home_adj
    
    def _poisson_predict(self, home_xg, away_xg):
        """Generate score prediction using Poisson distribution."""
        from scipy.stats import poisson
        
        max_goals = 6
        home_probs = [poisson.pmf(i, home_xg) for i in range(max_goals)]
        away_probs = [poisson.pmf(i, away_xg) for i in range(max_goals)]
        
        # Calculate score probabilities
        score_probs = np.outer(home_probs, away_probs)
        
        # Most likely score
        max_idx = np.unravel_index(score_probs.argmax(), score_probs.shape)
        home_goals, away_goals = max_idx
        
        return home_goals, away_goals, score_probs
```

### Ensemble Model

```python
class EnsemblePredictor:
    """Combine multiple models for robust predictions."""
    
    def __init__(self):
        self.models = {
            'xgboost': XGBoostPredictor(),
            'lightgbm': LightGBMPredictor(),
            'logistic': LogisticPredictor(),
            'random_forest': RandomForestPredictor()
        }
        self.weights = {
            'xgboost': 0.35,
            'lightgbm': 0.30,
            'logistic': 0.15,
            'random_forest': 0.20
        }
    
    def predict(self, features):
        """Ensemble prediction using weighted average."""
        all_probs = []
        
        for name, model in self.models.items():
            probs = model.predict_proba(features)
            all_probs.append(self.weights[name] * probs)
        
        # Weighted average
        final_probs = sum(all_probs)
        
        return {
            'home_win': final_probs[0],
            'draw': final_probs[1],
            'away_win': final_probs[2],
            'model': 'ensemble'
        }
```

---

## API Reference

### CLI Commands

```bash
# Predict a single match
python scripts/predict.py --match "Brazil vs Germany"

# Batch prediction from file
python scripts/predict.py --input matches.csv --output predictions.json

# Fetch historical data
python scripts/fetch_data.py --teams "Brazil" "Germany" --output data/

# Run tournament simulation
python scripts/simulate.py --teams 32 --iterations 10000

# Update rankings
python scripts/update_rankings.py --source fifa
```

### Python API

```python
from cant_stop_win import Predictor, DataFetcher, TournamentSimulator

# Initialize
predictor = Predictor(model='xgboost')
fetcher = DataFetcher()

# Get prediction
match_data = fetcher.get_match_data("Brazil", "Germany")
prediction = predictor.predict(match_data)

print(f"Brazil win: {prediction['home_win']:.1%}")
print(f"Draw: {prediction['draw']:.1%}")
print(f"Germany win: {prediction['away_win']:.1%}")
print(f"Expected: {prediction['predicted_score']}")
```

---

## Tournament Simulation

### Monte Carlo Simulation

```python
import numpy as np
from itertools import product

class TournamentSimulator:
    def __init__(self, teams, predictor):
        self.teams = teams
        self.predictor = predictor
        self.results = {team: {'wins': 0, 'finals': 0, 'champion': 0} 
                       for team in teams}
    
    def simulate_tournament(self, n_iterations=10000):
        """Run Monte Carlo simulation of entire tournament."""
        for _ in range(n_iterations):
            tournament_result = self._simulate_once()
            self._update_results(tournament_result)
        
        return self._get_probabilities(n_iterations)
    
    def _simulate_once(self):
        """Simulate one complete tournament."""
        # Simulate groups
        groups = self._draw_groups()
        group_results = self._simulate_groups(groups)
        
        # Simulate knockout
        knockout = self._get_knockout_teams(group_results)
        
        while len(knockout) > 1:
            knockout = self._simulate_knockout_round(knockout)
        
        return knockout[0]  # Champion
    
    def _simulate_groups(self, groups):
        """Simulate group stage."""
        results = {}
        for group_name, group_teams in groups.items():
            # Round-robin
            matches = list(product(group_teams, repeat=2))
            points = {team: 0 for team in group_teams}
            
            for home, away in matches:
                pred = self.predictor.predict(home, away)
                result = self._sample_result(pred)
                
                if result == 'home':
                    points[home] += 3
                elif result == 'draw':
                    points[home] += 1
                    points[away] += 1
            
            # Top 2 advance
            sorted_teams = sorted(points.items(), key=lambda x: -x[1])
            results[group_name] = [t[0] for t in sorted_teams[:2]]
        
        return results
    
    def _simulate_knockout_round(self, teams):
        """Simulate knockout round."""
        winners = []
        for i in range(0, len(teams), 2):
            match = [teams[i], teams[i+1]]
            pred = self.predictor.predict(match[0], match[1])
            
            if np.random.random() < pred['home_win']:
                winners.append(match[0])
            elif np.random.random() < pred['draw'] / (1 - pred['home_win']):
                # Penalty shootout - 50/50
                winners.append(match[np.random.randint(2)])
            else:
                winners.append(match[1])
        
        return winners
    
    def _sample_result(self, pred):
        """Sample a result based on prediction probabilities."""
        r = np.random.random()
        if r < pred['home_win']:
            return 'home'
        elif r < pred['home_win'] + pred['draw']:
            return 'draw'
        else:
            return 'away'
```

---

## World Cup 2026 Specifics

### Tournament Format

- **Dates:** June 8 - July 19, 2026
- **Host:** USA, Canada, Mexico (co-hosted)
- **Teams:** 48 teams (expanded from 32)
- **Venues:** 16 venues across 3 countries

### New Format

```
Group Stage: 12 groups of 4 teams (previously 8 groups of 4)
Knockout: Top 2 from each group + 8 best 3rd place → R16
```

### Key Considerations for 2026

1. **Expanded tournament** - More matches, more data points
2. **Co-hosting** - Multiple time zones, travel fatigue
3. **Summer heat** - Some venues will be HOT
4. **New teams** - More diverse participant pool

---

## Best Practices

### Data Quality

1. **Verify data sources** - Cross-reference multiple sources
2. **Handle missing data** - Use imputation or drop if too sparse
3. **Update regularly** - Form changes over time
4. **Consider context** - Friendly vs competitive matches

### Model Training

1. **Use appropriate time window** - 5-10 years of data
2. **Validate properly** - Time-based split, not random
3. **Test on held-out tournaments** - 2018, 2022 data
4. **Ensemble for robustness** - Combine multiple models

### Interpretation

1. **Uncertainty matters** - Provide confidence intervals
2. **Context is key** - Injuries, suspensions, fatigue
3. **Home advantage varies** - Neutral venues in knockout
4. **Variance is high** - Single match = high variance event

---

*Remember: Football is beautiful because it's unpredictable. Use these tools to have fun, not to stress!*
