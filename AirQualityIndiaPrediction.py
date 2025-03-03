import pandas as pd
import glob

class DataLoader:
    def __init__(self, file_pattern):
        self.file_pattern = file_pattern
        self.file_paths = glob.glob(self.file_pattern)  # Get all matching files
        self.data = None
    
    def load_files(self):
        """Reads and merges all specified CSV files."""
        if not self.file_paths:
            print("No files found matching the pattern.")
            return
        df_list = [pd.read_csv(file) for file in self.file_paths]
        self.data = pd.concat(df_list, ignore_index=True)
    
    def get_shape(self):
        """Returns the shape of the dataset."""
        if self.data is not None:
            return self.data.shape
        return None
    
    def get_summary(self):
        """Returns summary statistics of the dataset."""
        if self.data is not None:
            return self.data.describe()
        return None

# Usage
file_pattern = '/Users/deepak.kumar2/Downloads/Archive 2/DL*.csv'  # Adjusted to match multiple files
data_loader = DataLoader(file_pattern)
data_loader.load_files()

print("Dataset Shape:", data_loader.get_shape())
print("Summary Statistics:")
print(data_loader.get_summary())
