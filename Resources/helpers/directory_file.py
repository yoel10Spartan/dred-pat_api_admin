import os
import os.path
from Resources.helpers.generate_id import GenerateID, IDStrInt

class DirectoryFile:
    def __init__(self) -> None:
        self.__path: str = '' 
        self.directories: list = []
        self.records: list = []
        self.__search_initializer = None

    @property
    def _path(self):
        return self.__path
        
    @_path.setter
    def _path(self, path):
        self.path = path
        self.__search_initializer = os.scandir(path)

    def access(self):
        return os.access(self.path, mode=os.F_OK)

    def start_search(self):
        if self.access():
            for entry in self.__search_initializer:
                id_entry = GenerateID( IDStrInt().length(10).build_with_letters_numbers() ).get()
                if entry.is_dir():
                    self.directories.append({'id': id_entry, 'directory': entry.name})
                if entry.is_file():
                    self.records.append({'id': id_entry, 'file': entry.name})