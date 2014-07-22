from Queue import Queue


def evaluate_rpn(tokens):
  stk = []

  while not tokens.empty():
    token = tokens.get()

    if is_operand(token):
      stk.append(token)
    else:
      val0, val1 = stk.pop(), stk.pop()
      num = eval(val1 + token + val0)
      stk.append(str(num))

  return stk.pop()

def infix_to_rpn(expression):

  # The Shunting Yard algorithm by Dr. Dijkstra himself
  stk = []
  queue = Queue()
  tokens = expression.replace(" ", "") 

  for token in tokens:
    if is_operand(token):
      queue.put(token)
    elif is_operator(token):
      token_preced = get_preced(token)
      while stk and is_operator(stk[-1]) and get_preced(stk[-1]) > token_preced:
        queue.put(stk.pop())
      stk.append(token)
    elif token == '(':
      stk.append(token)
    elif token == ')':
      while stk[-1] != '(':
        queue.put(stk.pop())
      stk.pop()
   
  while stk:
   queue.put(stk.pop())
  return queue

def is_operand(token):
  return token.isdigit()

def is_operator(token):
  return token in '+-*/'

def get_preced(token):
  if not is_operator(token):
    return TypeError('Token is not an operator!')

  precedences = {'+': 0,
                 '-': 0,
                 '*': 1,
                 '/': 1}
 
  return precedences[token]
