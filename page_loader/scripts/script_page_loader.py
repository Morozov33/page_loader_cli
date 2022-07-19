#!/usr/bin/env python3

'''Start main script for page-loader utilite'''

import argparse
import logging
import sys
from page_loader.load import download


def main():
    parser = argparse.ArgumentParser(
        description='Download page in HTML-file along the specified path')
    parser.add_argument('download_url')
    parser.add_argument('-o', '--output', dest='path_to_file',
                        default='cwd',
                        help='''Path to download htlm-file.
                                Default - current work directory''')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%d.%m.%y  %I:%M:%S')
    logging.info('Started download page')
    try:
        download(args.download_url, args.path_to_file)
    except Exception:
        sys.exit(1)
    else:
        logging.info('Finished download page and local files')
        sys.exit()


if __name__ == '__main__':
    main()
