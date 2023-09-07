#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the maximum number for each round.

    Returns:
        str or None: The name of the player that won the most rounds or None if it's a tie.
    """

    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    # Calculate prime numbers using the Sieve of Eratosthenes algorithm
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Count the number of prime numbers less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the winner based on the number of wins
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
