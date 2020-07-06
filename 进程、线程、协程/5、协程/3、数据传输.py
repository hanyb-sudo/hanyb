

def run():
    #空变量，存储的作用data始终为空
    data = ""
    r = yield data
    print(1, r, data+"*")
    r = yield data
    print(2, r, data+"*")
    r = yield data
    print(3, r, data+"*")
    yield data


m = run()
print("*********")
print(m.send(None))
m.send("han")
print("*********")