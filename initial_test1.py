
import graphlab as gl
from graphlab import *
train_data = gl.load_sframe('train_data')

all_keys = ['source','hour', 'weekday', 'tag_type','geo_label_4','geo_label_40',
            'description_words','summary_length','summary_words',
            'num_comments',	'num_views','num_votes']

features = ['source','hour', 'weekday', 'tag_type','geo_label_4','geo_label_40',
            'description_words','summary_length','summary_words',
            'num_comments',	'num_views']

# split the data into training data and testing data


train_data['geo_label_4'] = train_data['geo_label_4'].apply(lambda x: str(x))
train_data['geo_label_40'] = train_data['geo_label_40'].apply(lambda x: str(x))
train_data['weekday'] = train_data['weekday'].apply(lambda x: str(x))
train_data['summary_length'] = train_data['summary_length'].apply(lambda x: str(x) if x <=5 else '6')

extract_train_data, extract_test_data = train_data.select_columns(all_keys).random_split(fraction=0.7, seed=None)


train_data.column_types()

train_data.column_names()


m = linear_regression.create(extract_train_data, target='num_votes',             
                             features = features)



coefficients = m['coefficients']


predictions = m.predict(extract_test_data)

results = m.evaluate(extract_test_data)

print predictions

print results


# print coefficients.topk('Coefficient', k=100)


