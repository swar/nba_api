from tools.stats.endpoint_analysis.data import missing_parameter_regex
import re

nba_response = "Invalid parameters; The value 'a' is not valid for StartPeriod.; The StartPeriod property is required.; The value 'a' is not valid for EndPeriod.; The EndPeriod property is required."

def test_requried_parameter_regex():

    re_parameter_regex = re.compile(missing_parameter_regex)

    invalid_value_index = re_parameter_regex.groupindex['invalid_value'] - 1
    invalid_parameter_index = re_parameter_regex.groupindex['invalid_parameter'] - 1
    required_parameter_index = re_parameter_regex.groupindex['required_parameter'] - 1

    matches = re_parameter_regex.findall(nba_response)
    
    match = matches[0]
    assert match[invalid_value_index] == 'a'
    assert match[invalid_parameter_index] == 'StartPeriod'
    assert match[required_parameter_index] == ''

    match = matches[1]
    assert match[invalid_value_index] == ''
    assert match[invalid_parameter_index] == ''    
    assert match[required_parameter_index] == 'StartPeriod'

    match = matches[2]
    assert match[invalid_value_index] == 'a'
    assert match[invalid_parameter_index] == 'EndPeriod'
    assert match[required_parameter_index] == ''

    match = matches[3]
    assert match[invalid_value_index] == ''
    assert match[invalid_parameter_index] == ''    
    assert match[required_parameter_index] == 'EndPeriod'
