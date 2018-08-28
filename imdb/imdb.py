import bs4 as bs
import requests, re
import pandas as pd
import time, datetime
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import argparse, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default='tt0068646',
                        help='Enter Movie ID?')
    args = parser.parse_args()
    sys.stdout.write(str(get_single_movie(args)))

def get_single_movie(args):
    
    start_time  = datetime.datetime.now()

    #return 'Function Started at : {} '.format(start_time)

    url = 'https://www.imdb.com/title/{}/'.format(args.id)
    response = requests.get(url)

    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(request, response.status_code))

    soup = bs.BeautifulSoup(response.text, 'html.parser')

    # Movie container

    movie_data = soup.find_all('div', id = 'content-2-wide')

    for detail in movie_data:

        # For get title,rating,votes,metascore,director
        top_data = detail.find('div', id = 'main_top')
        rating_info = top_data.find('div', class_ = 'ratings_wrapper')
        
        title = top_data.find('div', class_ = 'title_wrapper').h1.text
        rating = rating_info.find('strong').span.text
        votes = rating_info.find('span', class_ = 'small').text
        metascore = top_data.find('div', class_= 'metacriticScore').span.text
        director = top_data.find('div', class_ = 'plot_summary').a.text

        # For Extract Certificate and genere
        story_line = detail.find('div', id = 'titleStoryLine')

        certificate = story_line.find_all('div', class_ = 'txt-block')[1].find('span').text
        genere = story_line.find_all('div', class_ = 'see-more')[1].find('a').text

        # For Extract Country , language, Release Date

        title_detail = detail.find('div', id = 'titleDetails')
        
        countries = title_detail.find_all('div', class_ = 'txt-block')[1].find_all('a')
        country = []
        for count in countries:
            country.append(count.text)

        language = title_detail.find_all('div', class_ = 'txt-block')[2].find('a').text
        release_date = title_detail.find_all('div', class_ = 'txt-block')[3].text

        budget = title_detail.find_all('div', class_ = 'txt-block')[6].text
        OpeningWeekendUSA = title_detail.find_all('div', class_ = 'txt-block')[7].text
        GrossUSA = title_detail.find_all('div', class_ = 'txt-block')[8].text
        CumulativeWorldwideGross = title_detail.find_all('div', class_ = 'txt-block')[9].text

        end_time  = datetime.datetime.now()

        return '''Movie name : {} \n
                Rating : {} \n
                Votes : {} \n
                Metascore : {} \n
                Certificate : {} \n
                Genere : {} \n
                Country : {} \n
                Language : {} \n
                ReleaseDate : {} \n
                Budget : {} \n
                OpeningWeekendUSA : {} \n
                GrossUSA : {} \n
                CumulativeWorldwideGross : {} \n'''.format(title,rating,votes,metascore,certificate,genere,country,language,release_date,budget,OpeningWeekendUSA,GrossUSA,CumulativeWorldwideGross)

        #return 'Function Finished at : {} '.format(end_time)

        #return 'Time Difference {} '.format(end_time - start_time)

if __name__ == '__main__':
    main()                 
 
        
