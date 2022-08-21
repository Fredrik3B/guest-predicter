# Input: 1. Mengde rein i m.m., 2. CAF scoren
# Output: 1-100, hvor 1 er dårlig, og 100 er bra.

def rainFunction(rainAmount): # 0.88m.m. = 1 poeng || 0m.m. = 10 poeng
    try: 
        if rainAmount <= 0.88 and rainAmount >= 0:
            score = -40.7925407925407*rainAmount**4 + 12.2377622377621*rainAmount**3 + 28.1468531468532*rainAmount**2 - 20.5244755244755*rainAmount + 10
            return score
        elif rainAmount < 0:
            print("\nError: rainAmount cannot be less than 0\n")
        elif rainAmount > 0.88:
            return 1
        else:
            print("\nSomething went wrong!\n")

    except:
        print("\nPlease make sure that an integer is being passed in.\n")

def cloudFunction(caf): # caf = cloud area fraction (0-100) 
    try:
        if caf < 100 and caf >= 0:
            score = 0.000000212704*caf**4 - 0.0000433760684*caf**3 + 0.0018307109557*caf**2 - 0.052433954934*caf + 10
            if score > 10:
                return 10
            elif score < 1:
                return 1
            else:
                return score
        elif caf == 100:
            return 1
        elif caf > 100:
            print("\nThe CAF score cannot be larger than 100\n")
        elif caf < 0:
            print("\nThe CAF score cannot be smaller than 0\n") 
        else:
            print("\nSomething went wrong!\n")
    except:
        print("\nError, try passing in an integer between 0-100\n")

def scoreFunction(rainAmount, caf):
    rainScore = rainAmount*1.5
    cafScore = caf*0.5
    try:
        x = isinstance(rainAmount, (float, int))
        y = isinstance(caf, (float, int))
        if x == True and y == True:
            score = rainFunction(rainScore) * cloudFunction(cafScore)
            if score > 100 or score < 1:
                print("\nNikolai, you fool!\n")
            else:
                return score
        else:
            print("\nError, you are not passing in integers\n")
    except:
        print("\nSomething went wrong!\n")


