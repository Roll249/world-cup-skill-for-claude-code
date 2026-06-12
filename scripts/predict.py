#!/usr/bin/env python3
"""
World Cup Match Predictor
Predicts match outcomes using ML models
"""

import argparse
import json
import numpy as np
from typing import Dict, List

class Predictor:
    """Predict World Cup match outcomes."""
    
    def __init__(self, model: str = 'ensemble'):
        self.model = model
        self.home_advantage = 0.4  # Goals advantage for home team
    
    def calculate_features(self, home_data: Dict, away_data: Dict) -> np.ndarray:
        """Calculate features for prediction."""
        features = []
        
        # FIFA ranking difference (scaled)
        home_rank = home_data.get('fifa_ranking', 10)
        away_rank = away_data.get('fifa_ranking', 10)
        features.append((away_rank - home_rank) / 100)
        
        # Form difference
        home_form = self._calculate_form(home_data.get('recent_form', []))
        away_form = self._calculate_form(away_data.get('recent_form', []))
        features.append(home_form - away_form)
        
        # Goal averages
        home_avg_scored = home_data.get('avg_goals_scored', 1.5)
        home_avg_conceded = home_data.get('avg_goals_conceded', 1.2)
        away_avg_scored = away_data.get('avg_goals_scored', 1.4)
        away_avg_conceded = away_data.get('avg_goals_conceded', 1.3)
        
        features.append(home_avg_scored - away_avg_conceded)
        features.append(away_avg_scored - home_avg_conceded)
        
        # Home advantage
        features.append(self.home_advantage)
        
        return np.array(features)
    
    def _calculate_form(self, results: List[str]) -> float:
        """Calculate form score from results (W=1, D=0.5, L=0)."""
        if not results:
            return 0.5
        
        scores = {'W': 1.0, 'D': 0.5, 'L': 0.0}
        total = sum(scores.get(r, 0.5) for r in results)
        return total / len(results)
    
    def predict(self, home_data: Dict, away_data: Dict) -> Dict:
        """Predict match outcome."""
        features = self.calculate_features(home_data, away_data)
        
        # Simple logistic-like model (placeholder for real ML)
        # In production, this would use trained XGBoost/LightGBM model
        
        # Calculate base probabilities using features
        feature_sum = features.sum()
        
        # Home win probability (sigmoid-like)
        home_win = 0.4 + 0.15 * np.tanh(feature_sum)
        draw = 0.25 - 0.05 * abs(feature_sum)
        away_win = 0.35 - 0.15 * np.tanh(feature_sum)
        
        # Normalize
        total = home_win + draw + away_win
        home_win /= total
        draw /= total
        away_win /= total
        
        # Predict score using Poisson-like model
        home_xg = 1.4 + 0.2 * features[0] + 0.1
        away_xg = 1.2 - 0.2 * features[0] - 0.1
        
        home_goals = self._poisson_goal(home_xg)
        away_goals = self._poisson_goal(away_xg)
        
        return {
            'home_win': float(home_win),
            'draw': float(draw),
            'away_win': float(away_win),
            'predicted_score': f"{home_goals}-{away_goals}",
            'home_goals': home_goals,
            'away_goals': away_goals,
            'over_2_5': float(home_xg + away_xg > 2.5),
            'btts': float(home_goals > 0 and away_goals > 0)
        }
    
    def _poisson_goal(self, xg: float) -> int:
        """Predict goals using Poisson-like distribution."""
        # Simplified - in reality would use scipy.stats.poisson
        probs = [np.exp(-xg) * xg**i / np.math.factorial(i) for i in range(5)]
        probs = np.array(probs) / sum(probs)
        return np.random.choice([0, 1, 2, 3, 4], p=probs)
    
    def format_prediction(self, prediction: Dict, home: str, away: str) -> str:
        """Format prediction for display."""
        output = []
        output.append(f"\n⚽ {home.upper()} vs {away.upper()} ⚽")
        output.append("━" * 40)
        output.append("\nWin Probabilities:")
        output.append(f"  {home}: {prediction['home_win']:.1%}")
        output.append(f"  Draw: {prediction['draw']:.1%}")
        output.append(f"  {away}: {prediction['away_win']:.1%}")
        output.append(f"\nExpected Score: {prediction['predicted_score']}")
        output.append(f"Over 2.5 Goals: {'Yes' if prediction['over_2_5'] else 'No'}")
        output.append(f"Both Teams Score: {'Yes' if prediction['btts'] else 'No'}")
        output.append("━" * 40)
        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Predict World Cup matches")
    parser.add_argument("--match", help="Match in format 'Team1 vs Team2'")
    parser.add_argument("--model", default="ensemble", help="Model to use")
    parser.add_argument("--data", help="JSON file with match data")
    parser.add_argument("--output", help="Output file")
    
    args = parser.parse_args()
    
    predictor = Predictor(model=args.model)
    
    # Load data
    if args.data:
        with open(args.data) as f:
            data = json.load(f)
        home_data = data.get('home', {})
        away_data = data.get('away', {})
        home_name = home_data.get('name', 'Home')
        away_name = away_data.get('name', 'Away')
    elif args.match:
        # Parse match string
        parts = args.match.replace(' vs ', ' vs ').split(' vs ')
        if len(parts) != 2:
            print("Error: Use format 'Team1 vs Team2'")
            return
        
        home_name, away_name = [p.strip() for p in parts]
        
        # Generate placeholder data (in production, would fetch real data)
        home_data = {
            'name': home_name,
            'fifa_ranking': 10,
            'recent_form': ['W', 'W', 'D', 'W', 'L'],
            'avg_goals_scored': 1.8,
            'avg_goals_conceded': 0.9
        }
        away_data = {
            'name': away_name,
            'fifa_ranking': 15,
            'recent_form': ['W', 'D', 'W', 'L', 'W'],
            'avg_goals_scored': 1.5,
            'avg_goals_conceded': 1.1
        }
    else:
        print("Usage: python predict.py --match 'Brazil vs Germany'")
        print("   or: python predict.py --data match_data.json")
        return
    
    # Make prediction
    prediction = predictor.predict(home_data, away_data)
    
    # Format output
    output = predictor.format_prediction(prediction, home_name, away_name)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump({'prediction': prediction, 'teams': {'home': home_name, 'away': away_name}}, f, indent=2)
        print(f"Prediction saved to {args.output}")
    
    print(output)


if __name__ == "__main__":
    main()
