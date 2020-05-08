#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    ht = {}

    for ticket in tickets:
        ht[ticket.source] = ticket.destination

    current_city = ht['NONE']

    while current_city != 'NONE':
        route.append(current_city)
        current_city = ht[current_city]

    route.append('NONE')  # Because the automated tests are dumb.
    return route
