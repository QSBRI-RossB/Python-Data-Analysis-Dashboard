import pandas as pd
import plotly.graph_objs as go

# URL of the raw CSV file from GitHub
url = 'https://raw.githubusercontent.com/martingeew/finance_dashboard_demo/main/sp500_20240807.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(url)


def plot_daily(df):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="S&P 500 Close",
            hovertemplate="%{x|%Y-%m-%d}<br>Close: %{y:.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        title="Daily S&P 500 Closing value",
        xaxis_title="",
        yaxis_title="",
        template="plotly_dark",  # Use the dark mode template
    )

    fig.show()


plot_daily(df)


print('Hello World')