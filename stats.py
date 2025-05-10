def count_words(content: str):
    words = content.split()
    return len(words)

def count_characters(content: str):
    # start = round(time.time() * 1000)
    counts = {}

    # My version
    # avg time: 20 ms

    # content = content.lower()
    # unique_content = ''.join(set(content))
    # for char in unique_content:
    #     counts[char] = content.count(char)
    
    # Boot.dev version
    # avg time: 40 ms
    for c in content:
        lowered = c.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1

    # end = round(time.time() * 1000)
    # diff = end - start
    # print(diff)

    return counts

def sort_characters(chars):
    libs = []

    def sort_on(dict):
        return dict["num"]

    for char in chars:
        libs.append({'char': char, 'num': chars[char]})

    libs.sort(reverse=True, key=sort_on)

    return libs