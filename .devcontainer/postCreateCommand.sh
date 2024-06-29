pip install --upgrade pip
poetry install
# Activate poetry environment
source $(poetry env info --path)/bin/activate

# Update PYTHONPATH to include the virtual environment's Python interpreter
echo "export PYTHON_PATH=$(poetry env info --path)/bin/python" >> ~/.bashrc
