#!/usr/bin/env python3
"""Module that shows log parsing using a mongodb and python"""


from pymongo import MongoClient


if __name__ == "__main__":
    """Return the log stats of the nginx db"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    len_coll = nginx_collection.count_documents({})
    print(len_coll, 'logs')
    print('Methods:')
    print('\tmethod GET: ', nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'GET']}})
        )
    print('\tmethod POST: ', nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'POST']}})
        )
    print('\tmethod PUT: ', nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'PUT']}})
          )
    print('\tmethod Patch: ', nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'PATCH']}})
        )
    print('\tmethod delete: ', nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'DELETE']}})
        )
    print(len(list(nginx_collection.
          find({'method': 'GET', 'path': '/status'}))), 'status_check')
