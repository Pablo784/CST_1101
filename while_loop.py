## ## ## SECTION ONE - INITIALIZATION ## ## ##



## Initialize Variables with Default Values

range_end = 11   ## end the range before this index position

range_start = 0   ## index position of start of range

range_step = 1   ## amount to step through range index values

i = 0        ## current value of index position

x = 0        ## value of element at current index position

response = ''    ## empty list in response variable for input statements 

x = range_start





## ## ## SECTION TWO - EXAMPLE ## ## ##

while x < range_end:

  print("The value of x is: ", x, " at loop iteration ", i,".")

  i += 1

  x += range_step 
