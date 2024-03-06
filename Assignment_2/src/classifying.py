#### 
# Script for classifying
####

#import packages
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

def train_classify(X_train_features, y_train, classifier_type, random_state=42, activation='logistic', hidden_layer_sizes=(20,), max_iter=1000):
    if classifier_type == 'logreg':
        classifier = LogisticRegression(random_state = random_state)
    elif classifier_type == 'mlp':
        classifier = MLPClassifier(activation = activation,
                                    hidden_layer_sizes = hidden_layer_sizes,
                                    max_iter = max_iter,
                                    random_state = random_state)    
    else:
        raise ValueError("Inappropriate classifier type. Expected 'logreg' or 'mlp'.")
    
    fit_classifier = classifier.fit(X_train_features, y_train)
    return fit_classifier