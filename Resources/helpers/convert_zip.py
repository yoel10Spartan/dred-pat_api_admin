import shutil
import os
import pathlib
from aiofiles.os import wrap

class CheckFile:
    def __init__(self, name_file, directory_to_search) -> None:
        self.name_file = name_file
        self.directory_to_search = directory_to_search
    
    def file_exists(self):
        files = os.scandir(self.directory_to_search)
        for entry in files:
            if entry.name == self.name_file: 
                return True
        return False

    @staticmethod
    def directory_exists(path: str):
        return [pathlib.Path(path), os.access(path, os.F_OK)]

class ConvertZIP:
    def __init__(self, 
        compressed_files_directory: str,
        directory_to_compress: str
    ) -> None:
        self.compressed_files_directory: str = compressed_files_directory
        self.directory_to_compress: str = directory_to_compress
        self.compressed_file_path: str = ''
        self.access: bool = False
        self.path: str = ''
        self.existing_file: bool = False

    def __start_verification(self):
        [self.path, self.access] = CheckFile.directory_exists(self.directory_to_compress)
        self.existing_file = CheckFile(
            '{}.zip'.format(self.path.name), 
            self.compressed_files_directory
        ).file_exists()

    async def __conversion(self):
        self.__start_verification()
        make_archive = wrap(shutil.make_archive)
        base_name = '{}{}'.format(str(self.compressed_files_directory), str(self.path.name))
        if self.access and (not self.existing_file):
            await make_archive(
                base_name=base_name, 
                format='zip', 
                root_dir=self.directory_to_compress
            )
        self.compressed_file_path = '{}.zip'.format(base_name)

    async def start_conversion(self):
        await self.__conversion()