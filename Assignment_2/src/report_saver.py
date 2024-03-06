#### 
# Script for saving report and models
####

#import packages
import os
import pandas as pd
from sklearn import metrics
from joblib import dump, load

def save_models(classifier, vectorizer, output_path):
    #Save the classifier and vectorizer
    dump(classifier, os.path.join(output_path, f"classifier{classifier}.joblib"))
    dump(vectorizer, os.path.join(output_path, "vectorizer.joblib"))


def save_report(y_test, y_pred, output_path):
    #Save the classification report
    class_report = metrics.classification_report(y_test, y_pred)
    
    with open(output_path, "w") as report_file:
        report_file.write(class_report)
    print("Report file saved")