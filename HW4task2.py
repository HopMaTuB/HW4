def get_cats_info(path):
    try:
        with open(path,"r") as file:
            cat = []
            for info in file:
                info = info.strip().split(",")
                cat.append({"id":info[0],"name":info[1],"age":info[2]})

    except FileNotFoundError:
        return f"File not found"
    except Exception as error:
        return f"{error}"
    
    return cat



                
