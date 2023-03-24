file = open('./main/answer.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))
if(len(per_word)>10):
    print("greater than 10")
else:
    print("less than 10")


