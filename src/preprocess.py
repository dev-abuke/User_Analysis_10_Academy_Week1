import sys

import numpy as np
import pandas as pd
import sys
import os
# sys.path.append(os.path.abspath(os.path.join('./')))
# from logger import Logger


class PreProcess:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.df = df
            # self.logger = Logger("preprocessing.log").get_app_logger()
            # self.logger.info(
            # 'Successfully Instantiated Outlier Class Object')
        except Exception:
            # self.logger.exception(
            # 'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)

    def percent_missing_values(self, df: pd.DataFrame):
        # Total missing values
        mis_val = df.isnull().sum()

        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        #round the percent to 2 decimal point
        mis_val_percent = np.round(mis_val_percent, 2)
        print(f"The telecom dataset contains {mis_val_percent} % missing values.")

    def total_percent_missing(self, df: pd.DataFrame):
        """Get the percentage of missing values in the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be preprocessed

        Returns:
            pd.DataFrame: the dataframe
        """
        # Calculate total number of missing values
        totalMissing = df.isna().sum().sum()

        # Calculate percentage of missing values
        print("Dataset contains", round(
            (totalMissing/len(df.values.flat)) * 100, 2), "%", "Total Missing Values.")
