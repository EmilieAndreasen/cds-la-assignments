######
# Assignment 3 - Query expansion with word embeddings
######

# Importing packages
import os
import argparse
import pandas as pd
import gensim.downloader as api

# Defining argument parsing with argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description="Query expansion with word embeddings.")
    parser.add_argument('--data', type=str, required=True, help='Path to the dataset file')
    parser.add_argument('--artist', type=str, required=True, help='The music artist(s) to inspect')
    parser.add_argument('--word', type=str, required=True, help='The search word to expand')
    return parser.parse_args()

# Defining functions
## Loading the dataset from the given filepath
def load_data(filepath):
    return pd.read_csv(filepath)

## Loading the pretrained word embedding model from gensim
def load_model():
    return api.load("glove-wiki-gigaword-50")

## Expanding the query by finding similar words with word embeddings
def expand_query(model, word):
    """
    Args:
        model: The word embedding model.
        word: The target word to expand.
        
    Returns:
        A list containing the original word and its similar words.
    """
    return [word] + [result[0] for result in model.most_similar(word)]

## Calculating the percentage of songs by an artist that mention any of the query words
def calc_artist_query_perc(df, artist, query_words):
    """ 
    Args:
        df: The dataframe containing the songs dataset.
        artist: The name of the artist to inspect.
        query_words: A list of words to search for in the songs.
        
    Returns:
        The percentage of songs by the artist that contain any of the query words.
    """
    # Filtering to only have the songs by the specified artist in 'artist_songs'.
    artist_songs = df[df['artist'].str.lower() == artist.lower()]

    # Filtering to only have the rows where the lambda function returns True.
    relevant_songs = artist_songs[artist_songs['text'].apply(lambda lyrics: any(word in lyrics for word in query_words))]
    
    if artist_songs.shape[0] > 0:
        percentage = (relevant_songs.shape[0] / artist_songs.shape[0]) * 100
    else:
        percentage = 0
    return percentage

# Main function
def main():
    # Using the argument parsing and above functions
    args = parse_arguments()
    df = load_data(args.data)
    model = load_model()
    query_words = expand_query(model, args.word)
    percentage = calc_artist_query_perc(df, args.artist, query_words)
   
   # Ensuring an "out" directory exists
    output_dir = "../out"
    os.makedirs(output_dir, exist_ok=True)  # Creating the directory if it does not exist
    
    # Defining the output file path
    output_file = os.path.join(output_dir, f"{args.artist.replace(' ', '_')}_{args.word.replace(' ', '_')}_results.txt")

    
    # Getting the 10 most similar words to the specified word (for more clarity)
    similar_words = [word for word, _ in model.most_similar(args.word, topn=10)]

    # Writing the results and the similar words to the file
    with open(output_file, 'w') as file:
        file.write(f"{percentage:.2f}% of {args.artist}'s songs contain words related to {args.word}\n")
        file.write("\nBased on general language patterns, the words most similar to the specified term are:\n")
        file.write("\n".join(similar_words))

    # Print the result to the console as well
    print(f"{percentage:.2f}% of {args.artist}'s songs contain words related to {args.word}")

if __name__ == "__main__":
    main()