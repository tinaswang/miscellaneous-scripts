# A short script to separate male and female TCGA microarray data
# by turning data into a pandas DataFrame
# Optimized for Broad Institute Firehose (http://gdac.broadinstitute.org/) data

import pandas as pd
import numpy as np


# need to get the lists of all male and female patients
f_data = open("lusc_f.txt", "r")
m_data = open("lusc_m.txt", "r")
# turn into python lists
f_list = f_data.read().splitlines()
m_list = m_data.read().splitlines()


# Because there are multiple json objects in the file, data is a list of dictionaries
df = pd.read_table('microarray.txt', header = 0, index_col = 0, dtype=None)
df_f = pd.DataFrame(index=df.index)
id_list = list(df.columns.values)
concat_id_list = [patient[:-16] for patient in id_list]
df.columns = concat_id_list
# open a new file to write to
f = open('f_lusc_data.txt', 'w')
for patient in f_list:
	if patient in concat_id_list:
		# add data to new dataframe
		df_f[patient] = df[patient]
		# drop female patient from original data frame
		df.drop(patient, axis=1)
# write dataframe to new file
df.to_csv('f_data.txt')

# close the files
f.close()
f_data.close()
m_data.close()

