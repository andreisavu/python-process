
import unittest

from killableprocess import Popen
from subprocess import PIPE
from time import time
from math import floor

class TestKillProcess(unittest.TestCase):

    def test_InTimeRun(self):
        start = time()
        p = Popen(['python', 'dummy.py', '-t', '1', '-l', '2'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        out_length = len(filter(None, stdout.split("\n")))
        err_length = len(stderr.split("\n"))

        self.assertEquals(out_length, 2)
        self.assertEquals(err_length, 2)
        self.assertEquals(floor(time()-start), 2)

    def test_timeExceeded(self):
        start = time()
        p = Popen(['python', 'dummy.py', '-t', '1', '-l', '2'], stdout=PIPE, stderr=PIPE)
        retcode = p.wait(1)
        self.assertEquals(retcode, -9)
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()

