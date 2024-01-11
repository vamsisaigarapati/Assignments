def balancedOrNot(expressions, max_replacements):
    results = []

    for i in range(len(expressions)):
        expression = expressions[i]
        max_replacement = max_replacements[i]

        result = is_balanced(expression, max_replacement)
        results.append(result)

    return results

def is_balanced(expression, max_replacements):
    open_count = 0

    for char in expression:
        if char == '<':
            open_count += 1
        elif char == '>':
            if open_count > 0:
                open_count -= 1
            elif max_replacements > 0:
                max_replacements -= 1
            else:
                return False

    return open_count == 0
