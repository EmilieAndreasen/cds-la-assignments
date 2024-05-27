# Assignment 1: Extracting Linguistic Features Using SpaCy
This repository contains a Python script designed to extract linguistic features from text files in the 'Uppsala Student English Corpus' (USE) using `SpaCy`. Additional functionality for measuring and extracting environmental impact of the code with `CodeCarbon` is also present within the script.

More specifically, the repository contains the main Python script, output CSV files for all the data's sub-folders along with a CodeCarbon emission CSV file, and finally, other relevant files for setting up and running the script (for further details, see *Repository structure*).

### Task Overview
For this assignment, the primary aim was to analyse a corpus of texts from the USE (see *Data Source*) to determine the relative frequency of certain parts of speech and the occurrence of unique named entities. The code had to be able to do the following:  
1. Loop over each text file contained in the data folder and sub-folders.
2. Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjectives, and Adverbs per 10,000 words.
    - Total number of unique Persons (PER), Locations (LOC), and Organisations (ORG) entities.
3. For each sub-folder (e.g., a1, a2, a3, ...), save a table with the extracted information in CSV format.
4. Add `CodeCarbon` functionality to track and measure the environmental impact of the code.  

### Repository Structure
Below is the directory structure of the repository. Make sure to have a similar layout for easy navigation and reproducibility purposes.  
```
.
Assignment_1/
│
├── in/
│   └── USEcorpus/
│       ├── a1/
│       ├── a2/
│       ├── ...
│
├── out/
│   ├── a1_linguistic_features.csv
│   ├── a2_linguistic_features.csv
│   ├── ...
│   ├── emissions.csv
│
├── src/
│ └── main.py
│
├── README.md
├── requirements.txt
├── run.sh
└── setup.sh
```

## Data Source
The data used for this assignment is a collection of essays from the Department of English, Uppsala University, spanning the years 1999-2001. The essays are organised by essay type (i.e., the sub-folders correspond to the type of essay, numbered a1-a5, b1-b8, and c1). Specifically, the types of essays described in the USEmanual are:  

**First-term essays:**
- **a1.** Evaluation  
- **a2.** Argumentation
- **a3.** Reflections
- **a4.** Literature course assignment
- **a5.** Culture course assignment

**Second-term essays:**
- **b1.** Causal analysis
- **b2.** Argumentation
- **b3.** Short papers in English linguistics
- **b4.** English literature
- **b5.** American literature
- **b6.** Taboo, not taboo
- **b7.** Politics and education
- **b8.** School visit reports

**Third-term essays:**
- **c1.** Literature course assignments

For more details about the data and the types of essays, visit the following [website](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). To use the data, simply follow the link, download the corpus, unzip it, and save it to the `in` folder.

## Steps for Re-running the Analysis
### Setting Up and Running the Code
To re-run the analysis, follow the steps outlined below:

**1. Download and Prepare the Repository:**  
Start by downloading the zip file and unzip it in your desired location. When done, navigate to the `Assignment_1` folder.  
(Ensure that the dataset of text files is downloaded and placed in the `in` folder, as specified above.)

**2. Set Up the Virtual Environment:**  
Execute the following command in your terminal to set up the Python virtual environment and install the needed dependencies.
```
bash setup.sh 
```

**3. Activate the Virtual Environment and Run the Code:**  
Run the script by executing the following command in your terminal. It will activate the virtual environment, run the Python script with the command line arguments that you provide, and then deactivate the environment when finished.
```
bash run.sh --dataset_path=./in/USEcorpus --output_dir=./out
```

### Command Line Arguments
These are the two args that can be passed:  
**--dataset_path:** Path to the dataset directory containing sub-folders with text files.  
**--output_dir:** Directory where the results CSV will be saved, defaults to `../out`.  

## Summary of Key Points from Outputs
The outputs for two of the CSV files are presented below to illustrate what the results generally show. The remaining outputs can be viewed in the `out` folder for detailed examination.

