
# HackerRank.pdf

HackerRank problems in PDF by categories.

Since HackerRank is nice enough to provide all problem statements in PDF, this script only downloads all the PDFs and merges them into a single bundle.

Files can be [downloaded from the releases page]().

## Running the script

The script is written in a very Unix-y way - it only does the minimal task of listing PDF URLs of a category.

Downloading of the PDFs is left to `wget`, while their merging (into a single file) is done by [`pdf-merge`](https://github.com/dufferzafar/.scripts/blob/master/pdf-merge)

As an example:

```bash
python3 hacker-rank-pdf.py dynamic-programming

cd "Dynamic Programming"

bash *.sh

sed 's/.*"\(.*\)".*/\1/' *.sh | pdf-merge -o "Dynamic Programming.pdf" -C "|" -f -
```

<!-- 
Difficulties:

Easy
Medium
Hard
Advanced
Expert
-->
