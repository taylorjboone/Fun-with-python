# a little text editor to use in powershell

print "What file would you like to view?"
answer = raw_input("> ")

def open_file(f):
  f.read(open(f))
  
open_file(answer)
close(answer)
