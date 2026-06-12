# Can't Stop Win - Agent Skills Specification

## Overview

**Name:** cant-stop-win  
**Version:** 1.0.0  
**Description:** World Cup 2026 prediction skills for Claude Agent  
**License:** Apache 2.0

## Skills

### `cant-stop-win`

Predicts World Cup 2026 match outcomes using historical data, ML models, and tournament simulation.

#### Triggers
- "predict World Cup match"
- "build prediction model"
- "simulate tournament"
- "analyze team form"
- "who will win"

#### Capabilities
- Single match prediction (win/draw/loss probabilities)
- Expected score calculation
- Tournament Monte Carlo simulation
- Form analysis
- Head-to-head statistics
- Betting insights

#### Data Sources
- FIFA Rankings API
- Kaggle Historical Datasets
- Transfermarkt
- Flashscore/SofaScore

#### Models
- XGBoost
- LightGBM
- Logistic Regression
- Ensemble

## File Structure

```
skills/
└── cant-stop-win/
    ├── SKILL.md              # Main skill file
    ├── reference.md          # Technical documentation
    ├── examples.md           # Usage examples
    ├── README.md            # Skill documentation
    ├── requirements.txt     # Python dependencies
    ├── __init__.py          # Package init
    ├── scripts/
    │   ├── fetch_data.py   # Data fetching
    │   ├── predict.py      # Match prediction
    │   └── simulate.py      # Tournament simulation
    └── data/
        └── README.md        # Data directory
```

## Dependencies

- Python 3.8+
- numpy>=1.21.0
- pandas>=1.3.0
- scipy>=1.7.0
- scikit-learn>=1.0.0
- xgboost>=1.5.0
- lightgbm>=3.3.0

## Usage

### Claude Code
```
/plugin install cant-stop-win@username/cant-stop-win-skills
```

### Direct
```bash
python scripts/predict.py --match "Brazil vs Germany"
python scripts/simulate.py --iterations 10000
```

## Changelog

### 1.0.0 (2026-06-12)
- Initial release
- Match prediction with ML models
- Tournament simulation
- Form analysis
