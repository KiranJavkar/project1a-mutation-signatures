import pandas as pd
import numpy as np
from sklearn.decomposition import NMF

def np_save(npz_file_name, np_object):
	f = open(npz_file_name,'wb')
	np.save(f, np_object)
	f.close()

#full_catalog_pd = pd.read_pickle('full_catalog_pd.pkl')
#genome_catalog_pd = pd.read_pickle('genome_catalog_pd.pkl')
exome_catalog_pd = pd.read_pickle('exome_catalog_pd.pkl')

#P_list_full = []
#E_list_full = []

P_list_exome = []
E_list_exome = []

#P_list_genome = []
#E_list_genome = []

for i in range(100):
	print(i)
	model = NMF(n_components=27, init='random', max_iter=10000)
#	P = model.fit_transform(full_catalog_pd)
#	E = model.components_
#	P_list_full.append(P)
#	E_list_full.append(E)
	
	P = model.fit_transform(exome_catalog_pd)
	E = model.components_
	P_list_exome.append(P)
	E_list_exome.append(E)
	
#	P = model.fit_transform(genome_catalog_pd)
#	E = model.components_
#	P_list_genome.append(P)
#	E_list_genome.append(E)

#np.save('P_full.npz', np.array(P_list_full))
#np.save('E_full.npz', np.array(E_list_full))
np.save('P_exome27sig_1.npz', np.array(P_list_exome))
np.save('E_exome27sig_1.npz', np.array(E_list_exome))
#np.save('P_genome.npz', np.array(P_list_genome))
#np.save('E_genome.npz', np.array(E_list_genome))
