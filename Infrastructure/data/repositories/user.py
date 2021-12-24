from Domain.users.Model.user_entities import UserModel
from Infrastructure.data.home import OpenConectionUSER
from Infrastructure.data.models.users import Users
from Resources.helpers.generate_id import GenerateID, IDInt


@OpenConectionUSER
def get_all_users(session):
    return session.query(Users)

@OpenConectionUSER
def get_an_user(email: str, session):
    return session.query(Users).filter(Users.email_user == email)

@OpenConectionUSER
def delete_user(id: int, session):
    user = session.query(Users).filter(Users.id == id).one()
    session.delete(user)

@OpenConectionUSER
def add_new_user(data: UserModel, session):
    user_data = data.dict()
    user_data['id'] = GenerateID( IDInt().length(6).build_with_numbers() ).get()
    user = Users(**user_data)
    session.add(user)