from problem3 import find_valid_names
from problem4 import choose_valid_bot_name

def main():
    """
    Run a small test of the name-filtering and bot-choice functions.

    Primary author: Ephraim Alemayehu
    
    """
    used_names = {"Michael Jordan", "Miley Cyrus"}
    celebrity_names = [
        "Michael Jordan",
        "Miley Cyrus",
        "Mickey Mouse",
        "Marilyn Monroe",
        "Megan Fox",
        "Zendaya"
    ]

    valid_names = find_valid_names("M", used_names, celebrity_names)
    bot_name = choose_valid_bot_name("M", used_names, celebrity_names)

    print("Valid names:", valid_names)
    print("Bot choice:", bot_name)


if __name__ == "__main__":
    main()


def load_celebrities(filepath="celebrities.txt"):
    """
    Load celebrity names from a text file. 

    Args:
        filepath (str): Path to the celebrities text file.

    Returns:
        list[str]: A list of celebrity names. 

    Primary Author: Jamie Rivera

    """
    with open(filepath, "r", encoding = "utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_required_letter(name):
    """
    Return the first letter of the last name (the required 
    starting letter for the next player's turn).

    Args:
        name (str): A celebrity full name.

    Returns:
    str: One uppercase letter.
    """
    return name.strip().split()[-1][0].upper()

def get_valid_input(prompt, required_letter, used_names, celebrity_names):
    """
    Prompt the player until they enter a valid celebrity name.

    A valid entry must:
    - Exist in the celebrity list
    - Not have been used already
    - Start with the required letter

    Args:
        prompt (str): The input prompt to display. 
        required_letter (str): The letter the name must start with. 
        used_names (set[str]): Names already used in the game. 
        celebrity_names (list[str]): The full celebrity list. 

    Returns:
        str: A valid celebrity name. 
    """

    while True:
        entry = input(prompt).strip().title()

        if entry not in celebrity_names:
            print(f"{entry} is not in the celebrity list. Try Again!")
            continue

        if entry in used_names:
            print(f"{entry} has already been used. Try again!")
            continue

        if entry.split()[0][0].upper() != required_letter:
            print(f"Name must start with '{required_letter}'. Try again!")
            continue

        return entry

def play_vs_bot(celebrity_names):
    """
    Run a single games between the player and the bot. 

    The player goes first by entering any celebrity. Then turns alternate. 
    The game ends when either the player or the bot cannot find a valid name. 

    Args:
        celebrity_names (list[str]): the full celebrity list. 

    """

    used_names = set()
    required_letter = None

print("You go first! Enter any celebrity to begin: \n")

while True:

    prompt = "You: " if required_letter is None else 
    f"You must pick a celebrity that starts with '{required_letter}': "

if required_letter is None:
    player_name = input(prompt).strip().title()
    while player_name not in celebrity_names or len(player_name.split()) < 2:
        print("Not a valid celebrity name. Try Again!")
        player_name = get_valid_input(prompt, required_letter, used_names, celebrity_names)

used_names.add(player_name)
required_letter = get_required_letter(player_name)
print(f"Good Job! Next name must start with '{required_letter}'. \n")


print("Bot is thinking...")
bot_name = choose_valid_bot_name(required_letter, used_names, celebrity_names)

if bot_name is None:
    print(f"Bot has no valid name starting with '{required_letter}'."
    print("You Win! \n")
    break

used_names.add(bot_name)
required_letter = get_required_letter(bot_name)
print(f"Bot: '{bot_name}'")
print(f"Next name must start with '{required_letter}'. \n")


if not find_valid_names(required_letter, used_names, celebrity_names):
    print(f"No valid names left starting with '{required_letter}'.")
    print("Bot Wins! Better luck next time!")
    break


def play_vs_friend(celebrity_names):
    """ 
    Run a single game session between two human players. 

    Players alternate turns. The game ends when a player 
    cannot name a valid celebrity or gives up. 

    Args:
        celebrity_names (list[str]): The full celebrity list.

    """

    used_names = set()
    required_letter = None
    current_player = 1

print("Player 1 goes first! Enter any celebrity to start. \n")

while True:
    if required_letter is None:
        entry = input(f"Player {current_player}: ").strip().title()
        while entry not in celebrity_names or len(entry.split()) < 2:
            print("Not a valid celebrity name. Try again!")
            entry = input(f"Player {current_player}: ").strip().title()

    else:
        prompt = f"Player {current_player} your celeb must start with '{required_letter}': "
        entry = get_valid_input(prompt, required_letter, used_names, celebrity_names)

    used_names.add(entry)
    required_letter = get_required_letter(entry)
    print(f"Next name must start with '{required_letter}'. \n")


    next_player = 2 if current_player == 1 else 1

    if not find_valid_names(required_letter, used_names, celebrity_names):
        print(f"No valid names left starting with '{required_letter}'.") 
        print(f"Player {current_player} Wins! Player {next_player} has no valid names.")

        break

    current_player = next_player


def main():
    """
    Starting set-up of Celebrity Word Jab.

    Loads the celebrity list, lets the player choose a mode (vs bot; vs player),
    and runs the game loop. 

    """
    print("=" * 40)
    print("      CELEBRITY WORD JAB")
    print("=" * 40)
    print("Rules: Name a celebrity. The next player must name")
    print("another celebrity whose FIRST name start with the LAST")
    print("name's first letter of the previous.")
    print("Example: Michael JACKSON -> JANIS Joplin")
    print("=" * 40)

    while True:
        print("\n Choose a mode: ")
        print(" 1 - Play vs Bot")
        print(" 2 - Play vs Friend")
        print(" 3 - Quit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            play_vs_bot(celebrity_names)
        elif choice == "2":
            play_vs_friend(celebrity_names)
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
                                                     




                                                    








    





    
