class learnings:

    ''' 
    This math method have 2 variables (num1 and num2) that contains integer 
    number and returns the big number between the 2 integer numbers.
      '''
    @staticmethod
    def math():
        num1 = 4
        num2 = 7
        print("check the biggest number between " + str(num1) + " and " + str(num2))
        big =  num1 if (num1 >= num2) else num2
        print("The biggest number is : " +  str(big))
        return big

    '''
    This user_input method at first print texts (enter a positive number) and takes the input 
    from the user which must be an integer number and check if it is positive,nuetral or negative
    and prints a message to tell the user what the number is and after returns True if the number
    is positive else returns false.
    '''
    @staticmethod
    def user_input():
        correct_answer = False
        print("enter a positive number")
        num= int(input())
        if num == 0:
            print(str(num) + " is neutral number")
        elif num > 0:
            print(str(num) + " is a positive number")
            correct_answer = True
        else:
            print(str(num) + " is a negative number")
        return correct_answer

'''
This condition below tells python to execute only if run as a script and this help us when
we are importing learnings class in test_work.py file for making test because this 
codes under our condition will not be executed  which is also not a part of our test
'''
if __name__ == "__main__":
    print("--------------first task-----------------")
    learnings.math()
    print("--------------second task----------------")
    learnings.user_input()
