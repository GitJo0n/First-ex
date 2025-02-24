import time

def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

my_bag = []

start = time.time()

insert(my_bag, '휴대폰')
insert(my_bag, '지갑')
insert(my_bag, '손수건')
insert(my_bag, '빗')

end = time.time()
print('실행시간:', end - start)
# print('가방속의 물건:', my_bag)

""" insert(my_bag, '빗')
remove(my_bag, '손수건')

print('가방속의 물건:', my_bag) """

