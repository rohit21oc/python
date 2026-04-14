lists = [15,25,69,58,69,15,1,2,5,15,36,15]
result = []

high_occur_elem = 0;
high_occur = 0;

for num in lists:
    if num not in result:
        result.append(num)

for num in result:
    c = lists.count(num)
    if c>high_occur:
        high_occur = c
        high_occur_elem = num
    print(f"{num} is occure {c} times")
print(high_occur_elem)
print(high_occur)
    
