from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict={}
    for x in word:
        if(x) not in my_dict:
            my_dict[x] = 1
        else:
            my_dict[x]+=1
    return my_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
