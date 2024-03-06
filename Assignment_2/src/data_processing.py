####
# Script for data processing functions
####

#import packages
import pandas as pd
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def load_data(filename):
    data = pd.read_csv(filename, index_col=0)
    data.sample(10)
    return data

def split_vectorizer_fit(data, text, label, max_features, test_size = 0.2, ngram_range = (1,2), lowercase = True, max_df = 0.95, min_df = 0.05):
    # Labeling the data
    X = data[text]
    y = data[label]

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Vectorizing the data and doing feature extraction
    vectorizer = TfidfVectorizer(ngram_range = ngram_range, 
                                lowercase =  lowercase,
                                min_df = min_df, 
                                max_features = max_features) 

    # Training first
    X_train_features = vectorizer.fit_transform(X_train)
    # Then test data
    X_test_features = vectorizer.transform(X_test) 
    return X_train_features, X_test_features, y_train, y_test, vectorizer
