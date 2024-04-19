# cds-la-assignment 4

Assignment 4 for CDS Language Analytics.

By: Emilie Munch Andreasen

## Objectives
### Assignment 4 - Emotion analysis with pretrained language models
Winter is... just finished, actually.

In class this week, we've seen how pretrained language models can be used for a range of tasks. In this assignment, we're going to use these models to perform some computational text analysis of some culturally significant data - scripts from the television show Game of Thrones. The scripts have been split into lines, with additional metadata showing who spoke each line, which episode that line comes from, and which season that episode belongs to.

In this assignment, we are going to investigate whether the emotional profile of this show changed over the course of its seven series, and we want to know which characters exhibit the most extreme emotions.

For this assignment, you should write code which does the following:
- Predict emotion scores for all lines in the data
- For each season
    - Plot the distribution of all emotion labels in that season
- For each emotion label
    - Plot the relative frequency of each emotion across all seasons
- Finally, your repository should include a writtens summary and interpretation of what you think this analysis might being showing. You do not need to be a media studies expert here - just describe what you see and what that might mean in this context.

## Data availability
The data needed for the assignment can be found here: https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv 

## Technicalities

For this assignment, the 'setup.sh' should be run to install the required libraries. 

## Folder structure

The folders are structured as follows:

| Column | Description|
|--------|:-----------|
| ```in```| Contains a sample of the data for running the code quickly |
| ```out```| Contains the outputted plots and emotion analysis |
| ```src```  | Contains the Python script used for assignment 4 |

## Interpretation of outputs
The emotion analysis of the different scripts from the TV show 'Game of Thrones' gives an insight into the show's emotional profile across its eight seasons.

From both the plot showing the relative frequency of the various emotions across seasons and the second plot showing the emotional content season by season, it can be seen that the 'neutral' emotion is the most prevelant one by a notable amount. This result could suggest that much of the dialogue does not convey pronounced emotion. An instance of such a case can be seen in the 'Emotion_Analysis_Output.csv': "My name is Daenerys-" (line 4555).

However, there are also instances of lines that could argueably be seen as conveying an emotion, which the model simply classifies as 'neutral'. E.g., "The lion's not his sigil, idiot. He's a stag, like his father." (line 2064). This line, in context of the scene, could also be seen as the character (i.e., Arya Stark) showing anger/frustration towards her sister (i.e., Sansa Stark).
This points to the language model not being "sensitive" enough, or, more likely, that because it cannot process the context of scenes as a whole, but instead predicts emotions simply from the line (i.e., an isolated sentence), it struggles to accurately classify all lines.

Despite this, the plots show that there are also occurances of other emotions. Of these, 'anger', 'surprise', and 'disgust' are also quite prevelant throughout the different seasons. This seems plausible, as 'Game of Thrones' is known to be a dramatic adult-oriented show, which is not afraid of featuring macabre and somewhat controversial topics.
While these three emotions, along with the 'neutral' one, are consistently shown as the top four, the last three emotions do shift around from season to season. This can be seen in the plot showing the emotional content season by season. Such changes could correlate to the different plot events and tone setting for each season.

All in all, this analysis indicates that 'Game of Thrones' stays quite consistent in the conveyed emotional profile across seasons. Although it should be noted that the model's predictions are limited to the textual data and lack the nuances and "depth" of human context recognition.  