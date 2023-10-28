def double_stuff(a_list) : ## argument assigned to a_list

  new_list = [] ## initiate an empty list

  for value in a_list:

    new_list += [2* value] ## append an element

  return new_list ## return the new_list value (elements)



things = [1,2,3,4]



print("list things: ",things)



print("double_stuff returns: ", double_stuff(things))

other_things = [2,5, 'Spam', 9.5]

print(double_stuff(other_things))

[4,10, 'SpamSpam', 19.0]

other_things

[2,5, 'Spam', 9.5]


