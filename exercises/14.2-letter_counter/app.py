par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for x in par:
    if x != " ":
        if str(x.lower()) in counts.keys():
            counts[str(x.lower())] += 1
        else:
            counts[str(x.lower())] = 1

print(counts)

