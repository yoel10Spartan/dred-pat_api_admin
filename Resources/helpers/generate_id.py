import random
import string
from typing import List
from pydantic import validate_arguments
from pydantic import BaseModel

# ===================================================================================

# GenerateID( IDInt().length(10).build_with_numbers() ).get()
# GenerateID( IDStrInt().length(10).build_with_letters_numbers() ).get()

class Material(BaseModel):
    items_str: List[str] = [*list(string.ascii_lowercase), *[str(i) for i in range(9)]*3]

class BaseID:
    def __init__(self) -> None:
        self.id = None
        self.range_id: int = 0
    
    def length(self, max_length: int):
        self.range_id = max_length
        return self

    @property
    def _get(self):
        return self.id

class IDInt(BaseID):
    def build_with_numbers(self):
        self.id = IdConstructor.form_id_int( self.range_id )
        return self

class IDStrInt(BaseID):
    def build_with_letters_numbers(self):
        self.id = IdConstructor.form_id_string( self.range_id )
        return self

class IdConstructor:
    @staticmethod
    @validate_arguments
    def form_id_string( range_values: int ) -> str:
        return ''.join([ 
            random.choice( Material().items_str ) for _ in range( range_values ) 
        ])

    @staticmethod
    @validate_arguments
    def form_id_int( range_values: int ) -> int:
        return int(''.join([ 
            str(random.randrange(0,9)) for _ in range( range_values ) 
        ]))

class GenerateID:
    def __init__(self, construction_element: BaseID) -> None:
        self.__construction_element: BaseID = construction_element
        
    def get(self):
        return self.__construction_element._get

# ===================================================================================