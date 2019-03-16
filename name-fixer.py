#/bin/python3
from difflib import SequenceMatcher
import argparse
import bs4
import os
import re
import requests

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of TV show')
    parser.add_argument('directory', help='Name of directory')
    parser.add_argument('-c', help='remove first 5 characters of tv name', action='store_true')
    parser.add_argument('-u', help='Do these episodes need to be sorted?', action='store_true')

    try:
        return vars(parser.parse_args())
    except IOError:
        parser.error('Error')

def find_episodes(name):
    tvdb_url = 'https://www.thetvdb.com'

    search_request = requests.get(tvdb_url + '/search?q=' + name.replace(' ', '+') + '&l=en')
    search_soup = bs4.BeautifulSoup(search_request.text, features='html.parser')

    search_shows = search_soup.find('table', {'class': 'table table-hover'}).find_all('a')

    number = 1
    for show in search_shows:
        print(str(number) + ': ' + show.text)
        number += 1

    choice = int(input())
    if choice < 0 or choice > (number - 1):
        exit(1)

    show = search_shows[choice - 1]
    show_name = show.text
    print('\nSelected ' + show_name + '\n')

    episodes_link = tvdb_url + show.get('href') + '/seasons/all'
    episodes_request = requests.get(episodes_link)
    episodes_soup = bs4.BeautifulSoup(episodes_request.text, features='html.parser')

    seasons = episodes_soup.find('div', {'class': 'col-xs-12 col-sm-8 episodes'}).find_all('h3')

    episodes = []

    for i in range(len(seasons)):
        season_episodes = episodes_soup.find('div', {'class': 'col-xs-12 col-sm-8 episodes'}).find_all('table', {'class': 'table table-hover'})[i]

        season_number = seasons[i].text.strip()

        if season_number == 'Specials':
            season_number = 'S0'
        else:
            season_number = season_number.replace('Season ', 'S')

            if len(season_number) is 2:
                season_number = season_number[0] + '0' + season_number[1]

        for episode in season_episodes.find('tbody').find_all('tr'):
            episode_number = 'E' + episode.find_all('td')[0].text.strip()

            if len(episode_number) is 2:
                episode_number = episode_number[0] + '0' + episode_number[1]

            episode_title = episode.find('span', {'class': 'change_translation_text', 'data-language': 'en'}).text.strip()

            episode_name = show_name + ' ' + season_number + ' ' + episode_number + ' - ' + episode_title

            episodes.append(episode_name)

    for episode in episodes:
        print(episode)

    return episodes

def check_rename(root, file, filename, similar):

    print('Original:', file)

    if similar is True:
        print('Possible:', filename)
        print('Are these the same?')
    else:
        print('Fixed:   ', filename)

    option = input()

    if option.lower() in ['y', 'yes']:
        os.rename(os.path.join(root, file), os.path.join(root, filename))
        print(filename)
        print()
        return True
    return False

def get_extension(file):
    if file[-4:] in ['.avi', '.mp4']:
        return file[-4:]
    else:
        return file

def main():
    parser = process_arguments()
    name = parser['name']
    directory = parser['directory']
    clean = parser['c']
    unsorted = parser['u']
    #episodes = find_episodes('Firefly')

    if unsorted is True:
        episodes = find_episodes(name)

        for root, directories, files in os.walk(directory):
            for file in files:
                # if file[-4:] not in ['.avi', '.mp4']:
                #     print('Original:', file)
                #     print('Fixed:   ', file + '.avi')
                #     os.rename(os.path.join(root, file), os.path.join(root, file + '.avi'))

                extension = get_extension(file)
                file_clean = file.replace(extension, '')

                for episode in episodes:
                    episode_clean = episode.split(' - ')[1]

                    if file_clean.lower() in episode.lower():
                        if file_clean.lower() != episode.lower():
                            if check_rename(root, file, episode + extension, False):
                                break
                    elif SequenceMatcher(a=file_clean, b=episode_clean).ratio() >= 0.8:
                        if check_rename(root, file, episode + extension, True):
                            break

    else:
        for root, directories, files in os.walk(directory):
            for file in files:
                if clean is True:
                    if re.search(r'(\d)(\d)( )([-])( )', file):
                        filename = file[5:]
                        check_rename(root, file, filename, False)
                if file[:3].isdigit():
                    filename = name + ' S' + file[0] + ' E' + file[1:]
                    check_rename(root, file, filename, False)

if __name__=='__main__':
    main()
