
# Solution 1 - (Direct Approach) (Time Complexity O(n^2) and Space Complexity O(n))
def isPalindromesol1(string):
    # Write your code here.
    if string == string[::-1]:
        return True
    return False


# Solution 2 - (Direct Approach) (Time Complexity O(n^2) and Space Complexity O(n))
def isPalindromesol2(string):
    # Write your code here.
    stringreverse = ""
    for i in reversed(range(len(string))):
        stringreverse += string[i]
    return string == stringreverse


# Solution 3 - (Direct Approach) (Time Complexity O(n) and Space Complexity O(n))
def isPalindromesol3(string):
    # Write your code here.
    stringreversearray = []
    for i in reversed(range(len(string))):
        stringreversearray.append(string[i])
    return string == "".join(stringreversearray)


# Solution 4 - (Recursive Algorithm Approach) (Time Complexity O(n) and Space Complexity O(n))
def isPalindromesol4(string, index=0):
    # Write your code here.
    backwardindex = len(string) - 1 - index
    return True if index >= backwardindex else string[index] == string[backwardindex] and isPalindromesol4(string, index + 1)


# Solution 5 - (Comparison using pointer approach) (Time Complexity O(n) and Space Complexity O(1))
# Most Efficient Solution
def isPalindromesol5(string):
    # Write your code here.
    leftindex = 0
    rightindex = len(string) - 1
    while leftindex < rightindex:
        if string[leftindex] != string[rightindex]:
            return False
        leftindex += 1
        rightindex -= 1
    else:
        return True


if __name__ == '__main__':
    text = input('Enter a string to check for Palindrome:')
    print(isPalindromesol1(text))
    print(isPalindromesol2(text))
    print(isPalindromesol3(text))
    print(isPalindromesol4(text))
    print(isPalindromesol5(text))
