import seaborn as sns
 
def main():
    df = sns.load_dataset('iris')
    new_df = choose_species(df, 'setosa') # Select only the species here
    sns_plot = sns.pairplot(new_df, hue='species')
    sns_plot.figure.savefig("output.png")
 
 
if __name__ == '__main__':
    main()