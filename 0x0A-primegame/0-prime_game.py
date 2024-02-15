#!/usr/bin/python3

"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    function that determines who is the winner
    """
    def sieve(n):
        """
        function that determines the prime numbers
        """
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return primes

    def winner(n):
        """
        function that returns wo is winner
        """
        if n == 1:
            return "Ben"
        primes = sieve(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    ben_wins = 0
    maria_wins = 0
    for n in nums:
        if winner(n) == "Ben":
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
