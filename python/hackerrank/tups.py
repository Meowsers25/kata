def lets_do_this_shit(nums):
    input_list = nums.split()
    # input_list = [int(x) for x in input_list]
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    t = tuple(input_list)
    print(hash(t))

lets_do_this_shit('1 2 3 4')

# nums is a string entered with spaces
# need to convert to integers
# 4, 5 converts to ints
# 6 makes list a tuple
# 5 hashes it out
# function is called lets do this shit because I tried this in VIM
# and honestly, its shit :)

