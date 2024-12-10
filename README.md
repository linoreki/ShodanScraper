No problem! Here's a customized `README.md` for your `shodanscraper` script:

# ShodanScraper

A Python-based web scraper that interacts with the Shodan search engine to collect publicly available IP addresses and ports based on a given query. The scraper allows you to repeat the same query multiple times and navigate through multiple pages of results.

## Table of Contents
1. [About](#about)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Arguments](#arguments)
5. [Contributing](#contributing)
6. [License](#license)

## About

`ShodanScraper` is a Python script that scrapes data from the Shodan search engine. It allows users to perform queries, iterate through search result pages, and save the resulting IP addresses and ports into a text file. The number of search repetitions and the number of pages to scrape are customizable through command-line arguments.

## Installation

### Prerequisites
- Python 3.x
- `requests`
- `beautifulsoup4`

### Steps to install:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shodanscraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd shodanscraper
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Example:
To run the web scraper, use the following command:
```bash
python shodanscraper.py -t 3
```
This will perform the search query `http.favicon.hash:"1624375939"` three times and scrape results from each page.

## Arguments

- `-t, --times`: **Required**. The number of times to repeat the search query (integer). Example: `-t 3` will repeat the query 3 times.

### Output:
The script saves the results in a file called `ips_puertos.txt`. Each entry in the file contains an IP address and port number in the format:

```
IP_ADDRESS PORT
```

## Contributing

If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation of Customization:
- **Title & Description**: I've updated the project name to `ShodanScraper` and provided a brief description of what the script does.
- **Usage**: Explained how to run the script with an example command (`python shodanscraper.py -t 3`).
- **Arguments**: Included an explanation for the `-t` argument that controls the number of times the query is repeated.

You can paste this content into a `README.md` file for your `shodanscraper` repository. Let me know if you'd like any more tweaks!
