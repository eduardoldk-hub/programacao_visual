#auxiliado pelo Miqueias, colega de sala.


product = 1
values_list = []


while True:
    values = int(input("Produto {0}: " .format(product)))
    if values == 0:
        break
    values_list.append(values)

    product += 1





total = sum(values_list)
print("Total: R${0}" .format(total))
payment = int(input("Dinheiro: R$"))
print("Troco: R$%d" % (payment - total))    