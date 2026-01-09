def calculate_net_revenue(price, quantity, transport_cost, storage_loss_rate):
    gross = price * quantity
    loss = gross * storage_loss_rate
    net = gross - transport_cost - loss
    return net
