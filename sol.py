class node:
    def _init_(s,i):
        s.value=i
        s.next=None
head=None
head=node(1)
temp=head
for i in range(2,100):
    temp.next=node(i)
    temp=temp.next
temp.next=node(100)
temp=temp.next
temp.next=head
temp=head
# while temp.next!=head:
#     print(temp.value)
#     temp=temp.next
# print(temp.value)
temp=head
while True:
    temp1=temp
    temp=temp.next
    temp1.next=temp.next
    temp=temp.next
    temp1=temp1.next
    if temp1.next==temp1:
        break
print("soldier with life is ",temp1.value)