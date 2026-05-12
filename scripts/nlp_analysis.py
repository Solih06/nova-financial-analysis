from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load a sample of your headlines
headlines = ["Apple stocks soar after earnings", "Market falls amid inflation fears"] 

# Initialize and fit TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
tfidf_matrix = vectorizer.fit_transform(headlines)

# Display keywords with highest scores
feature_names = vectorizer.get_feature_names_out()
print("Top Keywords identified by TF-IDF:", feature_names)