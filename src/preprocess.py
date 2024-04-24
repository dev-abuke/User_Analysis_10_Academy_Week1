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
        """Remove columns with missing values higher than the specified percentage.

        This method drops columns from the given dataframe where a percentage of
        missing values is greater than the specified percentage. This preprocessing
        step is important to avoid issues during model training and to reduce the
        dimensionality of the dataset.

        The percentage of missing values for each column is calculated using the
        pandas DataFrame method `isna`. This method returns a boolean array indicating
        the location of missing values in the DataFrame. The mean of the boolean array
        is then calculated to give the percentage of missing values for each column.

        A boolean mask is created by comparing the percentage of missing values
        to the specified percentage. The mask is True for columns where the percentage
        of missing values is greater than the specified percentage.

        The columns with missing values greater than the specified percentage
        are dropped from the dataframe using the pandas DataFrame method `loc`.
        The `loc` method allows us to select rows and columns based on label(s) or
        a boolean array. In this case, we are passing a boolean array to select
        the columns where the condition is True. We use the tilde (~) operator to
        invert the boolean array.

        Args:
            percentage: The maximum percentage of missing values allowed.
            df (pd.DataFrame): DataFrame to be preprocessed

        Returns:
            pd.DataFrame: The preprocessed DataFrame with variables removed
                that had more than the specified percentage of missing values.
        """
        # Calculate the percentage of missing values for each column
        missing_percent = df.isna().mean()
        print(missing_percent)
        # Create a boolean mask to identify columns with missing values > percentage or 0.25
        mask = missing_percent > percentage

        # Drop columns with missing values greater than the specified percentage
        return df.loc[:, ~mask]

    def fill_missing_median(self, df):
        """This method fills missing numerical values in the given dataframe
        with the median of that column's values. This preprocessing step is
        important because missing values can significantly impact the results
        of machine learning algorithms. The median is a robust measure of
        central tendency that is less affected by outliers than the mean.

        The method first makes a copy of the input dataframe to prevent
        modifying the original data. It then gets the column names of all
        numerical columns in the dataframe.

        Next, the method uses pandas DataFrame method `fillna` to replace
        missing values in each numerical column with the median of that
        column's values. The `fillna` method takes two arguments: the first is
        the value to fill missing values with, and the second is the axis
        along which to fill missing values. In this case, we want to fill
        missing values in each column, so we pass in `axis=0`. We also pass
        in a Series object containing the median of each column, which is
        calculated using the pandas Series method `median`.

        Finally, the method returns a list of the preprocessed numerical
        columns.

        Args:
            df (pd.DataFrame): The dataframe to be preprocessed

        Returns:
            list: The list of preprocessed numerical columns
        """
        df_filled = df.copy()
        # Get the column names of all numerical columns
        numerical_cols = df.select_dtypes(include=np.number).columns

        # Replace missing values with median for each numerical column
        df_filled[numerical_cols] = df_filled[numerical_cols].fillna(df_filled[numerical_cols].median(), axis=0)
        
        # Return the list of preprocessed numerical columns
        return numerical_cols, df_filled

    def fill_categorical(self, df, cols, numerical_cols, df_filled):
        """Fill categorical variables.

        This function fills categorical variables with the mode of that column
        in the dataframe. The mode is the most frequently occurring value in
        the column. If there are multiple modes, it fills with the first
        mode (index 0).

        The function takes in the following arguments:
            df (pd.DataFrame): The dataframe to be preprocessed
            cols(list): List of columns
            num_cols(list): List of numerical columns
            df_single(pd.DataFrame): Dataframe with filled numerical variables

        The function does the following:
            1. Get the set difference of all categorical columns and numerical
               columns to get the categorical columns.
            2. Replace missing values in the categorical columns with the mode
               of that column in the dataframe using df[cat_cols].mode().iloc[0]
            3. Return the new columns in the dataframe (df_cols) and the
               preprocessed dataframe (df_single) and the list of categorical
               columns (cat_cols)

        Returns:
            tuple: (df_cols (list), df_single (pd.DataFrame), cat_cols (list))
        """
        non_numerical_cols = list(set(cols) - set(numerical_cols))

        df_filled[non_numerical_cols] = df_filled[non_numerical_cols].fillna(df[non_numerical_cols].mode().iloc[0])

        df_cols = df_filled.columns

        return df_cols, df_filled, non_numerical_cols
