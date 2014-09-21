"""
Understanding the data set
"""
import sys
import getopt
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from itertools import cycle
import nltk.probability


def process_plaintext(dir_path):
    reader = CategorizedPlaintextCorpusReader(dir_path,
                    r'.*\.txt', cat_pattern=r'.+_.+_(.*)\.txt')
    facilitator_files = reader.fileids(categories='facilitator')
    participant_files = reader.fileids(categories='participant')
    print facilitator_files, participant_files

    #print reader.categories()
    #print len(reader.words())
    print len(reader.sents())

    fac_words = [word for word in reader.words(facilitator_files)]
    par_words = [word for word in reader.words(participant_files)]

    fac_words = edit_tokens(fac_words)
    par_words = edit_tokens(par_words)

    speakers = (
        [(word, 'facilitator') for word in reader.words(facilitator_files)] +
        [(word, 'participant') for word in reader.words(participant_files)]
    )

    fd_fac = nltk.FreqDist(fac_words)
    vocab_fac = fd_fac.keys()

    fd_par = nltk.FreqDist(par_words)
    vocab_par = fd_par.keys()

    print "Fac Vocab: " , len(vocab_fac)
    print vocab_fac[:20]
    print "Par Vocab: " , len(vocab_par)
    print vocab_par[:20]
    fd_par.plot(100, cumulative=True)

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
