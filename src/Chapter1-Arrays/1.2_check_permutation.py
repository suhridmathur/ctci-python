# 1.2 Check Permutation: Given two strings, write a method to decide if
# one is a permutation of the other. Assume white spaces ARE significant and
# all characters are in lowercase.


def is_permutation(first, second):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    length_first = len(first)
    length_second = len(second)

    if length_first != length_second:
        return False

    char_map = {}
    for character in first:
        if char_map.get(character):
            char_map[character] += 1
        else:
            char_map[character] = 1

    for character in second:
        if not char_map.get(character):
            return False
        char_map[character] -= 1
    return True


if __name__ == "__main__":
    string1 = "tac"
    string2 = "cat"
    string3 = "sat"

    print(
        f"'{string1}' is permutation of '{string2}': {is_permutation(string1, string2)}"
    )
    print(
        f"'{string3}' is permutation of '{string2}': {is_permutation(string3, string2)}"
    )

# Output:
# 'tac' is permutation of cat: True
# 'sat' is permutation of cat: False
