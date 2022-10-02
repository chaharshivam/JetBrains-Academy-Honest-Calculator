dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence_list = input().split()
found = False
for word in sentence_list:
    if word in dictionary:
        continue
    else:
        found = True
        print(word)
if not found:
    print("OK")
