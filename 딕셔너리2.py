dict2={"name":"hm","age":"29","phone":"010-2818-8632"}
print(dict2)
del dict2["age"]
print(dict2)
print(dict2["name"])
print(dict2.get("phone")) #위에 해당 요소 출력하는 문과 결과가 동일 시 하게 나옴! (.get()이라는 함수를 이용!)
print(dict2.values()) #{"key":"value"}값으로 dictionary는 이루어져 있는데, keys는 key값만 출력
for key,value in dict2.items():
    print(key,value)
#key in 딕셔너리명
    print("mh"in dict2)
    print(dict2.clear()) #dict2 요소를 전부 날리는 함수!
