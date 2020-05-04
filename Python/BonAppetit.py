def bonAppetit(bill,k,bcharged):
    total = sum(bill)
    bactual = (total - bill[k]) // 2
    if bcharged - bactual == 0:
        print("Bon Appetit")
    else:
        print(bcharged - bactual)
        

items = [3, 10, 2, 9]
bonAppetit(items,1,12) # 5
bonAppetit(items,1,7) # bon apetit
