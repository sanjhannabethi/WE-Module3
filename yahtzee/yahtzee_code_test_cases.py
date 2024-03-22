from collections import Counter

def is_large_straight(dice: list[int]) -> bool:
    return sorted(set(dice)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

def is_small_straight(dice: list[int]) -> bool:
    return any(sorted(set(dice[i : i + 4])) == list(range(min(dice[i : i + 4]), max(dice[i : i + 4])+1)) for i in range(len(dice)-3))

def score(dice: list[int]) -> dict[str, int]:
    score_card = {}

    # Calculate upper section scores
    for number in range(1, 7):
        score_card[f'{number}s'] = dice.count(number) * number

    # Calculate bonus for upper section
    upper_section_score = sum(score_card[f'{number}s'] for number in range(1, 7))
    if upper_section_score >= 63:
        score_card['Bonus'] = 35

    # Calculate lower section scores
    counts = Counter(dice)
    if len(counts) == 1:  # Yahtzee
        score_card['Yahtzee'] = 50
    else:
        score_card['Three of a kind'] = sum(dice) if any(count >= 3 for count in counts.values()) else 0
        score_card['Four of a kind'] = sum(dice) if any(count >= 4 for count in counts.values()) else 0
        score_card['Full house'] = 25 if len(counts) == 2 and 2 in counts.values() and 3 in counts.values() else 0
        score_card['Small straight'] = 30 if is_small_straight(dice) else 0
        score_card['Large straight'] = 40 if is_large_straight(dice) else 0
        score_card['Chance'] = sum(dice)

    return score_card

# Example usage:
dice = [1, 2, 3, 4, 5]
print(score(dice))

from collections import Counter
import random

def roll_dice(num_dice: int = 5) -> list[int]:
    """
    Simulate rolling a given number of dice.

    Parameters:
    - num_dice: The number of dice to roll. Default is 5.

    Returns:
    A list containing the results of rolling the dice.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]

def is_large_straight(dice: list[int]) -> bool:
    return sorted(set(dice)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

def is_small_straight(dice: list[int]) -> bool:
    return any(sorted(set(dice[i : i + 4])) == list(range(min(dice[i : i + 4]), max(dice[i : i + 4])+1)) for i in range(len(dice) - 3))

def get_score(dice: list[int]) -> dict[str, int]:
    score_card = {}

    # Calculate upper section scores
    for number in range(1, 7):
        score_card[f'{number}s'] = dice.count(number) * number

    # Calculate bonus for upper section
    upper_section_score = sum(score_card[f'{number}s'] for number in range(1, 7))
    if upper_section_score >= 63:
        score_card['Bonus'] = 35

    # Calculate lower section scores
    counts = Counter(dice)
    if len(counts) == 1:  # Yahtzee
        score_card['Yahtzee'] = 50
    else:
        score_card['Three of a kind'] = sum(dice) if any(count >= 3 for count in counts.values()) else 0
        score_card['Four of a kind'] = sum(dice) if any(count >= 4 for count in counts.values()) else 0
        score_card['Full house'] = 25 if len(counts) == 2 and 2 in counts.values() and 3 in counts.values() else 0
        score_card['Small straight'] = 30 if is_small_straight(dice) else 0
        score_card['Large straight'] = 40 if is_large_straight(dice) else 0
        score_card['Chance'] = sum(dice)

    return score_card

# Example usage:
rolled_dice = roll_dice()
print("Rolled dice:", rolled_dice)
print("Score:", get_score(rolled_dice))

def execute_tests():
    # Test Case 1: Basic Functionality
    dices = [1, 1, 1, 1, 1]
    assert score(dices)['Yahtzee'] == 50, "Incorrect score for Yahtzee"

    # Test Case 2: All Ones
    dice_ones = [1, 1, 1, 1, 1]
    assert score(dice_ones)['1s'] == 5, "Incorrect score for all ones"

    # Test Case 3: All Sixes
    dice_sixes = [6, 6, 6, 6, 6]
    assert score(dice_sixes)['6s'] == 30, "Incorrect score for all sixes"

    # Test Case 4: Full House
    dice_full_house = [2, 2, 3, 3, 3]
    assert score(dice_full_house)['Full house'] == 25, "Incorrect score for full house"

    # Test Case 5: Small Straight
    dice_small_straight = [1, 2, 3, 4, 6]
    assert score(dice_small_straight)['Small straight'] == 30, "Incorrect score for small straight"

    # Test Case 6: Large Straight
    dice_large_straight = [2, 3, 4, 5, 6]
    assert score(dice_large_straight)['Large straight'] == 40, "Incorrect score for large straight"

    # Test Case 7: Yahtzee
    dice_yahtzee = [3, 3, 3, 3, 3]
    assert score(dice_yahtzee)['Yahtzee'] == 50, "Incorrect score for yahtzee"

    # Test Case 8: Three of a Kind
    dice_three_of_a_kind = [3, 3, 3, 4, 5]
    assert score(dice_three_of_a_kind)['Three of a kind'] == 18, "Incorrect score for three of a kind"

    # Test Case 9: Four of a Kind
    dice_four_of_a_kind = [2, 2, 2, 2, 5]
    assert score(dice_four_of_a_kind)['Four of a kind'] == 13, "Incorrect score for four of a kind"

    # Test Case 10: Chance
    dice_chance = [1, 2, 3, 4, 5]
    assert score(dice_chance)['Chance'] == 15, "Incorrect score for chance"

    # Test Case 11: No Upper Section Bonus
    dice_no_bonus = [1, 2, 3, 4, 5]
    assert 'Bonus' not in score(dice_no_bonus), "Upper section bonus awarded incorrectly"

    # Add more test cases for the remaining scenarios...

    print("All test cases passed!")

# Execute the tests
execute_tests()
