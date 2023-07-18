#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock, patch, mock_open
from scrape_borrowbox_books import login, save_cookies, load_cookies, navigate_to_my_loans, download_books
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    @patch('selenium.webdriver.Chrome')
    def test_login(self, MockChrome):
        # Arrange
        mock_driver = MockChrome.return_value
        mock_element = MagicMock()
        mock_driver.find_element.return_value = mock_element

        # Act
        login(mock_driver, 'username', 'password')

        # Assert
        mock_driver.get.assert_called_once_with('https://hampshire.borrowbox.com/login')
        mock_driver.find_element.assert_any_call(By.ID, 'form-input-1')
        mock_driver.find_element.assert_any_call(By.ID, 'form-input-2')
        mock_element.send_keys.assert_any_call('username')
        mock_element.send_keys.assert_any_call('password')


class TestSaveCookies(unittest.TestCase):
    @patch('selenium.webdriver.Chrome')
    @patch('pickle.dump')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_cookies(self, mock_open, mock_dump, MockChrome):
        # Arrange
        mock_driver = MockChrome.return_value
        mock_driver.get_cookies.return_value = [{'name': 'cookie1', 'value': 'value1'}]

        # Act
        save_cookies(mock_driver)

        # Assert
        mock_driver.get_cookies.assert_called_once()
        mock_open.assert_called_once_with('cookies.pkl', 'wb')
        mock_dump.assert_called_once_with([{'name': 'cookie1', 'value': 'value1'}], mock_open.return_value)

class TestLoadCookies(unittest.TestCase):
    @patch('selenium.webdriver.Chrome')
    @patch('pickle.load')
    @patch('builtins.open', new_callable=mock_open)
    def test_load_cookies(self, mock_open, mock_load, MockChrome):
        # Arrange
        mock_driver = MockChrome.return_value
        mock_load.return_value = [{'name': 'cookie1', 'value': 'value1'}]

        # Act
        load_cookies(mock_driver)

        # Assert
        mock_open.assert_called_once_with('cookies.pkl', 'rb')
        mock_load.assert_called_once_with(mock_open.return_value)
        mock_driver.add_cookie.assert_called_once_with({'name': 'cookie1', 'value': 'value1'})

class TestNavigateToMyLoans(unittest.TestCase):
    @patch('selenium.webdriver.Chrome')
    def test_navigate_to_my_loans(self, MockChrome):
        # Arrange
        mock_driver = MockChrome.return_value

        # Act
        navigate_to_my_loans(mock_driver)

        # Assert
        mock_driver.get.assert_called_once_with('https://hampshire.borrowbox.com/home/my-loans')

class TestDownloadBooks(unittest.TestCase):
    @patch('selenium.webdriver.Chrome')
    def test_download_books(self, MockChrome):
        # Arrange
        mock_driver = MockChrome.return_value
        mock_element = MagicMock()
        mock_driver.find_elements.return_value = [mock_element]

        # Act
        download_books(mock_driver)

        # Assert
        mock_driver.get.assert_called_with('https://hampshire.borrowbox.com/home/my-loans')
        mock_driver.find_elements.assert_called_with(By.CLASS_NAME, 'button-download')
        mock_element.click.assert_called()

if __name__ == '__main__':
    unittest.main()
