from domain.entities.account import Account
from domain.interfaces import UseCase
import requests
from domain.constants import BASE_URL, ACCOUNT_HEADERS


class AccountGetter(UseCase):

    def execute(self, *args, **kwargs) -> Account:
        response = requests.get(f"{BASE_URL}/my/agent", headers=ACCOUNT_HEADERS)

        if response.status_code == 200:
            return self._parse_account_data(response.json())
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def _parse_account_data(self, api_response: dict) -> Account:
        data = api_response["data"]
        return Account.from_dict(data)

if __name__ == "__main__":
    from pprint import pprint
    account = AccountGetter().execute()
    pprint(account)
