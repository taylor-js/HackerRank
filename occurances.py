def occurances(words):
    hashmap = {}
    for elem in words:
        hashmap.update({ elem:words.count(elem) })
    return hashmap.values()


arr = ["bcdef","abcdefg","bcde","bcdef"]
print(occurances(arr))