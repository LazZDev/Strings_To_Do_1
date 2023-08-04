# Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks.
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".


def remove_blanks(string):
    return "".join(string.split())


input1 = " Pl ayTha tF u nkyM usi c "
result1 = remove_blanks(input1)
print(result1)

# Get Digits
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.


def get_digits(string):
    return int("".join(filter(str.isdigit, string)))


input2 = "0s1a3y5w7h9a2t4?6!8?0"
result2 = get_digits(input2)
print(result2)

# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW".
# Given "Live from New York, it's Saturday Night!", return "LFNYISN".


def get_acronym(string):
    return "".join(word[0].upper() for word in string.split())


input3_1 = " there's no free lunch - gotta pay yer way. "
result3_1 = get_acronym(input3_1)
print(result3_1)

input3_2 = "Live from New York, it's Saturday Night!"
result3_2 = get_acronym(input3_2)
print(result3_2)

# Zip Arrays into Dictionary
# Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.


def zip_arrays_into_dictionary(arr1, arr2):
    return dict(zip(arr1, arr2))


arr1 = ["abc", 3, "yo"]
arr2 = [42, "wassup", True]
result4 = zip_arrays_into_dictionary(arr1, arr2)
print(result4)

# Invert Hash
# Dictionaries are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys.
# Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.


def invert_hash(assoc_dict):
    return {value: key for key, value in assoc_dict.items()}


assoc_dict = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
result5 = invert_hash(assoc_dict)
print(result5)
