def word_count(s):
    # Your code here
    my_table = {}
    if s == "":
        return my_table
    s = s.lower()
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('\t', ' ')
    false_values = '":;,.-+=/\|[]{}()*^&'
    filtered = ""
    
    for item in s:
        if item not in false_values:
            filtered += item

    filtered = filtered.split(' ')
    for word in filtered:
        if len(word) > 0:
            if my_table.get(word):
                my_table[word] += 1
            else:
                my_table[word] = 1

    return my_table

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))