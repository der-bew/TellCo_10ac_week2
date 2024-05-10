import pandas as pd
import numpy as np


class MissingValueHandler():
    def __init__(self, df):
        self.df = df
    
    def df_info(self):
         # Display DataFrame's information
        print("\nDataFrame Information:")
        print(self.df.info())
        
    def check_duplicate(self):
        # Identify and report duplicated values
        duplicates = self.df.duplicated()
        print("\nDuplicated values:")
        print(duplicates.sum(), "duplicated rows") 
    
    def calculate_missing_percentage(self):
        # Calculate and return the percentage of missing values in each column
        missing_values = self.df.isnull().sum() * 100 / len(self.df)
        return missing_values

    def fill_missing_with_mean(self):
        """
        Fill missing values in numeric columns with the mean of the column.
        
        :return: None
        """
         # Iterate over each column in the DataFrame
        for col in self.df.columns:
            # Check if the column is numeric
            if self.df[col].dtype == np.float64:
                # Fill missing values with the mean for numeric columns
               self.df.col  = self.df[col].fillna(self.df[col].mean())
            else:
                # Leave object columns as they are
                pass

    def handle_missing_values(self):
        # drop missing values with the mean
       return self.df.dropna(inplace=True)


class OutlierHandler:
    def __init__(self, df):
        self.df = df

    def detect_and_handle(self):
        # Select only numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        # Calculate Q1 and Q3 (1st and 3rd quartiles) for numeric columns
        Q1 = self.df[numeric_cols].quantile(0.25)
        Q3 = self.df[numeric_cols].quantile(0.75)
        
        # Calculate the Interquartile Range (IQR) for numeric columns
        IQR = Q3 - Q1
        
        # Define the outlier boundaries for numeric columns
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Identify outliers for numeric columns
        outliers = self.df[(self.df[numeric_cols] < lower_bound) | (self.df[numeric_cols] > upper_bound)]
        
        # Drop rows containing outliers from numeric columns
        self.df = self.df.drop(outliers.index)
        
        return self.df