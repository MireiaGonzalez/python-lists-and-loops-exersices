theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wiki_woko(num):
    if num == 0:
        return "woko"
    else:
        return "wiki"


wiki_woko_list = list(map(wiki_woko, theBools))
print(wiki_woko_list)


