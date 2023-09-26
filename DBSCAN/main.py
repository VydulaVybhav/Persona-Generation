import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load spending data
spending_data = pd.read_csv('spending_data.csv')

# Load music data
music_data = pd.read_csv('music_data.csv')

# Combine both datasets if they share a common identifier (e.g., user ID)
# You should adjust this based on your actual data structure
combined_data = spending_data.merge(music_data, on='User')

# Define the features for clustering (e.g., spending attributes, music attributes)
spending_features = ['Weekly Spend']
music_features = ['danceability', 'energy', 'acousticness']

# Preprocess the features (standardize them)
preprocessor = ColumnTransformer(
    transformers=[
        ('spending', StandardScaler(), spending_features),
        ('music', StandardScaler(), music_features)
    ])

# Create a DBSCAN clustering pipeline
dbscan_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('dbscan', DBSCAN(eps=0.5, min_samples=5))  # Adjust hyperparameters as needed
])

# Fit the DBSCAN model to the data
cluster_labels = dbscan_pipeline.fit_predict(combined_data)

# Add the cluster labels to the combined dataset
combined_data['cluster'] = cluster_labels

# Get unique cluster labels
unique_clusters = combined_data['cluster'].unique()

# Create and save separate Excel files for each cluster
for cluster_label in unique_clusters:
    cluster_data = combined_data[combined_data['cluster'] == cluster_label]
    file_name = f'cluster_{cluster_label}.xlsx'  # Customize the file name as needed
    cluster_data.to_excel(file_name, index=False)

print("Cluster files saved.")
