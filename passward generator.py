# passward generator
import random
L = "abcdefghijklmnopqrstuvzxyz"
U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = "1234567890"
S = "*':;!?/)(+-&_£#@][✓%€¥$¢^°={}\×÷π√•|`~"
A = L+U+N+S
LN = 9
passward = "".join(random.sample(A, LN))
print("your passward is : ", passward)