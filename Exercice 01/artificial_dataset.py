import numpy as np
import pandas as pd

def generate_correlated_data(n: int, mean1: float, std1: float, mean2: float, std2: float, correlation: float) -> np.array:
    """
    Generates a sample of n points with a specified correlation.
    
    :param n: Number of datapoints
    :param mean1: Mean of the first variable
    :param std1: Standard deviation of the first variable
    :param mean2: Mean of the second variable
    :param std2: Standard deviation of the second variable
    :param correlation: Target correlation between the two variables
    :return: n x 2 matrix with the correlated variables
    """
    # Create a sample with the desired correlation matrix
    cov_matrix = [[std1**2, correlation*std1*std2], [correlation*std1*std2, std2**2]]
    sample = np.random.multivariate_normal([mean1, mean2], cov_matrix, n)
    return sample

def create_dataset(n: int) -> pd.DataFrame:
    np.random.seed(0)

    means = [1, 2.5, 5, 10, 20, 50]
    stds = [0.5, 1, 1.5, 2, 2.5, 3]

    # Create positively correlated data for columns 3 and 4
    columns = [None] * 6  # Initialize list for columns
    columns[2], columns[3] = generate_correlated_data(n, means[2], stds[2], means[3], stds[3], 0.8).T

    # Generate negatively correlated data for columns 2 and 5
    columns[1], columns[4] = generate_correlated_data(n, means[1], stds[1], means[4], stds[4], -0.8).T

    # Generate the rest of the columns with different means and standard deviations
    for i, (mean, std) in enumerate(zip(means, stds)):
        if columns[i] is None:
            columns[i] = np.random.normal(mean, std, n)
    columns[0] = np.round(columns[0]).astype(int)  # Ensures column has integer data

    # Create DataFrame
    df = pd.DataFrame(data=np.array(columns).T, columns=[f'feature_{i}' for i in range(1, 7)])

    # Shuffle the last column until low correlation is achieved with all other columns
    min_correlation = 0.1
    attempts = 0
    max_attempts = 1000  # Set a maximum number of shuffling attempts

    while attempts < max_attempts and min_correlation >= 0.1:
        np.random.shuffle(df['feature_6'].values)  # Shuffle feature_6 inplace
        max_correlation = df.corr().abs().loc['feature_6'].drop('feature_6').max()
        if max_correlation < min_correlation:
            min_correlation = max_correlation
        attempts += 1
    return df

def main():
    """
    Main function to generate and save the dataset.
    """
    n = 300  # number of datapoints
    df = create_dataset(n)
    df.to_csv('artificial_dataset.csv', index=False)

if __name__ == "__main__":
    main()
