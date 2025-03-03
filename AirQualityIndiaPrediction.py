import pandas as pd
import glob

class DataLoader:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data = None
    
    def load_files(self):
        """Reads and merges all specified CSV files."""
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
file_paths = ['/mnt/data/DL039.csv', '/mnt/data/DL040.csv']
data_loader = DataLoader(file_paths)
data_loader.load_files()

print("Dataset Shape:", data_loader.get_shape())
print("Summary Statistics:")
print(data_loader.get_summary())
