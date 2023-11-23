# fruits = ["mango", "banana", "apple", "grapes", "staberry", "kiwi"]

# ['mango', 'banana', 'apple', 'grapes', 'staberry', 'kiwi']
# >>> fruits.append('apple')

# ['mango', 'banana', 'apple', 'grapes', 'staberry', 'kiwi', 'apple']
# >>> fruits.append('orange')

# ['mango', 'banana', 'apple', 'grapes', 'staberry', 'kiwi', 'apple', 'orange']
# >>> fruits = ["mango", "banana", "apple", "grapes", "staberry", "kiwi"]

# ['mango', 'banana', 'apple', 'grapes', 'staberry', 'kiwi']
# >>> fruits.append('orange')

# ['mango', 'banana', 'apple', 'grapes', 'staberry', 'kiwi', 'orange']
# >>> fruits.insert(2,'goava')

# ['mango', 'banana', 'goava', 'apple', 'grapes', 'staberry', 'kiwi', 'orange']
# >>> fruits.insert(9,'goava')

# ['mango', 'banana', 'goava', 'apple', 'grapes', 'staberry', 'kiwi', 'orange', 'goava']
# >>> l1 = [14,"fsd"]
# >>> l2 = [54,"dfdfdf",478,true]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> l1 [1,7,8]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list indices must be integers or slices, not tuple
# >>> l2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'l2' is not defined. Did you mean: 'l1'?
# >>>
# >>>
# >>> l1=[1,7,8]
# >>> l2=[5,8,3,'hf',true]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> l1+l2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'l2' is not defined. Did you mean: 'l1'?
# >>>
# >>>
# >>> l1=[1,7,8]
# >>> l2=[5,8,3,'hf',True]
# >>> l1+l2
# [1, 7, 8, 5, 8, 3, 'hf', True]
# >>> l1=[1,7,8]
# >>> l2=[5,8,3,'hf',true]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> l1=[1,7,8]
# >>> l2=[5,8,3,'hf',True]
# >>> l1+l2
# [1, 7, 8, 5, 8, 3, 'hf', True]
# >>> del fruits[1]
# >>> fruits
# ['mango', 'goava', 'apple', 'grapes', 'staberry', 'kiwi', 'orange', 'goava']
# >>> fruits.pop(goava)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'goava' is not defined
# >>> fruits.pop()
# 'goava'
# >>> fruits
# ['mango', 'goava', 'apple', 'grapes', 'staberry', 'kiwi', 'orange']
# >>> fruits.pop(1)
# 'goava'
# >>> fruits.remove('a

obj = {1, "de" , True, "fdsfds"}
print(obj)

arr = [1,2,3,4,5, 'de' , False, {'gh', 1}, [1,2,True]]
print(arr)