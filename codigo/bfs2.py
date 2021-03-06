# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:57:22 2020

@author: Fernando
"""

from collections import deque

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

def shortest_path(g, start, end):
    paths = {None: []}
    for parent, child in bfs(g, start):
        paths[child] = paths[parent] + [child]
        if child == end:
            return paths[child]
    return None # or raise appropriate exception

if __name__ == '__main__':
    # a sample graph
    graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F', 'D'],
             'F': ['C']}