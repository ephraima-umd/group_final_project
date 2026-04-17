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
    - Chooses to skip their turn
    - Enters a regular (non-special) name

    Args:
        player (Player): The current player object with name, score, and turn status.
        name (str): The celebrity name entered by the player.

    Returns:
        bool: True if the player should get another turn, False if the turn should
              pass to the next player.
    """
    # Split the name into first and last parts
    name_parts = name.strip().split()
    
    # Check if it's a special name (first and last name start with same letter)
    if len(name_parts) >= 2:
        first_initial = name_parts[0][0].lower()
        last_initial = name_parts[-1][0].lower()
        
        if first_initial == last_initial:
            # Award one point to the player
            player.score += 1
            print(f"SPECIAL NAME! {player.name} gets 1 point and another turn!")
            print(f"{player.name}'s score is now {player.score}")
            
            # Mark other players as skipped for this round
            # (Assuming game has a list of players and a current round tracker)
            return True  # Signal that this player gets another turn
    
    return False  # Normal turn, move to next player