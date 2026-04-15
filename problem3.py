def find_valid_names(required_letter, used_names, celebrity_names):
    """
    Return all valid unused celebrity names that start with the required letter.

    A valid name must:
    - have at least a first and last name
    - not already be in used_names
    - have a first name that starts with required_letter

    Primary author: Ephraim Alemayehu
    Techniques demonstrated: comprehensions / generator expressions

    Args:
        required_letter (str): One alphabetical character.
        used_names (set[str]): Names already used in the game.
        celebrity_names (list[str]): Celebrity names available in the game.

    Returns:
        list[str]: A list of valid unused names.

    Raises:
        ValueError: If required_letter is not one alphabetical character.
    """
    if len(required_letter) != 1 or not required_letter.isalpha():
        raise ValueError("required_letter must be one letter.")

    required_letter = required_letter.lower()

    return [
        name for name in celebrity_names
        if len(name.split()) >= 2
        and name not in used_names
        and name.split()[0][0].lower() == required_letter
    ]