# NBA Analytics Recipes & Workflows

Actionable CLI commands and scripts for common statistical investigations.

---

## 1. Step-Back 3-Point Rankings

Find the highest volume and most efficient step-back 3-point shooters across the NBA.

```powershell
# Top volume step-back 3-point shooters in the league (min 50 attempts)
.\scripts\nba.ps1 action-shots --action-type "Step Back" --shot-type 3pt --min-fga 50 --sort FGA --top 10

# Most accurate step-back 3-point shooters (min 40 attempts, sorted by eFG%)
.\scripts\nba.ps1 action-shots --action-type "Step Back" --shot-type 3pt --min-fga 40 --sort EFG_PCT --top 10
```

---

## 2. Pick & Roll Ball Handler Leaderboard

Evaluate which primary creators generate the most points per possession (PPP) out of pick-and-roll sets.

```powershell
# High-volume P&R creators (min 200 possessions, sorted by PPP)
.\scripts\nba.ps1 play-types --play-type PRBallHandler --min-poss 200 --sort PPP --top 10

# Individual player P&R breakdown (e.g., Jalen Brunson or Luka Doncic)
.\scripts\nba.ps1 play-types --player "Brunson" --play-type PRBallHandler
```

---

## 3. Pull-Up vs Catch-and-Shoot Splits

Compare an individual player's shooting percentages when creating off the dribble versus spotting up off the catch.

```powershell
# Player shot type splits (Catch & Shoot vs Pullups)
.\scripts\nba.ps1 shot-tracking --player "Stephen Curry" --split general

# Player dribble volume efficiency (0 dribbles vs 1 vs 2 vs 7+ dribbles)
.\scripts\nba.ps1 shot-tracking --player "Stephen Curry" --split dribbles

# League-wide catch-and-shoot leaders (min 150 attempts, sorted by 3PT%)
.\scripts\nba.ps1 shot-tracking --catch-and-shoot --min-fga 150 --sort FG3_PCT --top 10

# League-wide pull-up leaders (min 200 attempts, sorted by volume)
.\scripts\nba.ps1 shot-tracking --pullups --min-fga 200 --sort FGA --top 10
```

---

## 4. True Shooting Percentage (TS%) vs Usage Rate (USG%)

Identify the most efficient high-volume offensive engines in the league.

```powershell
# High-efficiency rotation players (min 1000 total minutes, sorted by True Shooting %)
.\scripts\nba.ps1 advanced-stats --min-min 1000 --sort TS_PCT --top 10

# High-usage offensive engines (min 1000 total minutes, sorted by Usage Rate)
.\scripts\nba.ps1 advanced-stats --min-min 1000 --sort USG_PCT --top 10

# Individual player advanced profile (OffRTG, DefRTG, NetRTG, AST%, TS%, USG%, PIE)
.\scripts\nba.ps1 advanced-stats --player "Nikola Jokic"
```

---

## 5. Player Full Shot Mechanics & Action Diet

See every shot type a player uses in a season, from step-backs and fadeaways to driving floaters and rim finishes.

```powershell
# Full action diet and frequency for Shai Gilgeous-Alexander
.\scripts\nba.ps1 shot-chart --player "Shai" --min-fga 10 --top 15

# Victor Wembanyama's fadeaways and turnaround jumpers
.\scripts\nba.ps1 shot-chart --player "Wembanyama" --action-type "Fadeaway"
```

---

## 6. Defensive Disruptor & Hustle Leaderboard

Find who creates extra possessions through deflections, charges drawn, and loose balls.

```powershell
# Top deflection leaders per game (min 20 MPG)
.\scripts\nba.ps1 hustle-stats --min-min 20 --sort DEFLECTIONS --top 10

# Screen assist leaders (big men creating points for guards)
.\scripts\nba.ps1 hustle-stats --min-min 20 --sort SCREEN_AST_PTS --top 10
```
