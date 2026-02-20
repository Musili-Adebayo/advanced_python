# Task
# From temperatures = [30,22,35,19,40], print those above average.

temperatures = [30,22,35,19,40]
average = sum(temperatures) / len(temperatures)
for temp in temperatures:
    if temp > average:
        print(temp)
        