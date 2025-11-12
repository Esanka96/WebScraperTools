import unittest
import pandas as pd
import os
from unittest.mock import patch, MagicMock,mock_open,call,Mock
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import random
import json
import os
import glob
from AR1575 import (main,get_soup,log_error,append_values_to_final_list,create_final_json_file,extract_main_page_data,get_pdf_path_with_download,get_pdf_content,
                    errors,data,uniqueIdentity,region,jurisdiction,category,title,casKeyValue)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

class Test_AR1575(unittest.TestCase):

    @staticmethod
    def find_json_path():

        folder_path = "out"
        json_files = glob.glob(os.path.join(folder_path, "**", "*.json"), recursive=True)
        if json_files:
            latest_file = max(json_files, key=os.path.getmtime)
            return latest_file
        else:
            print("No JSON files found in the folder or its subfolders.")
            return None

    @classmethod
    def setUpClass(cls):

        main()

        cls.test_json_path = "test.json"
        cls.current_json_path = cls.find_json_path()

        with open(cls.test_json_path, "r", encoding="utf-8") as test_f:
            cls.test_json_data = json.load(test_f)

        with open(cls.current_json_path, "r", encoding="utf-8") as actual_f:
            cls.current_json_data = json.load(actual_f)

    def test_01_json_required_keys(self):
        required_keys = {"UniqueIdentity", "region", "Jurisdiction", "category", "title", "casKey", "dateAndTime", "errors", "data"}
        self.assertTrue(required_keys.issubset(self.current_json_data.keys()))

    def test_02_json_key_data_types(self):
        self.assertIsInstance(self.current_json_data["UniqueIdentity"], str)
        self.assertIsInstance(self.current_json_data["region"], str)
        self.assertIsInstance(self.current_json_data["Jurisdiction"], str)
        self.assertIsInstance(self.current_json_data["category"], str)
        self.assertIsInstance(self.current_json_data["title"], str)
        self.assertIsInstance(self.current_json_data["casKey"], (str, type(None)))
        self.assertIsInstance(self.current_json_data["errors"], list)
        self.assertIsInstance(self.current_json_data["data"], list)

    def test_03_json_column_and_row_consistency(self):
        first_row_keys = set(self.current_json_data["data"][0].keys())
        for row in self.current_json_data["data"]:
            self.assertEqual(set(row.keys()), first_row_keys)

    def test_04_json_colunm_name_and_count(self):
       actual_colunm_count = len(self.current_json_data["data"][0].keys())
       test_colunm_count = len(self.test_json_data["data"][0].keys())
       self.assertEqual(test_colunm_count, actual_colunm_count)
       self.assertEqual(self.test_json_data["data"][0].keys(), self.current_json_data["data"][0].keys())

    def test_05_json_meta_content(self):
        self.assertEqual(self.current_json_data["title"], self.test_json_data["title"])
        self.assertEqual(self.current_json_data["UniqueIdentity"], self.test_json_data["UniqueIdentity"])
        self.assertEqual(self.current_json_data["region"], self.test_json_data["region"])
        self.assertEqual(self.current_json_data["Jurisdiction"], self.test_json_data["Jurisdiction"])
        self.assertEqual(self.current_json_data["category"], self.test_json_data["category"])
        self.assertEqual(self.current_json_data["casKey"], self.test_json_data["casKey"])
        datetime.strptime(self.current_json_data["dateAndTime"], "%Y-%m-%d %H:%M:%S")

    def test_06_json_data_content(self):
        current_all_sha_hashes = [item["sha_hash"] for item in self.current_json_data["data"]]
        sample_size = min(10, len(current_all_sha_hashes))
        sampled_sha_hashes = random.sample(current_all_sha_hashes, sample_size)
        test_sha_hashes = {item["sha_hash"] for item in self.test_json_data["data"]}

        for current_sha_hash in sampled_sha_hashes:
            self.assertIn(current_sha_hash, test_sha_hashes, f"SHA hash {current_sha_hash} not found in test JSON data")

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_07_get_soup_success(self, mock_get, mock_sleep):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body><h1>Test</h1></body></html>"
        mock_get.return_value = mock_response

        soup = get_soup("http://example.com")
        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.h1.text, "Test")
        mock_get.assert_called_once()
        mock_sleep.assert_not_called()

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_08_get_soup_after_retries(self, mock_get, mock_sleep):
        mock_response_fail = MagicMock(status_code=500)
        mock_response_success = MagicMock(status_code=200, content=b"<html><body>OK</body></html>")
        mock_get.side_effect = [mock_response_fail, mock_response_fail, mock_response_success]

        soup = get_soup("http://example.com", retries=3, delay=0)
        self.assertEqual(soup.body.text, "OK")
        self.assertEqual(mock_get.call_count, 3)

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_09_get_soup_exception_and_retries(self, mock_get, mock_sleep):
        mock_get.side_effect = [
            requests.exceptions.ConnectionError("Fail 1"),
            requests.exceptions.Timeout("Fail 2"),
            MagicMock(status_code=200, content=b"<html><body>OK</body></html>")
        ]

        soup = get_soup("http://example.com", retries=3, delay=0)
        self.assertEqual(soup.body.text, "OK")
        self.assertEqual(mock_get.call_count, 3)

    def test_10_log_error(self):
        errors.clear()
        test_message = "This is a test error"

        log_error(test_message)

        self.assertIn(test_message, errors)
        self.assertEqual(len(errors), 1)

    @patch('common.clean_newlines_in_dataframe')
    @patch('common.save_output_to_json')
    @patch('common.returnJsonPath')
    def test_11_create_final_json_file(self, mock_return_json_path, mock_save_output_to_json,
                                    mock_clean_newlines_in_dataframe):

        test_data = [{"key1": "value1", "key2": "value2"}, {"key1": "value3", "key2": "value4"}]

        mock_return_json_path.return_value = "mock_path.json"

        mock_cleaned_df = pd.DataFrame(test_data)
        mock_clean_newlines_in_dataframe.return_value = mock_cleaned_df

        create_final_json_file(test_data)

        mock_clean_newlines_in_dataframe.assert_called_once()
        actual_data = mock_clean_newlines_in_dataframe.call_args[0][0].to_dict(orient='records')

        self.assertEqual(test_data, actual_data)

        mock_return_json_path.assert_called_once_with(uniqueIdentity)

        expected_json_path = "mock_path.json"
        expected_data = mock_cleaned_df
        mock_save_output_to_json.assert_called_once_with(
            uniqueIdentity,
            region,
            jurisdiction,
            category,
            title,
            errors,
            expected_data,
            expected_json_path,
            casKeyValue
        )

        actual_saved_data = mock_save_output_to_json.call_args[0][6]
        self.assertTrue(
            actual_saved_data.equals(expected_data)
        )

    def test_12_append_values_to_final_list(self):
        data.clear()

        append_values_to_final_list(
            "001",
            "焊接作業"
        )

        expected = {
            "項次": "001",
            "作業名稱": "焊接作業",
        }

        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], expected)

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_13_get_pdf_content_success_first_try(self, mock_get, mock_sleep):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"%PDF-1.4 test content"
        mock_get.return_value = mock_response

        content = get_pdf_content("http://example.com/sample.pdf", retries=3, delay=0)
        self.assertEqual(content, b"%PDF-1.4 test content")
        mock_get.assert_called_once()
        mock_sleep.assert_not_called()

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_14_get_pdf_content_success_after_retries(self, mock_get, mock_sleep):
        mock_fail = MagicMock(status_code=500)
        mock_success = MagicMock(status_code=200, content=b"%PDF-retry-success")
        mock_get.side_effect = [mock_fail, mock_fail, mock_success]

        content = get_pdf_content("http://example.com/sample.pdf", retries=3, delay=0)
        self.assertEqual(content, b"%PDF-retry-success")
        self.assertEqual(mock_get.call_count, 3)

    @patch('AR1575.time.sleep')
    @patch('AR1575.requests.get')
    def test_15_get_pdf_content_with_exceptions_then_success(self, mock_get, mock_sleep):
        mock_get.side_effect = [
            requests.exceptions.ConnectionError("Failed to connect"),
            requests.exceptions.Timeout("Timeout"),
            MagicMock(status_code=200, content=b"%PDF-exception-recovery")
        ]

        content = get_pdf_content("http://example.com/sample.pdf", retries=3, delay=0)
        self.assertEqual(content, b"%PDF-exception-recovery")
        self.assertEqual(mock_get.call_count, 3)


    @patch("builtins.open", new_callable=mock_open)
    @patch("AR1575.common.returnSourceFilePath")
    @patch("AR1575.get_pdf_content")
    def test_16_get_pdf_path_with_download(self, mock_get_pdf_content, mock_return_path, mock_file_open):
        html = '''
            <html>
            <body>
                <ul>
                    <li class="pdf">
                        <a href="https://example.com/files/sample.pdf">Sample PDF</a>
                    </li>
                </ul>
            </body>
            </html>
        '''
        content = BeautifulSoup(html, "html.parser")

        mock_get_pdf_content.return_value = b"%PDF-mock"
        mock_return_path.return_value = "/tmp/testfile.pdf"

        get_pdf_path_with_download(content)

        mock_get_pdf_content.assert_called_once_with("https://example.com/files/sample.pdf")
        mock_file_open.assert_called_once_with("/tmp/testfile.pdf", "wb")
        mock_file_open().write.assert_called_once_with(b"%PDF-mock")

    @patch("AR1575.pdfplumber.open")
    @patch("AR1575.append_values_to_final_list")
    def test_17_extract_main_page_data_success(self, mock_append, mock_pdfplumber):

        mock_pdf = MagicMock()
        mock_page1 = MagicMock()
        mock_page1.extract_text.return_value = "附表一"
        mock_page1.extract_tables.return_value = [[["項次", "作業名稱"], ["1", "Chemical A"], ["2", "Chemical B"]]]

        mock_page2 = MagicMock()
        mock_page2.extract_text.return_value = "附表"
        mock_page2.extract_tables.return_value = [[["項次", "作業名稱"], ["1", "Chemical A"]]]

        mock_page3 = MagicMock()
        mock_page3.extract_text.return_value = "附表"
        mock_page3.extract_tables.return_value = [[["項次", "作業名稱"], ["1", "Chemical A"]]]

        mock_page4 = MagicMock()
        mock_page4.extract_text.return_value = "附表二"
        mock_page4.extract_tables.return_value = []

        mock_pdf.pages = [mock_page1,mock_page2,mock_page3, mock_page4]
        mock_pdfplumber.return_value.__enter__.return_value = mock_pdf

        extract_main_page_data("dummy.pdf")

        mock_append.assert_has_calls([
            call("1", "Chemical A"),
            call("2", "Chemical B")
        ])
        self.assertEqual(mock_append.call_count, 2)

if __name__ == '__main__':
    unittest.main()