from itertools import permutations
def print_permutations(string):
    print(f"All permutations: {string}")
    for per in permutations(string):
        print(''.join(per))
user=input()
print_permutations(user)