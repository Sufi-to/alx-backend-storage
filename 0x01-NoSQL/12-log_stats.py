#!/usr/bin/env python3
"""Module that shows log parsing using a mongodb and python"""


if __name__ == "__main__":
    """Return the log stats of the nginx db"""
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    len_coll = nginx_collection.count_documents({})
    print("{} logs".format(len_coll))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, method_count))
    print("{} status check".format(
        len(list(nginx_collection.find({'method': 'GET', 'path': '/status'}))))
        )
