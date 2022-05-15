
def say() -> str:
    """tst function.

    Returns:
        str: Hello world
    """
    return "Hello world"


def hello_name(name: str = "User") -> str:
    """Hello.

    Args:
        name (str, optional): user name. Defaults to "User".

    Returns:
        str: Hello {user name}
    """
    return f"Hello {name}"


if __name__ == "__main__":
    print(say())
    name = input("What is your name? - ")
    print(hello_name(name))
