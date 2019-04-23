# Created by: Chris Asante
# Created on: 16-April-2019
# Created for: ICS3U
# 6-03
# This program allows the user to input their mailing address information and returns it back to them in 
# the proper format.

from enum import Enum

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type , city_name, province_initials, postal_code):
        
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code

a_mailing_address = MailAddress(input("First Name: "), input("Last Name: "), input("Address number: "), input("Street Name: "), input("Street Type: "), input("City Name: "), input("Province (initials): "), input("Postal Code: "))

print("\n" + a_mailing_address.first_name + " " + a_mailing_address.last_name + "\n" + a_mailing_address.house_number + " " + a_mailing_address.street_name + " " + a_mailing_address.street_type + "\n" + a_mailing_address.city_name + ", " + a_mailing_address.province_initials + " " + a_mailing_address.postal_code + "\n")
