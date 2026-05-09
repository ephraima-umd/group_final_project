def special_name_turn(player, name):
    """
    Handle the turn logic when a player enters a special name.

    A special name is when the first letter of the first name matches the
    first letter of the last name (e.g., "Marilyn Monroe" or "Robert Redford").

    When a special name is entered:
    - The player gains 1 point
    - All other players are skipped for this round
    - The same player gets an immediate extra turn
    - This repeats as long as the player keeps entering special names

    The special turn streak ends when the player either:
    - Chooses to skip their turn (enters "skip" or "pass")
    - Enters a regular (non-special) name

    Args:
        player (Player): The current player object with name, score, and turn status.
        name (str): The celebrity name entered by the player.

    Returns:
        bool: True if the player should get another turn, False if the turn should
              pass to the next player.
    """
    # Check if player wants to skip their special streak
    if name.lower() == "skip" or name.lower() == "pass":
        print(f"{player.name} chooses to skip their special turn streak.")
        print(f"Moving to next player.")
        return False
    
    # Split the name into first and last parts
    name_parts = name.strip().split()
    
    # Check if the name has at least first and last name
    if len(name_parts) >= 2:
        # Get the first letter of the first name
        first_initial = name_parts[0][0].lower()
        # Get the first letter of the last name
        last_initial = name_parts[-1][0].lower()
        
        # Check if it's a special name (both initials match)
        if first_initial == last_initial:
            # Award one point to the player
            player.score = player.score + 1
            print(f"SPECIAL NAME! {player.name} gets 1 point and another turn!")
            print(f"{player.name}'s score is now {player.score}")
            
            # Signal that this player gets another turn
            return True
    
    # Not a special name, move to next player
    return False


def is_special_name(name):
    """
    Check if a celebrity name is a special name (alliteration).

    A special name is defined as a name where the first letter of the
    first name matches the first letter of the last name.

    Args:
        name (str): The celebrity name to check.

    Returns:
        bool: True if the name is a special name, False otherwise.
    """
    # Check if player wants to skip
    if name.lower() == "skip" or name.lower() == "pass":
        return False
    
    name_parts = name.strip().split()
    
    # Need at least first and last name to check
    if len(name_parts) < 2:
        return False
    
    # Compare first letters of first and last name
    first_initial = name_parts[0][0].lower()
    last_initial = name_parts[-1][0].lower()
    
    # Return True if they match
    if first_initial == last_initial:
        return True
    else:
        return False


def handle_special_name_streak(player, required_letter, used_names, celebrity_names, get_valid_input_function):
    """
    Handle a player's special name streak where they keep getting extra turns.

    This function continues giving the player turns as long as they keep
    entering special names. The streak ends when they enter a regular name
    or choose to skip.

    Args:
        player (Player): The current player object.
        required_letter (str): The letter the next name must start with.
        used_names (set[str]): Names already used in the game.
        celebrity_names (list[str]): List of all valid celebrity names.
        get_valid_input_function (function): Function to get valid player input.

    Returns:
        str or None: The final regular name that ended the streak, or None if player skipped.
    """
    print(f"\n--- SPECIAL NAME STREAK for {player.name}! ---")
    print("You keep playing until you enter a regular name or type 'skip'")
    
    streak_continues = True
    final_name = None
    
    while streak_continues:
        # Prompt for another name
        prompt = f"{player.name}, enter another name starting with '{required_letter}' (or 'skip' to end streak): "
        entered_name = get_valid_input_function(prompt, required_letter)
        
        # Check if player wants to skip
        if entered_name.lower() == "skip" or entered_name.lower() == "pass":
            print(f"{player.name} chooses to end their special streak.")
            print(f"No points awarded for skipping.")
            streak_continues = False
            final_name = None
        
        # Check if it's a special name
        elif is_special_name(entered_name):
            # Award point and continue streak
            player.score = player.score + 1
            print(f"ANOTHER SPECIAL NAME! {player.name} gets 1 more point!")
            print(f"{player.name}'s score is now {player.score}")
            print("You get ANOTHER turn! Keep going or type 'skip' to stop.")
        
        else:
            # Regular name ends the streak
            print(f"Regular name entered. {player.name}'s special streak ends.")
            final_name = entered_name
            streak_continues = False
    
    return final_name
