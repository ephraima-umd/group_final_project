def apply_random_bonus(player):
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

    Returns:
        str: A message describing what bonus or penalty occurred.
    """
    import random
    
    # 20% chance of random event
    if random.random() < 0.2:
        event_type = random.choice(["bonus", "steal", "skip_next", "penalty"])
        
        if event_type == "bonus":
            bonus = random.randint(1, 3)
            player.score += bonus
            return f"LUCKY BREAK! {player.name} gets {bonus} bonus points!"
        
        elif event_type == "steal" and hasattr(player, 'game'):
            # Steal 1 point from a random active player
            other_players = [p for p in player.game.players if p != player and p.is_active]
            if other_players:
                victim = random.choice(other_players)
                if victim.score > 0:
                    victim.score -= 1
                    player.score += 1
                    return f"POWER MOVE! {player.name} steals 1 point from {victim.name}!"
        
        elif event_type == "skip_next":
            # Mark next player as skipped
            if hasattr(player, 'game'):
                player.game.skip_next_player = True
                return f"TRICK PLAY! The next player's turn is skipped!"
        
        elif event_type == "penalty":
            penalty = 1
            player.score = max(0, player.score - penalty)
            return f"OH NO! {player.name} loses {penalty} point!"
    
    return f"{player.name} plays it safe this turn."