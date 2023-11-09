header_template = """
## _{parameter_name}_
"""

regex_pattern_body_template = """
#### Class `{python_class}`
##### Patterns 
{regex_patterns}
"""

regex_pattern_line_template = """ - `{pattern}`"""


variable_body_template = """
Variable Name | Value
------------ | -------------
{variables}
"""

variable_line_template = """_**{name}**_ {additional_tags}| `{value}`"""
