def alphabeta(node, is_max=True, alpha=float('-inf'), beta=float('inf')):
    if node and not node.children:
        return (node.val, [node])
    elif is_max:
        # Can always fall back on alpha. This is the lower bound score
        for child in node.children:
            score, path = minimax(child, False, alpha, beta)
            # Prune here. A grandparent would not go down this path since beta
            # is lower than score. That is, it already knows a path that's better
            # than anything in this subtree.
            if score > beta:
                return (score, path + [node])
            elif score > alpha:
                alpha = score
                best_path = path + [node]

        return (alpha, best_path)

    else: # Minimizer
        for child in node.children:
            # Can always fall back on beta. This is the upper bound score
            score, path = minimax(child, True, alpha, beta)
            # Prune here. A grandparent would not go down this path since alpha
            # is higher than score.
            if alpha > score:
                return (score, path + [node])
            elif score < beta:
                beta = score
                best_path = path + [node]
        return (beta, best_path)
