######
# Training logictic regression classifier on data
######

# Importing packages
# System tools
import os
import sys
sys.path.append("..")

# Data munging tools
import pandas as pd

# Machine learning stuff
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

# Visualisation
import matplotlib.pyplot as plt

# Loading the data
filename = os.path.join("..","in","fake_or_real_news.csv")

data = pd.read_csv(filename, index_col=0)

data.sample(10)

# Labeling the data
X = data["text"]
y = data["label"]

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X,           # texts for the model
                                                    y,          # classification labels
                                                    test_size=0.2,   # create an 80/20 split
                                                    random_state=9) # random state for reproducibility

# Vectorizing the data and doing feature extraction
vectorizer = TfidfVectorizer(ngram_range = (1,2),     # unigrams and bigrams (1 word and 2 word units)
                             lowercase =  True,       # specifying transformation of lower case letters
                             max_df = 0.95,           # remove very common words (top 5%)
                             min_df = 0.05,           # remove very rare words (bottom 5%)
                             max_features = 100)      # keep only top 100 features

### Fitting the data
# first we fit to the training data...
X_train_feats = vectorizer.fit_transform(X_train)

#... then do it for our test data
X_test_feats = vectorizer.transform(X_test)

# get feature names
feature_names = vectorizer.get_feature_names_out()

# Setting classifier 
classifier = LogisticRegression(random_state=9).fit(X_train_feats, y_train)

# Making predictions using classifier
y_pred = classifier.predict(X_test_feats)

# Making classification report 
class_report = metrics.classification_report(y_test, y_pred)

from joblib import dump, load
dump(classifier, "../models/LR_classifier.joblib")
dump(vectorizer, "../models/tfidf_vectorizer.joblib")

# Saving the report as a text file
# Save the report to a text file
with open("classification_report.txt", "w") as report_file:
    report_file.write(class_report)