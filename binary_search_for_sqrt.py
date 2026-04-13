def square_root_bisection(num,tol=1e-4,max_iteration=50):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif num==0 or num==1:
        print(f"The square root of {num} is {num}")
        return num
    
    else:
        low = 0
        high = 1 if num < 1 else num
        iteration = 0
        while high - low>= tol and iteration <= max_iteration:
            mid = (low + high) / 2
            mid_squared = mid * mid
            iteration += 1
            print(low,mid,mid_squared,high)
            if mid_squared < num:
                low = mid
                print('l')
            elif mid_squared > num:
                high = mid
                print('g')
            elif mid_squared == num:
                print(f"The square root of {num} is approximately {mid}")
                return mid
        if iteration > max_iteration:
            print(f"Failed to converge within {max_iteration} iterations")
            return None
            
        factor = 1/tol
        value = (low + high) / 2
        square_root = round(value*factor)/factor
        print(f"The square root of {num} is approximately {square_root}")
        return square_root
                
            

    
print(square_root_bisection(0.25, 1e-7, 50))
