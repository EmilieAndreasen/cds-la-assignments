######
# Assignment 5 - Evaluating Environmental Impact of Your Exam Portfolio
# Author: Emilie Munch Andreasen
# Date: 25-05-2024
######

# Importing packages
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Defining argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Evaluate environmental impact of previous assignments.')
    parser.add_argument('--dataset_path', type=str, default='../in', help='Path to the CSV emission files')
    parser.add_argument('--output_dir', type=str, default='../out', help='Output directory for the plots')
    return parser.parse_args()

##### 
# Defining Functions
#####

def load_data(dataset_path):
    """
    Loads emissions data from CSV files in the specified directory.

    Parameters:
        dataset_path (str): Path to the directory containing the CSV files.

    Returns:
        dict: Dictionary containing concatenated data for each assignment.
    """
    assignments = {}
    files = sorted(os.listdir(dataset_path))
    
    for file in files:
        if file.endswith(".csv"):
            assignment_name = file.replace('_emission.csv', '') 
            if assignment_name not in assignments:
                assignments[assignment_name] = []
            df = pd.read_csv(os.path.join(dataset_path, file))
            print(f"Loaded {file} with columns: {df.columns.tolist()}") 
            df['file'] = file  
            assignments[assignment_name].append(df)
    
    for key in assignments:
        assignments[key] = pd.concat(assignments[key], ignore_index=True)
    return assignments

def calculate_total_emissions(assignments):
    """
    Calculates total emissions for each assignment.

    Parameters:
        assignments (dict): Dictionary containing emissions data for each assignment.

    Returns:
        dict: Total emissions for each assignment.
    """
    total_emissions = {}
    for assignment, df in assignments.items():
        total_emissions[assignment] = df['emissions'].sum()
    return total_emissions

def calculate_task_emissions(assignments):
    """
    Calculates emissions for each task in each assignment.

    Parameters:
        assignments (dict): Dictionary containing emissions data for each assignment.

    Returns:
        pd.DataFrame: Emissions data for each task and assignment.
    """
    task_emissions_list = []
    for assignment, df in assignments.items():
        if 'task_name' in df.columns:
            task_emissions = df.groupby('task_name')['emissions'].sum().reset_index()
            task_emissions['assignment'] = assignment 
            task_emissions_list.append(task_emissions)
    
    if task_emissions_list:
        return pd.concat(task_emissions_list, ignore_index=True)
    else:
        return pd.DataFrame(columns=['task_name', 'emissions', 'assignment'])

def plot_assignment_emissions(total_emissions, output_dir):
    """
    Plots and saves the total emissions for each assignment.

    Parameters:
        total_emissions (dict): Total emissions for each assignment.
        output_dir (str): Directory to save the plot image.
    """
    assignments = list(total_emissions.keys())
    emissions = list(total_emissions.values())

    plt.figure(figsize=(12, 8))
    assignment_colours = {
        'A1': 'powderblue',
        'A2_logreg': 'seagreen',
        'A2_neural': 'limegreen',
        'A3_1': 'purple',
        'A3_2': 'orchid',
        'A4': 'dodgerblue'
    }

    barplot = plt.bar(assignments, emissions, color=[assignment_colours.get(a, 'black') for a in assignments])
    for i, bar in enumerate(barplot):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{emissions[i] / sum(emissions) * 100:.2f}%',
                 ha='center', va='bottom', fontsize=10, rotation=0)
    
    plt.yscale('log')
    plt.title('Total Emissions for Each Assignment', fontsize=12)
    plt.xlabel('Assignments')
    plt.ylabel('Total Emissions (CO₂eq)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'total_emissions_by_assignment.png'))
    plt.close()

def plot_task_emissions(task_emissions, output_dir):
    """
    Plots and saves the emissions for each task in each assignment, both combined and individually.

    Parameters:
        task_emissions (pd.DataFrame): Emissions data for each task and assignment.
        output_dir (str): Directory to save the plot images.
    """
    assignment_colours = {
        'A2_logreg': 'seagreen',
        'A2_neural': 'limegreen',
        'A3_1': 'purple',
        'A3_2': 'orchid',
        'A4': 'dodgerblue'
    }

    # Combined plot
    plt.figure(figsize=(12, 8))
    for assignment in task_emissions['assignment'].unique():
        subset = task_emissions[task_emissions['assignment'] == assignment]
        colour = assignment_colours.get(assignment, 'black')
        barplot = plt.bar(subset['task_name'] + f' ({assignment})', subset['emissions'], color=colour, label=assignment)

        for bar in barplot:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height / subset["emissions"].sum() * 100:.2f}%',
                     ha='center', va='bottom', fontsize=10, rotation=0)
    
    plt.yscale('log')
    plt.title('Task Emissions for Each Assignment', fontsize=12)
    plt.xlabel('Tasks Within Scripts')
    plt.ylabel('Total Emissions (CO₂eq)')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'task_emissions_combined.png'))
    plt.close()

    # Individual plots (A1 not included)
    for assignment in task_emissions['assignment'].unique():
        plt.figure(figsize=(12, 8))
        subset = task_emissions[task_emissions['assignment'] == assignment]
        colour = assignment_colours.get(assignment, 'black')
        barplot = plt.bar(subset['task_name'], subset['emissions'], color=colour, label=assignment)

        for bar in barplot:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height / subset["emissions"].sum() * 100:.2f}%',
                     ha='center', va='bottom', fontsize=10, rotation=0)
        
        plt.yscale('log')
        plt.title(f'Task Emissions for {assignment}', fontsize=12)
        plt.xlabel('Task')
        plt.ylabel('Total Emissions (CO₂eq)')
        plt.xticks(rotation=90)
        plt.tight_layout(pad=2)
        plt.savefig(os.path.join(output_dir, f'{assignment}_task_emissions.png'))
        plt.close()

#####
# Main Function
#####

def main():
    args = parse_arguments()

    os.makedirs(args.output_dir, exist_ok=True)
    
    data = load_data(args.dataset_path)

    total_emissions = calculate_total_emissions(data)
    task_emissions = calculate_task_emissions(data)
    
    plot_assignment_emissions(total_emissions, args.output_dir)
    plot_task_emissions(task_emissions, args.output_dir)

if __name__ == '__main__':
    main()