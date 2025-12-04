import matplotlib.pyplot as plt

def make_bar_chart(df, column):
    plt.figure(figsize=(6,4))
    plt.bar(df.index, df[column])
    plt.title("Bar Chart")
    plt.xlabel("Row Index")
    plt.ylabel(column)
    plt.savefig("data/chart.png")
    plt.close()
