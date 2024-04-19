import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for random jitter

def plot_categorical_numerical(data, categorical_col, numerical_col, alpha=0.7, point_size=20, jitter=0.2):
    """
    Plots a scatter plot of a numerical column, colored by categories from a categorical column.
    Includes jitter on the x-axis to reduce overlap of points.

    Parameters:
    - data: pd.DataFrame containing the data.
    - categorical_col: String name of the column in 'data' that is categorical.
    - numerical_col: String name of the column in 'data' that is numerical.
    - alpha: Transparency of the points.
    - point_size: Size of each point.
    - jitter: Amount of jitter to apply on x-axis; default is 0.2.
    """
    # Ensure the categorical data is of type 'category' to help with coloring
    data[categorical_col] = data[categorical_col].astype('category')

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    categories = data[categorical_col].cat.categories
    # Generate a range for each category to position x coordinates
    x_pos = np.arange(len(categories))

    for i, category in enumerate(categories):
        subset = data[data[categorical_col] == category]
        # Apply jitter by adding a small random noise to x positions
        jittered_x = x_pos[i] + np.random.normal(loc=0, scale=jitter, size=len(subset))
        plt.scatter(
            jittered_x,  # X-axis: jittered position
            subset[numerical_col],  # Y-axis: the numerical data
            label=category,  # Label for the legend
            alpha=alpha,  # Transparency
            s=point_size  # Size of each point
        )
    
    plt.title(f'Scatter Plot of {numerical_col} Colored by {categorical_col}')
    plt.xlabel('Categories')
    plt.xticks(x_pos, categories)  # Set x-ticks to category names
    plt.ylabel(numerical_col)
    plt.legend(title=categorical_col)
    plt.show()

def plot_scatter(df, x_col, y_col):
    """
    Generates a scatterplot for the specified columns of the dataframe.
    
    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    x_col (str): The name of the column to use as the x-axis.
    y_col (str): The name of the column to use as the y-axis.
    """
    if x_col in df.columns and y_col in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[x_col], df[y_col], alpha=0.5)
        plt.title(f'Scatter Plot of {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.show()
    else:
        print("One or both column names do not exist in the DataFrame")

def plot_histogram(dataframe, column_name, bins=100):
    """
    Plots a histogram of the specified column from the given DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The name of the column for which to plot the histogram.
        bins (int): Number of bins for the histogram. Default is 10.
    """
    # Check if the column exists in the DataFrame
    if column_name in dataframe.columns:
        # Plot the histogram
        dataframe[column_name].hist(bins=bins)
        plt.title(f'Histogram of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"Column '{column_name}' not found in the DataFrame.")