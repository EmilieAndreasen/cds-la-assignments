######
# Assignment 3 - Query Expansion with Word Embeddings
# Author: Emilie Munch Andreasen
# Date: 24-05-2024
######

# Importing packages
import os
import argparse
import pandas as pd
import gensim.downloader as api
import string
from codecarbon import EmissionsTracker

# Defining argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="Query expansion with word embeddings.")
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the dataset file')
    parser.add_argument('--output_dir', type=str, default='../out', help='Output directory for the resulting text files and emission files')    
    parser.add_argument('--artist', type=str, required=True, help='The music artist(s) to inspect')
    parser.add_argument('--word', type=str, required=True, help='The search word to expand')
    return parser.parse_args()

##### 
# Defining Functions
#####

def preprocess_text(text):
    """
    Preprocesses the text by lowercasing and removing punctuation.

    Parameters:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def load_data(filepath):
    """
    Loads data from a CSV file and preprocesses the 'text' column.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded and preprocessed data.
    """
    df = pd.read_csv(filepath)
    df['text'] = df['text'].apply(preprocess_text)
    return df

def load_model():
    """
    Loads a pretrained word embedding model from Gensim.

    Returns:
        Gensim model: Pretrained word embedding model.
    """
    return api.load("glove-wiki-gigaword-50")

def expand_query(model, word):
    """
    Expands the query by finding similar words using word embeddings.

    Parameters:
        model (Gensim model): The word embedding model.
        word (str): The target word to expand.

    Returns:
        list: A list containing the original word and its similar words.
    """
    return [word] + [result[0] for result in model.most_similar(word)]

def calc_perc(df, artist, query_words):
    """
    Calculates the percentage of songs by an artist that mention any of the query words.

    Parameters:
        df (DataFrame): The dataframe containing the songs dataset.
        artist (str): The name of the artist to inspect.
        query_words (list): A list of words to search for in the songs.

    Returns:
        float: The percentage of songs by the artist that contain any of the query words.
    """
    artist_songs = df[df['artist'].str.lower() == artist.lower()]

    relevant_songs = artist_songs[artist_songs['text'].apply(lambda lyrics: any(word in lyrics for word in query_words))]
    
    if artist_songs.shape[0] > 0:
        percentage = (relevant_songs.shape[0] / artist_songs.shape[0]) * 100
    else:
        percentage = 0
    return percentage

def save_results(output_dir, artist, word, percentage, similar_words):
    """
    Saves the analysis results to a text file.

    Parameters:
        output_dir (str): Directory where the results file will be saved.
        artist (str): Name of the artist analysed.
        word (str): The search word used for query expansion.
        percentage (float): Percentage of artist's songs that contain the related words.
        similar_words (list of str): List of words similar to the search word.
    """
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{artist.replace(' ', '_')}_{word.replace(' ', '_')}_results.txt")
    
    with open(output_file, 'w') as file:
        file.write(f"{percentage:.2f}% of {artist}'s songs contain words related to {word}\n")
        file.write("\nBased on general language patterns, the words most similar to the specified term are:\n")
        file.write("\n".join(similar_words))

    print(f"Results saved to {output_file}")

#####
# Main Function
#####

def main():
    args = parse_arguments()
    tracker = EmissionsTracker(
        project_name="query_expansion_embeddings",
        experiment_id="word_embeddings_usage",
        output_dir=args.output_dir,
        output_file="emissions.csv"
    )
    tracker.start()

    tracker.start_task("load_data")
    df = load_data(args.dataset_path)
    tracker.stop_task()

    tracker.start_task("load_model")
    model = load_model()
    tracker.stop_task()

    tracker.start_task("expand_query")
    query_words = expand_query(model, args.word)
    tracker.stop_task()

    tracker.start_task("calculate_percentage")
    percentage = calc_perc(df, args.artist, query_words)
    tracker.stop_task()

    tracker.start_task("save_results")
    similar_words = [word for word, _ in model.most_similar(args.word, topn=10)]
    save_results(args.output_dir, args.artist, args.word, percentage, similar_words)
    tracker.stop_task()

    tracker.stop()
    print(f"{percentage:.2f}% of {args.artist}'s songs contain words related to {args.word}")


if __name__ == "__main__":
    main()