import os

def clear_screen():
    """Clears the terminal screen to maintain secret bids."""
    # Works for both Windows ('nt') and macOS/Linux ('posix')
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bids_dict: dict):
    """Calculates and displays the highest bidder from the collected bids."""
    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bids_dict.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    clear_screen()
    print("=" * 40)
    print(f"  🏆 THE WINNER IS {winner.upper()} WITH A BID OF ${highest_bid:,.2f}! 🏆")
    print("=" * 40)


def main():
    bids = {}
    auction_active = True

    print("=" * 40)
    print("       WELCOME TO THE SILENT AUCTION       ")
    print("=" * 40)

    while auction_active:
        name = input("\nWhat is your name? ").strip()
        
        while not name:
            name = input("Name cannot be empty. Please enter your name: ").strip()

        # Validate numerical input for bid amount
        while True:
            try:
                bid = float(input("What is your bid? $"))
                if bid <= 0:
                    print("Bid amount must be greater than $0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical amount (e.g., 50 or 12.50).")

        # Save bidder and bid to dictionary
        bids[name] = bid

        # Check for more bidders
        while True:
            should_continue = input("\nAre there any other bidders? (yes/no): ").strip().lower()
            if should_continue in ['yes', 'y']:
                clear_screen()
                break
            elif should_continue in ['no', 'n']:
                auction_active = False
                break
            else:
                print("Please answer 'yes' or 'no'.")

    if bids:
        find_highest_bidder(bids)


if __name__ == "__main__":
    main()