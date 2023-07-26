from scrapy import Spider, Request


class BooksToScrapeComSpider(Spider):
    name = "books_toscrape_com"
    
        

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
            'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
            "http://books.toscrape.com/catalogue/category/books/art_25/index.html", 
            "http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html"
        ]
        for url in urls:
            category = url.replace('/', ' ').replace('_', ' ').split()[5]
            yield Request(url=url, callback=self.parse, cb_kwargs=dict(category=category))


    def parse(self, response, category):
        next_page_links = response.css(".next a")
        yield from response.follow_all(next_page_links)
        book_links = response.css("article a")
        yield from response.follow_all(book_links, callback=self.parse_book, cb_kwargs=dict(category=category))

    def parse_book(self, response, category):
            yield {
                "name": response.css("h1::text").get(),
                "price": response.css(".price_color::text").re_first("£(.*)"),
                "category" : category,
                "url": response.url,

            }

        

