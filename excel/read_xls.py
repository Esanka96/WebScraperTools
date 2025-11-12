import xlrd
import pandas as pd

def extract_excel_data(download_path):
    try:
        book = xlrd.open_workbook(download_path, ignore_workbook_corruption=True)
        sheet = book.sheet_by_index(0)
        data = [sheet.row_values(i) for i in range(sheet.nrows)]
        headers = ['Reference number' if str(col).strip() == '' else str(col).strip().replace('\n', ' ') for col in data[7]]
        df = pd.DataFrame(data[8:], columns=headers)
        df.dropna(axis=0, how='all', inplace=True)
        return df

    except Exception as e:
        errors.append(f"Failed to read Excel file: {e}")
        print(f"❌ Failed to read Excel file: {e}")
        return pd.DataFrame()

xls_path = ""