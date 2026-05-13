# nums = [12,75,85,64,15,72]
# print(nums[0])
# print(nums[0:3])
# print(nums[-1])  #Negative indexing [-5,-4,-3,-2,-1]
# print(nums[-5])

# names = ['Nitesh' , 'satyam' , 'suraj']
# print(names)

# values = [9.5 , 'Nitesh' , 25] # different datatypes 
# print(values)
# print(values[1])

# mil = [values ,names]
# print(mil)

numbers = [1,2,3,4,5]
numbers.append(6)  #lists are mutable 
print(numbers)
numbers.insert(6,7)
print(numbers)
numbers.remove(7)
print(numbers)
numbers.pop()
print(numbers)
numbers.extend([6,7,8,9])
print(numbers)
print(min(numbers) , max(numbers) , sum(numbers))