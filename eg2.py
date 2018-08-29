chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz., "

string = "It was a bright cold day in April,and the clocks were striking thirteen."

for char in chars:
  count = string.count(char)
  if count > 0:
    print (char, count)
    count = {}
for s in string:
  if count[s]:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] > 0:
    print (key, count[key])
