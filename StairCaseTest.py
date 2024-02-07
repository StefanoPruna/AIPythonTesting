def is_staircase(nums):
    col_length = 0
    staircase = []
    nums = []

#nums isn't an array, but staircase is
    while len(nums) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(nums.pop(0))

            if (len(nums) == 0):
                if i < col_length - 1:
                    return False
                return staircase
        staircase.append(column)
 
     
print(is_staircase(10))

def is_staircase(nums):
    col_length = 0
    staircase = []
    input_list = [5]
    nums = [5]
    input_list = nums.copy()

    while len(input_list) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(input_list.pop(0))

            if (len(input_list) == 0):
                if i < col_length - 1:
                    return False
                staircase.append(column)
                return staircase
        staircase.append(column)

print(is_staircase(5))