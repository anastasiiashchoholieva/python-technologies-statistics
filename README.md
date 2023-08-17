# Python technologies statistics based on jobs listed on Djinni

***

This project aims to gather statistics on the most demanded technologies in the Python development job market using web
scraping and data analysis techniques. It scrapes job vacancy descriptions from Djinni.co for Python Developer positions,
analyzes the technologies mentioned, and presents the data in a CSV file and a bar chart.

## Project structure

***

- config.py: Configuration file containing URL and keywords for search.
- app/parse.py: File with script responsible for web scraping and data parsing.
- result.csv: CSV file which contains data about technologies frequency.
- analysis.py: Main script that runs scraping, data parsing and visualization.
- README.md: Documentation file.

## Usage

***

- Clone the repository: `git clone https://github.com/your-username/python-tech-statistics.git`
- Install the requirements: `pip install -r requirements.txt`
- To run program: Open the `analyse.py` and run the `main` function. This will scrape job descriptions and generate a result CSV file. Then it will read the result CSV file, perform analysis,
and generate a bar chart.


## Requirements

***

- Python 3.x
- Beautiful Soup
- Requests
- Matplotlib

## Output chart example

***

![technologies_chart.png](chart%2Ftechnologies_chart.png)
