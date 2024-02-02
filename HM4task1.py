def total_salary(path):
    try:
        with open(path, 'r') as file:
            lst = []
            for line in file:
                line = line.strip().split(",")
                lst.append(int(line[1]))
            total = sum(lst)
            average = total//len(lst)
            return total, average
    
   
    except FileNotFoundError:
        return f"File not found"
    except Exception as error:
        return f"{error}"
    

# total,average = total_salary("salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average} ")



