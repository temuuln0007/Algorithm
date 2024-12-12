def decodeHuff(root, s):
    i = 0
    node = root
    res = ""
    while i < len(s):
        while node.data == chr(0):
            if s[i] == '0':
                assert node.left
                node = node.left
            else:
                assert node.right
                node = node.right
            i += 1
        res += node.data
        node = root
    print(res)