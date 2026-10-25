Day 1 (Oct 8)
Made the MST tracker UI again from scratch, no AI. 4 sliders stored in
variables and a submit button. When you press submit it adds a row to
the csv using an f-string. Already knew f-strings.

Day 2 (Oct 9)
Worked on writing the header only once. Used os.path.exists to check if
the file is there. "w" creates the file, "a" adds to it. Added a
DateTime column. Got stuck because my else was lined up with the wrong
if, and I had too many "with open" blocks.

Day 3 (Oct 10)
Fixed all my typos (os not so, exists not exist, balloons).
Learned write() only takes one string, so I can't pass 2 things.
header is a list so I used ",".join(header) to turn it into a string.
Header check and row writing are 2 separate things. Header only if the
file is new, row every time.
Lost my code with git restore because I didn't commit. Rewrote it and it
works now. Commit when something works.

day 4 : i fixed some bugs like doing .mean() two time on line 42 to 45 to get accurate value
fixed stats varaible on line 24  