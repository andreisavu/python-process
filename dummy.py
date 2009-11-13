r""" Dummy process used for testing

You can configure the amount of output and the total run time.
"""

import sys

from optparse import OptionParser
from time import time, sleep

def main():
    opt, args = parse_cli()

    lines = 20
    try:
        lines = int(opt.lines)
    except ValueError:
        print >>sys.stderr, 'Ignoring lines number. Using default value: %d' % lines 

    time_per_line = None
    try:
        if opt.time is not None: 
            time_per_line = float(opt.time)
    except ValueError:
        pass

    loop_start = time()
    for i in xrange(0, lines):
        start = time()
        print '#%d: %s' % (i, opt.content)
        if time_per_line is not None:
            try:
                sleep(time_per_line - (time()-start))
            except KeyboardInterrupt:
                print >>sys.stderr, 'Killed by user'
                return 1

    print >>sys.stderr, 'Loop run time: %d seconds' % int(time() - loop_start)
    return opt.retcode

def parse_cli():
    parser = OptionParser()

    parser.add_option('-t', '--time', dest='time',
        help='line display TIME. by default unset', metavar='TIME')

    parser.add_option('-l', '--lines', dest='lines',
        help='number of output LINES. by default 20', metavar='LINES',
        default=20)

    parser.add_option('-c', '--content', dest='content',
        help='line CONTENT', metavar='CONTENT',
        default='dummy process output')

    parser.add_option('-r', '--retcode', dest='retcode',
        help='return CODE', metavar='CODE', default=0)

    return parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())

