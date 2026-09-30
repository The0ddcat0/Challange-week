def guess_flag(a):
    a = a.split(" ")    
    if a.isdigit(a[0]) and a.isdigit(a[1]):
        return True
    else:
        print("big balls by ac/dc")