Zillow Web Scraper
This Python script enables scraping real estate data from Zillow by utilizing the Zillow search URL. The script extracts information such as property details, location, and other relevant data in a structured format and saves it to an Excel file.

Features:
Zillow Data Extraction: Extracts real estate data from Zillow using a provided search URL.
Parameter Handling: Parses the Zillow search URL to extract parameters for the API request.
Pagination Support: Handles multiple pages of search results to ensure comprehensive data retrieval.
Proxy Integration: Utilizes the Scraper API for proxy support, enhancing the scraping process.
Usage:
Provide a Zillow search URL when prompted.
Specify the output file name (e.g., data.xlsx) for storing the extracted data.
Dependencies:
flatten_json: Library for flattening nested JSON structures.
pandas: Data manipulation and analysis library.
requests: HTTP library for making API requests.
Configuration:
Set your Scraper API key in the SCRAPER_API_KEY variable.
Note:
This script supports the extraction of real estate data for residential properties.
Make sure to adhere to Zillow's terms of service and usage policies.
Feel free to contribute, report issues, or suggest improvements!

