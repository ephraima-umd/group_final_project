"""
CelebrityWordJab - Main Game File
A trivia naming game where players take turns naming celebrities.
"""

import random
from problem_1 import special_name_turn, is_special_name, handle_special_name_streak
from problem_3 import eject_player_if_invalid, validate_and_process_turn, check_name_validity
from problem_4 import choose_valid_bot_name
from random_bonus import apply_random_bonus, apply_simple_bonus


# ============================================
# PLAYER CLASS
# ============================================

class Player:
    """
    Represents a player in the CelebrityWordJab game.
    """
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.is_active = True
        self.turns_taken = 0
    
    def __str__(self):
        return f"{self.name} (Score: {self.score})"


# ============================================
# GAME CLASS
# ============================================

class CelebrityWordJab:
    """
    Main game class that manages the CelebrityWordJab game.
    """
    
    def __init__(self, celebrity_file="celebrities.txt"):
        """
        Initialize the game with celebrity list and game state.
        
        Args:
            celebrity_file (str): Path to the file containing celebrity names.
        """
        self.celebrity_names = self.load_celebrities(celebrity_file)
        self.used_names = set()
        self.players = []
        self.current_player_index = 0
        self.game_over = False
        self.winner = None
        self.skip_tracker = {"skip": False}
        self.target_score = 21
        
        # Bonus feature flag (set to True to enable random bonuses)
        self.enable_bonuses = True
        
        # Print confirmation of loaded celebrities
        print(f"Loaded {len(self.celebrity_names)} celebrity names from {celebrity_file}")
    
    def load_celebrities(self, filepath):
        """
        Load celebrity names from a text file.
        
        Args:
            filepath (str): Path to the celebrities text file.
            
        Returns:
            list[str]: A list of celebrity names.
        """
        try:
            # Try to open and read the file
            file = open(filepath, "r", encoding="utf-8")
            celebrities = []
            
            # Read each line and strip whitespace
            for line in file:
                line = line.strip()
                if line:  # Only add non-empty lines
                    celebrities.append(line)
            
            # Close the file
            file.close()
            
            # Sort alphabetically
            celebrities.sort()
            
            print(f"Successfully loaded {len(celebrities)} celebrities from {filepath}")
            return celebrities
            
        except FileNotFoundError:
            # If file doesn't exist, show error and exit
            print(f"ERROR: {filepath} not found!")
            print(f"Please create a file named '{filepath}' with one celebrity name per line.")
            print("Example format:")
            print("  Adam Sandler")
            print("  Angelina Jolie")
            print("  Beyonce Knowles")
            
            # Return empty list (game won't work properly)
            return []
    
    def add_player(self, name):
        """
        Add a new player to the game.
        
        Args:
            name (str): The player's name.
        """
        if len(self.players) < 4:
            new_player = Player(name)
            self.players.append(new_player)
            print(f"Welcome {name}! You have been added to the game.")
        else:
            print("Maximum 4 players already in the game!")
    
    def get_required_letter_from_name(self, name):
        """
        Extract the required letter from a full celebrity name.
        
        Args:
            name (str): The celebrity name.
            
        Returns:
            str: The first letter of the last name.
        """
        # Split the name into parts
        name_parts = name.strip().split()
        
        # Get the last part (last name) and take its first letter
        last_name = name_parts[-1]
        required_letter = last_name[0].upper()
        
        return required_letter
    
    def get_valid_input(self, prompt, required_letter):
        """
        Get valid input from the player.
        
        Args:
            prompt (str): The input prompt to display.
            required_letter (str): The letter the name must start with.
            
        Returns:
            str: A valid celebrity name or "skip".
        """
        while True:
            entry = input(prompt).strip().title()
            
            # Allow skip
            if entry.lower() == "skip" or entry.lower() == "pass":
                return entry
            
            # Check if name has at least first and last name
            name_parts = entry.split()
            if len(name_parts) < 2:
                print("Name must have at least a first and last name. Try again!")
                continue
            
            # Check if name exists in the celebrity database
            if entry not in self.celebrity_names:
                print(f"'{entry}' is not in our celebrity list. Try again!")
                continue
            
            # Check if name has already been used
            if entry in self.used_names:
                print(f"'{entry}' has already been used in this game! Try again!")
                continue
            
            # Check if name starts with required letter
            first_initial = entry.split()[0][0].upper()
            if first_initial != required_letter.upper():
                print(f"Name must start with '{required_letter.upper()}'. Try again!")
                continue
            
            return entry
    
    def display_scores(self):
        """
        Display all player scores in a formatted table.
        """
        print("\n" + "=" * 40)
        print("CURRENT SCORES:")
        print("-" * 40)
        
        # Sort players by score (highest first) using bubble sort (beginner friendly)
        sorted_players = []
        for player in self.players:
            sorted_players.append(player)
        
        # Simple bubble sort to avoid lambda
        for i in range(len(sorted_players)):
            for j in range(i + 1, len(sorted_players)):
                if sorted_players[i].score < sorted_players[j].score:
                    # Swap
                    temp = sorted_players[i]
                    sorted_players[i] = sorted_players[j]
                    sorted_players[j] = temp
        
        # Display each player
        for i in range(len(sorted_players)):
            player = sorted_players[i]
            if player.is_active:
                status = "ACTIVE"
            else:
                status = "EJECTED"
            print(f"{i+1}. {player.name}: {player.score} points [{status}]")
        
        print("=" * 40 + "\n")
    
    def display_used_names(self):
        """
        Display recently used names (last 5).
        """
        if len(self.used_names) > 0:
            print("\nRecently used names:")
            
            # Convert set to list and get last 5
            used_list = list(self.used_names)
            recent_names = []
            
            # Get last 5 items or fewer
            start_index = len(used_list) - 5
            if start_index < 0:
                start_index = 0
            
            for i in range(start_index, len(used_list)):
                recent_names.append(used_list[i])
            
            for name in recent_names:
                print(f"  - {name}")
            print()
    
    def show_game_status(self):
        """
        Display current game status including scores and used names.
        """
        self.display_scores()
        if len(self.used_names) > 0:
            self.display_used_names()
    
    def check_winner(self):
        """
        Check if any player has reached the target score.
        
        Returns:
            Player or None: The winner if exists, None otherwise.
        """
        for player in self.players:
            if player.is_active and player.score >= self.target_score:
                return player
        return None
    
    def process_regular_turn(self, player, name, required_letter):
        """
        Process a regular turn (non-special name).
        
        Args:
            player (Player): The current player.
            name (str): The entered celebrity name.
            required_letter (str): The required starting letter.
            
        Returns:
            bool: True if turn was successful, False if player was ejected.
        """
        # Validate and process the turn
        success = validate_and_process_turn(player, name, self.used_names, self.celebrity_names)
        
        if success == False:
            return False
        
        # Apply random bonus if enabled
        if self.enable_bonuses == True:
            bonus_message = apply_random_bonus(player, self.players, self.skip_tracker)
            print(f"  -> {bonus_message}")
        
        print(f"  -> {player.name} now has {player.score} points!")
        return True
    
    def process_special_turn(self, player, name):
        """
        Process a special name turn (alliteration that gives extra turns).
        
        Args:
            player (Player): The current player.
            name (str): The special celebrity name.
            
        Returns:
            bool: True if turn was successful, False if player was ejected.
        """
        # Handle the special name turn logic
        another_turn = special_name_turn(player, name)
        
        if another_turn == True:
            print(f"\n{player.name} gets another turn due to special name!")
            
            # Get the required letter for the next turn
            required_letter = self.get_required_letter_from_name(name)
            
            # Enter the special name streak
            final_name = handle_special_name_streak(
                player, required_letter, self.used_names, 
                self.celebrity_names, self.get_valid_input
            )
            
            # If player didn't skip, add the final name to used_names
            if final_name is not None:
                self.used_names.add(final_name)
                print(f"  -> {player.name}'s score is now {player.score}")
        
        # Add original name to used_names
        if name not in self.used_names:
            self.used_names.add(name)
        
        return True
    
    def process_bot_turn(self, player, required_letter):
        """
        Process a bot player's turn (automatic name selection).
        
        Args:
            player (Player): The bot player.
            required_letter (str): The required starting letter.
            
        Returns:
            tuple: (success, new_required_letter)
        """
        print(f"\n🤖 BOT TURN: {player.name} is thinking...")
        
        bot_name = choose_valid_bot_name(required_letter, self.used_names, self.celebrity_names)
        
        if bot_name is None:
            print(f"  -> {player.name} has no valid names to play!")
            print(f"  -> {player.name} is ejected from the game!")
            player.is_active = False
            return False, required_letter
        
        print(f"  -> {player.name} chooses: {bot_name}")
        
        # Check if it's a special name
        if is_special_name(bot_name) == True:
            player.score = player.score + 1
            print(f"  -> SPECIAL NAME! {player.name} gets an extra point!")
        
        # Add to used names and award point
        self.used_names.add(bot_name)
        player.score = player.score + 1
        
        print(f"  -> {player.name} now has {player.score} points!")
        
        # Get the required letter for next player
        next_required = self.get_required_letter_from_name(bot_name)
        
        return True, next_required
    
    def take_turn(self, player, required_letter):
        """
        Process a single turn for a player.
        
        Args:
            player (Player): The player taking the turn.
            required_letter (str): The required starting letter for the name.
            
        Returns:
            tuple: (was_successful, new_required_letter)
        """
        # Check if player is active
        if player.is_active == False:
            print(f"{player.name} is no longer in the game. Skipping turn.")
            return False, required_letter
        
        # Check if this turn should be skipped due to bonus effect
        skip_next = self.skip_tracker.get("skip", False)
        if skip_next == True:
            print(f"\n{player.name}'s turn is SKIPPED due to a TRICK PLAY bonus!")
            self.skip_tracker["skip"] = False
            return True, required_letter
        
        # Check if player is a bot (name starts with "Bot_")
        if player.name.startswith("Bot_") == True:
            return self.process_bot_turn(player, required_letter)
        
        print(f"\n{'='*50}")
        print(f"{player.name}'s TURN (Score: {player.score})")
        print(f"Required first letter: {required_letter}")
        print(f"{'='*50}")
        
        # Get player input (no examples shown)
        prompt = f"\n{player.name}, enter a celebrity name starting with '{required_letter}': "
        name = self.get_valid_input(prompt, required_letter)
        
        # Check if player wants to skip
        if name.lower() == "skip" or name.lower() == "pass":
            print(f"{player.name} skips their turn. No points awarded.")
            return True, required_letter
        
        # Check if the name is a special name
        if is_special_name(name) == True:
            success = self.process_special_turn(player, name)
        else:
            success = self.process_regular_turn(player, name, required_letter)
            # Add regular name to used_names
            if name not in self.used_names:
                self.used_names.add(name)
        
        if success == False:
            return False, required_letter
        
        # Get the required letter for the next player
        next_required = self.get_required_letter_from_name(name)
        
        return True, next_required
    
    def run(self):
        """
        Main game loop.
        """
        print("\n" + "=" * 50)
        print("🎮 WELCOME TO CELEBRITYWORDJAB! 🎮")
        print("=" * 50)
        print("\nRULES:")
        print("1. Players take turns naming celebrities")
        print("2. Your name must start with the first letter of the previous player's LAST name")
        print("3. Special names (same first/last letter) give bonus points AND extra turns")
        print("4. Type 'skip' to skip your turn without penalty")
        print("5. First to reach 21 points wins!")
        print("6. Invalid names or repeats will eject you from the game!")
        
        if self.enable_bonuses == True:
            print("7. BONUS FEATURE: Random events can happen each turn!")
        
        print("\n" + "-" * 50)
        
        # Check if celebrities were loaded
        if len(self.celebrity_names) == 0:
            print("\nERROR: No celebrity names loaded. Cannot start game.")
            print("Please create a 'celebrities.txt' file with celebrity names.")
            return
        
        # Get number of players
        while len(self.players) < 1:
            try:
                num_players_input = input("\nHow many human players? (1-4): ")
                num_players = int(num_players_input)
                
                if num_players >= 1 and num_players <= 4:
                    for i in range(num_players):
                        name = input(f"Enter name for Player {i+1}: ").strip()
                        if name == "":
                            self.add_player(f"Player{i+1}")
                        else:
                            self.add_player(name)
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Add bot players if less than 4 total
        total_players = len(self.players)
        if total_players < 4:
            num_bots = 4 - total_players
            for i in range(num_bots):
                bot_name = f"Bot_{i+1}"
                self.add_player(bot_name)
                print(f"🤖 Bot {bot_name} has joined the game!")
        
        # Random starting letter
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_index = random.randint(0, len(alphabet) - 1)
        current_letter = alphabet[random_index]
        print(f"\n🎲 Starting letter: {current_letter}")
        
        # Main game loop
        turn_count = 0
        while self.game_over == False:
            # Get current player
            current_player = self.players[self.current_player_index]
            
            # Skip inactive players
            if current_player.is_active == False:
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                continue
            
            # Show game status every 3 turns
            if turn_count % 3 == 0 and turn_count > 0:
                self.show_game_status()
            
            # Take the turn
            success, current_letter = self.take_turn(current_player, current_letter)
            
            # Check for winner
            winner = self.check_winner()
            if winner is not None:
                self.game_over = True
                self.winner = winner
                break
            
            # Move to next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            turn_count = turn_count + 1
        
        # Game over - show winner
        print("\n" + "=" * 50)
        print(f"🏆 GAME OVER! {self.winner.name} WINS with {self.winner.score} points! 🏆")
        print("=" * 50)
        self.display_scores()


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == "__main__":
    # Create and run the game
    game = CelebrityWordJab("celebrities.txt")
    game.run()
