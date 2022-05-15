
import main


def test_say():
    assert main.say() == "Hello world"


def test_hello_user_name():
    name = "Aleksii"
    assert main.hello_name(name) == "Hello Aleksii"
