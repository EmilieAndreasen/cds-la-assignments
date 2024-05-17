# Assignment 1: Extracting Linguistic Features Using SpaCy
This repository contains a Python script designed to extract linguistic features from text files using SpaCy.

More specifically, the repository contains the main Python script, output CSV files for all the data's sub-folders along with a CodeCarbon emission CSV file, and other relevant files for setting up and running the script (for further details, see *Repository structure*)

### Task Overview
For this assignment, the primary aim was to analyse a corpus of texts to determine the relative frequency of certain parts of speech and the occurrence of unique named entities.


### Repository Structure
Below is the directory structure of the repository. Make sure to have a similar layout for easy navigation and reproducibility purposes.  


## Data Source

## Steps for Re-running the Analysis
### Setting Up and Running the Code
To re-run the analysis, follow the steps outlined below:

**1. Download and Prepare the Repository:**  
Start by downloading the zip file and unzip it in your desired location. When done, navigate to the `Assignment_1` folder.  
(Ensure that the dataset of XXX is downloaded and placed in the `in` folder, as specified above.)

**2. Set Up the Virtual Environment:**  
Execute the following command in your terminal to set up the Python virtual environment and install the needed dependencies.
```
bash setup.sh 
```

**3. Activate the Virtual Environment and Run the Code:**  
Run the script by executing the following command in your terminal. It will activate the virtual environment, run the Python script with the command line arguments that you provide, and then deactivate the environment when finished.
```
bash run.sh --dataset_path=./in/newspapers --output_dir=./out
```

### Command Line Arguments
These are the two args that can be passed:  
**--dataset_path:** Path to the directory containing the sub-folder with images.  
**--output_dir:** Optional. Directory where the results CSV and plots will be saved, defaults to ../out.  