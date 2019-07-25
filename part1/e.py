s = input()
import json
struct = json.loads(s)

count_dict = 0
count_list = 0

def clean_struct(struct):
    global count_dict, count_list
    if isinstance(struct, list):
        index = 0
        while index < len(struct):
            value = struct[index]
            struct[index] = clean_struct(value)
            if struct[index] == None:
                del struct[index]
            else:
                index += 1
        if len(struct) == 0:
            count_list += 1
            return None
        
    if isinstance(struct, dict):
        for key, value in list(struct.items()):
            struct[key] = clean_struct(value)
            if struct[key] == None:
                del struct[key]
        if len(struct) == 0:
            count_dict += 1
            return None
    return struct
clean_struct(struct)

print(count_dict, count_list)