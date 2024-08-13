#!/usr/bin/env python3
"""Module that shows log parsing using a mongodb and python"""


from pymongo import MongoClient


if __name__ == "__main__":
    """Return the log stats of the nginx db"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    len_coll = nginx_collection.count_documents({})
    print("{} logs".format(len_coll))
    print('Methods:')
    print("\tmethod GET: ".format(nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'GET']}})
        ))
    print("\tmethod POST: ".format(nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'POST']}})
        ))
    print("\tmethod PUT: ".format(nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'PUT']}})
        ))
    print("\tmethod Patch: ".format(nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'PATCH']}})
        ))
    print("\tmethod delete: {}".format(nginx_collection.count_documents(
        {'$expr': {'$eq': ['$method', 'DELETE']}})
        ))
    print("{} status check".format(
        len(list(nginx_collection.find({'method': 'GET', 'path': '/status'}))))
        )
