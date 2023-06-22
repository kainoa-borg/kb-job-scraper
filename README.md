# KB Job Scraper

KB Job Scraper is a python library that provides methods to scrape Indeed for jobs and job descriptions without the bloat of Indeed's interface.

## Installation

KB Job Scraper is still under development, but once it is further developed it will be possible to access with API endpoints for job searching.

## Usage

```python
# prompts for and returns user inputted job and location
get_input()

# returns a list of jobs in HTML form
main()

# returns a Job object with job title, company name, description, and a link to the company
parse_job_soup(job_soup)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)