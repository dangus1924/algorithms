'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here 
    odd_ball = {}
    for i in arr:
        if i not in odd_ball:
            odd_ball[i] = 1
        else:
            odd_ball[i] += 1
    for num, amount in odd_ball.items():
        
        if amount == 1:
            return num
            
        
         
    

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")