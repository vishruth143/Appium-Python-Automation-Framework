# pylint: disable=[missing-function-docstring, missing-module-docstring, unspecified-encoding, invalid-name]
# pylint: disable=[import-error, line-too-long, raise-missing-from]
import os
import json

import pandas as pd
import yaml

def load_json(file_path: str) -> dict:
    """
    Method to read data from JSON
    :param str file_path: file path
    :return: JSON
    :rtype: dict
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'The file "{file_path}" does not exist.')
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except json.JSONDecodeError as e:
        # Re-raise a custom exception with 'from' to preserve the traceback
        raise json.JSONDecodeError(f'Failed to load JSON file {file_path}: {str(e)}', e.doc, e.pos) from e


def load_yaml(file_path: str) -> dict:
    """
    Method to read data from YAML
    :param str file_path: file path
    :return: YAML
    :rtype: dict
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'The file "{file_path}" does not exist.')
        with open(file_path) as file_handler:
            return yaml.safe_load(file_handler)
    except yaml.YAMLError as e:
        # Re-raise a custom exception with 'from' to preserve the traceback
        raise yaml.YAMLError(f'Failed to load YAML file {file_path}: {str(e)}') from e

def load_xlsx_sheet(file_path: str, sheet_name: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading Excel file '{file_path}' sheet '{sheet_name}': {e}")
