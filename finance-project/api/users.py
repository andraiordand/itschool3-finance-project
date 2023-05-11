from fastapi import APIRouter, Depends

from domain.asset.factory import AssetFactory
from domain.asset.repo import AssetRepo
from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from persistence.user_file import UserPersistenceFile
from persistence.user_sqlite import UserPersistenceSqlite

users_router = APIRouter(prefix="/users")


def get_user_repo() -> UserRepo:
    user_persistence = UserPersistenceFile("main_users.json")
    user_persistence = UserPersistenceSqlite()
    repo = UserRepo(user_persistence)
    return UserRepo(user_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users(repo=Depends(get_user_repo)):
    return repo.get_all()


# create POST /<user_id>/stocks
# the user can add a stock to its portfolio, by giving the ticker and the number of units it has
# save the country, full name of the company
# when we get a specific user we get the price of every stock the user has and the money it has on it


@users_router.get("/{user_id}", response_model=UserInfo)
def get_user(user_id: str, repo=Depends(get_user_repo)):
    return repo.get_by_id(user_id)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd, repo=Depends(get_user_repo)):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user

# TODO delete a user, DELETE /users/{user_id}

# TODO fix api, return asset info


@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd, repo=Depends(get_user_repo)):
    new_asset = AssetFactory().make_new(asset.ticker)  # TODO homework, if asset exception throw 400
    user = repo.get_by_id(user_id)  # TODO homework, check we have a user otherwise throw exception code 404
    #user.add_stock(new_asset)
    AssetRepo().add_to_user(user, new_asset)
    return new_asset


@users_router.put("/{user_id}", response_model=UserInfo)
def edit_by_id(user_id: str, username: str, repo=Depends(get_user_repo)):
    repo.edit_by_id(user_id, username)
    return repo.get_by_id(user_id)


@users_router.delete("/{user_id}")
def delete_user(user_id: str, repo=Depends(get_user_repo)):
    repo.delete_by_id(user_id)
