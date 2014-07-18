class Pizza(object):
    def __init__(self):
        self._price = None
    def get_price(self):
        return self._price
class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 8.5
class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 15.5
class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5
        
if __name__ == '__main__':
    for pizza_class in (HamAndMushroomPizza, DeluxePizza, HawaiianPizza):
        print 'Price of {0} is {1}' \
             .format(pizza_class.__name__, pizza_class().get_price())
