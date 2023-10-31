import os


def get_pah(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_FILE = get_pah('books.csv')
JSON_FILE = get_pah('users.json')
JSON_FILE_W = get_pah('result.json')


