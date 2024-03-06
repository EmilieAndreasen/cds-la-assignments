# cds-la-assignment 2

Assignment 2 for CDS Language Analytics.

By: Emilie Munch Andreasen

## Objectives
### Assignment 2 - Text classification benchmarks
This assignment is about using scikit-learn to train simple (binary) classification models on text data. For this assignment, we'll continue to use the Fake News Dataset that we've been working on in class.

For this exercise, you should write two different notebooks. One should train a logistic regression classifier on the data; the second notebook should train a neural network on the same dataset. Both notebooks should do the following:

- Save the classification report to a text file the folder called out
- Save the trained models and vectorizers to the folder called models

## Technicalities

For this assignment, it is necessary to pip install the modules specified in the requirements.txt file.

## Folder structure

The folders are structured as follows:

| Column | Description|
|--------|:-----------|
| ```in```  | Contains the data used for assignment 2 |
| ```models```  | Contains the outputted models |
| ```out```| Contains all the outputted csv files |
| ```src```  | Contains the Python scripts used for assignment 2, where main.py is the main script |

## References
Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., … Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2

McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

Pedregosa, F., Varoquaux, Ga'el, Gramfort, A., Michel, V., Thirion, B., Grisel, O., … others. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825–2830.

Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.
