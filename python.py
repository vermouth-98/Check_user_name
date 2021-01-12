current_name = ['admin','long','hai','huong','minh']
new_name= ['Hai', 'Cuong','Huong','SUONG']
if new_name and current_name:
    for value_new_name in new_name:
        if value_new_name.lower() in current_name:
            print(" Enter a new username please!"+ value_new_name)
        else:
            current_name.append(value_new_name.lower())
print(current_name)