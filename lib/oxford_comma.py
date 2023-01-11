def oxford_comma(items):
   
    # if len(items) == 1:
    #     return "".join(items)
    # elif len(items) == 2:
    #   return  " and ".join(items)
    # elif len(items) == 3:
    #     sen = []
    #     for i, val in items:
    #         while i != 2:
    #             sentence = f"{val}, "
    #             sen.append(sentence)
    #         sent = f"and {val}"
    #         sen.append(sent)
    #     return sen  
    
    if len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return "{}, and {}".format(", ".join(items[:-1]), items[-1])  
            

# Resource used: https://stackoverflow.com/questions/19838976/grammatical-list-join-in-python
        

    
