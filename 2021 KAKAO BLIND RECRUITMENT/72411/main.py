import collections
from itertools import combinations

def solution(orders, course):
    orders_list = []
    for size in course:
        order_menus = []
        for order in orders:
            order_menus += combinations(sorted(order), size)
        most_ordered = collections.Counter(order_menus).most_common()
        orders_list += [ most for most, count in most_ordered if count > 1 and count == most_ordered[0][1] ]
    return [ ''.join(order) for order in sorted(orders_list) ]
