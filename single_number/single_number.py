'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    odd_ball = []
    while arr:
        if len(arr) == 1:
            odd_ball.append(arr[0])
            arr.pop(0)
            return odd_ball
        elif arr[0] == arr[1]:
            arr.pop(0)
            arr.pop(0)
        
        elif arr[0] != arr[1]:
            odd_ball.append(arr[0])
            arr.pop(0)
        

    
        
         
    return odd_ball
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")