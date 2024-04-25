import webbrowser
import main
import sys
import requests
import hashlib


class SoteraDriver:
    def __init__(self) -> None:
        self.backend_url = "http://localhost:8000/api/v1"

    def create_account(self, user_id: int) -> str | None:
        data = {
            "key_id": user_id,
            "nonce": hashlib.md5(str(user_id).encode()).hexdigest(),
        }
        auth_url = f"{self.backend_url}/auth/signup"
        response = requests.post(
            url=auth_url, json=data, headers={"Content-Type": "application/json"}
        )

        if response.status_code == 409:
            print("Account with that Finger-print already exists!\nTry Logging In")
            return None
        return response.json()["key"]
        # return "lmao"

    def login_web(self, user_id: int) -> bool:
        data = {
            "key_id": user_id,
            "nonce": hashlib.md5(str(user_id).encode()).hexdigest(),
        }
        login_url = f"{self.backend_url}/auth/login"
        response = requests.post(
            url=login_url, json=data, headers={"Content-Type": "application/json"}
        )
        if response.status_code != 200:
            print("You Session Expired! or Something Went Wrong")
            return False

        session_id = response.json()["key"]

        opened = webbrowser.open(
            f"http://localhost:5173/dashboard?session={session_id}"
        )
        url = f"http://localhost:5173/dashboard?session={session_id}"
        print(f" {opened} If the browser did not open, Please go to {url}")
        return True

    def get_latest_int(self) -> int:
        with open("latest.int.txt", "r") as reader:
            try:
                data = reader.readline()
                print(data)
                return int(data)
            except ValueError as ve:
                print("ve", ve)
                sys.exit(1)
            except Exception as e:
                print(e)
                sys.exit(1)

    def write_latest_int(self, new: int) -> int:
        with open("latest.int.txt", "w") as writer:
            writer.write(str(new))
        return new

    def register(self):
        latest_int = self.get_latest_int()
        print(f"Enrolling {latest_int+1}")
        if main.enroll_finger(latest_int + 1):
            self.write_latest_int(latest_int + 1)
            data = self.create_account(latest_int + 1)
            if not data:
                pass
            webbrowser.open(f"http://localhost:5173/dashboard?session={data}")
        else:
            print("Registration Failed! :(")

    def login(self) -> None:
        result = main.search_fingerprint()
        if not result:
            print("Such finterprint Not Found!")
            return
        print("Finger-print Found!, Logging you in! ", result)
        if not self.login_web(result):
            print("Web Browser Opening Failed!")
