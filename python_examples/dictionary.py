users = {
    'emrullah' : {
        'age' : 25,
        'roles' : ['admin'],
        'surname' : 'polat',
        'dogumyeri' : 'malatya',
        'tel_number' : '5551864406'
    },
    'harun' : {
        'age' : 27,
        'roles' : ['admin','user'],
        'surname' : 'kayabaşı',
        'dogumyeri' : 'ağrı',
        'tel_number' : '5468005844'
    }
}
print(users['emrullah']['roles'])

#listeleri eşleştirip dict elde etme
list1 = ['a','b','c','d','e']
list2 = [1,2,3,4,5]
list3 = ['ankara','istanbul','antalya','elazığ','konya']
rehber = list(zip(list1, list2, list3))
print(rehber)

