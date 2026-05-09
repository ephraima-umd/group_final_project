from problem3 import find_valid_names
from problem4 import choose_valid_bot_name


class Player:
    """
    Represent a player in CelebrityWordJab.

    Primary Author: Ephraim Alemayehu
    """

    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1


def load_celebrities(filepath="celebrities.txt"):
    """
    Load celebrity names from a text file.

    Primary Author: Jamie Rivera
    Techniques Demonstrated: with statements
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def get_required_letter(name):
    """
    Return the first letter of the celebrity's last name.

    Primary Author: Ephraim Alemayehu
    """
    return name.strip().split()[-1][0].upper()


def get_valid_input(player, required_letter, used_names, celebrity_names):
    """
    Prompt a player until they enter a valid celebrity name.

    Primary Author: Bryton Joachim
    """
    while True:
        if required_letter is None:
            prompt = f"{player.name}, enter any celebrity: "
        else:
            prompt = f"{player.name}, enter a celebrity starting with {required_letter}: "

        entry = input(prompt).strip().title()

        if entry not in celebrity_names:
            print("That celebrity is not in the list. Try again.")
        elif entry in used_names:
            print("That celebrity has already been used. Try again.")
        elif len(entry.split()) < 2:
            print("Enter a first and last name.")
        elif required_letter is not None and entry.split()[0][0].upper() != required_letter:
            print(f"The first name must start with {required_letter}.")
        else:
            return entry


def play_game(celebrity_names, vs_bot=False):
    """
    Run one game of CelebrityWordJab.

    Primary Author: Ephraim Alemayehu
    """
    players = [Player("Player 1"), Player("Bot" if vs_bot else "Player 2")]
    used_names = set()
    required_letter = None
    current = 0

    while True:
        player = players[current]

        if vs_bot and player.name == "Bot":
            entry = choose_valid_bot_name(required_letter, used_names, celebrity_names)

            if entry is None:
                print("Bot has no valid move. Player 1 wins!")
                break

            print(f"Bot chooses: {entry}")
        else:
            entry = get_valid_input(player, required_letter, used_names, celebrity_names)

        used_names.add(entry)
        player.add_point()
        required_letter = get_required_letter(entry)

        print(f"Next name must start with {required_letter}.")
        print(f"Score: {players[0].name}: {players[0].score} | {players[1].name}: {players[1].score}\n")

        current = 1 - current

        if not find_valid_names(required_letter, used_names, celebrity_names):
            print(f"{players[current].name} has no valid move.")
            print(f"{players[1 - current].name} wins!")
            break


def main():
    """
    Start CelebrityWordJab.

    Primary Author: Bryton Joachim
    """
    celebrity_names = load_celebrities()

    print("CELEBRITY WORD JAB")
    print("The next celebrity's first name must start with")
    print("the first letter of the previous celebrity's last name.\n")

    while True:
        print("1 - Play vs Bot")
        print("2 - Play vs Friend")
        print("3 - Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            play_game(celebrity_names, vs_bot=True)
        elif choice == "2":
            play_game(celebrity_names, vs_bot=False)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
