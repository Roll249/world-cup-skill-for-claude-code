# 🏆 Can't Stop Win 🏆

### The World Cup 2026 Prediction Skill That's Probably More Confident Than It Should Be

---

## What Even Is This?

Ever wanted to predict World Cup matches but your crystal ball is in the shop? Want to build a machine learning model but your inner Stats Bro is on vacation? Well, congratulations! You've found the skill that lets you do both!

**Can't Stop Win** is your one-stop-shop for:
- 🧠 Predicting match outcomes using AI and data science
- 📊 Building prediction pipelines that make you look smart
- 🎰 Getting "insights" for betting (do it, we won't judge... much)
- 🏆 Simulating entire tournaments and pretending you knew all along

---

## Installation

```bash
# Clone this bad boy
git clone https://github.com/your-username/cant-stop-win.git

# Install dependencies
pip install -r requirements.txt

# Run like a champion
python scripts/predict.py --match "Brazil vs Argentina"
```

---

## Quick Start

### CLI Mode

```bash
# Predict a match
python scripts/predict.py --match "France vs Germany"

# Simulate the whole tournament
python scripts/simulate.py --iterations 10000

# Get match analysis
python scripts/analyze.py --teams Brazil Germany
```

### Python Mode

```python
from cant_stop_win import Predictor, DataFetcher

# Initialize the predictor (it needs no encouragement)
predictor = Predictor(model='xgboost')

# Get prediction
result = predictor.predict("Brazil", "Germany")

print(f"Brazil Win: {result['home_win']:.1%}")
print(f"Draw: {result['draw']:.1%}")
print(f"Germany Win: {result['away_win']:.1%}")
print(f"\nPredicted Score: {result['predicted_score']}")
```

**Output:**
```
Brazil Win: 45.2%
Draw: 27.8%
Germany Win: 27.0%

Predicted Score: 2-1 (Brazil)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Key Insight: Brazil's attack vs Germany's suspect defense = bad day for Die Mannschaft
```

---

## How It Works (The "Sciencey" Part)

### Step 1: Gather Data 📊

We pull data from:
- FIFA rankings (because numbers mean authority)
- Historical match results (from when your parents were kids)
- Team form (because momentum is REAL)
- Head-to-head records (vengeance is a dish best served cold)

### Step 2: Feature Engineering 🧪

We calculate things like:
- FIFA ranking difference (Spain ranked 8th? RIP.)
- Weighted form over last 10 matches (recent = matters more)
- Expected goals (xG) - the metric that makes you sound smart
- Home advantage (~0.4 goals worth, according to science)
- Player availability (that missing midfielder THO)

### Step 3: ML Magic ✨

Multiple models compete to predict:
- **XGBoost** - The overachiever
- **LightGBM** - The fast kid who still gets A's
- **Logistic Regression** - The reliable one
- **Ensemble** - All of them voting on your fate

### Step 4: Profit(?) 💰

Just kidding. You get predictions. Maybe some glory. Definitely some debates with friends.

---

## Features

| Feature | Description |
|---------|-------------|
| Single Match Prediction | "Will Brazil win?" (Spoiler: Probably not this time) |
| Tournament Simulation | Monte Carlo that tells you who's winning 10,000 times |
| Form Analysis | Are they in form or just lucky? |
| Head-to-Head | History lessons nobody asked for |
| Betting Insights | For educational purposes only (wink) |
| Export to JSON/CSV | Data for your spreadsheets of regret |

---

## The Models

### Logistic Regression
The baseline. Like training wheels but for data science. Fast, interpretable, and won't judge you for using it.

### XGBoost
The popular kid. Everyone uses it, and for good reason! Handles missing data, non-linear patterns, and makes you feel like a real data scientist.

### LightGBM
XGBoost's faster cousin who finished the marathon while XGBoost was still stretching.

### Ensemble
Democracy in action. Four models vote, you suffer the consequences of their collective wisdom.

---

## Example Predictions

### Group Stage

```
🌎 WORLD CUP 2026 - GROUP A PREDICTIONS 🌎

Team          | Pts | GD  | Qualified?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🇧🇷 Brazil     |  7  | +4  | ✅ YES
🇨🇭 Switzerland |  4  | +1  | ✅ YES
🇨🇲 Cameroon    |  3  | -2  | ❌ NO
🇷🇸 Serbia     |  2  | -3  | ❌ NO

"Switzerland's defensive tactics will frustrate Brazil, 
but the Samba boys will squeeze through. Cameroon and 
Serbia fight for nothing but pride and 4th place."
```

### Knockout Stage

```
⚽ QUARTER-FINAL: Brazil vs France ⚽
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Win Probability:
Brazil 🇧🇷    42%
Draw          27%
France 🇫🇷     31%

Expected Score: 1-1 (Brazil wins on penalties)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Narrative: "Neymar vs Mbappé. The dream final that 
wasn't meant to be. Brazil edges it in the lottery 
of destiny."
```

---

## The Science Behind It

### Why Home Advantage Matters

Home advantage is worth approximately **0.4 goals** in international football. This comes from:
- Crowd support (they're loud and annoying)
- No travel fatigue
- Referee bias (subconscious or otherwise)
- Sleeping in your own bed

### Why Recent Form Matters

The formula uses exponential decay weighting:
```
Form = Σ(result[i] × 0.85^i) / Σ(0.85^i)
```

Where:
- result[i] = 1 for Win, 0.5 for Draw, 0 for Loss
- i = 0 for most recent, increasing backward
- 0.85 = decay factor (because 2 years ago is basically ancient history)

### Why xG is a Big Deal

Expected Goals (xG) measures quality of chances, not just quantity. A team that scores 3 goals from 0.5 xG is LUCKY. A team scoring 2 from 2.5 xG is UNLUCKY but CREATING CHANCES.

---

## Tips for Using This (Don't Be That Guy)

### ✅ DO:
- Use predictions for fun and friendly debates
- Build models and learn about ML
- Impress your friends with data science jargon
- Accept that football is unpredictable (looking at you, 2018 Germany)

### ❌ DON'T:
- Bet your life savings (or any savings, really)
- Blame us when your "sure thing" loses
- Become insufferable at parties
- Forget that the model doesn't know about:
  - Team spirit
  - Referee having a bad day
  - That random deflection that goes in
  - Divine intervention

---

## FAQ

**Q: Is this accurate?**
A: Accuracy varies. We're not saying our model predicted Greece winning 2004, but we're not NOT saying it either. ⚽✨

**Q: Can I use this to make money?**
A: You *could*. But you probably *shouldn't*. The house always wins, and the house in football is called "variance."

**Q: Why "Can't Stop Win"?**
A: Because when you start predicting World Cup matches, you literally cannot stop yourself from predicting more matches. It's a disease. There is no cure.

**Q: Will this predict the World Cup winner?**
A: Maybe! Probably not! Definitely maybe!

---

## Contributing

Found a bug? Want to add a feature? Think our model is garbage?

1. Fork it
2. Create your branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Added something amazing'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a PR
6. Argue about it in the comments

---

## License

MIT License - Use it, abuse it, just don't blame us when France loses again.

---

## Acknowledgments

- FIFA for making rankings that mean everything and nothing
- All the footballers who give us content
- The universe for being fundamentally unpredictable
- Coffee for making this possible

---

## The Fine Print

**DISCLAIMER:** This tool is for entertainment and educational purposes only. We take no responsibility for:
- Lost bets
- Broken friendships
- Existential crises caused by unexpected results
- The general chaos of football

Predictions are just predictions. They're right when they're right, and wrong when they're wrong. That's the beauty of the beautiful game.

---

*Made with ❤️ and an unhealthy obsession with football statistics*

**Version:** 1.0.0
**Last Updated:** June 2026 (World Cup Edition)
**Status:** Ready to ruin your expectations

---

#️⃣ #CantStopWin #WorldCup2026 #ProbablyShouldBetOnBrazil
