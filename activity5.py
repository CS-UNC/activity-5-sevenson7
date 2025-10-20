# words_file = open('CROSSWD.txt','r')

# print(type(words_file))

# data = [1, 3, 2, 8, 5, 6, 10]

# print([2*x for x in data if x%2 ==0])

# while True:
#     print(words_file.readline())

# for line in words_file:
#     print(line)

# words = []
# for line in words_file:
#     print(line.strip())

file = open('CROSSWD.txt','r')

def twenty_or_more(file):
    file = open(file,'r')
    print([x.strip() for x in file if len(x.strip()) > 20])
   
result = twenty_or_more('CROSSWD.txt')   
        
def has_no_e(word):
    # word = open(word,'r')
    # for x in word:
    if "e" in word:
        return False
    else:
        return True
    
print(has_no_e('loud'))

def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
    return True

