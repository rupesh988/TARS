import pandas as pd
import matplotlib.pyplot as plt
import os
from pandas.plotting import scatter_matrix, lag_plot, autocorrelation_plot, radviz, andrews_curves, parallel_coordinates

def analyze_dataset(csv_file, output_folder):
    # output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(csv_file,encoding="ISO-8859-1")

    # Scatter Matrix
    plt.figure()
    scatter_matrix(df, figsize=(10, 10), diagonal='kde')
    plt.suptitle("Scatter Matrix", size=16)
    plt.savefig(os.path.join(output_folder, "scatter_matrix.png"))
    plt.close()

    # Lag Plot (for time series analysis, using the first column by default)
    plt.figure()
    lag_plot(df[df.columns[0]])
    plt.title(f"Lag Plot ({df.columns[0]})", size=16)
    plt.savefig(os.path.join(output_folder, "lag_plot.png"))
    plt.close()

    # Autocorrelation Plot (for time series analysis, using the first column by default)
    plt.figure()
    autocorrelation_plot(df[df.columns[0]])
    plt.title(f"Autocorrelation Plot ({df.columns[0]})", size=16)
    plt.savefig(os.path.join(output_folder, "autocorrelation_plot.png"))
    plt.close()

    # Andrews Curves (will plot without class information)
    if len(df.columns) > 1:
        plt.figure(figsize=(10, 6))
        andrews_curves(df, df.columns[-1])
        plt.title("Andrews Curves")
        plt.savefig(os.path.join(output_folder, "andrews_curves.png"))
        plt.close()

    # Parallel Coordinates (will plot without class information)
    if len(df.columns) > 1:
        plt.figure(figsize=(10, 6))
        parallel_coordinates(df, df.columns[-1])
        plt.title("Parallel Coordinates")
        plt.savefig(os.path.join(output_folder, "parallel_coordinates.png"))
        plt.close()

    # RadViz (can use a category column if needed; here the last column will be treated as categorical)
    if len(df.columns) > 1:
        plt.figure(figsize=(10, 6))
        radviz(df, df.columns[-1])
        plt.title("RadViz Plot")
        plt.savefig(os.path.join(output_folder, "radviz.png"))
        plt.close()

    print(f"All plots saved to {output_folder}")
