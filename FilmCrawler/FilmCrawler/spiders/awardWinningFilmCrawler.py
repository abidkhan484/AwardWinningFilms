import scrapy
from FilmCrawler.items import FilmcrawlerItem
from re import search

class awardWinningFilmSpider(scrapy.Spider):
    name = "awardWinningFilmCrawler"

    base_url = 'https://en.wikipedia.org'

    def start_requests(self):
        start_url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
        
        # crawler start request here
        yield scrapy.Request(url=start_url, callback=self.parse)


    def parse(self, response):
        # data extracting from the initial page
        rows = response.css('.wikitable tr').getall()

        total_rows = len(rows)
        for i in range(1, total_rows):
            html_string = rows[i]
            selector = scrapy.Selector(text=html_string, type="html")

            # introducing the FilmcrawlerItem
            movie_details = FilmcrawlerItem()
            movie_link = selector.css('td:nth-child(1) a::attr(href)').get()
            movie_url = self.base_url + movie_link if movie_link else ''
            movie_details = {
                'movie_name' : selector.css('td:nth-child(1) a::text').get(),
                'release_year' : selector.css('td:nth-child(2) a::text').get(),
                'award' : selector.css('td:nth-child(3)::text').get(),
                'nomination' : selector.css('td:nth-child(4)::text').get().strip('\n'),
                'movie_url' : movie_url
            }

            if movie_url:
                # the below request is sent to the movie details page
                request = scrapy.Request(movie_url, callback=self.parse_film_details_page)
                # movie_details data is passed to the details page
                request.meta['movie_details'] = movie_details
                yield request
            else:
                yield movie_details


    def parse_film_details_page(self, response):
        # data extracting from the details page
        movie_details = response.meta['movie_details']
        rows = response.css('.infobox tr')
        total_rows = len(rows)

        # as movie name is already collected; so we skip the first row
        starting_idx = 1
        # Poster image of the film takes the 2nd row (hypothesis)
        # that's why the below checking, to escape the image
        if total_rows > starting_idx and rows[starting_idx].css('td::attr(colspan)').get() is '2':
            starting_idx += 1

        for i in range(starting_idx, total_rows):
            row = rows[i]
            # title variable is the left column and
            title = row.css('th *::text').get()
            if not title:
                continue
            # answers valiable is the right column of the infotable
            answers = row.css('td *::text').getall()

            # the above getall function returns all tags inner next including newline
            # so, the below filter is required
            # re.search('^\[\d]$', valid_str) is to remove reference links (e.g [1])
            answers = [valid_str for valid_str in answers if valid_str is not '\n' and search('^\[\d]$', valid_str) is None]

            movie_details[title] = answers

        return movie_details

