"""
Understanding the data set
"""

import sys
import getopt
import nltk.probability
import random
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from nltk.model import NgramModel
from itertools import cycle

def process_plaintext(dir_path):
    reader = CategorizedPlaintextCorpusReader(dir_path,
                    r'.*\.txt', cat_pattern=r'.+_.+_(.*)\.txt')
    facilitator_files = reader.fileids(categories='facilitator')
    participant_files = reader.fileids(categories='participant')
    print facilitator_files, participant_files

    #print reader.categories()
    #print len(reader.words())
    #print len(reader.sents())

    fac_words = [word for word in reader.words(facilitator_files)]
    par_words = [word for word in reader.words(participant_files)]

    fac_words = edit_tokens(fac_words)
    par_words = edit_tokens(par_words)

    speakers = (
        [(word, 'facilitator') for word in reader.words(facilitator_files)] +
        [(word, 'participant') for word in reader.words(participant_files)]
    )

    features = get_features(speakers)

    size = int(len(features) * 0.3)
    nb_train = features[size:]
    nb_test = features[:size]

    classifier = nltk.NaiveBayesClassifier.train(nb_train)
    print "Classifier labels:", classifier.labels()
    print classifier.show_most_informative_features()
    print "Clasify test:", nltk.classify.accuracy(classifier, nb_test)
    #print classifier.classify(get_features(["Yolo", "bag", "sp"], False))
    
    #random.shuffle(speakers)
    three_quarters = int(len(speakers) * 0.75)
    train = speakers[:three_quarters]
    test = speakers[three_quarters:]

    est = lambda fdist, bins: nltk.probability.LaplaceProbDist(fdist)
    un_lm = NgramModel(1, train, estimator=est)
    bi_lm = NgramModel(2, train, estimator=est)
    tr_lm = NgramModel(3, train, estimator=est)
    qu_lm = NgramModel(4, train, estimator=est)
    pe_lm = NgramModel(5, train, estimator=est)
    print un_lm
    print bi_lm
    print tr_lm
    print qu_lm
    print pe_lm
    print "1 gram Perplexity:", un_lm.perplexity(test)
    print "2 gram Perplexity:", bi_lm.perplexity(test)
    print "3 gram Perplexity:", tr_lm.perplexity(test)
    print "4 gram Perplexity:", qu_lm.perplexity(test)
    print "5 gram Perplexity:", pe_lm.perplexity(test)

    print bi_lm.generate(10, ["uh", "sp"])

    fd_fac = nltk.FreqDist(fac_words)
    vocab_fac = fd_fac.keys()

    fd_par = nltk.FreqDist(par_words)
    vocab_par = fd_par.keys()

    print "Fac Vocab: " , len(vocab_fac)
    print "Fac Tokens: " , len(fac_words)
    print vocab_fac[:20]
    print "Par Vocab: " , len(vocab_par)
    print "Par Tokens: " , len(par_words)
    print vocab_par[:20]
    fd_par.plot(50)

def get_features(arr, known=True):
    features = []
    if known:
        for i, (w, subject) in enumerate(arr):
            print i, w
            features.append( (prev_features(arr, i), subject) )
    else:
        for i, w in enumerate(arr):
            print i, w
            features.append( (prev_features(arr, i)) )
    return features

def prev_features(words, i):
    features = {}
    if i == 0:
        features["prev-word"] = "<S>"
    else:
        features["prev-word"] = words[i-1]

    if i == 0 or i == 1:
        features["prev-word-2"] = "<S>"
    else:
        features["prev-word-2"] = words[i-2]
    return features

def edit_tokens (input_words):
    """
    Merge "{", ".+", "}" into one token
    """
    length = len(input_words)
    for i, w in enumerate(input_words):
        if (w == "{"):
            if (i+2 < length):
                if (input_words[i+2] == "}"):
                    input_words[i:i+3] = [''.join(input_words[i:i+3])]
    return input_words


def main(argv):
    # parse command line options
    try:
        # list of argv from below,
        # string of one letter options e.g. -h, -w
        # list of long options, e.g. --help
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

    process_plaintext('./ps16_dev_data/plain_text/AS1_split_fac_part_plain_text')

if __name__ == "__main__":
    # first argv is the script name, which we don't care about
    # so just pass the rest of it to main
    main(sys.argv[1:])
