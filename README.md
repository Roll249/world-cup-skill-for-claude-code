# Can't Stop Win - World Cup 2026 Prediction Skills

> 🏆 Claude Agent Skills for predicting FIFA World Cup 2026 match outcomes

<p align="center">
  <img src="https://img.shields.io/badge/World%20Cup-2026-FFD700?style=for-the-badge" alt="World Cup 2026">
  <img src="https://img.shields.io/badge/Claude-AI%20Skills-FF6B6B?style=for-the-badge" alt="Claude AI Skills">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
</p>

---

## 🎯 What Is This?

A collection of **Claude Agent Skills** for predicting World Cup 2026 matches. Whether you want to:

- 🤖 **Get AI-powered match predictions** directly from Claude
- 📊 **Build ML prediction pipelines** with historical data
- 🏆 **Simulate entire tournaments** using Monte Carlo methods
- 📈 **Analyze team form** and betting insights

This skill set has got you covered.

## 🚀 Quick Start

### For Claude Code Users

```bash
# Install the skill
/plugin install cant-stop-win@your-username/cant-stop-win-skills

# Then just ask Claude!
"predict Brazil vs Argentina final"
"simulate World Cup 2026"
"build a model to predict matches"
```

### For Claude.ai

Upload this repository as a custom skill via Settings → Skills → Upload Skill.

### For Python Developers

```bash
# Clone the repo
git clone https://github.com/your-username/cant-stop-win-skills.git
cd cant-stop-win-skills

# Install dependencies
pip install -r skills/cant-stop-win/requirements.txt

# Run predictions
python scripts/predict.py --match "Brazil vs Germany"
```

## 📁 Repository Structure

```
cant-stop-win-skills/
├── skills/
│   └── cant-stop-win/           # The main Claude Skill
│       ├── SKILL.md             # Skill instructions (auto-loaded by Claude)
│       ├── reference.md         # Technical documentation
│       ├── examples.md          # Usage examples
│       ├── README.md            # Skill-specific README
│       ├── requirements.txt     # Python dependencies
│       ├── scripts/             # Python scripts
│       │   ├── fetch_data.py   # Data fetching
│       │   ├── predict.py      # Match prediction
│       │   └── simulate.py      # Tournament simulation
│       └── data/               # Sample data directory
├── scripts/                     # Standalone CLI tools
├── SPEC.md                     # Skill specification
└── README.md                   # This file
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

## 🤖 Available Skills

### `cant-stop-win`

The main prediction skill. Use when:
- Predicting World Cup match outcomes
- Building ML prediction models
- Analyzing team statistics
- Simulating tournament outcomes

## 📖 Documentation

- [Skill README](skills/cant-stop-win/README.md) - Skill-specific documentation
- [Reference Guide](skills/cant-stop-win/reference.md) - Technical details & ML models
- [Examples](skills/cant-stop-win/examples.md) - Usage examples

## 🔧 Technical Stack

- **Python 3.8+**
- **Machine Learning**: scikit-learn, XGBoost, LightGBM
- **Data Processing**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn, plotly

## 📊 Data Sources

The skills support integration with:
- FIFA Official Rankings API
- Kaggle Historical Datasets
- Transfermarkt Player Stats
- Flashscore/SofaScore APIs

## 🎯 Prediction Example

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
✅ Brazil's home advantage
✅ Neymar's influence in midfield
⚠️ Germany's defensive issues
```

## 🏆 Tournament Simulation

```
🏆 WORLD CUP 2026 - WINNER PROBABILITIES 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 🇧🇷 Brazil         18.5%  ████████████
2. 🇫🇷 France         15.2%  ██████████
3. 🇩🇪 Germany        12.8%  ████████
4. 🇦🇷 Argentina       11.4%  ███████
5. 🇪🇸 Spain          9.7%   ██████
...

Based on 10,000 simulations
```

## 📝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ⚠️ Disclaimer

**This tool is for entertainment and educational purposes only.** Predictions are just predictions - they can be wrong. We take no responsibility for lost bets, broken friendships, or existential crises caused by unexpected match results.

## 📄 License

Apache License 2.0 - See [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with ❤️ for football fans who think they know better than the experts ⚽🏆
</p>
