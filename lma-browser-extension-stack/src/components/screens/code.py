import collections
nums1 = [2,4]
nums2 = [6,5,4,3,2,7]
st = []

next_great = collections.defaultdict(lambda x :-1)
for i in nums2:
    while st and st[-1] < i:
        next_great[st.pop()] = i
        
    st.append(i)
    
    
prev= float('-inf')
while st:
    cur = st.pop()
    if prev > cur:
        next_great[cur] = prev
    else:
        next_great[cur] = -1
        
    prev =  max(prev , cur)
     
    
ans = []

for i in range(0 , len(nums1)):
    ans.append(next_great[nums1[i]])
    
    
print(ans)
    