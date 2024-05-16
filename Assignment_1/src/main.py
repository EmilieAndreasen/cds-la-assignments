######
# Assignment 1 - Extracting Linguistic Features Using SpaCy
# Author: Emilie Munch Andreasen
# Date: 16-05-2024
######

# Importing libraries
import argparse
import os
import spacy
import pandas as pd
import re
from codecarbon import EmissionsTracker

# Defining argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract linguistic features from text files.')
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the dataset directory containing sub-folders with text files')
    parser.add_argument('--output_dir', type=str, default='../out', help='Output directory for the resulting CSV files')
    return parser.parse_args()

# Loading spacy
nlp = spacy.load("en_core_web_md")

##### 
# Defining Functions
#####

def cleaning_text(text):
    """
    Cleans the input text by removing any content within '<>'.

    Parameters:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    return re.sub(r'<.*?>', '', text)

def process_text(file_path, nlp):
    """
    Processes a text file to extract linguistic features.

    Parameters:
        file_path (str): Path to the text file.
        nlp (spacy.Language): The SpaCy language model.

    Returns:
        dict: Extracted linguistic features.
    """
    with open(file_path, 'r', encoding='latin1') as f:
        text = cleaning_text(f.read())

    doc = nlp(text)

    pos_counts = {'NOUN': 0, 'VERB': 0, 'ADJ': 0, 'ADV': 0}
    unique_entities = {'PERSON': set(), 'LOC': set(), 'ORG': set()}

    for token in doc:
        if token.pos_ in pos_counts:
            pos_counts[token.pos_] += 1
    for ent in doc.ents:
        if ent.label_ in unique_entities:
            unique_entities[ent.label_].add(ent.text)

    total_words = len([token for token in doc if token.is_alpha])
    relative_freq = {pos: ((count / total_words) * 10000) for pos, count in pos_counts.items()}

    data = {
        'RelFreq NOUN': relative_freq.get('NOUN', 0),
        'RelFreq VERB': relative_freq.get('VERB', 0),
        'RelFreq ADJ': relative_freq.get('ADJ', 0),
        'RelFreq ADV': relative_freq.get('ADV', 0),
        'Unique PER': len(unique_entities['PERSON']),
        'Unique LOC': len(unique_entities['LOC']),
        'Unique ORG': len(unique_entities['ORG']),
    }
    return data

#####
# Main Function
#####

def main():
    args = parse_arguments()

    dataset_path = args.dataset_path
    output_path = args.output_dir

    os.makedirs(output_path, exist_ok=True)

    for directory in sorted(os.listdir(dataset_path)):
        subfolder = os.path.join(dataset_path, directory)
        filenames = sorted(os.listdir(subfolder))

        results = []

        # Emissions tracker
        tracker = EmissionsTracker(project_name=f"emissions_{directory}", 
                                   experiment_id=f"emissions_{directory}",
                                   output_dir=os.path.join(output_path),
                                   output_file=f"emissions.csv")
        tracker.start()

        for text_file in filenames:
            file_path = os.path.join(subfolder, text_file)
            file_data = process_text(file_path, nlp)
            results.append({'Filename': text_file, **file_data})
        df = pd.DataFrame(results)
        df.to_csv(os.path.join(output_path, f"{directory}_linguistic_features.csv"), index=False)
        print(f"Linguistic feature extraction completed. Results are saved in {output_path}")

        # Stop tracking emissions for the assignment
        tracker.stop()

if __name__ == "__main__":
    main()
