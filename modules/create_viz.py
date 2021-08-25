import matplotlib.pyplot as plt
import seaborn as sns

def outliers_plot(df, labels, typeOfPlot=0):
    if typeOfPlot in [0, 2]:
        plt.figure(figsize=(7,7))
        sns.scatterplot(data=df, x=labels['x'], y=labels['y'])
        plt.show()
    if typeOfPlot in [1, 2]:    
        plt.figure(figsize=(7,7))
        sns.set(style="whitegrid")
        sns.boxenplot(data=df,scale="linear",x=labels['x'],y=labels['y'], color="orange")
        plt.show()