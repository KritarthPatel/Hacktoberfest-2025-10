def is_self_dividing(x: int) -> bool:
    """Check if a number is self-dividing (no zero digits, divisible by each digit)."""
    original = x
    while x > 0:
        digit = x % 10
        if digit == 0 or original % digit != 0:
            return False
        x //= 10
    return True

# Read input
n = int(input().strip())

# Collect self-dividing numbers
result = [i for i in range(1, n + 1) if is_self_dividing(i)]

# Print output
if result:
    print(" ".join(map(str, result)))
else:
    print(-1)
