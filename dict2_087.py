dict={"key1":10,"key2":5,"key3":8,"key4":3,"key5":7}
print("sorted dictionary:")
print(sorted(dict.items(), key =lambda kv:(kv[1], kv[0])))  
