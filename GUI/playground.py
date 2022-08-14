if __name__ == '__main__':
    a = {"abc": [{"a":1, "b":2}, {"a":2, "b":2}, {"a":3, "b":2}]}

    for object in a["abc"]:
        object["b"] = "Once"
    print(a)

    a["abc"][1]["b"] = "Twice"
    print(a)

    object = a["abc"][1]
    object["b"] = "Three"
    print(a,object)