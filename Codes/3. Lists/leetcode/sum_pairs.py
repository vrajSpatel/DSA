'''
Example:
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
'''
def pair_sum(q7, sum):
    # TODO
    pair=[]
    for i in range(len(q7)):
        for j in range(i+1,len(q7)):
            if q7[i]+q7[j]==sum:
                pair.append(f"{q7[i]}+{q7[j]}")
    return pair;

q7=[2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(pair_sum(q7,7))