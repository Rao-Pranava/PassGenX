import itertools
import argparse

def load_usernames(filename):
    """Loads usernames from a file."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def generate_passwords(usernames, common_patterns):
    """Generates passwords based on usernames and common patterns."""
    passwords = set()
    
    for username in usernames:
        for pattern in common_patterns:
            passwords.add(f"{username}{pattern}")
            passwords.add(f"{pattern}{username}")
    
    return passwords

def save_passwords(passwords, output_file):
    """Saves the generated passwords to a file."""
    with open(output_file, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    print(f"[+] Password list saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a wordlist by appending common prefixes and suffixes to usernames.")
    parser.add_argument("-i", "--input", required=True, help="Path to the username file.")
    parser.add_argument("-o", "--output", default="CustomPassword.txt", help="Output file for generated passwords (default: CustomPassword.txt)")
    args = parser.parse_args()
    
    usernames = load_usernames(args.input)
    if not usernames:
        print("No usernames loaded. Exiting...")
        return
    
    common_patterns = [
        "@123", "1234!", "2024", "007", "@password", "@pass", "pass@", "99", "1999", "2000", "2023", "!", "@!", "admin", "root",
        "password", "qwerty", "abcd", "123456", "hello", "world", "secure", "access", "test", "demo", "welcome", "love", "star",
        "moon", "sun", "earth", "sky", "king", "queen", "hero", "champ", "master", "ninja", "dragon", "gamer", "hacker", "shadow",
        "thunder", "storm", "light", "dark", "ghost", "fire", "water", "wind", "tiger", "lion", "wolf", "eagle", "falcon", "knight",
        "legend", "warrior", "super", "mega", "ultra", "pro", "elite", "vip", "god", "power", "magic", "phoenix", "snake", "venom",
        "spider", "batman", "superman", "ironman", "thor", "flash", "joker", "nintendo", "playstation", "xbox", "steam", "epic",
        "gta", "fifa", "valorant", "fortnite", "csgo", "dota", "league", "pubg", "minecraft", "roblox", "amongus", "overwatch",
        "apex", "halo", "callofduty", "warzone", "battlefield", "zelda", "mario", "metroid", "cyberpunk", "witcher", "starwars",
        "harrypotter", "lotr", "avengers", "deadpool", "matrix", "joker", "jedi", "sith", "darth", "vader", "yoda", "gandalf",
        "frodo", "sam", "spock", "kirk", "skywalker", "mando", "boba", "drake", "taylor", "kanye", "eminem", "rickroll", "rick",
        "morty", "strangerthings", "squidgame", "anime", "naruto", "sasuke", "onepiece", "luffy", "dragonball", "goku", "vegeta",
        "kakarot", "trunks", "akira", "deathnote", "light", "ryuk", "demon", "nezuko", "zenitsu", "tanjiro", "slayer", "animefan",
        "otaku", "pokemon", "pikachu", "charizard", "eevee", "snorlax", "yugioh", "kaiba", "joey", "magician", "exodia", "mewtwo",
        "red", "blue", "silver", "gold", "platinum", "ruby", "sapphire", "emerald", "diamond", "pearl", "black", "white", "x", "y",
        "sun", "moon", "sword", "shield"
    ]
    
    passwords = generate_passwords(usernames, common_patterns)
    save_passwords(passwords, args.output)
    
if __name__ == "__main__":
    main()
