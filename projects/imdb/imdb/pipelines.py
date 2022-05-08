# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3


class MongodbPipeline:
    collection_name = 'best_movies'

    # @classmethod
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get('MONGO_URI'))

    def open_spider(self, spider):
        # logging.warning('Spider opened from Pipeline')
        self.client = pymongo.MongoClient("mongodb+srv://dajebbar:purpel@cluster0.1l5ej.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client['IMDB']

    def close_spider(self, spider):
        # logging.warning('Spider closed from Pipeline')
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item


class SqLitedbPipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect('imdb.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute(
                '''
                    create table best_movies(
                        title text,
                        year text,
                        genre text,
                        permission text,
                        duration_hr text,
                        duration_min text,
                        noted_imdb text,
                        movie_poster text,
                        play_trailer text,
                        movie_url text
                    )
                '''
            )
        except sqlite3.OperationalError:
            pass

        self.connection.commit()
        

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute(
            '''
                insert into best_movies(title, year, genre, 
                permission, duration_hr, duration_min, 
                noted_imdb, movie_poster, play_trailer, movie_url) values(?,?,?,?,?,?,?,?,?,?)
            ''', (
                item.get('title'), item.get('year'), item.get('genre'),item.get('permission'),
                item.get('duration_hr'),item.get('duration_min'),item.get('noted_imdb'),
                item.get('movie_poster'),item.get('play_trailer'),item.get('movie_url')
            ))
        self.connection.commit()
        return item
