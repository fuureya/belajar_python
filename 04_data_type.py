age = 17
salary = 5000.00

print(type(age))
print(type(salary))


#type daya primitif 

#integer, float, complex

#type data collection

#list 
variabel_list = [1, "Dicoding", True, 1.0]
print(type(variabel_list))

print(variabel_list[0])

variabel_list[0] = "Berubah"
print(variabel_list[0])

# slicing

print(variabel_list[0:2])


#tuple
#merupakan jenis dari list yang tidak dapat di ubah element nya. umumnya tuple di gunakan untuk data yang bersifat sekali deklarasi dan dapat di eksekusi lebih cepat. tuple di definisikan dengan kurung () dan setiap elemen di dalam nya di pisah dengan koma.

x = (1, "dicoding", 1+3)
print(type(x))

#contoh tidak dapat di ubah 
# x[0] = "berubah"