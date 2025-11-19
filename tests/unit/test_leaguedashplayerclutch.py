from nba_api.stats.endpoints import leaguedashplayerclutch
import pandas as pd
import datetime

# Determine a valid season for testing (e.g., current or previous)
current_year = datetime.date.today().year
season_str = f"{current_year - 1}-{str(current_year)[2:]}"

print(f"Testing LeagueDashPlayerClutch endpoint for {season_str}...")
try:
    # We call the endpoint with standard parameters
    data = leaguedashplayerclutch.LeagueDashPlayerClutch(
        season=season_str,
        season_type_all_star="Regular Season"
    ).get_data_frames()

    # get_data_frames() returns a list of DataFrames. We check the first one.
    df = data[0]

    # Check if the DataFrame has data (at least one player row)
    if len(df) > 0:
        print(f"Successfully retrieved {len(df)} rows.")
        print(df.head())
        print("\n✅ Test PASSED!")
    else:
        print("\n❌ Test FAILED: Retrieved 0 rows of data. Check API call or Season.")

except Exception as e:
    print(f"\n❌ Test FAILED: An error occurred during the API call.")
    print(e)