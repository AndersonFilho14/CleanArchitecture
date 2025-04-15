from .user_finder import UserFider
from src.infra.db.repositories.users_repository import UsersRepository

def test_find():
    user_finder = UserFider(users_repositories= UsersRepository )