"""Data imported from the archives."""

import yaml


def load_yaml(file_name: str, subdir: str) -> object:
    """Converts YAML file to Python object.
    
    Args:
      file_name:
        Name of file to be imported.
      subdir:
        Directory where the file is stored.

    Returns:
        Data contained in the target file, converted to a Python object.
    """
    file_path = f"{subdir}/{file_name}"
    with open(file_path) as file:
        yaml_stream = file.read()

    return yaml.safe_load(yaml_stream)

MOVIES = load_yaml(file_name="movies.yml", subdir="archives")

NAME_EXCEPTION_DICT = load_yaml(file_name="name_exceptions.yml", subdir="archives")
