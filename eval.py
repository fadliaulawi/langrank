import math

gold = [3, 1, 0, 4, 2]
pred = [0, 4, 1, 2, 3]

dct = {gold[i]:pred[i] for i in range(5)}
#print(dct)
#raise Exception()

pred = [dct[k] for k in sorted(dct)]
gold = [i for i in range(4, -1, -1)]

print('Rel pred', pred)
print('Rel gold', gold)

def dcg(arr):
	sc = 0
	#print(arr)
	for i in arr:
		a = 2**i - 1
		#print(arr.index(3))
		b = math.log(arr.index(i) + 2, 2)
		#print(a, b)
		#print(a/b)
		sc += (a/b)

	return sc

print('dcg', dcg(pred))
print()
print('idcg', dcg(gold))
