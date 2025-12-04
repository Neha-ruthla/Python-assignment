
from modules.data_loader import load_data, save_data
from modules.processor import clean_data, calculate_summary
from modules.visualizer import make_bar_chart
from config import INPUT_PATH, OUTPUT_PATH
from utils import print_line

def main():
    print(" Loading data...")
    df = load_data(INPUT_PATH)

    print_line()
    print("Cleaning data...")
    df = clean_data(df)

    print_line()
    print(" Calculating Summary...")
    summary = calculate_summary(df, "kwh")
   # column name

    print(summary)

    print_line()
    print(" Saving cleaned output...")
    save_data(df, OUTPUT_PATH)

    print_line()
    print(" Generating chart...")
    make_bar_chart(df, "kwh")

    print(" Project Completed Successfully!")

if __name__ == "__main__":
    main()
