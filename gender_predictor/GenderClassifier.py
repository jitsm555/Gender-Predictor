'''
This class responsible for classifying gender based on the given name.
We are using NaiveBayesClassifier classifier to classify gender names
There are three types of gender we are cassifying here
a.Male
b.Female
c.Unisex
https://stackoverflow.com/questions/28708705/pypi-400-upload-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
Note:This classification purely based on the data, and some pre-conditions.
'''

from nltk import NaiveBayesClassifier, classify
import gender_predictor.GenderLoader as GenderLoader
import random


class GenderClassifier:
    def get_features(self):
        male_names, female_names = self._load_names()

        feature_set = list()

        for nameTuple in male_names:
            features = self._name_features(nameTuple[0])
            male_prob, female_prob = self._get_prob_distr(nameTuple)
            features['male_prob'] = male_prob
            features['female_prob'] = female_prob
            feature_set.append((features, 'M'))
        # print(feature_set)

        for nameTuple in female_names:
            features = self._name_features(nameTuple[0])
            male_prob, female_prob = self._get_prob_distr(nameTuple)
            features['male_prob'] = male_prob
            features['female_prob'] = female_prob
            feature_set.append((features, 'F'))

        return feature_set

    def train_and_test(self, training_percent=0.80):
        feature_set = self.get_features()
        random.shuffle(feature_set)

        name_count = len(feature_set)

        cut_point = int(name_count * training_percent)

        train_set = feature_set[:cut_point]
        test_set = feature_set[cut_point:]

        self.train(train_set)

        return self.test(test_set)

    def classify(self, name):
        feats = self._name_features(name)
        return self.classifier.classify(feats)

    def train(self, train_set):
        self.classifier = NaiveBayesClassifier.train(train_set)
        return self.classifier

    def test(self, test_set):
        return classify.accuracy(self.classifier, test_set)

    def _get_prob_distr(self, nameTuple):
        male_prob = (nameTuple[1] * 1.0) / (nameTuple[1] + nameTuple[2])
        if male_prob == 1.0:
            male_prob = 0.99
        elif male_prob == 0.0:
            male_prob = 0.01
        else:
            pass
        female_prob = 1.0 - male_prob
        return (male_prob, female_prob)

    def get_most_informative_features(self, n=5):
        return self.classifier.most_informative_features(n)

    def _load_names(self):
        return GenderLoader.get_name_list()

    def _name_features(self, name):
        name = name.upper()
        return {
            'last_letter': name[-1],
            'last_two': name[-2:],
            'last_three': name[-3:],
            'last_is_vowel': (name[-1] in 'AEIOUY')
        }


if __name__ == "__main__":
    gp = GenderClassifier()
    accuracy = gp.train_and_test()
    print('Accuracy: %f' % accuracy)
    print('Most Informative Features')
    feats = gp.get_most_informative_features(10)
    for feat in feats:
        print('\t%s = %s' % feat)
    name = input('Enter name to classify: ')
    print('\n%s is classified as %s' % (name, gp.classify(name)))


def classify_gender(name):
    gp = GenderClassifier()
    accuracy = gp.train_and_test()
    print('Accuracy: %f' % accuracy)
    return gp.classify(name)
