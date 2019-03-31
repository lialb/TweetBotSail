import random
import pandas as pd
import string

TWEET_LENGTH = 280

'''
 Returns a dictionary with word frequencies associated with each word
 @param library: an array of strings to parse from
 @return a tuple containing beginning words, word-frequency dictionary
'''
def get_markov_dict(library):
    word_chain = {}
    begin_words = []
    for sentence in library:
        last_word = ''
        clean_sentence = clean_string(sentence)
        begin_words.append(clean_sentence.split(' ')[0])
        for word in clean_sentence.split(' '):
            if word not in word_chain:
                word_chain[word] = []
            if last_word != '':
                word_chain[last_word].append(word)
            last_word = word
    return begin_words, word_chain

def clean_string(input):
    input = input.replace('&amp', '&')
    input = input.replace('&;', ';')
    input = input.replace('@', '')
    input = input.replace('#', '')
    return input;

def get_tweets_csv(csv):
    df = pd.read_csv(csv)
    return df['text'].tolist()

def generate_tweet(csv):
    begin_words, word_chain = get_markov_dict(get_tweets_csv(csv))
    word = random.choice(begin_words)
    ret_str = ''
    for i in range(100):
        if (len(ret_str) + len(word + ' ')) > TWEET_LENGTH:
            break
        ret_str += word + ' '
        clean_word = clean_string(word)
        if (word_chain[clean_word] == []):
            break
        word = random.choice(word_chain[clean_word])
    return ret_str

# print(generate_tweet('csv/obama.csv'))
