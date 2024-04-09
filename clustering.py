

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Assuming df is your DataFrame and it already contains the necessary data
df = ...

# If 'StartLocation', 'Personality', 'Interests', 'Destination' are categorical, convert them to numerical
le = LabelEncoder()
categorical_features = ['StartLocation', 'Personality', 'Interests', 'Destination']

for feature in categorical_features:
    if df[feature].dtype == 'object':
        df[feature] = le.fit_transform(df[feature])

# Define the model
kmeans = KMeans(n_clusters=3, random_state=0)  # Change n_clusters as needed

# Fit the model
kmeans.fit(df)

# Get the cluster assignments
df['Cluster'] = kmeans.labels_

# Now, df['Cluster'] contains the cluster assignments