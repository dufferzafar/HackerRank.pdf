""" HackerRank PDF Downloader. """

import time

import requests

CATEGORY = "dynamic-programming"

ROOT = "https://www.hackerrank.com/rest/contests/master"
CHALLENGES = ROOT + "/tracks/algorithms/challenges"
PDF_URL = ROOT + "/challenges/{slug}/download_pdf?language=English"

OUT_FMT = "wget -O '{file_name}' {url}"

params = {"offset": 0, "limit": 10, "filters[subdomains][]": CATEGORY}

# Wouldn't have to use this hack, if do-while loops exist
questions = 1
while questions:

    questions = requests.get(CHALLENGES, params=params).json()["models"]

    for Q in questions:

        file_name = Q["difficulty_name"] + " | " + Q["name"] + ".pdf"
        url = PDF_URL.format(slug=Q['slug'])

        print(OUT_FMT.format(file_name=file_name, url=url))

    # Wait for some time between calls
    time.sleep(1)

    params['offset'] += params['limit']

    break
