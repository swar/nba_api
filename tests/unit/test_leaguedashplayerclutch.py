from nba_api.stats.endpoints import leaguedashplayerclutch
import pandas as pd
import datetime

# This script verifies that the endpoint can be called successfully.

# Determine a valid season for stable testing
current_year = datetime.date.today().year
season_str = f"{current_year - 1}-{str(current_year)[2:]}"

print(f"Testing LeagueDashPlayerClutch endpoint for {season_str}...")
try:
    # Call the endpoint using the simplified, working parameter names
    data = leaguedashplayerclutch.LeagueDashPlayerClutch(
        season=season_str,
        season_type_all_star="Regular Season",
        clutch_time="Last 5 Minutes",
        point_diff=5
    ).get_data_frames()

    # Check if the DataFrame has data
    df = data[0]

    if len(df) > 0:
        print(f"Successfully retrieved {len(df)} rows.")
        print("\n✅ Test PASSED!")
    else:
        print("\n❌ Test FAILED: Retrieved 0 rows of data.")

except Exception as e:
    print(f"\n❌ Test FAILED: An error occurred during the API call.")
    print(e)