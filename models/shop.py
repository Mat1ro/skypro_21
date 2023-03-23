from models.abstract import Storage


class Shop(Storage):
    def __init__(self, items: dict, capacity=20):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, quantity):
        if self.get_unique_items_count() < 5:
            if self.get_free_space() > quantity:
                if self.items.get(title) is None:
                    self.items[title] = quantity
                else:
                    self.items[title] += quantity
                print(f"Курьер везет {quantity} {title} со склада в магазин\n"
                      f"Курьер доставил {quantity} {title} в магазин")
            else:
                print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")
        else:
            print('В магазине недостаточно места для еще одного товара')

    def remove(self, title, quantity):
        if self.items.get(title) is not None:
            if self.items[title] - quantity > 0:
                print(f"Нужное количество есть в магазине\n"
                      f"Курьер забрал {quantity} {title} с магазина")
                self.items[title] -= quantity
            else:
                print('Не хватает товара на складе, попробуйте заказать меньше')
        else:
            print(f'{title} - нет на складе')

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        for k, v in self.items.items():
            print(k, v)

    def get_unique_items_count(self):
        return len(self.items.keys())
