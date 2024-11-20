# Task 1

class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items

    def __repr__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self.items})"

class OrderQueue:
    def __init__(self):
        self.queue = []  # Using a list to implement the queue

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order {order.order_id} added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("No orders to process.")
            return None
        order = self.queue.pop(0)
        print(f"Processing order {order.order_id}.")
        return order

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            print("No orders to peek.")
            return None
        return self.queue[0]

    def display(self):
        print("Current order queue:")
        for order in self.queue:
            print(order)

# Example usage:
order_queue = OrderQueue()
order1 = Order(1, "Alice", ["Burger", "Fries"])
order2 = Order(2, "Bob", ["Pizza", "Soda"])
order3 = Order(3, "Charlie", ["Salad", "Water"])

# Enqueue orders
order_queue.enqueue(order1)
order_queue.enqueue(order2)
order_queue.enqueue(order3)

# Display the queue
order_queue.display()

# Dequeue an order and process
order_queue.dequeue()

# Display the queue again
order_queue.display()