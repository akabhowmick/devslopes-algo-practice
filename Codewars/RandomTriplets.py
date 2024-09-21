# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

# As a simplification, you may assume that no letter occurs more than once in the secret string.

# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

from collections import defaultdict, deque


def recover_secret(triplets):
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    for triplet in triplets:
        for i in range(len(triplet)):
            if triplet[i] not in in_degree:
                in_degree[triplet[i]] = 0

        for i in range(len(triplet) - 1):
            if triplet[i + 1] not in graph[triplet[i]]:
                graph[triplet[i]].add(triplet[i + 1])
                in_degree[triplet[i + 1]] += 1

    queue = deque()
    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char)

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(result)


# Graph: Shows how letters are ordered based on the triplets.
# In-Degree: Counts how many letters come before each letter.
# Queue: Helps to process letters in the correct order, starting with those that can be added first.
