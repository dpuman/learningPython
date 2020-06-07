from collections import deque
que = deque([])
que.append(1)
que.append(2)
que.append(30)

print(que)

que.popleft()
print(que)
if not que:
    print("Disable")
