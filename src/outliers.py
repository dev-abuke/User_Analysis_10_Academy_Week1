import sys

import numpy as np
import pandas as pd
import sys
import os
# sys.path.append(os.path.abspath(os.path.join('./')))
# from logger import Logger


class Outliers:
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


    def get_numerical_columns(self, df: pd.DataFrame):
        # Get the column names of all numerical columns
        numerical_cols = df.select_dtypes(include=np.number).columns
        
        # Return the list of preprocessed numerical columns
        return numerical_cols

    def calculate_num_outliers_zscore(self, col):
        """Calculate the number of outliers for each numerical column.

        This function calculates the number of outliers in a given numerical
        column using the Z-score method. The Z-score is a measure of how many
        standard deviations away a data point is from the mean. If the Z-score is
        greater than a certain threshold (3 in this case), it is considered an
        outlier. The threshold is set to 3 because it is a commonly used value
        for detecting outliers in statistical data analysis. See:
        https://en.wikipedia.org/wiki/Outlier#Z-score_method

        Args:
            col (pd.Series): a series to be analyzed

        Returns:
            int: The number of outliers in the given column
        """
        # Set a threshold for what is considered an outlier. A Z-score
        # greater than this threshold is considered an outlier.
        thres = 3 #https://www.linkedin.com/advice/0/how-can-you-determine-threshold-outlier-detection-0hycf#:~:text=Choosing%20a%20threshold%20for%20outlier%20detection%20involves%20statistical%20methods%20tailored,data%20under%20a%20normal%20distribution.

        # Calculate the mean and standard deviation of the given column
        mean = col.mean()
        std = col.std()

        # Calculate the Z-scores using the formula (x - mean) / std
        z_scores = (col - mean) / std

        # Count the number of outliers (i.e., values with an absolute value
        # greater than the threshold)
        outliers = np.count_nonzero(np.abs(z_scores) > thres)

        return outliers
    def Inter_quatile_method(self, col):
        q1 = col.quantile(0.25)
        q3 = col.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = col[(col < lower_bound) | (col > upper_bound)].count()
        return outliers