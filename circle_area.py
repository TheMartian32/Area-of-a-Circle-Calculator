import math
from math import pi
from CommonUses import common_inputs

"""
This script calculates many things for circles. Many of which are circumference, area, perimeter, radius, and diameter.
Along with this, it uses the python math module and pi.
"""
##############################################################################################

ci = common_inputs
ci = ci.repeat_question()


class CalculatoinsAndInputs():

    def what_calc(self):
        """
        Asks the user what calculation they're going to be making.
        """

        # * While the inputed answer is not equal to the desired answer, it keeps asking the user for the calculation type.
        while True:
            result = ci.ask_for('\nWhat type of calculation are you making?: ',
                                'Not a supported calculation type.', str)

            if result == 'area of a circle':
                my_calc.area_of_circle()
                break

            if result == 'find radius' or 'circumference' or 'diameter':
                my_calc.circumference_radius_diameter()
                break

            else:
                print('Not currently supported calculation type.\n')


##############################################################################################


    def area_of_circle(self):
        """Returns the area of a circle with the given parameters.

        Returns:
            Float or int -- Returns a float or integer as a result of the calculation.
        """

        result = ci.ask_for('\nRadius, diameter or semicircle?: ',
                            'Not radius or diameter', str).lower()

        # * If radius is given, it calculates the area.

        if result == 'radius':

            # * user_input: Asks the user for the radius of the circle.
            user_input = float(
                input('\nWhat is the radius? (integers or decimals only) '))

            return print(f'\nThe area is {pi*user_input**2}')
        # * If the diameter is given, it calculates the area.
        if result == 'diameter':

            ask_for_diameter = float(input('\nWhat is the diameter? '))
            ask_for_diameter = ask_for_diameter/2
            return print(f'\nThe area is {pi*ask_for_diameter**2}')

        # * If the diameter is given ( which it then turns into radius ) it calculates the area of the semicircle.
        if result == 'semicircle':

            ask_for_diameter = float(input('\nWhat is the diameter? '))
            ask_for_diameter = ask_for_diameter/2
            calc = (pi*ask_for_diameter**2)/2
            return print(f'\nThe area of the semicircle is {calc}')

##############################################################################################

    def circumference_radius_diameter(self):
        """Using user provided parameters it calculates circumference, radius, or diameter

        Returns:
            float or int -- Returns the  circumference, radius, or diameter.
        """
        # * Asks for the radius, circumference
        result = ci.ask_for('\nRadius, circumference, or diameter?: ',
                            'Thats not supported', str).lower()

        # * Asks the user for the diameter
        if result == 'radius':

            diameter = float(input('What is the diameter?: '))
            return print(f'\nThe radius is {diameter/2}')

        # * Asks the user for the diameter
        if result == 'diameter':
            radius = float(input('What is the radius?: '))
            return print(f'\nThe diameter is {radius*2}')

        # * Asks the user for the diameter
        if result == 'circumference':
            circumference = float(input('What is the diameter?: '))
            return print(f'The circumference of the circle is {pi*circumference}')


##############################################################################################
my_calc = CalculatoinsAndInputs()


if __name__ == '__main__':
    my_calc.what_calc()

    repeat = ''
    while repeat != 'y' and 'n':
        # * Asks to repeat the script.
        repeat = input(
            '\nWould you like to repeat the program? (Y/N): ').lower()
        if repeat[0] == 'y':
            my_calc.what_calc()
            continue
        if repeat[0] == 'n':
            break
