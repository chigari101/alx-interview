#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = [0]
    while queue:
        curr_box = queue.pop(0)
        keys = boxes[curr_box]
        for key in keys:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

