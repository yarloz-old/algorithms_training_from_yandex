import sys


def main():
    purchases = {}
    for line in sys.stdin:
        customer, item, quantity = line.split()
        quantity = int(quantity)
        if customer in purchases:
            if item in purchases[customer]:
                purchases[customer][item] += quantity
            else:
                purchases[customer][item] = quantity
        else:
            purchases[customer] = {}
            purchases[customer][item] = quantity
    purchases = {customer: {item: purchases[customer][item] for item in sorted(purchases[customer])}
                 for customer in sorted(purchases)}
    for customer in purchases:
        print(customer + ":")
        for item, quality in purchases[customer].items():
            print(item, quality)


if __name__ == "__main__":
    main()