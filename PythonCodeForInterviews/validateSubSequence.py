def isValidSubsequenceFor(array, sequence):
    # Write your code here.
    seq_idx = 0
    for i in array:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx] == i:
            seq_idx += 1
    return seq_idx == len(sequence)


if __name__ == "__main__":
    given_array = [3, 1, 8, 5, -1, 4, 6]
    given_seq = [1, 5, 6]
    print(isValidSubsequenceFor(given_array, given_seq))





















# def isValidSubsequenceWhile(array, sequence):
#     # Write your code here.
#     arr_idx = 0
#     seq_idx = 0
#     while all((arr_idx < len(array), seq_idx < len(sequence))):
#         if array[arr_idx] == sequence[seq_idx]:
#             seq_idx += 1
#         arr_idx += 1
#     return seq_idx == len(sequence)

#
#
#
#
#
    # print(isValidSubsequenceWhile(given_array, given_seq))