import random
import pandas as pd
import string

sentence = "one fish two fish red fish blue fish black fish blue fish old fish new fish this one has a little star this one has a little car say what a lot of fish there are yes some are red and some are blue some are old and some are new some are sad and some are glad and some are very very bad why are they sad and glad and bad i do not know go ask your dad some are thin and some are fat the fat one has a yellow hat are"

TWEET_LENGTH = 280

'''
 Returns a dictionary with word frequencies associated with each word
 @param library: an array of strings to parse from
 @return word-frequency dictionary
'''
def get_markov_dict(library):
    word_chain = {}
    last_word = ""
    for sentence in library:
        for word in sentence.split(' '):
            # Cleaned word used for keys, with punctuation and case being added in the key values
            clean_word = clean_string(word)
            if clean_word not in word_chain:
                word_chain[clean_word] = []
            if last_word != "":
                word_chain[last_word].append(word)
            last_word = word
    return word_chain

def clean_string(input):
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    # TODO: get string stripping punctuation working
    return input;

def get_tweets_csv(csv):
    # CSV file has weird encoding, so not default
    df = pd.read_csv(csv, encoding='cp1252')
    return df['text'].tolist()

def generate_tweet(csv):
    word_chain = get_markov_dict(get_tweets_csv(csv))
    word = random.choice(list(word_chain))
    ret_str = ""
    for i in range(100):
        if (len(ret_str) + len(word + ' ')) > TWEET_LENGTH:
            break
        ret_str += word + ' ' 
        clean_word = clean_string(word)
        if (word_chain[clean_word] == []):
            break
        word = random.choice(word_chain[clean_word])
    return ret_str

print(generate_tweet('trump_tweets.csv'))
