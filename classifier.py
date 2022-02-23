import json
import csv
import re
import math


class Classifier:
    def __init__(self):
        self.trigrams = {}
        self.trigrams_total = {}
        self.unique_trigrams = []
        self.__trained = False
    
    def train(self, file):
        '''
        Takes a csv file as input without headers.
        Each row must contain two columns separated by commas.
        The first column a string.
        The second column the label.
        '''
        with open(file, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                label = row[1]
                words = self._extract_words(row[0])
                for word in words:
                    self._extract_trigrams(word, label)
        self._calculate_probabilities()
        self.__trained = True
        
    def _extract_words(self, row):
        '''
        A very simple regex to separate words
        '''
        return re.findall(r"\w+", row)
        
    def _extract_trigrams(self, word, label):
        '''
        This function extracts the trigrams from each word
        '''
        self._add_label(label)
        processed_word = self._pre_process_word(word)
        for i in range(len(processed_word)-2):
            self._count_trigram(processed_word[i:i+3], label)
            
    def _add_label(self, label):
        '''
        Add the label to the dictionaries if it was not added previously
        '''
        if label not in self.trigrams.keys():
            self.trigrams[label] = {}
            self.trigrams_total[label] = 0

    def _pre_process_word(self, word):
        '''
        Adds two dummy characters before and one after the word
        and transform it to lowerspace
        '''
        return '_*' + word.lower() + '#'
            
    def _count_trigram(self, trigram, label):
        '''
        Add the trigram frequency to the dictionary 
        '''
        if trigram not in self.trigrams[label].keys():                
            self.trigrams[label][trigram] = 1 #laplace smoothing
        self.trigrams[label][trigram] += 1
        self.trigrams_total[label] += 1
        self._add_unique_trigram(trigram)
        
    def _add_unique_trigram(self, trigram):
        '''
        Keeps a list of unique trigrams.
        '''
        if trigram not in self.unique_trigrams:
            self.unique_trigrams.append(trigram)
    
    def _calculate_probabilities(self):
        '''
        Calculates the probabilities for all extracted trigrams
        '''
        unique_total = len(self.unique_trigrams)
        for label, trigrams in self.trigrams.items():
            for trigram, frequency in trigrams.items():
                self.trigrams[label][trigram] = frequency/(self.trigrams_total[label] + unique_total)
                
    def save_model(self, filename):
        '''
        Saves trigrams probabilities to a file
        '''
        if self.__trained:
            with open(filename, "w") as outfile:
                model = {
                    'trigrams': self.trigrams,
                    'trigrams_total': self.trigrams_total,
                    'unique_trigrams': self.unique_trigrams
                }
                json.dump(model, outfile)
        else:
            raise Exception('Model is not trained yet.')
            
    def load_model(self, filename):
        '''
        Saves trigrams probabilities to a file
        '''
        try:
            with open(filename, "r") as inputfile:
                model = json.load(inputfile)
            self.trigrams = model['trigrams']
            self.trigrams_total = model['trigrams_total']
            self.unique_trigrams = model['unique_trigrams']
            self.__trained = True
        except OSError:
            return "Could not open/read file:", inputfile
    
    def predict(self, string):
        '''
        Assigns a label to a word or piece of text
        '''
        if not self.__trained:
            raise Exception('Model is not trained yet.')
        scores = {}
        for label in self.trigrams.keys():
            scores[label] = 0
            words = self._extract_words(string)
            for word in words:
                processed_word = self._pre_process_word(word)
                for i in range(len(processed_word)-2):
                    scores[label] += self._get_probability(label, processed_word[i:i+3])
        return max(scores, key=scores.get), scores
    
    def _get_probability(self, label, trigram):
        '''
        Tries to get the probability from the dictionary or calculates a mininum
        '''
        if trigram in self.trigrams[label].keys():
            return math.log(self.trigrams[label][trigram])
        else:
            return math.log(1/(len(self.unique_trigrams) + self.trigrams_total[label]))