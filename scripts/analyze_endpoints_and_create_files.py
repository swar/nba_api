from tools.stats.endpoint_analysis import analysis as endpoint_analysis
from tools.stats.endpoint_py_file_generator import generator as py_file_generator
from tools.stats.endpoint_documentation_generator import generator as endpoint_documentation_generator
from tools.stats.parameter_documentation_generator import generator as parameter_documentation_generator

# Analyze Endpoints

endpoint_analysis.analyze_and_save_endpoints()

# Generate Endpoint Py Files

py_file_generator.generate_endpoint_file()

# Generate Endpoint Documentation

endpoint_documentation_generator.generate_endpoint_documentation()

# Generate Parameter Documentation

parameter_documentation_generator.generate_parameter_documentation_file()
