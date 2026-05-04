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








    





    
