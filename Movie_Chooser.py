from typing import List
import argparse
import random

def process_arguments():
    parser = argparse.ArgumentParser()

    # genres
    parser.add_argument('-action', help='Action movie!', action='store_true')
    parser.add_argument('-adventure', help='Adventure movie!', action='store_true')
    parser.add_argument('-comedy', help='Comedy movie!', action='store_true')
    parser.add_argument('-drama', help='Drama movie!', action='store_true')
    parser.add_argument('-fantasy', help='Fantasy movie!', action='store_true')
    parser.add_argument('-horror', help='Horror movie!', action='store_true')
    parser.add_argument('-mystery', help='Mystery movie!', action='store_true')
    parser.add_argument('-romance', help='Romance movie!', action='store_true')
    parser.add_argument('-scifi', help='Science-Fiction movie!', action='store_true')
    parser.add_argument('-thriller', help='Thriller movie!', action='store_true')

    # other
    parser.add_argument('-all', help='Any movie!', action='store_true')
    parser.add_argument('-r', help='Watch already seen movie instead', action='store_true')

    try:
        return vars(parser.parse_args())
    except IOError:
        parser.error('Error')


class Movie(object):
    name = ''
    genres = []

    def __init__(self, name, genres):
        self.name = name
        self.genres = genres


def initialize_movies():
    movies: List[Movie] = []


    movies.append(Movie('A Funny Thing Happened On The Way To The Forum',
                        ['comedy', 'musical']))
    movies.append(Movie('Bill and Ted\'s Bogus Journey',
                        ['comedy', 'fantasy']))
    movies.append(Movie('Birdman',
                        ['comedy', 'drama']))
    movies.append(Movie('The Bourne Identity',
                        ['action', 'mystery', 'thriller']))
    movies.append(Movie('The Butterfly Effect',
                        ['drama', 'sci-fi', 'thriller']))
    movies.append(Movie('District 9',
                        ['sci-fi', 'thriller']))
    movies.append(Movie('Galaxy Quest',
                        ['comedy']))
    movies.append(Movie('The Hateful Eight',
                        ['drama', 'mystery']))
    movies.append(Movie('Hot Rod',
                        ['comedy']))
    movies.append(Movie('Independence Day',
                        ['action', 'adventure', 'sci-fi']))
    movies.append(Movie('John Wick 2',
                        ['action', 'thriller']))
    movies.append(Movie('The Men Who Stare at Goats',
                        ['comedy']))
    movies.append(Movie('Pacific Rim',
                        ['action', 'adventure', 'sci-fi']))
    movies.append(Movie('Pay It Forward',
                        ['drama']))
    movies.append(Movie('The Prestige',
                        ['drama', 'mystery', 'sci-fi']))
    movies.append(Movie('Primer',
                        ['drama', 'sci-fi', 'thriller']))
    movies.append(Movie('A Quiet Place',
                        ['drama', 'horror', 'mystery']))
    movies.append(Movie('Reservoir Dogs',
                        ['drama', 'thriller']))
    movies.append(Movie('Shutter Island',
                        ['mystery', 'thriller']))
    movies.append(Movie('The Usual Suspects',
                        ['mystery', 'thriller']))
    movies.append(Movie('Unbreakable',
                        ['drama', 'mystery', 'sci-fi']))
    movies.append(Movie('Vertigo',
                        ['mystery', 'romance', 'thriller']))
    movies.append(Movie('Wonder Woman',
                        ['action', 'adventure', 'fantasy']))

    # movies.append(Movie('',
    #                     ['']))


    return movies


def movies_in_genre(genre, movies):
    movies_found: List[Movie] = []

    for movie in movies:
        if genre in movie.genres:
            movies_found.append(movie)

    return movies_found


def main():
    parser = process_arguments()
    movies = initialize_movies()

    movies_selected = []
    genres = ''

    if True in parser.values():
        for argument in parser:
            if parser.get(argument) is True:
                genres = genres + argument + ', '
                for movie in movies_in_genre(argument, movies):
                    if movie not in movies_selected:
                        movies_selected.append(movie.name)



        print('Genre/s entered:', genres[:-2], '\n')

        if len(movies_selected) is 0:
            print('Since no movies were found matching the genre/s, we will instead pick a random movie out of all of the options')


    if len(movies_selected) is 0:
        for movie in movies:
            movies_selected.append(movie.name)

    movies_selected.sort()
    print('All movie options\n-----------------')
    for movie in movies_selected:
        print(movie)

    print('\nChosen movie\n------------')
    print(random.choice(movies_selected))


if __name__ == '__main__':
    main()