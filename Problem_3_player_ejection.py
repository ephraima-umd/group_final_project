def eject_player_if_invalid(player, name, used_names, celebrity_names):
    """
    Eject a player from the game if they fail to provide a valid celebrity name.

    A player is ejected immediately if:
    - They enter "skip", "pass", or "give up" (case insensitive)
    - They enter a name not in the celebrity_names database
    - They enter a name that has already been used (in used_names)
    - They enter a name with fewer than two parts (missing first or last name)

    Ejected players cannot continue playing and are removed from future turns.

    Args:
        player (Player): The current player being checked for ejection.
        name (str): The name entered by the player (or "skip"/"pass"/"give up").
        used_names (set[str]): Set of celebrity names already used in the game.
        celebrity_names (list[str]): List of all valid celebrity names.

    Returns:
        bool: True if the player was ejected, False if the player is still in the game.
    """
    # Check if player gave up voluntarily
    if name.lower() in ["skip", "pass", "give up"]:
        print(f"{player.name} has given up and is ejected from the game!")
        player.is_active = False
        return True
    
    # Check if name has at least first and last name
    name_parts = name.strip().split()
    if len(name_parts) < 2:
        print(f"Invalid name: '{name}' must have at least a first and last name.")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Check if name exists in the celebrity database
    if name not in celebrity_names:
        print(f"'{name}' is not in our celebrity database.")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Check if name has already been used
    if name in used_names:
        print(f"'{name}' has already been used in this game!")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Player is valid and stays in the game
    return False