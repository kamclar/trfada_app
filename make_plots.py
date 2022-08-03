import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def get_plot_params(col_names):
    if len(col_names) > 5:
        k = np.arange(1,len(col_names)+1)
        cols = len(col_names)/2
        rows = 2
    else:
        k = np.arange(1,len(col_names)+1)
        cols = len(col_names)
        rows = 1

    return k, int(cols), rows


def get_corr_plot(df1, df2):
    fig = plt.figure(figsize=(20,6))
    plt.subplots_adjust(hspace=0.3)
    for i, col in enumerate(df1.columns[2:]):
        k, cols, rows = get_plot_params(df1.columns[2:])

        axs = fig.add_subplot(rows, cols, k[i])
        g = plt.scatter(df1[col], 
                        df2['preds_'+col], 
                        alpha=0.8, edgecolors='white')

        r2 = r2_score(df1[col], 
                        df2['preds_'+col])
        axs.set_title(col.replace('docking_score_','')+' R2 = {:.2f}'.format(r2), 
                    fontsize = 12)    

    st = fig.suptitle("VDR"+', correlations of true and predicted values, test set', 
                    fontsize=20)

    st.set_y(1.1)
    fig.subplots_adjust(top=1.)

    # add frame around other frames
    g = fig.add_subplot(111, frameon=False)
    # hide it's ticks
    plt.tick_params(labelcolor='none', which='both', 
                    top=False, bottom=False, 
                    left=False, right=False)
    plt.ylabel('TRUE', fontsize = 20)
    plt.xlabel('PREDICTED', fontsize = 20)
    plt.show()

    return fig