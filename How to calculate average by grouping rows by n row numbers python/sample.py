import statistics

a = [1,2,3,4,5,6,7,8,9,10]
windowsize = 5
c = []

split_data = (a[i:i+windowsize] for i in range(0,len(a),windowsize))


for i in split_data:
    c.append(statistics.mean(i))
print(c)



