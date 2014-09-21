"""
Module docstring.

This serves as a long usage message.
"""
import sys
import getopt

def main(argv):
    # parse command line options
    try:
        # list of argv from below,
        # string of one letter options e.g. -h, -w
        # list of long options, e.g. --help
        opts, args = getopt.getopt(argv, "hw", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        if o in ("-w", "--wiki"):
            print "Using wiki..."
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    # first argv is the script name, which we don't care about
    # so just pass the rest of it to main
    main(sys.argv[1:])
