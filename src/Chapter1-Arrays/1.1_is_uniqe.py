# 1.1 Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you can't use additional data structure?


def check_is_unique_without_data_structure(string):
    """
    Time Complexity: O(1); Since we'll never iterate more than 128 chars
    Space Complexity: O(1); 
    """
    checker = 0
    for character in string:
        if checker & (1 << ord(character)):
            return False
        checker |= 1 << ord(character)
    return True


def is_unique(string):
    """
    Time Complexity: O(1); Since we'll never iterate more than 128 chars
    Space Complexity: O(1); Since we'll never store more than 128 chars 
    """
    if len(string) > 128:
        return False

    characters_dict = {}
    for character in string:
        if characters_dict.get(character):
            return False
        characters_dict[character] = True
    return True


if __name__ == "__main__":
    str1 = "missisippi"
    print(f"'{str1}' has all unique characters: {is_unique(str1)}")

    str2 = "no duplicates"
    print(f"'{str2}' has all unique characters: {is_unique(str2)}")


# Output:
#
# 'missisippi' has all unique characters: False
# 'no duplicates' has all unique characters: True
