__author__ = 'David Karchmer'

# https://github.com/ampervue/docker-ffmpeg

import sys
import argparse
import os
from subprocess import Popen, PIPE

FFMPEG_CMD = ['ffmpeg']

def execute_ffmpeg(args):

    command = FFMPEG_CMD + args
    print('Calling: ' + str(command))
    pipe = Popen(command, stderr=PIPE)
    print(str(pipe.stderr.read()))
    pipe.terminate()
    print('Done with FFMPEG')


def create_thumbnail(input_file_name):

    #thumbnail_file_name = input_file_name[:-3] + '.jpg'
    thumbnail_file_name = 'thumbnail.jpg'
    if os.path.isfile(thumbnail_file_name):
        os.remove(thumbnail_file_name)

    # Create a 100x100 thumbnail for the given video
    ffmpeg_args = ['-i',
                   input_file_name,
                   '-vcodec',
                   'mjpeg',
                   '-vframes',
                   '1',
                   '-ss',
                   '2',
                   '-s',
                   '100x100',
                   thumbnail_file_name]

    execute_ffmpeg(ffmpeg_args)

    return thumbnail_file_name



def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--file', dest='file', type=str,
                        help='Input File to Process')

    args = parser.parse_args(arguments)

    print(args)

    if not args.file:
        print('ERROR: Input file is required')

    thumbnail_file = create_thumbnail(args.file)
    if os.path.isfile(thumbnail_file):
        print('Thmbnail Created: ' + thumbnail_file)
    else:
        print('ERROR: Something went wrong')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
