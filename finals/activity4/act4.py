#1 
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    
    finalvalue = 0.0
    
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
            
        else:
            finalvalue += item.profit * W / item.weight
            break
        
    return finalvalue

if __name__ == "__main__":
    W = 10
    arr = [Item(10, 3), Item(15, 3), Item(10, 2), Item(12, 5), Item(8, 1)]

    max_val = fractionalKnapsack(W, arr)
    print(f"The maximum profit is: {max_val}")