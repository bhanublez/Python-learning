def combine_lists(list1, list2):
    combined_list = []  # Initialize an empty list variable
    list1.reverse()  # Reverse the order of "list1"
    combined_list = list2 + list1  # Combine the two lists
    return combined_list 
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
