#!/usr/bin/env python3

import requests
import subprocess

APP_KEY_FILE = 'APP_KEY'
UNSPLASH_API_URL = 'https://api.unsplash.com'
WALLPAPER_FILE = '/tmp/wallpaper'
WALLPAPER_SET_CMD = ['feh', '--bg-scale']


def main():
    with open(APP_KEY_FILE, mode='r') as app_key_file:
        APP_KEY = app_key_file.read()

    session = requests.session()
    params = {
        'client_id': APP_KEY,
        'orientation': 'landscape',
        'featured': True
    }
    response = session.get(UNSPLASH_API_URL + '/photos/random/', params=params)
    image_url = response.json()['urls']['full']
    image_response = session.get(image_url)

    with open(WALLPAPER_FILE, mode='wb') as wallpaper_file:
        wallpaper_file.write(image_response.content)

    subprocess.run(WALLPAPER_SET_CMD + [WALLPAPER_FILE])

    return True


if __name__ == '__main__':
    main()
