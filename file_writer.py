"""
File writing class
"""


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name
        
    def _file_write_all_str(self, string_to_write):
        f = open(self.file_name, "w+")
        f.write(string_to_write)
        f.close()