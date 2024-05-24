######
# Assignment 4 - Emotion Analysis with Pretrained Language Models
# Author: Emilie Munch Andreasen
# Date: 25-05-2024
######

# Importing packages
import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from codecarbon import EmissionsTracker

# Defining argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Perform emotion analysis on Game of Thrones scripts.')
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the CSV dataset file')
    parser.add_argument('--output_dir', type=str, required=False, default='../out', help='Output directory for the resulting outputs, plots, and emission files')
    return parser.parse_args()

##### 
# Defining Functions
#####

def load_data(input_file, output_dir):
    """
    Loads data from the specified input file or a pre-existing output file.

    Parameters:
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

def predict_emotions(data):
    """
    Analyses and predicts the emotion scores for all sentences in the data by employing a pretrained language model.

    Parameters:
        data (pd.DataFrame): DataFrame containing the script data.

    Returns:
        pd.DataFrame: DataFrame with added emotion scores.
    """
    print("Predicting emotions for each sentence. This can take a while...")
    classifier = pipeline("text-classification",
                          model="j-hartmann/emotion-english-distilroberta-base")
    
    sentences = [str(sentence) for sentence in data['Sentence'].tolist()]
    
    emotion_scores = classifier(sentences)

    labels = [entry['label'] for entry in emotion_scores]
    data['Emotion_Label'] = labels

    print("Emotion prediction completed")
    return data

def save_predicted_emotions(data, output_dir):
    """
    Saves the data with predicted emotions to a CSV file.

    Parameters:
        data (pd.DataFrame): DataFrame containing the script data with predicted emotions.
        output_dir (str): Directory to save the CSV file.
    """
    data.to_csv(os.path.join(output_dir, 'Emotion_Analysis_Output.csv'), index=False)

def plot_emotions_per_season(data, output_dir):
    """
    Plots the distribution of all emotion labels in each season and then saves the plots.

    Parameters:
        data (pd.DataFrame): DataFrame containing the script data with emotion scores.
        output_dir (str): Directory to save the plots.
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

    print("Emotion distribution per season plotted")

def plot_relative_freq_emotions(data, output_dir):
    """
    Plots the relative frequency of each emotion label across all seasons and saves the plot.

    Parameters:
        data (pd.DataFrame): DataFrame containing the script data with emotion scores.
        output_dir (str): Directory to save the plot.
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

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.subplots_adjust(right=0.75)
    plt.savefig(os.path.join(output_dir, 'relative_emotion_frequency.png'), bbox_inches='tight')
    plt.close()
    print("Relative frequency of emotion across seasons plotted")

#####
# Main Function
#####

def main():
    args = parse_arguments()
    tracker = EmissionsTracker(
        project_name="emotion_analysis",
        experiment_id="emotion_analysis_got",
        output_dir=output_dir,
        output_file="emissions.csv"
    )
    tracker.start()

    tracker.start_task("load_data")
    data = load_data(input_file, output_dir)
    tracker.stop_task()

    tracker.start_task("predict_emotions")
    data = predict_emotions(data)
    tracker.stop_task()

    tracker.start_task("plot_emotions_per_season")
    plot_emotions_per_season(data, output_dir)
    tracker.stop_task()

    tracker.start_task("plot_relative_freq_emotions")
    plot_relative_freq_emotions(data, output_dir)
    tracker.stop_task()
    
    tracker.stop()

    print(f"Analysis complete. Check the '{args.output_dir}' directory for the generated plots and emotion scores")

if __name__ == "__main__":
    main()