# BorrowBox-Scraper
Python script to hands-free download all audiobooks on loan from library BorrowBox account.

This script automates the process of downloading books from BorrowBox.
It uses Selenium WebDriver to log into BorrowBox, navigate to the "My Loans" page, and download all books.

## Requirements

- Python 3
- Selenium
- ChromeDriver
- WebDriver Manager for Python

## Usage

1. Install the required Python packages:

```
pip install selenium webdriver_manager
```

2. Replace `<Library Card Number>` and `<Pass Code>` in the `login` function with your actual BorrowBox library card number and pass code.

3. Run the script:

    ```
    python scrape_borrowbox_books.py
    ```


The script will log into BorrowBox, navigate to the "My Loans" page, and download all books.
The books will be downloaded to the default download directory of your Chrome browser.

## Testing

The script includes a unit test for the `login` function. To run the test, use the following command:

    ```
    python -m unittest test_scrape_borrowbox_books.py
    ```
