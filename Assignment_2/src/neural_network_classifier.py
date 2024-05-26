#####
# Assignment 2 - Text Classification Benchmarks
# Author: Emilie Munch Andreasen
# Date: 20-05-2024
#####

# Importing packages
import os
import argparse
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from joblib import dump
from codecarbon import EmissionsTracker

# Defining argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description='Train a neural network classifier on text data.')
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the CSV dataset file')
    parser.add_argument('--output_dir', type=str, default='../out', help='Output directory for the reports and emission files')
    parser.add_argument('--model_dir', type=str, default='../models', help='Directory to save the trained models and vectorizers')
    parser.add_argument('--max_features', type=int, default=500, help='Max number of features for the vectorizer')
    parser.add_argument('--test_size', type=float, default=0.2, help='Part of the dataset to include in the test split')
    parser.add_argument('--activation', type=str, default='logistic', help='Activation function for the neural network')
    parser.add_argument('--hidden_layer_sizes', type=tuple, default=(20,), help='Hidden layer sizes for the neural network')
    parser.add_argument('--max_iter', type=int, default=1000, help='Max number of iterations for the neural network')
    return parser.parse_args()

##### 
# Defining Functions
#####

def load_data(filename):
    """
    Loads data from a specified CSV file.

    Parameters:
        filename (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded data.
    """
    data = pd.read_csv(filename)
    return data

def split_vectorizer_fit(data, text_column, label_column, max_features, test_size):
    """
    Splits the data into training and testing sets and then vectorizes the text data.

    Parameters:
        data (DataFrame): The dataset containing text and labels.
        text_column (str): The name of the column containing text data.
        label_column (str): The name of the column containing labels.
        max_features (int): Max number of features for the vectorizer.
        test_size (float): Part of the dataset to include in the test split.

    Returns:
        tuple: Vectorized training and testing data, labels, and the vectorizer.
    """
    X = data[text_column]
    y = data[label_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2), 
        lowercase=True,
        min_df=0.05, 
        max_features=max_features
    )
    X_train_features = vectorizer.fit_transform(X_train)
    X_test_features = vectorizer.transform(X_test)
    
    return X_train_features, X_test_features, y_train, y_test, vectorizer

def train_classifier(X_train_features, y_train, activation, hidden_layer_sizes, max_iter):
    """
    Trains a neural network classifier.

    Parameters:
        X_train_features (sparse matrix): Vectorized training data.
        y_train (array): Training labels.
        activation (str): Activation function for the neural network.
        hidden_layer_sizes (tuple): Hidden layer sizes for the neural network.
        max_iter (int): Max number of iterations for the neural network.

    Returns:
        MLPClassifier: Trained neural network classifier.
    """
    classifier = MLPClassifier(
        activation=activation, 
        hidden_layer_sizes=hidden_layer_sizes, 
        max_iter=max_iter, 
        random_state=42
    )
    classifier.fit(X_train_features, y_train)
    return classifier

def save_models(classifier, vectorizer, model_dir):
    """
    Saves the trained classifier and vectorizer.

    Parameters:
        classifier (MLPClassifier): The trained classifier.
        vectorizer (TfidfVectorizer): The vectorizer.
        model_dir (str): Directory to save the models.
    """
    os.makedirs(model_dir, exist_ok=True)
    classifier_path = os.path.join(model_dir, 'neural_network_classifier.joblib')
    vectorizer_path = os.path.join(model_dir, 'vectorizer_neural.joblib')
    dump(classifier, classifier_path)
    dump(vectorizer, vectorizer_path)
    print(f"Model saved at: {classifier_path}")
    print(f"Vectorizer saved at: {vectorizer_path}")

def save_report(y_test, y_pred, output_dir):
    """
    Saves the classification report to a text file.

    Parameters:
        y_test (array): True labels for the test data.
        y_pred (array): Predicted labels for the test data.
        output_dir (str): Directory to save the report.
    """
    os.makedirs(output_dir, exist_ok=True)
    class_report = metrics.classification_report(y_test, y_pred)
    report_path = os.path.join(output_dir, 'neural_network_report.txt')
    with open(report_path, 'w') as report_file:
        report_file.write(class_report)
    print(f"Report saved at: {report_path}")

#####
# Main Function
#####

def main():
    args = parse_args()
    tracker = EmissionsTracker(
        project_name="text_classification_benchmarks", 
        experiment_id="neural_network", 
        output_dir=args.output_dir,
        output_file=f"emissions_neural.csv"
    )
    tracker.start()
    
    tracker.start_task("load_data")
    data = load_data(args.dataset_path)
    tracker.stop_task()

    tracker.start_task("split_vectorizer_fit")
    X_train_features, X_test_features, y_train, y_test, vectorizer = split_vectorizer_fit(data, "text", "label", args.max_features, args.test_size)
    tracker.stop_task()

    tracker.start_task("train_classifier")
    classifier = train_classifier(X_train_features, y_train, args.activation, args.hidden_layer_sizes, args.max_iter)
    tracker.stop_task()

    tracker.start_task("save_models")
    save_models(classifier, vectorizer, args.model_dir)
    tracker.stop_task()

    tracker.start_task("predict_and_save_report_neural")
    y_pred = classifier.predict(X_test_features)
    save_report(y_test, y_pred, args.output_dir)
    tracker.stop_task()

    tracker.stop()

if __name__ == "__main__":
    main()