# Usage: You can run this by passing in all the necessary parameters, however, it is recommended that you
# explore the grid_search_single_run.sh file and run it using something like that.
# If you want to run this stand-alone, then you can run it as follows:
# python3 final_project.py path/to/traindata.csv path/to/testdata.csv desired/path/to/result_file.csv

from fire import Fire
import itertools
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import scale
from gensim.models.fasttext  import FastText
from gensim.models.word2vec  import Word2Vec
import nltk
import re


# Creates a densely connected Keras model
def create_model(optimizer='adam', network_structure=[10, 10], input_dim=18829):

    model = Sequential()

    model.add(Dense(network_structure[0], input_dim=input_dim, activation='relu'))
    for i in range(1, len(network_structure)):
        model.add(Dense(network_structure[i], activation='relu'))
    model.add(Dense(3, activation='softmax'))

    # Compile model
    model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model


# Loads tweets and creates a synthetic feature based on the tweet text and user description
def load_data(trainset_filename, testset_filename):

    # load training dataset
    full_training_dataset = pd.read_csv(trainset_filename)

    # Create coding for target labels
    full_training_dataset.stance = pd.Categorical(full_training_dataset.stance, categories=["for", "against", "neutral"], ordered=True)
    full_training_dataset['code'] = full_training_dataset.stance.cat.codes

    # Create a synthetic feature which combines tweet text and user description text
    full_training_dataset['combined_t'] = full_training_dataset['tweet_t'] + ' ' + full_training_dataset['user_description']

    # Grab the relevant feature and target labels
    training_data = full_training_dataset['combined_t']
    training_labels = full_training_dataset['code']

    full_testing_dataset = pd.read_csv(testset_filename)

    full_testing_dataset.stance = pd.Categorical(full_testing_dataset.stance, categories=["for", "against", "neutral"], ordered=True)
    full_testing_dataset['code'] = full_testing_dataset.stance.cat.codes

    full_testing_dataset['combined_t'] = full_testing_dataset['tweet_t'] + ' ' + full_testing_dataset['user_description']
    testing_data = full_testing_dataset['combined_t']
    testing_labels = full_testing_dataset['code']

    testing_labels = pd.Categorical(testing_labels)

    return (training_data, training_labels, testing_data, testing_labels)


# Vectorizes data using the tfidf method
def tfidf_vectorize_data(train_data, test_data):

    # Set the vectorizer to transform the data into inputs for classifiers
    vectorizer = TfidfVectorizer(ngram_range=(1,3), analyzer='char', use_idf=True)
    x_train = vectorizer.fit_transform(train_data.values.astype('U'))
    x_test = vectorizer.transform(test_data.values.astype('U'))

    return x_train, x_test


# Calculates the tfidf values for every word in the corpus and returns a lookup table
# Reference https://ahmedbesbes.com/sentiment-analysis-on-twitter-using-word2vec-and-keras.html
def get_word_tfidf(train_data):

    # Remove anything non-alphabetic from the text, except underscores
    clean_data = list(map(lambda s: re.sub(r'[^\w]', ' ', str(s)), train_data))

    # Find the tfidf values for the corpus and create a lookup table for each word
    vectorizer = TfidfVectorizer(analyzer='word', use_idf=True)
    vectorizer.fit(train_data.values.astype('U'))
    tfidf = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))

    return tfidf


# Trains and returns a FastText model based on the training data
# Reference: https://towardsdatascience.com/understanding-feature-engineering-part-4-deep-learning-methods-for-text-data-96c44370bbfa
def train_fasttext(train_data):

    # Remove anything non-alphabetic from the text, except underscores
    clean_data = list(map(lambda s: re.sub(r'[^\w]', ' ', str(s)), train_data))

    # Break up the tweets into word lists
    wpt = nltk.WordPunctTokenizer()
    tokenized_corpus = [wpt.tokenize(tweet) for tweet in clean_data]

    # Set values for various parameters
    feature_size = 100    # Word vector dimensionality  
    window_context = 20          # Context window size
    min_word_count = 5   # Minimum word count                        
    sample = 1e-3   # Downsample setting for frequent words
    
    # sg decides whether to use the skip-gram model (1) or CBOW (0)
    ft_model = FastText(tokenized_corpus, size=feature_size, window=window_context, 
                        min_count=min_word_count,sample=sample, sg=0, iter=50)
                        
                        
    # view similar words based on gensim's FastText model
    similar_words = {search_term: [item[0] for item in ft_model.wv.most_similar([search_term], topn=5)]
                      for search_term in ['no', 'yes', 'please', 'coal', 'energy', 'jobs']}
    print(similar_words)                    

    return ft_model


