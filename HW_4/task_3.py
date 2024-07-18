def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    ways = [0] * (n + 1)

    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


def main():
    try:
        n = int(input('Enter the number of steps: '))
        if n < 0:
            raise ValueError('The number of steps cannot be negative.')
        else:
            print('The number of ways to climb', n, 'steps is:', count_ways(n))

    except ValueError:
        print(f'Invalid input.')


main()
