# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:00:13 2023

@author: KIIT
"""

class Spacecraft:
    def __init__(self, initial_coordinates, initial_direction):
        self.coordinates = initial_coordinates
        self.direction = initial_direction

    def move_forward(self):
        if self.direction == "N":
            self.coordinates[1] += 1
        elif self.direction == "S":
            self.coordinates[1] -= 1
        elif self.direction == "E":
            self.coordinates[0] += 1
        elif self.direction == "W":
            self.coordinates[0] -= 1
        elif self.direction == "Up":
            self.coordinates[2] += 1
        elif self.direction == "Down":
            self.coordinates[2] -= 1

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

    def angle_change_up(self):
        if self.direction == "Up":
            return
        self.direction = "Up"

    def angle_change_down(self):
        if self.direction == "Down":
            return
        self.direction = "Down"

    def execute_commands(self, command_list):
        for command in command_list:
            if command == "f":
                self.move_forward()
            elif command == "b":
                pass
            elif command == "l":
                self.turn_left()
            elif command == "r":
                self.turn_right()
            elif command == "u":
                self.angle_change_up()
            elif command == "d":
                self.angle_change_down()

import unittest

class TestSpacecraft(unittest.TestCase):
    def test_move_forward_N(self):
        sc = Spacecraft([0, 0, 0], "N")
        sc.move_forward()
        self.assertEqual(sc.coordinates, [0, 1, 0])

    def test_turn_left_N(self):
        sc = Spacecraft([0, 0, 0], "N")
        sc.turn_left()
        self.assertEqual(sc.direction, "W")

if __name__ == '__main__':
    unittest.main()

    # User input
    initial_x = int(input("Enter initial x-coordinate: "))
    initial_y = int(input("Enter initial y-coordinate: "))
    initial_z = int(input("Enter initial z-coordinate: "))
    initial_direction = input("Enter initial direction (N/S/E/W/Up/Down): ").capitalize()
    command_str = input("Enter commands (e.g., 'frubl'): ")
    command_list = list(command_str)

    chandrayaan = Spacecraft([initial_x, initial_y, initial_z], initial_direction)
    chandrayaan.execute_commands(command_list)

    print("Final Coordinates:", chandrayaan.coordinates)
    print("Final Direction:", chandrayaan.direction)
    
# if __name__ == '__main__':
#     unittest.main()

#     # User input
#     initial_x = int(input("Enter initial x-coordinate: "))
#     initial_y = int(input("Enter initial y-coordinate: "))
#     initial_z = int(input("Enter initial z-coordinate: "))
#     initial_direction = input("Enter initial direction (N/S/E/W/Up/Down): ").capitalize()
#     command_str = input("Enter commands (e.g., 'frubl'): ")
#     command_list = list(command_str)

#     chandrayaan = Spacecraft([initial_x, initial_y, initial_z], initial_direction)
#     chandrayaan.execute_commands(command_list)

#     print("Final Coordinates:", chandrayaan.coords)
#     print("Final Direction:", chandrayaan.direction)

