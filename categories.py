from db import DataBaseInteractor


class Users:
    object_dict = {}

    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Users({self.user_id}, "{self.name}", {self.age})'

    @classmethod
    def create_users_objects(cls, db_name: str, table_name: str):
        mydb = DataBaseInteractor(db_name)
        users = mydb.get_data(table_name, '*')

        order_num = 0
        for u in users:
            cls.object_dict[f'user_{order_num}'] = cls(u[0], u[1], u[2])
            order_num += 1


if __name__ == '__main__':
    Users.create_users_objects('general.db', 'users')
    print(Users.object_dict)
