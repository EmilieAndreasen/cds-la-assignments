# Assignment 3: Query Expansion with Word Embeddings
This repository contains a Python script designed to perform query expansion using word embeddings to analyse different artists' song lyrics. Additional functionality for measuring and extracting environmental impact of the code with `CodeCarbon` is also present within the script.

More specifically, the repository contains the main Python script, output text files along with CodeCarbon emission CSV files, and finally, other relevant files for setting up and running the script (for further details, see *Repository structure*).

### Task Overview
For this assignment, the primary aim was to analyse a corpus of song lyrics (see *Data Source*) to determine the percentage of songs by a specific artist that contain a given word or its related words using word embeddings. The code had to be able to do the following:  
1. Load the song lyric data.
2. Preprocess the text data.
3. Download/load a pretrained word embedding model using Gensim.
4. Take a specified word and identify the most similar words via word embeddings.
5. Calculate the percentage of songs by the specified artist that feature these.
6. Save the results in an "easy-to-understand" way.
7. Add `CodeCarbon` functionality to track and measure the environmental impact of the code.  

### Repository Structure
Below is the directory structure of the repository. Make sure to have a similar layout for easy navigation and reproducibility purposes.  
```
.
Assignment_3/
│
├── in/
│   └── Spotify_Million_Song_Dataset_exported.csv
│
├── out/
│   ├── emissions_base_2e62c1b3-d751-4db3-b173-d3859df3b1ec
│   ├── emissions_base_27bef7aa-4e38-4ef2-99d5-efade418d544
│   ├── emissions.csv
│   ├── Nina_Simone_burn_results.txt
│   ├── Nina_Simone_love_results.txt
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
The data used for this assignment is a collection of songs, accompanied by song lyrics and songs' artist(s), all of which are of string type. The dataset contains around 57,650 songs in total.

For more details about the data visit the following [website](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs). To use the data, simply follow the link, download the dataset, and save it to the `in` folder. Then ensure that there are '_' instead of spaces in the dataset's name.

## Steps for Re-running the Analysis
### Setting Up and Running the Code
To re-run the analysis, follow the steps outlined below:

**1. Download and Prepare the Repository:**  
If the attachment has not already been downloaded and unzipped, then start by downloading the zip file and unzip it in your desired location. When done, navigate to the `Assignment_3` folder.  
(Ensure that the 'Spotify Million Song Dataset_exported' dataset is downloaded and placed in the `in` folder, as specified above.)

**2. Set Up the Virtual Environment:**  
Execute the following command in your terminal to set up the Python virtual environment and install the needed dependencies.
```
bash setup.sh 
```

**3. Activate the Virtual Environment and Run the Code:**  
Run the script by executing the following command in your terminal. It will activate the virtual environment, run the Python script with the command line arguments that you provide, and then deactivate the environment when finished.
```
bash run.sh --dataset_path=./in/Spotify_Million_Song_Dataset_exported.csv --output_dir=./out --artist=<"artist"> --word=<word>
```

### Command Line Arguments
These are the arguments that can be passed:  
**--dataset_path:** Path to the dataset file containing the CSV files.  
**--output_dir:** Directory where the results text file and emission files will be saved, defaults to `../out`.  
**--artist:** The music artist(s) to inspect.  
**--word:** The search word to expand.  

## Summary of Key Points from Outputs
A summary of what the text file outputs for the query expansion analysis show are presented below.  

**Nina Simone 'Burn':**  
| Artist       | Word  | Percentage Songs with Related Words |
|--------------|-------|-------------------------------------|
| Nina Simone  | burn  | 20.25%                              |  

For the analysis with the chosen word 'burn', it was found that 20.25% of the chosen artist's, namely Nina Simone, songs contain words related to 'burn'. The similar words identified for the query expansion include terms like 'burning', 'smoke', 'dust', suggesting that themes of heat and destruction may feature in around ⅕ of Nina Simone's songs. However, it should be noted that among the other similar terms are also 'tear', 'stones', 'rush', and 'blowing', indicating that the context of 'burn' might extend to other concepts and themes.

**Nina Simone 'Love':**  
| Artist       | Word  | Percentage Songs with Related Words |
|--------------|-------|-------------------------------------|
| Nina Simone  | love  | 98.73%                              |  

For the analysis with the word 'love',' it was found that 98.73% of Nina Simone's songs contain words related to 'love'. This is a high percentage, which may indicate that love is a predominant theme in her music. Some of the identified similar words for the query expansion did also include terms like 'dream(s)', 'life', 'loves', and 'soul', but notably, 'me' and 'my' were also identified. Consequently, the high percentage may also arise because of words like the latter two being associated with 'love'.

## Discussion of Limitations and Possible Steps for Improvement  
This script offers valuable insights into the linguistic and thematic content of artists' (in this case, Nina Simone's) music through query expansion using word embeddings. However, there are several limitations and potential improvements to consider for enhancing the accuracy and applicability of the analysis.

Firstly, the script relies on a pretrained word embedding model from `Gensim` (i.e., `glove-wiki-gigaword-50`). While this model is useful for general language patterns, it may not be best choice for analysing song lyrics, which can contain unique vocabulary and various stylistic elements. As such, fine-tuning the model on a corpus of song lyrics could help improve the relevance of the similar words identified for the query expansion.

Another limitation to consider is that the accuracy of the identified similar words is based on general language patterns and may therefore not always align perfectly with the actual thematic content of the songs. This can lead to the inclusion of less relevant words in the query expansion, affecting the accuracy of the analysis. To address this the preprocessing steps could be improved. For instance, better handling of contractions, slang, and other more poetic language, could enhance the accuracy of the text analysis. Another idea could be to incorporate more context/semantic meaning-aware techniques like BERT (i.e., Bidirectional Encoder Representations from Transformers language model) or GPT (i.e., Generative Pre-trained Transformer language model) for query expansion might also identify more relevant similar words.

Finally, the current results are saved as text to a text file, which may not be the most optimal format for saving the data. Instead, saving the data to a table, whether in a CSV file or some other format, could help provide a clearer and more intuitive understanding of the results. Additionally, if it is implemented, it can allow for further analyses to be done more effectively.

In short, while the current script provides a solid foundation for linguistic and thematic analysis of song lyrics using query expansion with word embeddings, addressing the mentioned limitations and implementing the suggested improvements would enhance its accuracy, efficiency, and overall robustness.

## CarbonCode Tracking
As mentioned earlier, `CodeCarbon` has been implemented to measure and extract the environmental impact that the code had while running. Multiple CSV files containing information pertaining to this are therfore also present in this repository.  

For a detailed analysis of these results along with results for the other assignments, see `Assignment 5`.