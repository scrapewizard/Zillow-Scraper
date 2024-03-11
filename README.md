# Zillow Web Scraper

This Python script enables scraping real estate data from Zillow by utilizing the Zillow search URL. The script extracts information such as property details, location, and other relevant data in a structured format and saves it to an Excel file.

## Features

- **Zillow Data Extraction:** Extracts real estate data from Zillow using a provided search URL.
- **Parameter Handling:** Parses the Zillow search URL to extract parameters for the API request.
- **Pagination Support:** Handles multiple pages of search results to ensure comprehensive data retrieval.
- **Proxy Integration:** Utilizes the Scraper API for proxy support, enhancing the scraping process.

## Usage

1. **Provide a Zillow search URL when prompted.** Ensure to apply necessary filters to refine your number of results, considering Zillow's cap limit of 800 results.
2. Specify the output file name (e.g., `data.xlsx`) for storing the extracted data.

## Dependencies

- [flatten_json](https://pypi.org/project/flatten-json/): Library for flattening nested JSON structures.
- [pandas](https://pandas.pydata.org/): Data manipulation and analysis library.
- [requests](https://docs.python-requests.org/): HTTP library for making API requests.

## Configuration

- Set your [Scraper API](https://www.scraperapi.com/?fp_ref=python_automation) key in the `SCRAPER_API_KEY` variable.

## Note

- This script supports the extraction of real estate data for residential properties.
- Make sure to adhere to Zillow's terms of service and usage policies.

Feel free to contribute, report issues, or suggest improvements!

If you are looking for any scraper/automation [Contact me on Fiverr](https://go.fiverr.com/visit/?bta=707597&brand=fiverrcpa&landingPage=https%3A%2F%2Fwww.fiverr.com%2Fmajdmsahel%2Fdo-python-web-scraping-and-automation)

