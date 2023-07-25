"""A widget manufacturer is facing unexpectedly high demand for its new product,.
 They would like to satisfy as many customers as possible.
Given a number of widgets available and a list of customer orders, what is the maximum number of
 orders the manufacturer can fulfill in full?Function DescriptionComplete the function filledOrders
in the editor below. The function must return a single integer denoting the maximum possible number of
fulfilled orders.
filledOrders has the following parameter(s):
order : an array of integers listing the orders.
k : an integer denoting widgets available for shipment"""
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    order.sort()
    fulfilled_orders =0
    widgets_available=k
    for o in order:
        if o <= widgets_available:
            widgets_available = widgets_available-o
            fulfilled_orders =fulfilled_orders+1
        else:
            break
    return fulfilled_orders
            

if __name__ == '__main__':
   

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)

    print(result)
