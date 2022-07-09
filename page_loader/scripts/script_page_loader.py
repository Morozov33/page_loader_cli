#!/usr/bin/env python3

'''Start main script for page-loader utilite'''

import argparse
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
    print(download(args.download_url, args.path_to_file))


if __name__ == '__main__':
    main()
