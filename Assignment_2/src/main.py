####
# Main script for Assignment 2
####

# Importing packages
# System tools
import os
import sys
sys.path.append("..")

# Cutom/local functions
from data_processing import split_vectorizer_fit, load_data
from classifying import train_classify
from report_saver import save_models, save_report

# Loading the data
data = load_data(os.path.join("in","fake_or_real_news.csv"))

X_train_features, X_test_features, y_train, y_test, vectorizer = split_vectorizer_fit(data, "text", "label", max_features=500)

#Setting classifiers (both logistic regression and NN)
classifier_logreg = train_classify(X_train_features, y_train, classifier_type="logreg")
classifier_nn = train_classify(X_train_features, y_train, classifier_type="mlp")

#Making predictions using classifier
y_pred_logreg = classifier_logreg.predict(X_test_features)
y_pred_nn = classifier_nn.predict(X_test_features)

#Saving models
save_models(classifier_logreg, vectorizer, os.path.join("models"))
save_models(classifier_nn, vectorizer, os.path.join("models"))

#Saving classification report 
save_report(y_test, y_pred_logreg, os.path.join("out", "logreg_report.txt"))
save_report(y_test, y_pred_nn, os.path.join("out", "nn_report.txt"))
