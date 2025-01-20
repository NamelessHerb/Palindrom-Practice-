"""
125. Valid Palindrome

Given a string text, return true if it is a palindrome, or false otherwise.

For this question, letters are NOT case-sensitive, for example, "LEVeL" is a palindrome.
"""
# Change this function so it works correctly

def run_test():
  test_cases = [('level', True),
              ('LEVeL', True),
              ('levy', False),
              ('rotor', True),
              ('motor', False),
              ('No lemon no melon', True),
              ('No No', False),
              ('2025202', True),
              ('100P', False),
              ('Do geese see God', True)]
  for test_text, expected in test_cases:
      result = is_palindrome(test_text)
      msg = 'Correct' if expected == result else 'Wrong'
      print(f'[{msg:7s}] is_palindrome("{test_text}") should be {expected}')

def is_palindrome(message):
  message = message.replace(' ', '')
  message = message.upper()
  Keynum = len(message)

  if Keynum % 2 == 0:
      Key = int(Keynum / 2)
  else:
      Key = int((Keynum - 1) / 2)

  needlist = []

  for i in range(Key):
      needlist.append(message[i])

  yeslist = needlist[::-1]

  if Keynum % 2 == 0:
      Round = Key
  else:
      Round = Key + 1

  Check = []

  for i in range(Round, Keynum):
      Check.append(message[i])

  if Check == yeslist:
      return True

  else:
      return False

run_test()