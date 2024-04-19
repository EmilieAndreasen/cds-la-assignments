######
# Assignment 4 - Emotion analysis with pretrained language models
######

# Importing packages
import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Defining argument parsing with argparse
def parse_arguments():
    """
    Parse command-line arguments for script execution.
    """
    parser = argparse.ArgumentParser(description='Perform emotion analysis on Game of Thrones scripts.')
    parser.add_argument('-d', '--data_dir', type=str, required=True, help='Path to the CSV file.')
    parser.add_argument('-o', '--output_dir', type=str, required=False, default='out', help='Directory to save the output files to. Default is "out".')
    return parser.parse_args()

# Defining functions
## Loading the dataset from the given filepath
def load_data(input_file, output_dir):
    """
    Loads data from the specified input file or a pre-existing output file.

    Args:
        input_file (str): The path to the input data file.
        output_dir (str): Directory to check for existing output data.

    Returns:
        pd.DataFrame: Loaded data.
    """
    print("Loading data...")    
    emotion_predictions_output = os.path.join(output_dir, 'Emotion_Analysis_Output.csv')
    if os.path.exists(emotion_predictions_output):
        # In case the file exists, loading the data from it
        data = pd.read_csv(emotion_predictions_output)
    else:
        # If the file does not exist, loading data from the input file
        data = pd.read_csv(input_file)
        data = predict_emotions(data)
        save_predicted_emotions(data, output_dir)
    
    print(f"Data loaded. Total sentences: {len(data)}")
    return data

## Predicting emotion scores with pipeline classifier
def predict_emotions(data):
    """
    Analyses and predicts the emotion scores for all sentences in the data by employing a pretrained language model.

    Args:
        data (pd.DataFrame): DataFrame containing the script data.

    Returns:
        pd.DataFrame: DataFrame with added emotion scores.
    """
    print("Predicting emotions for each sentence. This can take a while...")
    classifier = pipeline("text-classification",
                          model="j-hartmann/emotion-english-distilroberta-base")
    
    # Converting the 'Sentence' column from the data to a list of strings
    sentences = [str(sentence) for sentence in data['Sentence'].tolist()]
    
    emotion_scores = classifier(sentences)

    # Extracting labels and updating
    labels = [entry['label'] for entry in emotion_scores]
    data['Emotion_Label'] = labels

    print("Emotion prediction completed.")
    return data

## Saving predicted emotions to a CSV file
def save_predicted_emotions(data, output_dir):
    """
    Saves the data with predicted emotions to a CSV file.

    Args:
        data (pd.DataFrame): DataFrame containing the script data with predicted emotions.
        output_dir (str): Directory to save the CSV file.

    Returns:
        None
    """
    data.to_csv(os.path.join(output_dir, 'Emotion_Analysis_Output.csv'), index=False)

## Plotting predicted emotions
def plot_emotions_per_season(data, output_dir):
    """
    Plots the distribution of all emotion labels in each season and then saves the plots.

    Args:
        data (pd.DataFrame): DataFrame containing the script data with emotion scores.
        output_dir (str): Directory to save the plots.

    Returns:
        None
    """
    print("Plotting emotion distribution per season...")
    
    emotion_colours = {
        'anger': 'red',
        'joy': 'yellow',
        'sadness': 'blue',
        'disgust': 'green',
        'fear': 'purple',
        'surprise': 'pink',
        'neutral': 'gray'        
    }

    seasons = data['Season'].unique()
    num_seasons = len(seasons)

    fig, axes = plt.subplots(2, 4, figsize=(20, 20))

    axes = axes.flatten()
    
    # Looping through each season
    for i, (season, ax) in enumerate(zip(seasons, axes)):
        season_data = data[data['Season'] == season]
        emotion_count = season_data['Emotion_Label'].value_counts()
        
        ax.bar(emotion_count.index, emotion_count.values, color=[emotion_colours.get(emotion, 'black') for emotion in emotion_count.index])
        ax.set_title(f'Distribution of the 7 Emotion Labels in {season}')
        ax.set_xlabel('Emotion Label')
        ax.set_ylabel('Frequency')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'all_seasons_emotions.png'))
    plt.close()

    print("Emotion distribution per season plotted.")

## Plotting relative frequency
def plot_relative_freq_emotions(data, output_dir):
    """
    Plots the relative frequency of each emotion label across all seasons and saves the plot.

    Args:
        data (pd.DataFrame): DataFrame containing the script data with emotion scores.
        output_dir (str): Directory to save the plot.

    Returns:
        None
    """
    print("Plotting relative frequency of emotions across seasons...")
    seasons = data['Season'].unique()
    
    plt.figure()
    width = 0.8 / len(seasons) 
    offset = -0.4  
    
    for season in seasons:
        season_data = data[data['Season'] == season]
        relative_freq = season_data['Emotion_Label'].value_counts(normalize=True)
        labels = relative_freq.index
        values = relative_freq.values
        plt.bar(labels, values, width=width, align='center', label=f'{season}', alpha=0.8)
        offset += width  
    
    plt.title('Relative Frequency of Emotion Labels Across All Seasons')
    plt.xlabel('Emotion Label')
    plt.ylabel('Relative Frequency')

    # Placing the legend to the right side of the plot
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.subplots_adjust(right=0.75)
    plt.savefig(os.path.join(output_dir, 'relative_emotion_frequency.png'), bbox_inches='tight')
    plt.close()
    print("Relative frequency of emotion across seasons plotted.")

# The main function
def main():
    """
    Main function to execute the emotion analysis pipeline.
    """
    args = parse_arguments()
    input_file = args.data_dir
    output_dir = args.output_dir
    
    # Ensuring that the output dir exists
    os.makedirs(output_dir, exist_ok=True)

    data = load_data(input_file, output_dir)

    plot_emotions_per_season(data, output_dir)

    plot_relative_freq_emotions(data, output_dir)
    
    print(f"Analysis complete. Check the '{args.output_dir}' directory for the generated plots and emotion scores.")

if __name__ == "__main__":
    main()
