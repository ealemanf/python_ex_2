# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

#The pattern for a regex should include
# r at the beginning to write in raw format
# \w to get letters, numbers and hyphen. 
# @ to get one @symbol
# \w{3,16} to check the length in the pre@ part and post @part
# \. to get a . character
# to make sure there are no more than three characters after the last dot. \w{2,3}
#use $ to avoid additional characters after the email

import re

def is_valid_email_address(email):
    return re.match('^[a-zA-Z0-9_.+-]{3,16}@[a-zA-Z0-9-]{2,16}\.[a-zA-Z0-9-.]{2,3}$', email)
    
email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]   

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":
    
    
    # validate each email from the list
    for e in email_list:
        match = re.search('^[a-zA-Z0-9_.+-]{3,16}@[a-zA-Z0-9-]{2,16}\.[a-zA-Z0-9-.]{2,3}$', e)
        if match != None:
            print("Correct format", e)
        else:
            print ("Incorrect Format", e)

#The list verification works. 
#The function, however, was not used and couldn't figure out how to do it. 
gave_up = False
attempts= 0

while attempts < 4:
    email = input("Enter your e-mail")
    attempts = attempts + 1
    valid = is_valid_email_address(email)
    if valid: 
        print(email, "is correct")
    else: 
        print("Invalid email, try again", email)
    if attempts >= 3:
        gave_up = True
        print("Sorry. All your attempts have been used up.")
        break





        
        


        
