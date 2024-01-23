#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    nginx_logs = client.logs.nginx
    print("{} logs".format(nginx_logs.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            nginx_logs.count_documents({"method": method})
        ))
    print("{} status check".format(
        nginx_logs.count_documents({"method": "GET", "path": "/status"})
    ))
