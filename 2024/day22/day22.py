from math import floor


def process_input(filename):
    secrets = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            secrets.append(int(line.strip()))
    return secrets


def mix_and_prune(secret, num):
    return (secret ^ num) % 16777216


def calculate_next_secret(num):
    num = mix_and_prune(num, num * 64)
    num = mix_and_prune(num, floor(num / 32))
    num = mix_and_prune(num, (num * 2048))
    return num


def get_nth_secret(secret, n):
    for x in range(n):
        secret = calculate_next_secret(secret)
    return secret


def get_secret_totals(secrets, n):
    total = 0
    for secret in secrets:
        total += get_nth_secret(secret, n)
    return total


input_secrets = process_input('input.txt')
print(f'Part 1: {get_secret_totals(input_secrets, 2000)}')