def get_user_input():
    """
    Get players name, if its not there it gives us an error
    """
    player_name = input("Enter the player's last name to search: ").strip()
    if not player_name:
        raise ValueError("Player name cannot be empty.")
    return player_name
