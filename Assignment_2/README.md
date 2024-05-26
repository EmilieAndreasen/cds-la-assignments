# Assignment 2: Text Classification Benchmarks
This repository contains Python-based scripts designed to train and evaluate text classification models on the 'Fake or Real News' dataset using two approaches:
- **Logistic Regression Classifier:** Employs logistic regression to predict whether a news article is real or fake based on text features extracted using TF-IDF vectorization.
- **Neural Network Classifier:** Employs a neural network to predict whether a news article is real or fake using TF-IDF vectorization along with complex model architecture with hidden layers.    

Additional functionality for measuring and extracting environmental impact of the code with `CodeCarbon` is also present within the script.

More specifically, the repository contains two Python scripts - one for each classifier - output files for classification reports along with CodeCarbon emission CSV files, models and vectorizers, and finally, other relevant files for setting up and running the script (for further details, see *Repository structure*).

### Task Overview
For this assignment, the primary objective was to train and evaluate simple classification models on structured text data (see *Data Source*) using `scikit-learn`. The code had to be able to do the following:  
1. Write two different scripts, one for training a logistic regression classifier and another for training a neural network classifier.
2. Save classification reports for both classifiers to text files in the `out` folder.
3. Save the trained models and vectorizers to the `models` folder.
4. Add `CodeCarbon` functionality to track and measure the environmental impact of the code. 

### Repository Structure
Below is the directory structure of the repository. Make sure to have a similar layout for easy navigation and reproducibility purposes.  
```
.
Assignment_2/
│
├── in/
│   └── fake_or_real_news.csv
│
├── out/
│   ├── emissions_base_5a7f2be7-24ab-47dc-b2e1-d26733703d45.csv
│   ├── emissions_base_cba4807f-da1d-4bcc-b7f3-ce70f0be0750.csv
│   ├── emissions_logreg.csv
│   ├── emissions_neural.csv
│   ├── logistic_regression_report.txt
│   ├── neural_network_report.txt
│
├── src/
│   ├── logistic_reg_classifier.py
│   ├── neural_network.py
│
├── README.md
├── requirements.txt
├── run.sh
└── setup.sh
```

## Data Source
The data used for this assignment is a collection of news that have been organised into structured text data. Accompanying each news media is a label indicating it as either 'FAKE' or 'REAL'.

For more details about the data visit the following [website](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news). To use the data, simply follow the link, download the dataset, and save it to the `in` folder.

## Steps for Re-running the Analysis
### Setting Up and Running the Code
To re-run the analysis, follow the steps outlined below:

**1. Download and Prepare the Repository:**  
If the attachment has not already been downloaded and unzipped, then start by downloading the zip file and unzip it in your desired location. When done, navigate to the `Assignment_2` folder.  
(Ensure that the 'Fake or Real News' dataset is downloaded and placed in the `in` folder, as specified above.)

**2. Set Up the Virtual Environment:**  
Execute the following command in your terminal to set up the Python virtual environment and install the needed dependencies.
```
bash setup.sh 
```

**3. Activate the Virtual Environment and Run the Code:**  
Run the script by executing the following command in your terminal. It will activate the virtual environment, run the chosen Python script with the command line arguments that you provide, and then deactivate the environment when finished.
```
bash run.sh [script_name] --dataset_path=./in/fake_or_real_news.csv --output_dir=./out --model_dir=./models
```
Replace [script_name] with either **'logistic_reg_classifier.py'** or **'neural_network_classifier.py'** to choose which script to run.  

### Command Line Arguments
These are the args that can be passed in both scripts:  
**--dataset_path:** Path to the CSV dataset file.  
**--output_dir:** Directory where the results and emission CSV files will be saved, defaults to `../out`.  
**--model_dir:** Directory to save the trained models and vectorizers, defaults to `../models`.  
**--max_features:** Maximum number of features for the vectorizer, defaults to 500.  
**--test_size:** Part of the dataset to include in the test split, defaults to 0.2.  

Additionally, the neural network script accepts:  
**--activation:** Activation function for the neural network, defaults to 'logistic'.  
**--hidden_layer_sizes:** Hidden layer sizes for the neural network, defaults to (20,).  
**--max_iter:** Max number of iterations for the neural network, defaults to 1000.  

## Summary of Key Points from Outputs
The outputs for the text classification benchmarks using logistic regression and neural network models are presented below.  
**Logistic Regression Classifier:**  
| Class  | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| FAKE   | 0.89      | 0.88   | 0.88     | 628     |
| REAL   | 0.88      | 0.89   | 0.89     | 639     |
| **Accuracy** |       |        | 0.88     | 1267    |
| **Macro Avg**| 0.88  | 0.88   | 0.88     | 1267    |
| **Weighted Avg**| 0.88 | 0.88   | 0.88     | 1267    |  

The logistic regression classifier showed an overall accuracy of 88%, with both 'FAKE' and 'REAL' classes displaying balanced precision and recall scores, showing that the model can produce consistent classifications across both categories.  

**Neural Network Classifier:**  
| Class  | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| FAKE   | 0.90      | 0.87   | 0.88     | 628     |
| REAL   | 0.87      | 0.91   | 0.89     | 639     |
| **Accuracy** |       |        | 0.89     | 1267    |
| **Macro Avg**| 0.89  | 0.89   | 0.89     | 1267    |
| **Weighted Avg**| 0.89 | 0.89   | 0.89     | 1267    |  

The neural network classifier performed slightly better with an overall accuracy of 89%. It showed a higher precision for the 'FAKE' class and a higher recall for the 'REAL' class, demonstrating that this model also does well in distinguishing between the two categories.

All in all, the neural network classifier showed a slight marginal improvement over the logistic regression classifier in terms of accuracy and balance between precision and recall.

## Discussion of Limitations and Possible Steps for Improvement  
The two scripts in this assignment provide insights into training, evaluating, and comparing text classification models (i.e., logistic regression and neural network classifiers). Yet, there are also some limitations present which should be considered. 

First of all, the current models did not undergo thorough tuning of their hyperparameters, and as such, can benefit from doing so in future iterations. By doing so, both models may end up performing even better.  

Secondly, another important aspect is how the features were created/extracted from the text. The current implementation uses TF-IDF vectorization, which turns text into a "meaningful" representation of numbers, but does not fully capture the meaning and context of the words (i.e., it does not consider/capture the semantic meaning of the words). Exploring other methods like word embeddings, which can identify the relationships between words better, could help improve how well the models perform. Additionally, increasing the number of features considered might also help.

Another point is that in terms of computational efficiency, the scripts process the dataset sequentially, which is not that efficient for larger datasets. Therefore, by implementing parallel processing or using other more efficient data handling methods, the scripts could reduce computation time and resource usage.

Finally, visualisation and interpretability are also key areas for improvement. Adding visualisation tools could provide a better understanding of the models' performance and the underlying data patterns. This would also expand upon the current results and allow for better and more robust interpretations of them.

In short, while the current two scripts provide well-performing approaches to text classification, addressing the above limitations and implementing the suggested improvement strategies could lead to two more robust and better performing scripts.

## CarbonCode Tracking
As mentioned earlier, `CodeCarbon` has been implemented to measure and extract the environmental impact that the code had while running. Multiple CSV files containing information pertaining to this are therfore also present in this repository.  

For a detailed analysis of these results along with results for the other assignments, see `Assignment 5`.