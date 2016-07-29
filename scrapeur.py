#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import librairies
import argparse
import sys
import re
import urllib2
import csv


# parser arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input_path', type=str, help='path to the csv file with urls')
parser.add_argument('-o', dest='out', type=str, help='out file for saving data', default="./default.csv")

args = parser.parse_args()

def getAddress(url):
	# return a valid url, with http or https
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseForEmails(url):
	# add User-Agent
	ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	# open and read URLs + add a header
	j = urllib2.Request(getAddress(url), headers=ua)
	f = urllib2.urlopen(j)
	s = f.read()

	# define email regex
	emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', s, flags=re.IGNORECASE)

	# write emails in csv
	with open(args.out, 'a+') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		for email in emails:
			row[0] = email
			writer.writerow(row)

if __name__ == "__main__":
	# read all urls in csv
		with open(args.input_path, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			reader.next()

			for row in reader:
				url = row[0]
				parseForEmails(url)
