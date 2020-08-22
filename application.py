import argparse
from os import chdir
from subprocess import run as run_shell
from sys import exit

# create parser
parser = argparse.ArgumentParser(description='Award winning films service')

# Add the arguments
parser.add_argument('Service',
    metavar='service', 
    type=str, 
    help='"parse" to run the crawler; "serve" to serve the API')

# Execute the parse_args() method
args = parser.parse_args()

if (args.Service == 'parse'):
    chdir('FilmCrawler')
    run_shell(['scrapy', 'crawl', 'awardWinningFilmCrawler'])
elif (args.Service == 'serve'):
    run_shell(['python', 'manage.py', 'runserver', '8080'])
else:
    print('The argument hasn\'t specified.\nType "parse" to run the crawler or "serve" to serve API')
    exit()

