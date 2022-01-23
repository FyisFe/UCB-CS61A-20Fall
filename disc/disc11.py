def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == "and":
            return eval_and(exp.rest)
        else:
            return calc_apply(calc_eval(exp, first), list(exp.rest.map(calc_eval)))
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:
        return exp


def eval_and(operands):
    curr, val = operands, True
    while curr is not nil:
        val = calc_eval(curr.first)
        if val is False:
            return False
        curr = curr.rest
    return val