**B6 Linguistic Features**  
| Filename    | RelFreq NOUN | RelFreq VERB | RelFreq ADJ | RelFreq ADV | Unique PER | Unique LOC | Unique ORG |
|-------------|--------------|--------------|-------------|-------------|------------|------------|------------|
| 0107.b6.txt | 1907.43      | 1332.40      | 967.74      | 448.81      | 1          | 0          | 1          |
| 0137.b6.txt | 1937.87      | 1390.53      | 1005.92     | 591.72      | 1          | 0          | 0          |
| 0151.b6.txt | 1650.75      | 1446.11      | 736.70      | 613.92      | 3          | 0          | 0          |
| 0157.b6.txt | 1405.75      | 1613.42      | 814.70      | 734.82      | 2          | 0          | 0          |
| 0158.b6.txt | 1718.75      | 1419.27      | 846.35      | 742.19      | 2          | 0          | 0          |
| 0178.b6.txt | 1966.82      | 1255.92      | 1007.11     | 627.96      | 1          | 0          | 2          |
| 0185.b6.txt | 1830.07      | 1486.93      | 849.67      | 473.86      | 2          | 0          | 0          |
| 0198.b6.txt | 1693.29      | 1309.90      | 798.72      | 495.21      | 3          | 0          | 0          |
| 0219.b6.txt | 1926.75      | 1496.82      | 589.17      | 429.94      | 1          | 0          | 0          |
| 0223.b6.txt | 1892.27      | 1339.78      | 759.67      | 704.42      | 2          | 0          | 0          |
| 0238.b6.txt | 1522.12      | 1557.52      | 884.96      | 460.18      | 2          | 0          | 0          |
| 0318.b6.txt | 2057.47      | 1149.43      | 1000.00     | 528.74      | 5          | 0          | 2          |  

The text files from the 'Taboo, not taboo' display variation in relative frequencies of nouns, verbs, adjectives, and adverbs, along with counts of unique named entities. For instance, 0137.b6.txt has a high relative frequency of nouns (i.e, 1937.87) and verbs (i.e., 1390.53), while 0318.b6.txt has the highest noun frequency (i.e., 2057.47) and identifies 5 unique persons.

**C1 Linguistic Features**  
| Filename    | RelFreq NOUN | RelFreq VERB | RelFreq ADJ | RelFreq ADV | Unique PER | Unique LOC | Unique ORG |
|-------------|--------------|--------------|-------------|-------------|------------|------------|------------|
| 0140.c1.txt | 1865.64      | 1106.81      | 560.66      | 478.49      | 38         | 0          | 5          |
| 0165.c1.txt | 2163.39      | 1013.62      | 721.13      | 353.00      | 27         | 0          | 3          |
| 0200.c1.txt | 1439.11      | 1248.46      | 793.36      | 621.16      | 17         | 0          | 8          |
| 0219.c1.txt | 1665.33      | 1176.94      | 680.54      | 584.47      | 26         | 0          | 6          |
| 0238.c1.txt | 1315.79      | 1400.38      | 479.32      | 347.74      | 18         | 0          | 3          |
| 0501.c1.txt | 1474.46      | 1227.35      | 551.89      | 510.71      | 14         | 0          | 5          |
| 0502.c1.txt | 1581.36      | 1459.13      | 519.48      | 488.92      | 15         |  0          | 5          |
  
In this CSV, there are also several variations present for the linguistic features. 0140.c1.txt stands out with a high number of unique persons, namely 38, and a substantial relative frequency of nouns (i.e., 1865.64).  

Overall, the CSV files do not provide great/deep insights on their own, but the extracted linguistic information does allow for a solid starting point for further future analyses. 

## Discussion of Limitations and Possible Steps for Improvement  
This script provides insights into extracting linguistic features from text files using `SpaCy`. However, certain limitations should be considered to further enhance the model's performance in the future.  

Firstly, this script relies on `SpaCy` and its English model (i.e., `en_core_web_md`), which may not be fully optimised for this specific corpus. This could lead to potential problems or draw-backs when using it. To address this, fine-tuning could be used on the model. Additionally, a NER (i.e., named entity recognition) model could also be used to help improve performance.  

Another limitation to take into account, is that the script processes files sequentially, which may not be very efficient for larger datasets. This could be fixed by instead implementing parallel processing to reduce computation time and improve efficiency that way.  

Finally, as the current results are not that easily understandable or insightful, adding visualisation tools, such as graphs, could provide a better understanding of the data.  

In short, while the current script can extract linguistic features from text files, addressing the above limitations and implementing the suggested improvement strategies could lead to a more robust and better performing script.

## CodeCarbon Tracking
As mentioned earlier, `CodeCarbon` has been implemented to measure and extract the environmental impact that the code had while running. A CSV file containing information pertaining to this - called 'emissions.csv' - is therefore also present in this repository.  

For a detailed analysis of these results along with results for the other assignments, see `Assignment 5`.