#!/usr/bin/python3

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    # To keep track of number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Find the maximum n in nums to compute primes up to that number
    max_n = max(nums)
    
    # Sieve of Eratosthenes to determine all prime numbers up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False
    
    # List of prime numbers up to max_n
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Game simulation for each n in nums
    for n in nums:
        # Keep track of available numbers
        available = set(range(1, n + 1))
        turn = 0  # Maria's turn if 0, Ben's turn if 1
        
        while True:
            move_made = False
            
            # Find the first prime that is in the available set
            for prime in primes:
                if prime in available:
                    move_made = True
                    # Remove the prime and all its multiples
                    multiples = set(range(prime, n + 1, prime))
                    available -= multiples
                    break
            
            if not move_made:
                # No move can be made, the current player loses
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            # Switch turns
            turn = 1 - turn
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
