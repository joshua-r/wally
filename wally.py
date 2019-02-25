#!/usr/bin/env python3

'''Retrieve a random photo from Unsplash'''

import argparse
import requests

APP_KEY_FILE = 'APP_KEY'
UNSPLASH_API_URL = 'https://api.unsplash.com'


def read_file(filename):
    '''Read a text file as a string'''
    with open(filename, mode='r') as text_file:
        return text_file.read()


def write_image(image, filename):
    '''Write the image into a file'''
    with open(filename, mode='wb') as image_file:
        image_file.write(image)


def main():
    '''Retrieve a random photo from Unsplash'''
    # setup argparse
    parser = argparse.ArgumentParser(
        description='Get a random photo from unsplash.')
    parser.add_argument('--featured', action='store_true',
                        help='restrict to featured photos')
    parser.add_argument('--query',
                        default='wallpaper', help='term to search for')
    parser.add_argument('--filename',
                        default='/tmp/wallpaper.jpg', help='filename for the retrieved photo')
    args = parser.parse_args()

    # read the app key
    app_key = read_file(filename=APP_KEY_FILE)

    # request a single random photo
    session = requests.session()
    params = {
        'client_id': app_key,
        'orientation': 'landscape',
        'query': args.query,
        'featured': args.featured
    }
    response = session.get(UNSPLASH_API_URL + '/photos/random/', params=params)
    image_url = response.json()['urls']['full']
    image_response = session.get(image_url)

    # write the retrieved image
    write_image(image=image_response.content, filename=args.filename)


if __name__ == '__main__':
    main()
