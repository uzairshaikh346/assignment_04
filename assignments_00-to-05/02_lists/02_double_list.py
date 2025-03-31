def double_number(list):
   double_number_list = []
   for i in list:
      double_number_list.append(i*2)

   return double_number_list


list = [2,3,4,5]
result = double_number(list)

print(result)