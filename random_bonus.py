import random

def apply_random_bonus(player, all_players, skip_next_tracker):
    """
    Randomly award bonus points or penalties to make the game more exciting.

    There is a 20% chance of triggering a random event when a player
    successfully names a celebrity. Events include:
    - Bonus points (extra 1-3 points)
    - Steal a point from another player
    - Skip the next player's turn
    - Small penalty (lose 1 point, but never go below zero)

    Args:
        player (Player): The player who just successfully named a celebrity.
        all_players (list): List of all players in the game.
        skip_next_tracker (dict): A mutable object to track if next turn is skipped.

    Returns:
        str: A message describing what bonus or penalty occurred.
    """
    # Generate a random number between 0 and 1
    random_chance = random.random()
    
    # 20% chance of random event
    if random_chance < 0.2:
        # Choose a random event type
        event_options = ["bonus", "steal", "skip_next", "penalty"]
        event_type = random.choice(event_options)
        
        # Handle BONUS event
        if event_type == "bonus":
            bonus = random.randint(1, 3)
            player.score = player.score + bonus
            return f"LUCKY BREAK! {player.name} gets {bonus} bonus points!"
        
        # Handle STEAL event
        elif event_type == "steal":
            # Build list of other active players
            other_players = []
            for p in all_players:
                if p != player and p.is_active:
                    other_players.append(p)
            
            # If there are other players to steal from
            if len(other_players) > 0:
                victim = random.choice(other_players)
                
                # Check if victim has points to steal
                if victim.score > 0:
                    victim.score = victim.score - 1
                    player.score = player.score + 1
                    return f"POWER MOVE! {player.name} steals 1 point from {victim.name}!"
                else:
                    return f"STEAL ATTEMPT FAILED! {victim.name} has no points to steal!"
            else:
                return f"No other players to steal from! {player.name} gets nothing."
        
        # Handle SKIP NEXT event
        elif event_type == "skip_next":
            # Mark next player as skipped
            if skip_next_tracker is not None:
                skip_next_tracker["skip"] = True
                return f"TRICK PLAY! The next player's turn is skipped!"
            else:
                return f"TRICK PLAY! No skip tracker available!"
        
        # Handle PENALTY event
        elif event_type == "penalty":
            penalty = 1
            old_score = player.score
            
            # Subtract penalty but don't go below zero
            if player.score - penalty < 0:
                player.score = 0
            else:
                player.score = player.score - penalty
            
            if old_score > 0:
                return f"OH NO! {player.name} loses {penalty} point!"
            else:
                return f"OH NO! {player.name} has no points to lose!"
    
    # No event occurred
    return f"{player.name} plays it safe this turn."


def apply_simple_bonus(player, all_players):
    """
    A simpler version of random bonus that only affects the current player.
    No skip_next functionality, just bonus points, stealing, or penalty.

    Args:
        player (Player): The player who just successfully named a celebrity.
        all_players (list): List of all players for stealing.

    Returns:
        str: A message describing what bonus or penalty occurred.
    """
    # 25% chance of random event
    random_chance = random.random()
    
    if random_chance < 0.25:
        # Choose a random event type
        event_options = ["bonus", "steal", "penalty"]
        event_type = random.choice(event_options)
        
        # Handle BONUS event
        if event_type == "bonus":
            bonus = random.randint(1, 3)
            player.score = player.score + bonus
            return f"LUCKY BREAK! {player.name} gets {bonus} bonus points!"
        
        # Handle STEAL event
        elif event_type == "steal":
            # Build list of other active players
            other_players = []
            for p in all_players:
                if p != player and p.is_active:
                    other_players.append(p)
            
            # If there are other players to steal from
            if len(other_players) > 0:
                victim = random.choice(other_players)
                
                # Check if victim has points to steal
                if victim.score > 0:
                    victim.score = victim.score - 1
                    player.score = player.score + 1
                    return f"POWER MOVE! {player.name} steals 1 point from {victim.name}!"
                else:
                    return f"STEAL FAILED! {victim.name} has no points!"
            else:
                return f"No other players in the game!"
        
        # Handle PENALTY event
        elif event_type == "penalty":
            penalty = random.randint(1, 2)
            old_score = player.score
            
            # Subtract penalty but don't go below zero
            if player.score - penalty < 0:
                player.score = 0
            else:
                player.score = player.score - penalty
            
            if old_score >= penalty:
                return f"OH NO! {player.name} loses {penalty} points!"
            else:
                return f"OH NO! {player.name} loses {old_score} point(s) and hits zero!"
    
    return f"{player.name} plays it safe this turn."


def apply_guaranteed_bonus(player, all_players):
    """
    A version that ALWAYS gives a random bonus (no safe plays).
    Makes the game more chaotic and fun.

    Args:
        player (Player): The player who just successfully named a celebrity.
        all_players (list): List of all players for stealing.

    Returns:
        str: A message describing what bonus or penalty occurred.
    """
    # Choose a random event type (bonus appears twice for higher chance)
    event_options = ["bonus", "bonus", "steal", "steal", "penalty", "jackpot"]
    event_type = random.choice(event_options)
    
    # Handle BONUS event
    if event_type == "bonus":
        bonus = random.randint(1, 2)
        player.score = player.score + bonus
        return f"BONUS! {player.name} gets {bonus} extra point(s)!"
    
    # Handle JACKPOT event
    elif event_type == "jackpot":
        jackpot = random.randint(3, 5)
        player.score = player.score + jackpot
        return f"JACKPOT!!! {player.name} hits the jackpot and gets {jackpot} points!"
    
    # Handle STEAL event
    elif event_type == "steal":
        # Build list of other active players
        other_players = []
        for p in all_players:
            if p != player and p.is_active:
                other_players.append(p)
        
        if len(other_players) > 0:
            victim = random.choice(other_players)
            steal_amount = random.randint(1, 2)
            
            # Check if victim has enough points
            if victim.score >= steal_amount:
                victim.score = victim.score - steal_amount
                player.score = player.score + steal_amount
                return f"THEFT! {player.name} steals {steal_amount} point(s) from {victim.name}!"
            
            # Steal whatever they have
            elif victim.score > 0:
                stolen = victim.score
                player.score = player.score + stolen
                victim.score = 0
                return f"THEFT! {player.name} steals {stolen} point(s) from {victim.name}!"
            
            else:
                return f"THEFT FAILED! {victim.name} has no points to steal!"
        else:
            return f"No one to steal from!"
    
    # Handle PENALTY event
    elif event_type == "penalty":
        penalty = random.randint(1, 2)
        old_score = player.score
        
        # Subtract penalty but don't go below zero
        if player.score - penalty < 0:
            player.score = 0
        else:
            player.score = player.score - penalty
        
        if old_score >= penalty:
            return f"PENALTY! {player.name} loses {penalty} point(s)!"
        else:
            return f"PENALTY! {player.name} loses {old_score} point(s) and hits zero!"
    
    # Fallback (should never reach here)
    return f"Something weird happened!"
