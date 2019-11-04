#print("hello world!")

#print(3/2)

names=['okr', 'ssy', 'wudis', 'ijyed']
print(names)
#访问最后一个元素
print(names[-1].upper())
#尾部插入
names.append('zzy')
print(names)

#指定位置插入元素
names.insert(2, 'ccf')
print(names)

#删除元素，后续的列表前移
del names[1]
print(names)

#类似于队列，弹出尾部元素
last_name = names.pop()
print(last_name)
print(names)

#弹出特定位置元素
any_name = names.pop(2)
print(any_name)
print(names)

#删除特定的值
remove_value = names.remove('ccf')
print(remove_value) #None
print(names)

#删除不存在的值，会报错，ValueError: list.remove(x): x not in list
#none_value = names.remove('idf')
#print(none_value)
print(names)


# 排序
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lixiang', 'aux']
# cars.sort()
print(cars)

cars.reverse()

print(cars)
# 临时排序
print(sorted(cars, reverse=True))

print(len(cars))

empty_list = []
print(len(empty_list))
# 非列表调用len方法
# a = 1
#print(len(a))

# 遍历数组
print('遍历列表')
numbers = [11,23,87,90,21,46]
total = 0
for num in numbers:
	total+=num
# 遍历的临时变量居然在后面还可以使用，也是神奇
print(num)
print(total)










