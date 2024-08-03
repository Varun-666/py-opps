def isBalance(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '[', '>': '<'}

    for char in s:
        if char in '({[<':
            stack.append(char)
        elif char in ')}]>':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

test_string = "(){[<>]}"
if isBalance(test_string):
    print(f"'{test_string}' is balanced.")
else:
    print(f"'{test_string}' is not balanced.")
