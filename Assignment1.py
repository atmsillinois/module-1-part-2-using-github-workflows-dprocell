# Assignment 1
# Dara Procell
# August 29, 2025

'''
Takes user inputs, uses a function to calculate something, 
and prints the inputs and outputs to the screen.  Make sure your 
code is formatted according to PEP 8, and documented using PEP 257.
Every time you attempt to run the program or make a series of edits, 
commit your changes to GitHub with descriptive commit messages.  
For full credit, create at least one branch.  Add new functionality, 
commit, test, and then create a pull request and add it to your main 
branch. Add an open source software license.
'''


def calculate_dnf_runners(total_starters, total_finishers):
    """
    Calculate the number of runners who did not finish UTMB.
    
    Args:
        total_starters (int): Total number of runners who started the race
        total_finishers (int): Total number of runners who finished the race
    
    Returns:
        int: Number of runners who did not finish (DNF)
    
    Raises:
        ValueError: If finishers exceed starters or if values are negative
    """
    if total_starters < 0 or total_finishers < 0:
        raise ValueError("Number of runners cannot be negative")
    
    if total_finishers > total_starters:
        raise ValueError("Finishers cannot exceed total starters")
    
    return total_starters - total_finishers


def calculate_dnf_percentage(dnf_count, total_starters):
    """
    Calculate the DNF percentage.
    
    Args:
        dnf_count (int): Number of runners who did not finish
        total_starters (int): Total number of runners who started
    
    Returns:
        float: DNF percentage rounded to 2 decimal places
    """
    if total_starters == 0:
        return 0.0
    
    return round((dnf_count / total_starters) * 100, 2)


def get_user_input():
    """
    Get race statistics from user input.
    
    Returns:
        tuple: (total_starters, total_finishers) as integers
    """
    print("UTMB 2024 DNF Calculator")
    print("=" * 25)
    
    while True:
        try:
            total_starters = int(input("Enter total number of starters: "))
            total_finishers = int(input("Enter total number of finishers: "))
            return total_starters, total_finishers
        except ValueError:
            print("Please enter valid integers only.\n")


def main():
    """
    Main function to run the UTMB 2024 DNF calculator.
    """
    try:
        # Get user inputs
        starters, finishers = get_user_input()
        
        # Calculate DNF statistics
        dnf_count = calculate_dnf_runners(starters, finishers)
        dnf_percentage = calculate_dnf_percentage(dnf_count, starters)
        
        # Display results
        print("UTMB Race Results Summary:")
        print(f"Total starters:     {starters:,}")
        print(f"Total finishers:    {finishers:,}")
        print(f"Did not finish:     {dnf_count:,}")
        print(f"DNF percentage:     {dnf_percentage}%")
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please run the program again with valid inputs.")


if __name__ == "__main__":
    main()