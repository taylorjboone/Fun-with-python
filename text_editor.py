# a little text editor to use in powershell

print "What file would you like to view?"
answer = raw_input("> ")

rs = open(answer)
print rs.read()
rs.close()
