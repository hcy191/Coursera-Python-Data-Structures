#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = list()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        time = line[5]
        hours.append(time[0:2])
#print hours

counts = dict()

for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1 

#print counts

s = sorted([(k,v) for k,v in counts.items()])

#print s

for k,v in s:
    print k,v
