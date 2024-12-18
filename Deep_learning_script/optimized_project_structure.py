import os
import sys


def create_directory_structure(parent_path, project_name):
    # Create the base project directory
    base_path = os.path.join(parent_path, project_name)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Created project directory: {base_path}")
    else:
        print(f"Project directory already exists: {base_path}")

    # Directories to create
    dirs_to_create = [
        os.path.join(base_path, "data"),
        os.path.join(base_path, "data", "train"),
        os.path.join(base_path, "data", "val"),
        os.path.join(base_path, "data", "test"),
        os.path.join(base_path, "notebooks"),
        os.path.join(base_path, "src"),
        os.path.join(base_path, "outputs"),
        os.path.join(base_path, "outputs", "saved_models"),
        os.path.join(base_path, "outputs", "logs"),
        os.path.join(base_path, "outputs", "figures"),
        os.path.join(base_path, "scripts")
    ]

    for d in dirs_to_create:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"Created directory: {d}")
        else:
            print(f"Directory already exists: {d}")

    # Files to create with initial content
    files_to_create = {
        os.path.join(base_path, "requirements.txt"): "# List your project dependencies here\n",
        os.path.join(base_path, "README.md"): f"# {project_name}\n\nA brief description of your project.\n\n## Getting Started\n\nInstructions on how to set up and run the project.\n",
        os.path.join(base_path, "src", "data_utils.py"): "\"\"\"Functions for data loading and preprocessing\"\"\"\n\n# Add your data loading functions here.\n",
        os.path.join(base_path, "src", "models.py"): "\"\"\"Model definitions go here.\"\"\"\n\n# Define your custom CNN and code to load pretrained models.\n",
        os.path.join(base_path, "src", "train.py"): "\"\"\"Training functions.\"\"\"\n\n# Write code for training loops, callbacks, etc.\n",
        os.path.join(base_path, "src", "evaluate.py"): "\"\"\"Evaluation functions.\"\"\"\n\n# Add code for metrics calculation and model evaluation.\n",
    }

    for file_path, file_content in files_to_create.items():
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(file_content)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

    # Create a sample notebook for exploration
    sample_notebook_path = os.path.join(
        base_path, "notebooks", "01_exploration.ipynb")
    if not os.path.exists(sample_notebook_path):
        sample_notebook_content = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis\\n",
    "Describe what you want to explore in the dataset here."
   ]
  }
 ],
 "metadata": {
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
   }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}"""
        with open(sample_notebook_path, "w") as f:
            f.write(sample_notebook_content)
        print(f"Created file: {sample_notebook_path}")
    else:
        print(f"File already exists: {sample_notebook_path}")

    print("Project structure setup complete.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python setup_structure.py <parent_path> <project_name>")
        sys.exit(1)

    parent_path = sys.argv[1]
    project_name = sys.argv[2]

    create_directory_structure(parent_path, project_name)
