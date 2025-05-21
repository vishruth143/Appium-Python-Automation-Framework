import os

import pandas as pd

from kwa_demo_automation.framework.utilities.loaders import load_json, load_yaml, load_xlsx_sheet

class ConfigParser:
    CONFIG_FILE_PATHS = {
        'common_config': 'common_config.yml',
        'mobile_test_env_config': 'mobile/mobile_test_env_config.yaml',
        'mobile_test_data_config': 'mobile/mobile_test_data_config.yaml',
        'mobile_test_excel_data_config': 'mobile/mobile_test_excel_data_config.xlsx',
    }

    @staticmethod
    def load_config(config_name):
        config_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), ConfigParser.CONFIG_FILE_PATHS[config_name]))
        _, ext = os.path.splitext(config_path)
        if ext == '.json':
            config = load_json(config_path)
        elif ext in ('.yaml', '.yml'):
            config = load_yaml(config_path)
        else:
            raise ValueError(f'Unsupported file extension: {ext}')
        return config

    @staticmethod
    def load_xlsx(config_name: str, sheet_name: str) -> pd.DataFrame:
        """
        Load a specified sheet from an Excel file.

        :param sheet_name: Name of the sheet to load.
        :return: pandas DataFrame containing the sheet data.
        """
        config_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), ConfigParser.CONFIG_FILE_PATHS[config_name]))
        _, ext = os.path.splitext(config_path)

        if ext == '.xlsx':
            df = load_xlsx_sheet(config_path, sheet_name)
        else:
            raise ValueError(f'Unsupported file extension: {ext}')

        return df

    @staticmethod
    def resolve_config_path(config_name: str) -> str:
        """
        Resolve absolute path of the given config file name.
        :param config_name: Key from CONFIG_FILE_PATHS
        :return: Absolute path to the config file
        """
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), ConfigParser.CONFIG_FILE_PATHS[config_name])
        )