# Trains and returns a Word2Vec model based on the training data
# Reference: https://towardsdatascience.com/understanding-feature-engineering-part-4-deep-learning-methods-for-text-data-96c44370bbfa
def train_word2vec(train_data):

    # Remove anything non-alphabetic from the text, except underscores
    clean_data = list(map(lambda s: re.sub(r'[^\w]', ' ', str(s)), train_data))

    # Break up the tweets into word lists
    wpt = nltk.WordPunctTokenizer()
    tokenized_corpus = [wpt.tokenize(tweet) for tweet in clean_data]

    # Set values for various parameters
    feature_size = 100    # Word vector dimensionality  
    window_context = 20          # Context window size
    min_word_count = 5   # Minimum word count                        
    sample = 1e-3   # Downsample setting for frequent words
    
    # sg decides whether to use the skip-gram model (1) or CBOW (0)
    w2v_model = Word2Vec(tokenized_corpus, size=feature_size, window=window_context, 
                        min_count=min_word_count, sample=sample, sg=0, iter=50)

    w2v_model.train(tokenized_corpus, total_examples=len(tokenized_corpus), epochs=10)
                        
                        
    # view similar words based on gensim's Word2Vec model
    similar_words = {search_term: [item[0] for item in w2v_model.wv.most_similar(positive=[search_term], topn=5)]
                      for search_term in ['no', 'yes', 'please', 'coal', 'energy', 'jobs']}
    print(similar_words)                    

    return w2v_model


# Performs a grid search of densely connected networks, varying the number of nodes and number of layers
def run_grid_search(num_nodes, num_layers, train_data, train_labels, test_data, test_labels, output_file):

    df_model = pd.DataFrame(columns=['network_structure', 'loss', 'acc', 'f1'])

    index = 0

    # Iterates through every permutation of the number of layers and the number of nodes per layer
    for n in range(0, len(num_layers)):
        for i in list(itertools.permutations(num_nodes, num_layers[n])):
            model = create_model(network_structure=i, input_dim=train_data.shape[1])

            model.fit(train_data, train_labels, epochs=5, batch_size=128)

            loss_and_metrics = model.evaluate(test_data, test_labels, batch_size=128)
            prediction_y = model.predict(test_data, batch_size=128)
            y_pred = [None] * len(prediction_y)
            for j in range(0, len(prediction_y)):
                y_pred[j] = np.argmax(prediction_y[j])

            df_model.loc[index] = [" ".join(str(x) for x in i),
                             loss_and_metrics[0],
                             loss_and_metrics[1],
                             f1_score(test_labels, y_pred, average='macro')]
            index += 1

    # Prints and saves the results of each model
    print(df_model)
    df_model.to_csv(output_file)


# Computes averaged "tweet vectors" for each tweet
# Reference https://ahmedbesbes.com/sentiment-analysis-on-twitter-using-word2vec-and-keras.html
def get_Tweet_Vector(tweet, vec_size, vec_model, tfidf=None):

    vec = np.zeros(vec_size).reshape((1, vec_size))
    count = 0

    # Finds every word's embedding and weighting and then adds them to the tweet vector to get averaged
    for word in tweet:
        try:
            if tfidf is None:
                vec += vec_model.wv[word].reshape((1, vec_size))
            else: 
                vec += vec_model.wv[word].reshape((1, vec_size)) * tfidf[word]

            count += 1
        except KeyError: # handling the case where the token is not
                         # in the corpus. useful for testing.
            continue
    if count != 0:
        vec /= count
    return vec


def main(train_file=None, test_file=None, output=None):

    train_data, train_labels, test_data, test_labels = load_data(train_file, test_file)

    # Uncomment the line below if you'd like to vectorize the data using tf-idf (not recommened to use in combination with fastText or word2vec
    #x_train, x_test = tfidf_vectorize_data(train_data, test_data)

    # Simply fits the tfidf model and gathers the weights, doesn't change the data
    tfidf = get_word_tfidf(train_data)

    # Comment or uncomment either line below to change which embedding model you'd like to use.
    embedding_model = train_fasttext(train_data)
    #embedding_model = train_word2vec(train_data)

    # Gathers the tweet vectors and then normalizes them
    # Remove the tfidf variable from the argument list if you'd like to calculate vectors without it
    x_train = np.concatenate([get_Tweet_Vector(words, 100, embedding_model, tfidf) for words in list(map(lambda x: str(x).split(), train_data))])
    x_train = scale(x_train)

    # Gathers the tweet vectors and then normalizes them
    # Remove the tfidf variable from the argument list if you'd like to calculate vectors without it
    x_test = np.concatenate([get_Tweet_Vector(words, 100, embedding_model, tfidf) for words in list(map(lambda x: str(x).split(), test_data))])
    x_test = scale(x_test)

    # Adjust these to change the layer/nodes-per-layer permutation possibilities
    num_nodes = [10, 25, 50, 100, 500, 1000]
    num_layers = [1, 2, 3, 4]

    run_grid_search(num_nodes, num_layers, x_train, train_labels, x_test, test_labels, output)


if __name__ == '__main__':
    Fire(main)
