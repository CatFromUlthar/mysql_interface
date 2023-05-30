from db import DataBaseInteractor

from typing import Dict


class SiteElement:
    def __init_subclass__(cls):
        cls.object_dict: Dict[str, SiteElement] = {}

    @classmethod
    def create_class_objects(cls, db_name: str, table_name: str) -> None:
        mydb = DataBaseInteractor(db_name)
        objects = mydb.get_data(table_name, '*')

        order_num = 0
        for o in objects:
            cls.object_dict[f'{cls.__name__.lower()}_{order_num}'] = cls(o)
            order_num += 1


class User(SiteElement):

    def __init__(self, param_tuple: tuple):
        self.user_id = param_tuple[0]
        self.name = param_tuple[1]
        self.age = param_tuple[2]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_id}, "{self.name}", {self.age})'


class Menu(SiteElement):

    def __init__(self, param_tuple: tuple):
        self.title = param_tuple[0]
        self.link = param_tuple[1]

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.title}", "{self.link}")'


if __name__ == '__main__':
    User.create_class_objects('general.db', 'users')
    Menu.create_class_objects('general.db', 'menu')
    print(Menu.object_dict)
