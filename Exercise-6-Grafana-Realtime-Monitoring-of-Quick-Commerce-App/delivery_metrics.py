import random
import time
from prometheus_client import Gauge, Summary, start_http_server

# Delivery metrics
total_deliveries = Gauge(
    "total_deliveries",
    "Total number of deliveries"
)

pending_deliveries = Gauge(
    "pending_deliveries",
    "Number of pending deliveries"
)

on_the_way_deliveries = Gauge(
    "on_the_way_deliveries",
    "Number of deliveries on the way"
)

average_delivery_time = Summary(
    "average_delivery_time",
    "Delivery time in seconds"
)

def simulate_deliveries():
    while True:
        total = random.randint(50, 100)
        pending = random.randint(1, 15)
        on_the_way = max(0, total - pending)

        total_deliveries.set(total)
        pending_deliveries.set(pending)
        on_the_way_deliveries.set(on_the_way)

        delivery_time = random.uniform(10, 45)
        average_delivery_time.observe(delivery_time)

        print(
            f"Total: {total}, Pending: {pending}, "
            f"On the way: {on_the_way}, "
            f"Delivery time: {delivery_time:.2f}s",
            flush=True
        )

        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    print("Delivery metrics available on port 8000", flush=True)
    simulate_deliveries()
