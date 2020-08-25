#Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

#For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

a="))()("
forw=0
back=0
for x in a:
	if(x==")"):
		back+=1
	else:
		forw+=1
while(back>forw):
	a+="("
	forw+=1
while(back<forw):
	a+=")"
	back+=1
#(())