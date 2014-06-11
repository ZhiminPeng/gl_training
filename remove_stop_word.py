
stop_words = 'common-english-words.txt'
stop_words_list = []

for line in file('common-english-words.txt'):
    stop_words_list.extend(line.strip().split(','))

stop_word_set = set(stop_words_list)

def normalize_dict_values(d):
    total_value = np.sum(d.values())
    return dict([(k, v / total_value) for k, v in d.iteritems()])


train_data['summary_words'] = train_data['summary_words'].apply(lambda x: dict([(k,v) for k,v in x.iteritems() 
                                                                                    if k not in stop_word_set])) 
train_data['summary_words'] = train_data['summary_words'].apply(normalize_dict_values)


train_data['description_words'] = train_data['description_words'].apply(lambda x: dict([(k,v) for k,v in x.iteritems() 
                                                                                    if k not in stop_word_set])) 
train_data['description_words'] = train_data['description_words'].apply(normalize_dict_values)



