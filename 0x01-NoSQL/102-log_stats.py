#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_logs = nginx_collection.count_documents({})
    print(f'{num_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        counter = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {counter}')
    code_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{code_status} status check')
