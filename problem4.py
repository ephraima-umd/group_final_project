from problem3 import find_valid_names


def choose_valid_bot_name(required_letter, used_names, celebrity_names):
    """
    Choose a valid celebrity name for the bot's turn.

    The bot first finds all valid unused names that start with the required
    letter. If any valid name is a special name, the bot returns the first
    special name it finds. A special name is one where the first letter of
    the first name matches the first letter of the last name. If there are
    no special names, the bot returns the first valid name. If there are no
    valid names, it returns None.

    Primary author: Ephraim Alemayehu

    Args:
        required_letter (str): One alphabetical character.
        used_names (set[str]): Names already used in the game.
        celebrity_names (list[str]): Celebrity names available in the game.

    Returns:
        str | None: The chosen bot name, or None if no valid name exists.

    Raises:
        ValueError: If required_letter is not one alphabetical character.
    """
    valid_names = find_valid_names(required_letter, used_names, celebrity_names)

    for name in valid_names:
        parts = name.split()
        if parts[0][0].lower() == parts[-1][0].lower():
            return name

    if valid_names:
        return valid_names[0]

    return None