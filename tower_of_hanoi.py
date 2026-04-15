def hanoi_solver(disk):
    my_source = list(range(disk,0,-1))
    my_inter = []
    my_dest = [] 
    result = []
    result.append(f"{my_source.copy()} {my_inter.copy()} {my_dest.copy()}")
    def rec_helper(disk_num,source,inter,dest):            
        if disk_num == 0:
            return
        rec_helper(disk_num-1,source,dest,inter)
        moving = source.pop()
        dest.append(moving)
        result.append(f"{my_source.copy()} {my_inter.copy()} {my_dest.copy()}")
        rec_helper(disk_num-1,inter,source,dest)
        
        
    rec_helper(disk,my_source,my_inter,my_dest)
    return "\n".join(result)
print(hanoi_solver(3))