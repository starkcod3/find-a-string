def count_substring(string, sub_string):
    sum = 0
    m = len(string)-(len(sub_string)-1)
    for i in range(m):
        if string.count(sub_string,i,i+len(sub_string)):
            sum = sum + 1
    return sum