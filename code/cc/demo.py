count = 0
while True:
    count += 1
    if (count % 100000000) == 0:
        print(count, end='\r')