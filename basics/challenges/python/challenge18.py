import sys

class Solution:
    stack = []
    queues = []
    def pushCharacter(self,i):
        self.stack.append(i)
    def enqueueCharacter(self,i):
        self.queues.append(i)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queues.pop(0)

s=input()
obj=Solution()   
l=len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    