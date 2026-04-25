def avg_fuc(lists):
    total = 0;
    for num in lists:
        total +=num
    print(f"sum of Total number is: {total}")
    avg = total / len(lists)
    print(f"Average of the list is {avg}")

avg_fuc([10,12,14,16,18,20])
avg_fuc([10654,12645,65414,5416,65418,20651])