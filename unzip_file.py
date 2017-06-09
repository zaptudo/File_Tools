# coding: utf-8

import sys
import os
import zipfile

def main(path):

    if not os.path.exists(path):
        print 'File {file} does not exists'.format(file=path)
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(file=path, mode='w')
        zfile.extractall()
        print 'Extraction finished'
        

if __name__ == '__main__':
    main(sys.argv[0])