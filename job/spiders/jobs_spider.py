import scrapy
import pandas as pd
import os
import requests
import json

import os
import dotenv

dotenv.load_dotenv()

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [os.getenv("START_URLS")]
    output_file = 'output.csv'
    telegram_api_key = os.environ["TELEGRAM_API"]
    telegram_chat_id = os.environ["CHAT_ID"]
    
    print(telegram_chat_id)
    print(telegram_api_key)
    
    

    def __init__(self):
        super().__init__()
        self.existing_titles = set()

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        try:
            existing_data = pd.read_csv(self.output_file)
            self.existing_titles.update(existing_data['title'])
        except FileNotFoundError:
            pass

        posts = response.css('.post-entry')
        for post in posts:
            title = post.css('.heading a::text').get()
            article_url = response.urljoin(post.css('.heading a::attr(href)').get())
            if title not in self.existing_titles:
                yield scrapy.Request(url=article_url, callback=self.parse_article, meta={'title': title})

    def parse_article(self, response):
        title = response.meta['title']
        apply_link = response.css('#applylink::attr(href)').get()
        self.send_telegram_message(title, apply_link)
        yield {
            'title': title,
            'url': apply_link
        }

    def send_telegram_message(self, title, url):
        message = f"{title}\n\nApply Now: {url}\n\nJoin us on:\n\nTelegram : [Telegram](https://t.me/hirewavejobs)\n\nWhatsapp:[WhatsApp](https://whatsapp.com/channel/0029Va9NJdO6buMJkJrTkS3p)\n\nLinkedIn:[LinkedIn](https://www.linkedin.com/company/hirewave-fresherjobs-internships/)"
        
        link_preview_options = {
            'is_disabled': True,
            'url': url,
            'prefer_small_media': False,
            'prefer_large_media': False,
            'show_above_text': False
        }
        
        params = {
            'chat_id': self.telegram_chat_id,
            'text': message,
            'parse_mode': 'Markdown',
            'link_preview_options': json.dumps(link_preview_options)
        }
        response = requests.post(f'https://api.telegram.org/bot{self.telegram_api_key}/sendMessage', json=params)
        return response.json()


    def closed(self, reason):
        pass
