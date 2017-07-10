# a short script to delete all non-GTEx genetic data from TCGA microarray data
import pandas as pd
import numpy as np

# read in the microarray data as a pandas DataFrame
df = pd.read_table('f_data.txt', header = 0, index_col = 0, dtype=None)
row_names = list(df.index)

# read in the correspondence table of GTEx and TCGA genes 
df_genes = pd.read_table('../panda_data_updated/annotation.txt', header = 0, index_col = 0, dtype=None)
gtex_list = df_genes['geneNames'].tolist()

for row in row_names:
	if row not in gtex_list:
		df.drop(row)


# write dataframe to new file
df.to_csv('f_data_final.txt')

