import os

project_dir = os.path.abspath(
    os.path.join(os.path.abspath(__file__), os.path.pardir, os.path.pardir))

print(project_dir)