while True:
    try:
        no_of_item = int(input("enter the no of items to be sent "))
        if no_of_item > 0:
            break
        else:
            print(" enter a number greater than 0 ")
    except ValueError:
        print(" enter a number not a string ")

item_number = 0
item_wight = 0
max_total_weight = 20
max_item_wight = 10
min_item_weight = 1
current_pacakge_weight = 0
total_weight = 0
package_count = 0
most_unused_capacity = -1

for item_number in range (1, no_of_item):
    try:
        item_wight = int(input(f" enter the weight of item number {item_number}, weight should be from 1 to 10 or 0 to stop "))
    except ValueError:
        print(" please enter a number not string ")
        continue

    if item_wight == 0:
        print(" enter a nuber greater than 0 ")
        break

    elif item_wight < min_item_weight or item_wight > max_item_wight:
        print("pls enter between 1 to 10 ")
        continue

    if current_pacakge_weight + item_wight > max_total_weight:
        unused = max_total_weight - current_pacakge_weight
        print(f"package {package_count + 1} sent with {current_pacakge_weight} and unused is {unused} ")

        if unused > most_unused_capacity:
            most_unused_capacity = unused
            most_unused_capacity = package_count +1

        total_weight += current_pacakge_weight
        package_count += 1
        current_pacakge_weight = item_wight
    else:
        current_pacakge_weight += item_wight

if current_pacakge_weight > 0:
    unused = max_total_weight - current_pacakge_weight
    print(f" package {package_count + 1 } sent with {current_pacakge_weight}, unused is {unused}")

    if unused > most_unused_capacity:
        most_unused_capacity = unused
        most_unused_capacity = package_count + 1

    total_weight += current_pacakge_weight
    package_count += 1

total_unused = package_count * max_total_weight - total_weight

print(f" no of package sent = {package_count}")
print(f" total weight of package sent = {total_weight}")
print(f"total unused capacity = {total_unused}")
print(f"package with most unused capacity = {most_unused_capacity}")