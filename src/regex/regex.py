import re
from typing import Optional


def eval_none_str(x: Optional[int]) -> str:
    if x is None:
        return ""
    else:
        return str(x)


def rm_trailing_numbers(input_email: str, lb: int = 1, ub: Optional[int] = None) -> str:
    """[A function to remove the numbers behind the username of an email address]

    For example, a1234@gmail.com will be a@gmail.com with default values
    a1234@gmail.com will remain as it is if ub < 4. 
    
    Args:
        input_email (str): [A valid email]
        lb (int): [upper bound]
        ub (int): [lower bound]

    Returns:
        str: [email stripped]
    """
    preceding_token: str = "{" + str(lb) + "," + eval_none_str(ub) + "}"
    regex_string: str = r"[~0-9]{0}(?=@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)".format(
        preceding_token
    )

    return re.sub(regex_string, "", input_email)


def extract_username(input_email: str) -> str:
    """[extract username]

    a@gmail.com will become a
    Args:
        input_email (str): [a valid email]

    Returns:
        str: [the username portion]
    """
    return re.search(r"(.*)(?=@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", input_email).group()

