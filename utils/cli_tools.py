import re
import six
from PyInquirer import (
    Token,
    ValidationError,
    Validator,
    prompt,
    style_from_dict,
)
from pyfiglet import figlet_format


try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

style = style_from_dict(
    {
        Token.QuestionMark: "#fac731 bold",
        Token.Answer: "#4688f1 bold",
        Token.Instruction: "",  # default
        Token.Separator: "#cc5454",
        Token.Selected: "#0abf5b",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Question: "",
    }
)


def log(string, color="white", font="slant", figlet=False, attrs=None):
    if colored:
        if not figlet:
            six.print_(colored(string, color, attrs=attrs))
        else:
            six.print_(colored(figlet_format(string, font=font), color))
    else:
        six.print_(string)


class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(value.text)
            )


class SteamValidator(Validator):
    pattern = r"^[0-9]{17}$"

    def validate(self, value):

        if len(value.text) == 17:
            if re.fullmatch(self.pattern, value.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid SteamID64 (contents)",
                    cursor_position=len(value.text),
                )

        else:
            raise ValidationError(
                message="Invalid SteamID64 (length)", cursor_position=len(value.text)
            )


def ask_steamid():
    questions = [
        {
            "type": "input",
            "name": "steamid",
            "message": "Enter the SteamID64 to add",
            "validate": SteamValidator,
        },
    ]

    answer = prompt(questions, style=style)
    return answer


def ask_display_name():
    questions = [
        {
            "type": "input",
            "name": "displayname",
            "message": "Enter the DisplayName to add",
            "validate": EmptyValidator,
        },
    ]

    answer = prompt(questions, style=style)
    return answer


def ask_add_data():
    questions = [
        {
            "type": "confirm",
            "name": "add",
            "message": "Do you need to add any SteamID64s?",
            "default": False,
        },
    ]

    answer = prompt(questions, style=style)
    return answer


def ask_start():
    questions = [
        {
            "type": "confirm",
            "name": "start",
            "message": "Press enter to start",
        }
    ]

    answer = prompt(questions, style=style)
    return answer


def ask_exit():
    questions = [
        {
            "type": "confirm",
            "name": "exit",
            "message": "Exit?",
            "default": False,
        },
    ]

    answer = prompt(questions, style=style)
    return answer


def header(allowed: dict):
    log("OverlyPieShaper", color="blue", figlet=True)
    log(
        "Welcome to OverlyPieShaper, for all your traffic shaping needs",
        color="cyan",
        attrs=["bold"],
    )
    log(f"Loaded SteamIDs ({len(allowed.keys())}):", color="yellow")
    for k, v in allowed.items():
        log(f"\t{k} - {v}", color="yellow")
