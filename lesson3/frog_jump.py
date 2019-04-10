import math

def solution(current_location, destination, jump_distance):
    travel_distance = destination - current_location
    return math.ceil(travel_distance / jump_distance)
