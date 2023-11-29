import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Create a sample dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Value': np.random.rand(100) * 100  # Random data for illustration
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Set the smoothing parameter (alpha)
alpha_initial = 0.2

# Calculate EWMA
df['EWMA'] = df['Value'].ewm(alpha=alpha_initial, adjust=False).mean()

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

# Plot the original data and EWMA
line_original, = plt.plot(df.index, df['Value'], label='Original Data', color='blue')
line_ewma, = plt.plot(df.index, df['EWMA'], label=f'EWMA (Alpha)', color='red')

plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.title('Exponentially Weighted Moving Averages (EWMA)')
plt.grid(True)

# Add a slider for alpha
ax_alpha = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
s_alpha = Slider(ax_alpha, 'Alpha', 0.01, 1.0, valinit=alpha_initial)

# Update function for the slider
def update(val):
    alpha = s_alpha.val
    df['EWMA'] = df['Value'].ewm(alpha=alpha, adjust=False).mean()
    line_ewma.set_ydata(df['EWMA'])
    #line_ewma.set_label(f'EWMA (alpha={alpha:.2f})')
    plt.legend()
    fig.canvas.draw_idle()

# Attach the update function to the slider
s_alpha.on_changed(update)

# Show the plot
plt.show()
