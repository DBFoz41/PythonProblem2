"""
File reading class
"""

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        
    def file_read_all_str_list(self):
        f = open(self.file_name, "r")
        self.str_list = f.readlines()
        f.close()
        return self.str_list