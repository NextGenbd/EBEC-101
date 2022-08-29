"""
Author: Majharul hoque, hoque2@purdue.edu
Assignment: 00.1 - Hello User
Date: 08/29/2022

Description:
    Write a program that ask the user for their name, and then displays a greeting using their name.
    Test your program with the following data:
        Input                   Output
        spam                Hello spam!
        King Arthur         Hello King Arthur!
        Tim the Enchanter   Hello Tim the Enchanter!
Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():

    Name = input("What is your name? ")
    print("Hello ",Name,end='!\n')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
