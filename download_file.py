# -*- coding: utf-8 -*-

import io
import sys
from urllib2 import urlopen

def download_length(response, output, length):

    BUFF_SIZE = 1024

    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1

    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print 'Downloaded %d%%' % ( (float(time + 1) / float(times)) * 100 )

    print 'Download complete'


def download(response, output):

    BUFF_SIZE = 1024

    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)

        if not data:
            break

        output.write(data)
        print('Downloaded {bytes} bytes'.format(bytes=total_downloaded))

    print "Download complete"

def main():
    response = urlopen(sys.argv[1])
    out_file = io.FileIO('dados.zip', mode='w')

    info = response.info()
    content_length = info['Content-Length']

    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()
    print('Finished')

if __name__ == '__main__':
    main()