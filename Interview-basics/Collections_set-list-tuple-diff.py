# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and changeable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable (IMMUTABLE). Duplicates OK. FASTER   -> can be used when there is a fixed collection required and also can be used as a dictionary keys

# RIGHT
customDict = {
    (1,2) : "rohit",
    (2,3) : "rohit 2"
}

# WRONG
# customDict = {
#     [1,2] : "rohit",
#     [2,3] : "rohit 2"
# }

print(customDict)