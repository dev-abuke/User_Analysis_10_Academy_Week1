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
        
    def drop_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Drop duplicates.

        Drop duplicate rows from the dataframe.

        Args:
            df (pd.DataFrame): The dataframe to drop duplicates from.

        Returns:
            pd.DataFrame: The dataframe without duplicate rows.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df must be a pandas DataFrame. Got "
                            f"{type(df)} instead.")
        if df is None:
            raise ValueError("df cannot be None. It must be a valid pandas "
                             "DataFrame.")

        df = df.drop_duplicates()

        return df
    
    def clean_feature_name(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the feature names of the given dataframe.

        This method does the following:
            1. Replaces any whitespace with an underscore in the column names.
            2. Converts all column names to lowercase.
            3. In-place modifies the dataframe with the cleaned column names.

        Args:
            df (pd.DataFrame): The dataframe to be preprocessed.

        Returns:
            pd.DataFrame: The preprocessed dataframe with cleaned feature names.
        """
        df.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
        
        return df

    def drop_missing_variables(self, df: pd.DataFrame, percentage: float = 0.25) -> pd.DataFrame:
        """Drop variables with more than 25% missing values.

        This method drops columns in the given dataframe where a percentage of
        missing values is greater than 25%.

        Args:
            percentage: The maximum percentage of missing values allowed.
            df (pd.DataFrame): DataFrame to be preprocessed

        Returns:
            pd.DataFrame: The preprocessed DataFrame with variables removed
                that had more than the specified percentage of missing values.
        """
        # Calculate the percentage of missing values for each column
        missing_percent = df.isna().mean()

        # Create a boolean mask to identify columns with missing values > 30%
        mask = missing_percent > percentage

        # Drop columns with missing values greater than the specified percentage
        return df.loc[:, ~mask]

