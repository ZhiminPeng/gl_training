
import numpy as np

def remove_stop_words(data, column_name):

	stop_words = 'common-english-words.txt'
	stop_words_list = []
	
	for line in file('common-english-words.txt'):
		stop_words_list.extend(line.strip().split(','))
	
	stop_word_set = set(stop_words_list)

	return data[column_name].apply(lambda x: dict([(k,v) for k,v in x.iteritems() if k not in stop_word_set])) 

def normalize_dict_values(d):

	total_value = np.sum(d.values())
	return dict([(k, v / total_value) for k, v in d.iteritems()])
