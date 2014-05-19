import os
import math
import sys
import operator
from collections import Counter

global g_EntropyFileList

def GetEntropyFromFileNew(filename):
    with open(filename, 'rb') as f:
        buffer = f.read()
        size = f.tell()

    occurance = {}
    c = Counter(buffer)

    entropy = 0.0
    for x, y in c.items():
        if y != 0:
            temp = float(y) / float(size)
            entropy = entropy + (-temp * (math.log(temp) * float(math.log(2))))

    print("Entropy: %8.2f, %s" % (entropy, filename))
    g_EntropyFileList[filename] = entropy


def scanDir(folder):
    for dirname, dirnames, filenames in os.walk(folder):
        for subdirname in dirnames:
            scanDir(os.path.join(dirname, subdirname))

        for filename in filenames:
            GetEntropyFromFileNew(os.path.join(dirname,filename))


            
if __name__ == "__main__":
    print('File entropy of directory\n')

    if (len(sys.argv) == 1):
        print('Usage: entropydir.py <foldername>\n')
        exit()

    g_EntropyFileList = {}
    scanDir(sys.argv[1])

    # print top 100 files with highest entropy
    print( '\n\nTop 100 entropy entries sorted from high to low:')
    sorted_entropy = sorted(g_EntropyFileList.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_entropy[:100]:
        print( "Entropy: %8.2f, %s" % (item[1], item[0]))
