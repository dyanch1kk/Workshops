def sort_stack(stack):
    temp_stack_stack = []
    while stack:
        tmp = stack.pop()
        while temp_stack and temp_stack[-1] < tmp:
            stack.append(temp_stack.pop())
        temp_stack.append(tmp)
    while temp_stack:
        stack.append(temp_stack.pop())
    return stack

stack = [5, 3, 1, 4, 2]
print(sort_stack(stack)) 