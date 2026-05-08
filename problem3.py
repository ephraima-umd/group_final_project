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


"""
problem3.py - Game statistics and leaderboard utilities.

Techniques demonstrated:
- sequence unpacking
- use of a key function (lambda) with sorted()

Primary author: Jamie and Ephraim
"""

def parse_celebrity_name(full_name):
    """
    Unpack celeb's full name into first name, last name, and intials. 
    Uses sequence unpacking to extract name components cleanly. 

    Primary author: Jamie Rivera
    Techniques Demonstarted: sequence unpacking

    Args:
        full_name (str): A celebrity's full name (e.g. "Adam Sandler").

    Returns;
        tuple[str, str, str]: (first_name, last_name, initials)

    Raises: 
        ValueError: If full_name does not contain a first and last name.

    Example:
        >>> parse_celebrity_name("Adam Sandler")
        ('Adam', 'Sandler', 'AS')

    """
    parts = full_name.strip().split()
    if len(parts) < 2:
        raise ValueError(f"'{full_name}' must have at least a first and last name.")

    first, *middle, last = parts
    initials = first[0].upper() + last[0].upper()
    return first, last, initials

def rank_players(player_scores):
    """

    Return players sorted from highest to lowest score.

    Players with equal scores are sorted alphabetically by name as a "tiebreaker".
    Techniques Demonstrated: use of a key function (lambda) with sorted()

    Primary Author: Jamie Rivera

    Args:
        player_scores (dict[str, int]): Mapping a player name to score.

    Returns:
        list[tuple[str, int]]: List of (name, score) pairs, highest score first. 

    Example;
    >>>> rank_players({"Alice": 7, "Edward": 3, "Bella": 5})
        [('Alice', 7), ('Bella', 5), ('Edward', 3)]
    """
    return sorted(
        player_scores.items()
        key=lambda name_score: (-name_score[1], name_score[0])
    )



    def summarize(chain):
        """ 
        Each entry in the chain is a (name, player) tuple. 
        Sequence unpacking is used to cleanly separate name from player
        on each iteration. 

       Primary Author: Jamie

       Args;
           chain (list[tuple[str, str]]): List of (celebrity_name, player_name) pairs 
           representing the game's name chain in order. 

        Returns:
            list[str]: Easily readable summary lines, one chain per entry. 

        Example:
            >>  summarize(["Michael Jackson", "Alice"), ("Janet Jackson", "Bot")])
            ["#1: Alice played Michael Jackson (MJ)" , "#2: Bot played Janet Jackson (JJ)']
        """

    summary = []
    for i, (celebrity, player) in enumerate(chain, start=1):
        first, last, initials = parse_celebrity_name(celebrity)
        summary.append(f"#{i}: {player} played {celebrity} ({initials})")
    return summary

    
        









    
