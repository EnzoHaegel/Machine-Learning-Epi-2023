import pandas as pd
import numpy as np

# ANSI escape sequences to add color to output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_integers(df: pd.DataFrame) -> bool:
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
            return True
        if all(df[col] == df[col].astype(int)):
            return True
    return False

def print_colored_message(condition, true_message, false_message):
    if condition:
        print(f"{bcolors.OKGREEN}{true_message}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}{false_message}{bcolors.ENDC}")

def check_dataset_conditions(file_path: str):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Check for unique means
    means = df.mean()
    print(f"{bcolors.HEADER}\nMeans:\n{bcolors.ENDC}", means)
    all_means_different = len(set(means.round(3))) == len(means)
    print_colored_message(all_means_different, "All columns have different means: True", "All columns have different means: False")

    # Check for unique standard deviations
    stds = df.std()
    print(f"{bcolors.HEADER}\nStandard Deviations:\n{bcolors.ENDC}", stds)
    all_stds_different = len(set(stds.round(3))) == len(stds)
    print_colored_message(all_stds_different, "All columns have different standard deviations: True", "All columns have different standard deviations: False")

    # Check for at least one integer column
    has_integer_column = check_integers(df)
    print_colored_message(has_integer_column, "At least one column contains integers: True", "At least one column contains integers: False")

    # Check for at least one float column
    has_float_column = any(df.dtypes == 'float')
    print_colored_message(has_float_column, "At least one column contains floats: True", "At least one column contains floats: False")

    # Check for a column with mean close to 2.5
    mean_close_to_25 = any(np.isclose(means, 2.5, atol=0.1))
    print_colored_message(mean_close_to_25, "One column has a mean close to 2.5: True", "One column has a mean close to 2.5: False")

    # Check correlations
    corr_matrix = df.corr()
    print(f"{bcolors.HEADER}\nCorrelation Matrix:\n{bcolors.ENDC}", corr_matrix)
    positive_correlations = corr_matrix.values[np.triu_indices_from(corr_matrix.values, 1)].max() > 0.5
    negative_correlations = corr_matrix.values[np.triu_indices_from(corr_matrix.values, 1)].min() < -0.5
    zero_correlations = np.any(np.isclose(corr_matrix.values[np.triu_indices_from(corr_matrix.values, 1)], 0, atol=0.1))

    print_colored_message(positive_correlations, "Some columns are positively correlated: True", "Some columns are positively correlated: False")
    print_colored_message(negative_correlations, "Some columns are negatively correlated: True", "Some columns are negatively correlated: False")
    print_colored_message(zero_correlations, "At least two columns have a correlation close to 0: True", "At least two columns have a correlation close to 0: False")

# Specify the path to your CSV file
file_path = 'artificial_dataset.csv'
check_dataset_conditions(file_path)


