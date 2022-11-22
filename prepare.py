from langrank import prepare_train_file

#data = ['sample-data/ted-train.orig.aze', 'sample-data/ted-train.orig.ben', 'sample-data/ted-train.orig.fin']
#lang = ['aze', 'ben', 'fin']
#rank = [[0, 1, 2], [1, 0, 2], [1, 2, 0]]
data = ['eng.txt', 'fra.txt', 'ind.txt', 'jpn.txt', 'spa.txt']
lang = ['eng', 'fra', 'ind', 'jpn', 'spa']
rank = [[0, 1, 3, 4, 2], [2, 0, 3, 4, 1], [3, 1, 0, 4, 2], [3, 1, 4, 0, 2], [2, 1, 3, 4, 0]]

prepare_train_file(data, lang, rank, task='DEP')
