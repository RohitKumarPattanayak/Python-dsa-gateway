## question
## 1) print the number of digits for a given number n

# attempt-1-start :
# number = input('enter the number : ')
# print(len(number))
# attempt-1-end : 

# Note
# 1) i have user 'augmented statements' here feel free to research
# - count+=1 is count = count + 1
# - number_cpy//=10 is number_cpy = number_cpy//10


# attempt-2-start :
number = int(input('enter the number : '))
number_cpy = number
count = 0 
while (number_cpy):
    count+=1
    number_cpy//=10
print(count)
# attempt-2-end : 

# Note Verdict and Comparison Notes
# -------------------------------------------------------------
# Attempt-1 (String-based)
# Pros:
# 1) Very simple and short.
# 2) Easy to read and write, no loops needed.
# Cons:
# 1) Not a true numeric approach — you’re counting characters, not digits.
# 2) Fails for negative numbers and whitespace.
# 3) In interviews, it’s often seen as avoiding the algorithmic logic.

# Attempt-2 (Mathematical approach using //)
# Pros:
# 1) True numeric logic — uses integer division and loops.
# 2) Works correctly for negatives (with abs()) and for zero.
# 3) Shows good understanding of loops, conditions, and augmented assignments.
# 4) Demonstrates algorithmic thinking, preferred in interviews.
# Cons:
# 1) Slightly longer code.
# 2) Requires careful handling for the zero case.

# Verdict:
# ✅ Attempt-2 is better for interviews and learning since it shows deeper understanding
#    of number manipulation and algorithmic logic.
# ⚡ Attempt-1 is fine for quick scripts but not ideal to demonstrate programming skills.
