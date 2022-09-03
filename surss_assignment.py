#Question 2
def piece_of_file(file_string,n):
    print(file_string[0:n-1])
    """for i in range(n):
        print(file_string[i])"""
#Question 3
def head_tail_list(string_list,n):
    print(f"\n\n the first {n} words of lsit\n")
    for i in range(n):
        print(string_list[i])
    print(f"\n\nthe last {n} words of lsit\n")
    for i in range(len(string_list)-1,len(string_list)-n-1,-1):
        print(string_list[i])
#Question 4
def word_counter(string_list,letters):
    print("\n\n The no of words in which each letter occurs")
    letter_counter={}
    for i in letters:
        cntr=0
        for j in string_list:
            if i in j:
                cntr+=1
        letter_counter[i]=cntr
        print(f"{i} : {cntr}")
    return letter_counter
 #Question 5   
def word_counter_multiple(string_list,letters):
    print("\n\n The no of words in which each letter occurs at multiple times")
    for i in letters:
        cntr=0
        for j in string_list:
            cntr2=0
            for k in j:
                if k==i:
                    cntr2+=1
                if cntr2>1:
                    cntr+=1
                    break
        print(f"{i} : {cntr}")
  #Question 6       
def word_counter_at_positions(string_list,letters,max_length):
    for i in letters:
        counter_dict={}
        for j in range(max_length):
            counter_dict[j]=0
        for j in string_list:
            for k in range(len(j)):
                if j[k]==i:
                    counter_dict[k]+=1
        print(f"\n The no of times the letter {i} occurs at each position")
        for j,k in counter_dict.items():
            print(f"at {j+1} : {k}" )



# 1 reading the csv file and printing the 1st 30 characters of string
Wordle_MysteryWords = open(r"C:\Users\vamsisai.garapati\Documents\Wordle_MysteryWords.csv", "r")
file_string=Wordle_MysteryWords.read()
print("Printing 1st 30 characters of string\n")
piece_of_file(file_string,30) 

# converting the string to list and printing 1st30 and last 20 words
string_list=file_string.split()
head_tail_list(string_list,20)

full_string=file_string.replace('\n','')
letters=set(full_string)
#printing the number of words in which each letter occurs
letter_counter= word_counter(string_list,letters)

# printing the number of words in which each letter occurs in multiple number
word_counter_multiple(string_list,letters)

#printing the number of times each letter occurs in each position in a word 
max_length=0
for i in string_list:
    length=len(i)
    if length>max_length:
        max_length=length
word_counter_at_positions(string_list,letters,max_length)

#Letters and count in order of their numbers of occurrence in the file – highest to lowest
sorted_list=sorted(letter_counter.items(), key=lambda val: val[1],reverse=True)

print("\nLetters and count in order of their numbers of occurrence in the file – highest to lowest\n")
for i in sorted_list:
    print(f"{i[0]} : {i[1]}\n")
