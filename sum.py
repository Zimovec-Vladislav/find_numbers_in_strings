nums = "0123456789"
s = "s50x1x1xa1x25b54"
n = ""
summ = 0
war  = 0

for i in s:
    if i in nums:
        n += i

    if i == " " and n != "":
        summ += int(n)
        n = ""

    if (i not in nums) and (i != " ") and (n != ""):
        summ += int(n)
        n = ""
if n != "": summ += int(n)

print(summ)