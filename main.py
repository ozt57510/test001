"""General file with run project"""

def say() -> str:
    """First function.

    Returns:
        str: Hello world
    """
    return "Hello world"


def hello_name(user_name: str = "User") -> str:
    """Hello.

    Args:
        name (str, optional): user name. Defaults to "User".

    Returns:
        str: Hello {user name}
    """
    return f"Hello {user_name}"
