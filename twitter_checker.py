#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# Check if twitter usernames exist or are available
import argparse as ap
import requests
import time

def args():
    """ Get the arguments passed from the CLINE """
    parser = ap.ArgumentParser()
    parser.add_argument("u", help="The text file with all your usernames in")
    return parser.parse_args()

def checker():
    """Loop through lines and check for available usernames"""
    argslist = args()

    #our usernames are per line
    usernames = open(argslist.u, "r")
    lines = usernames.readlines()
    usernames.close()
    checked = open("saved.txt", "a+")
    for line in lines:
        url = "https://twitter.com/" + line.strip()
        check = requests.get(url)

        #a simple 404 will tell us it doesn't exist
        if check.status_code == 404:
            message = '%s is avaialble\n' % line.strip()
        elif check.status_code == 400:
            message = '%s is a bad formatted username. Alphanumeric only\n' % line.strip()
        else:
            message = '%s is taken\n' % line.strip()

        #save the results
        checked.write(message)
checker()
