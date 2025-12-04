import matplotlib.pyplot as plt

def plot_temperature(df, output_path):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['temperature'])
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.title("Daily Temperature Trend")
    plt.savefig(output_path)
    plt.close()

def plot_rainfall(df, output_path):
    monthly = df.groupby(df['date'].dt.month)['rainfall'].sum()
    plt.figure(figsize=(8, 5))
    plt.bar(monthly.index, monthly.values)
    plt.xlabel("Month")
    plt.ylabel("Rainfall")
    plt.title("Monthly Rainfall Total")
    plt.savefig(output_path)
    plt.close()

def plot_humidity(df, output_path):
    plt.figure(figsize=(8, 5))
    plt.scatter(df['temperature'], df['humidity'])
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.title("Humidity vs Temperature")
    plt.savefig(output_path)
    plt.close()

def plot_combined(df, output_path):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(df['date'], df['temperature'], label="Temperature")
    plt.title("Temperature Trend")

    plt.subplot(1, 2, 2)
    plt.scatter(df['temperature'], df['humidity'], label="Humidity")
    plt.title("Humidity vs Temp")

    plt.savefig(output_path)
    plt.close()
