#`/scripts/`

## `analyze_endpoints_and_create_files.py`

This is a script to analyze endpoints and create the .py files, endpoint documentation, and parameter documentation. 
Please note that this file might break dependent on major changes to the NBA API.

It will be beneficial to enable `DEBUG` and `DEBUG_STORAGE` to help in the debugging process.

 
## Configuration Options

`USER_ENDPOINTS` - A list of endpoints to analyze. Can be one or many endpoints. Can also be set to examine all end 
points with : `USER_ENDPOINTS = endpoint_list`

`COMBINE_WITH_EXISTING_ANALYSIS_JSON_AT_END` - If `True`, will output a finalized `complete_analysis.json`. This might 
be useful to compare with existing analysis.json to examine changes. 

