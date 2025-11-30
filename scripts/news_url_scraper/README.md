# This is a news paper url scraper for Hong Kong Fire Documentary

A simple web scraper for scraping urls from sites

## Features

- Scrape articles with keyword 大埔 or 宏福苑
- Output as markdown files

## Prerequisites

- **python 3.13**
- **uv**

## Run this

```bash
uv sync
uv run main.py
```

### uv will automatically create a virtual environment and download packages for you

## Contribute

You can add scrapers for different news site under `./scrapers/` with return format link the mingpao scraper. The script will handle markdown format and saving.
