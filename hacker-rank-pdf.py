"""
HackerRank PDF Downloader.

Usage: hacker-rank-pdf.py <category> > category.sh
"""

import os
import sys
import time

import requests

ROOT = "https://www.hackerrank.com/rest/contests/master"
CHALLENGES = ROOT + "/tracks/algorithms/challenges"
PDF_URL = ROOT + "/challenges/{slug}/download_pdf?language=English"

OUT_FMT = "wget -O \"{file_name}\" {url}"

category = sys.argv[1]
params = {"offset": 0, "limit": 10, "filters[subdomains][]": category}

dirname = " ".join(category.split("-")).title()
if not os.path.isdir(dirname):
    os.mkdir(dirname)

fname = dirname + "/" + category + ".sh"
output = open(fname, "w")

# Wouldn't have to use this hack, if do-while loops exist
questions = 1
while questions:

    questions = requests.get(CHALLENGES, params=params).json()["models"]

    for Q in questions:

        file_name = Q["difficulty_name"] + " | " + Q["name"].strip() + ".pdf"
        url = PDF_URL.format(slug=Q['slug'])

        output.write(OUT_FMT.format(file_name=file_name, url=url))
        output.write("\n")

    # Wait for some time between calls
    time.sleep(1)

    params['offset'] += params['limit']
