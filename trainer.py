'''
Trainer file for creating NBC to do sentiment analysis.
'''

from os import path, remove
import pickle


def train_shit():
    '''
    Training method to train a classifier and return it so that it can be pickled
    '''
    return 'blah'

if __name__ == "__main__":
    if path.isfile('./classifier.pickle'):
        delete = raw_input('Classifier exists. Delete? (Y/N)')
        if 'Y' in delete:
            print "deleting pickled trained classifier"
            remove('./classifier.pickle')
        else:
            print "Goodbye"
            exit(0)
    classifier = train_shit()
    print "Saving classifier now"
    f = open('classifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()
    print "Saved as classifier.pickle"
