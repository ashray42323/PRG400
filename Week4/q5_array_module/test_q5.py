import arraymodule

arraymodule.init(5)
arraymodule.set(0, 10)
arraymodule.set(1, 20)
print("0 ->", arraymodule.get(0))
print("1 ->", arraymodule.get(1))
arraymodule.free()
