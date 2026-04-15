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