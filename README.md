# 🏆 Can't Stop Win - World Cup 2026 Prediction Skills

> 🤖 Claude Agent Skills for predicting FIFA World Cup 2026 match outcomes

<p align="center">
  <img src="https://img.shields.io/badge/World%20Cup-2026-FFD700?style=for-the-badge" alt="World Cup 2026">
  <img src="https://img.shields.io/badge/Claude-Skills-FF6B6B?style=for-the-badge" alt="Claude Skills">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
</p>

---

## 🎯 What Is This?

A collection of **Claude Agent Skills** for predicting World Cup 2026 matches. 

Use it to:
- 🤖 **Get AI-powered match predictions** directly from Claude
- 📊 **Build ML prediction pipelines** with historical data
- 🏆 **Simulate entire tournaments** using Monte Carlo methods
- 📈 **Analyze team form** and betting insights

## 🚀 Installation

### Option 1: Claude Code Plugin (Recommended)

```bash
# In Claude Code, run:
/plugin install cant-stop-win@Roll249/world-cup-skill-for-claude-code
```

Then just ask Claude:
```
"predict Brazil vs Argentina final"
"simulate World Cup 2026"
"build a model to predict matches"
```

### Option 2: Manual Installation

```bash
# Clone the repo
git clone https://github.com/Roll249/world-cup-skill-for-claude-code.git
cd world-cup-skill-for-claude-code

# Copy skill to Claude's skills folder
mkdir -p ~/.cursor/skills/cant-stop-win
cp -r skills/cant-stop-win/* ~/.cursor/skills/cant-stop-win/

# Install dependencies
pip install -r skills/cant-stop-win/requirements.txt
```

### Option 3: Claude.ai Web

1. Go to Settings → Skills
2. Click "Upload Skill"
3. Upload `skills/cant-stop-win/SKILL.md`

## 📁 Repository Structure

```
world-cup-skill-for-claude-code/
├── skills/
│   └── cant-stop-win/           # Main Claude Skill
│       ├── SKILL.md             # Skill instructions
│       ├── reference.md         # Technical documentation
│       ├── examples.md          # Usage examples
│       └── requirements.txt     # Dependencies
├── scripts/
│   ├── fetch_data.py           # Data fetching
│   ├── predict.py              # Match prediction
│   └── simulate.py             # Tournament simulation
├── .claude-plugin/
│   └── marketplace.json         # Plugin manifest
├── README.md
└── SPEC.md
```

## 🎮 Features

| Feature | Description |
|---------|-------------|
| **Match Prediction** | Win/draw/loss probabilities, expected score |
| **Tournament Simulation** | Monte Carlo with 10,000+ iterations |
| **Form Analysis** | Weighted recent form analysis |
| **Head-to-Head** | Historical match records |
| **xG Modeling** | Expected goals prediction |
| **Betting Insights** | Value bet identification |

## 📖 Documentation

- [SKILL.md](skills/cant-stop-win/SKILL.md) - Main skill instructions
- [Reference Guide](skills/cant-stop-win/reference.md) - ML models & technical details
- [Examples](skills/cant-stop-win/examples.md) - Usage examples

## 🔧 Technical Stack

- **Python 3.8+**
- **Machine Learning**: scikit-learn, XGBoost, LightGBM
- **Data Processing**: pandas, numpy, scipy
- **APIs**: FIFA, Kaggle, Transfermarkt

## 📊 Example Output

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
```

## ⚠️ Disclaimer

**For entertainment and educational purposes only.** Predictions can be wrong. We take no responsibility for lost bets, broken friendships, or existential crises.

## 📄 License

Apache License 2.0

---

<p align="center">
  Made with ❤️ for football fans ⚽🏆
</p>
