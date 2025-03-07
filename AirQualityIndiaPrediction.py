import pandas as pd
import geopandas as gpd
import folium
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

def plot_geo_map(data, state_column, value_column):
    """Plots a geo-map of India using folium and geopandas."""
    # Load India states shapefile
    india_map = gpd.read_file("https://github.com/geohacker/india/releases/download/v1/states.geojson")
    
    # Aggregate data by state
    state_data = data.groupby(state_column)[value_column].sum().reset_index()
    
    # Merge with geo-data
    india_map = india_map.merge(state_data, left_on='id', right_on=state_column, how='left')
    
    # Create folium map
    m = folium.Map(location=[22, 80], zoom_start=5)
    folium.Choropleth(
        geo_data=india_map,
        name='choropleth',
        data=india_map,
        columns=[state_column, value_column],
        key_on='feature.properties.id',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=value_column
    ).add_to(m)
    
    return m

# Usage
file_pattern = '/Users/deepak.kumar2/Downloads/Archive 2/DL*.csv'  # Adjusted to match multiple files
data_loader = DataLoader(file_pattern)
data_loader.load_files()

print("Dataset Shape:", data_loader.get_shape())
print("Summary Statistics:")
print(data_loader.get_summary())

# Example Usage of Map (Modify 'state' and 'value' column as per dataset)
# map_obj = plot_geo_map(data_loader.data, 'state', 'value_column')
# map_obj.save("india_map.html")  # Save map as HTML
