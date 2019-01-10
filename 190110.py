str_data = "james justine martine mary unix linux java cotline tomas script moonjaein"
submit=str_data.title()
submit_list =submit.split()
print(submit_list)

data_err = "jAMES jUSTINE mARTINE mARY uNIX lINUX jAVA cOTLINE tOMAS sCRIPT mOONJAEIN"
data=data_err.swapcase()
print(data)


data_f1 = {'a':"apple", 'b':"banana", 'c':'cherry'}
data_f2 = {'o':"orange", 'p':"pineapple"}
submit_result = {}
submit_result.update(data_f1)
submit_result.update(data_f2)
print(submit_result)