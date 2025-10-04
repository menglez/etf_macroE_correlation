import matplotlib.pyplot as plt

def plot_all(combined_df, cb_diff_df, increase_etf=True):

    fig, ax1 = plt.subplots(figsize=(20, 4))

    # Plot first column on left y-axis
    ax1.plot(combined_df.index, combined_df.iloc[:, 0], color='blue', label=combined_df.columns[0])
    ax1.set_ylabel(combined_df.columns[0], color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create second y-axis
    ax2 = ax1.twinx()
    ax2.plot(combined_df.index, combined_df.iloc[:, 1], color='red', label=combined_df.columns[1])
    ax2.set_ylabel(combined_df.columns[1], color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Add title and show
    plt.title(f"{combined_df.columns[0]} VS {combined_df.columns[1]}")
    plt.show()

    if increase_etf == True:
        cb_diff_df['diff_etf'] = cb_diff_df['diff_etf'] * 10

    plt.figure(figsize=(20, 4))
    plt.axhline(y=0, color='orange', linestyle='--')
    plt.bar(cb_diff_df.index, cb_diff_df['diff_etf'], label='diff_etf', width=20, color='r')
    plt.bar(cb_diff_df.index, cb_diff_df['diff_ind'], label=f'diff_ind', width=10, color='b')
    plt.title(f"diff_etf Vs diff_ind")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()