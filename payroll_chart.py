import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. Font & Style Setup
# ==========================================
# Set the font to Arial or Helvetica for that clean journalistic look
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# ==========================================
# 2. Data Estimation
# ==========================================
years = np.arange(2009, 2026)
values = [
    -1.2, 0.6, 2.0, 2.2, 2.3, 3.0, 2.8, 2.4, 2.2, 2.5, 2.0, 
    -9.5, 6.8, 4.5, 3.1, 2.2, 0.584
]

# ==========================================
# 3. Plotting
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')

# Colors: Grey for history, Maroon for 2025
bar_colors = ['#999999'] * (len(years) - 1) + ['#800040']

ax.bar(years, values, color=bar_colors, width=0.6, alpha=0.8, zorder=3)

# ==========================================
# 4. Custom Y-Axis (Labels resting on gridlines)
# ==========================================
ax.yaxis.set_visible(False) # Hide default axis

# Define limits
ax.set_xlim(2008.5, 2026.5)
ax.set_ylim(bottom=-15.1, top=12) 

yticks = np.arange(-15, 11, 5)

for y in yticks:
    # Draw gridline behind bars
    ax.axhline(y, color='lightgrey', linewidth=0.8, zorder=0)
    
    # Label Text
    label = str(y)
    if y == 10:
        label = "10 million"
    
    # Place text resting on top of the line
    ax.text(2008.5, y + 0.2, label, 
            color='#444444', fontsize=10, va='bottom', ha='left')

# Bold zero line
ax.axhline(0, color='black', linewidth=1.2, zorder=3)

# ==========================================
# 5. X-Axis & Formatting
# ==========================================
# Hide all spines
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

# Custom X-ticks
major_xticks = [2010, 2015, 2020, 2025]
major_xticklabels = ['2010', "'15", "'20", "'25"]

ax.set_xticks(major_xticks)
ax.set_xticklabels(major_xticklabels, color='#444444', fontsize=10)
ax.set_xticks(years, minor=True)
ax.tick_params(axis='x', which='both', direction='out', length=3, color='#444444', top=False)

# ==========================================
# 6. Labels
# ==========================================
# Title
plt.title("Nonfarm payrolls, change from a year earlier", 
          loc='left', fontsize=14, fontweight='bold', color='#222222', pad=30)

# Data Label
ax.text(2025, 0.584 + 0.8, "2025:\n584,000", 
        ha='center', va='bottom', fontsize=11, fontweight='bold', color='#222222')

# Footnote
footnote_text = "Note: Seasonally adjusted, based on December level of each year\nSource: Labor Department"
# Slightly adjusted position to keep it close to the labels
fig.text(0.125, 0.03, footnote_text, ha='left', fontsize=9, color='#666666')

# Adjust margins
plt.subplots_adjust(bottom=0.15, left=0.05, right=0.95, top=0.85)

# Save the figure
plt.savefig('nonfarm_payrolls.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'nonfarm_payrolls.png'")
