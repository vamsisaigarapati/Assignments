import os

directory_name = "C://Users//vgara1//PycharmProjects//untitled//peakss"
stop_words=["not", "the", "are", "to", "in", "of", "at", "when", "each", "every", "all", "a", "on", "you", "can"]
stop_words_index={}
stop_words_rep={}
for word in stop_words:
    stop_words_rep[word]=0
    stop_words_index[word]={}
for filename in os.listdir(directory_name):
    f = os.path.join(directory_name, filename)
    if os.path.isfile(f):
        f = open(f, mode='r', encoding='utf-8')
        content=f.readline().split()
        for word in stop_words:
            # word=stop_words[i]
            for i in range(len(content)):
                if word==content[i]:
                    stop_words_rep[word] =stop_words_rep[word]+1
                    if stop_words_index[word].get(filename):
                        stop_words_index[word][filename].append(str(i+1))
                    else:
                        stop_words_index[word][filename]=[str(i+1)]
for word in stop_words:
    print(f"The word \"{word}\" repeated \"{stop_words_rep[word]}\" no of times in all files")
    if stop_words_rep[word]!=0:
        print(f"The word \"{word}\" occured at the mentioned place in the sentence- given file wise")
        for file,rep in stop_words_index[word].items():
            places=",".join(rep)
            print(f"{file} :{places}")
    print("\n\n")

