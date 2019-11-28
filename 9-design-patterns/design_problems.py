################################################
# Design Stack Overflow
################################################

# Question, Comment, Answer 

# Account: guest, member, admin, moderator

# Badge, Tag, Bounty 


class QuestionStatus(Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1,2,3,4

class QuestionClosingRemark(Enum):
    DUPLICATE, OFF_TOPIC, TOO_BROAD = 1,2,3

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1,2,3,4,5


class Account:
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.Active):
        self._id = id 
        self._password = password 
        self._name = name
        self._address = address
        self._email = email 
        self._phone = phone 
        self._status = status 
        self._reputation = 0 

    def reset_password(self):
        pass 

class Member: 
    def __init__(self, account):
        self._account = account 
        self._badges = []

    def get_reputation(self):
        return self._account.get_reputation()
    
    def get_email(self):
        return self._account.get_email()
    
    def create_question(self, question):
        pass 

    def create_tag(self, tag):
        pass 

class Admin(Member):
    def block_member(self, member):
        pass 

    def unblock_member(self, member):
        pass 

class Moderator(Member):
    def close_question(self, question):
        pass 

    def undelete_question(self, question):
        pass 


class Badge:
    def __init__(self, name, description):
        self._name = name 
        self._description = description 
    
class Tag: 
    def __init__(self, name, description):
        self._name = name 
        self._description = description 
        self._daily_asked_frequency = 0 
        self._weekly_asked_frequency = 0 

class Notification: 
    def __init__(self, id, content):
        self._notification_id = id 
        self._created_on = datetime.datetime.now()
        self._content = content 
    
    def send_notification(self):
        None 
    

class Photo: 
    def __init__(self, id, path, member):
        self._photo_id = id 
        self._photo_path = path 
        self._creation_date = datetime.datetime.now()
        self._creating_member = member 
    
    def delete(self):
        pass 

class Bounty: 
    def __init__(self, reputation, expiry):
        self._reputation = reputation 
        self._expiry = expiry 
    
    def modify_reputation(self, reputation):
        pass 


from abc import ABC, abstractmethod 

class Search(ABC):
    def search(self, query):
        pass 

import datetime 

class Question(Search):
    def __init__(self, title, description, bounty, asking_member):
        self._title = title 
        self._description = description 
        self._view_count = 0 
        self._vote_count = 0
        self._creation_time = datetime.datetime.now()
        self._update_time = datetime.datetime.now()
        self._status = QuestionStatus.OPEN 
        self._closing_remark = QuestionClosingRemark.DUPLICATE 
        self._bounty = bounty 
        self._asking_member = asking_member 
        self._photos = []
        self._comments = []
    
    def close(self):
        pass 

    def undelete(self):
        pass 

    def add_comment(self, comment):
        pass 

    def add_bounty(self, bounty):
        pass 

    def search(self, query):
        pass 


class Comment: 
    def __init__(self, text, member):
        self._text = text 
        self._creation_time = datetime.datetime.now()
        self._flag_count = 0 
        self._vote_count = 0 
        self._asking_member = member 

    def increment_vote_count(self):
        pass 


class Answer: 
    def __init__(self, text, member):
        self._answer_text = text 
        self._accepted = False 
        self._vote_count = 0 
        self._flag_count = 0 
        self._creation_time = datetime.datetime.now()
        self._creating_member = member 
        self._photos = [] 
    
    def increment_vote_count(self):
        pass 


################################################
# ATM 
################################################

class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5

class TransactionStatus(Enum):
    SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE = 1, 2, 3, 4, 5, 6

class CustomerStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, CLOSED, UNKNOWN = 1, 2, 3, 4, 5, 6, 7

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self._street_address = street 
        self._city = city 
        self._state = state 
        self._zip_code = zip_code 
        self._country = country 
    

class Customer:
    def __init__(self, name, address, email, phone, status):
        self._name = name 
        self._address = address 
        self._email = email 
        self._phone = phone 
        self._status = status 
        self._card = Card()
        self._account = Account 

    def make_transaction(self, transaction):
        pass 

    def get_billing_address(self):
        pass 

class Card: 
    def __init__(self, number, customer_name, expiry, pin):
        self._card_number = number 
        self._customer_name = customer_name 
        self._card_expiry = expiry 
        self._pin = pin 

    def get_billing_address(self):
        pass 


class Account:
    def __init__(self, account_number):
        self._account_number = account_number 
        self._total_balance = 0.0 
        self._available_balance = 0.0

    def get_available_balance(self):
        return self._available_balance

class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self._withdraw_limit = widthdraw_limit 

class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        self._debit_card_number = debit_card_number

class Bank: 
    def __init__(self, name, bank_code):
        self._name = name 
        self._bank_code = bank_code 
    
    def get_bank_code(self):
        return self._bank_code
    
    def add_atm(self, atm):
        pass 


class ATM: 
    def __init__(self, id, location):
        self._atm_id = id 
        self._location = location 
        self._cash_dispenser = CashDispenser()
        self._keypad = Keypad()
        self._screen = Screen()
        self.__printer = Printer()
        self.__check_deposit = CheckDeposit()
        self.__cash_deposit = CashDeposit
    
    def authenticate_user(self):
        pass 

    def make_transaction(self, customer, transaction):
        pass 

class CashDispenser:
    def __init__(self):
        self._total_five_dollar_bills = 0 
        self._total_twenty_dollar_bills = 0 
    
    def dispense_cash(self, amount):
        pass 

    def can_dispense_cash(self):
        pass 

class Keypad:
    def get_input(self):
        pass 

class Screen:
    def show_message(self, message):
        pass 

    def get_input(self):
        pass 

class Printer:
    def print_receipt(self, transaction):
        pass 

class DepositSlot(ABC):
    def __init__(self):
        self._total_amount = 0.0 
    
    def get_total_amount(self):
        return self._total_amount
    
class CheckDepositSlot(DepositSlot):
    def get_check_amount(self):
        pass 

class CashDepositSlot(DepositSlot):
    def receive_dollar_bill(self):
        pass 


class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self._transaction_id = id 
        self._creation_time = creation_date 
        self._status = status 
    
    def make_transaction(self):
        pass 

class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self._account_id = account_id 
    
    def get_account_id(self):
        return self._account_id 
    
class Depsoit(Transaction):
    def __init__(self, amount):
        self._amount = amount 
    
    def get_amount(self):
        return self._amount 

class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self._check_number = check_number 
        self._bank_code = bank_code 
    
    def get_check_number(self):
        return self._check_number

class CashDeposit(Deposit): 
    def __init_-(self, cash_deposit_limit):
        self._cash_deposit_limit = cash_deposit_limit
    
class Withdraw(Transaction):
    def __init__(self, amount):
        self._amount = amount 
    
    def get_amount(self):
        return self._amount 

class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self._destination_account_number = destination_account_number

    def get_destination_number(self):
        return self._destination_account_number



################################################
# Flight Management System
################################################

# Airline, Airport, Aircraft

# Flight,  Itinerary, FlightInstance, FlightSeat

# FlightReservation

class Address: 
    def __init__(self, street, city, state, zip_code, country):
        self._street_address = street
        self._city = city 
        self._state = state 
        self._zip_code = zip_code 
        self._country = country 


class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self._id = id 
        self._password = password 
        self._status = status 
    
    def reset_password(self):
        pass 

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self._name = name 
        self._address = address 
        self._email = email 
        self._phone = phone 
        self._account = account 

class Customer(Person):
    def __init__(self, frequent_flyer_number):
        self._frequent_flyer_number = frequent_flyer_number
    
    def get_itineraries(self):
        pass 

class Passenger: 
    def __init__(self, name, passport_number, date_of_birth):
        self._name = name 
        self._passport_number = passport_number
        self._date_of_birth = date_of_birth 
    
    def get_passport_number(self):
        return self._passport_number


class Airport: 
    def __init__(self, name, address, code):
        self._name = name 
        self._address = address 
        self._code = code 
    
    def get_flights(self):
        pass 

class Aircraft: 
    def __init__(self, name, model, manufacturing_year):
        self._name = name 
        self._model = model 
        self._manufacturing_year = manufacturing_year
        self._seats = []
    
    def get_flights(self):
        pass 

class Seat: 
    def __init__(self, seat_number, type, seat_class):
        self._seat_number = seat_number 
        self._type = type 
        self._seat_class = seat_class 

class FlightSeat(Seat):
    def __init__(self, fare):
        self._fare = fare 
    
    def get_fare(self):
        return self._fare 


class WeeklySchedule:
    def __init__(self, day_of_week, departure_time):
        self._day_of_week = day_of_week
        self._departure_time = departure_time 
    
class CustomSchedule:
    def __init__(self, custom_date, departure_time):
        self._custom_date = custom_date 
        self._departure_time = departure_time
    
class Flight: 
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self._flight_number = flight_number 
        self._departure = departure 
        self._arrival = arrival 
        self._duration_in_minutes = duration_in_minutes
        self._weekly_schedules = []
        self._flight_instances = []

class FlightInstance:
    def __init__(self, departure_time, gate, status, aircraft):
        self._departure_time = departure_time 
        self._gate = gate 
        self._status = status 
        self._aircraft = aircraft 
    
    def cancel(self):
        pass 

    def update_status(self, status):
        pass 


class FlightReservation:
    def __init__(self, reservation_number, flight, aircraft, creation_date, status):
        self._reservation_number = reservation_number 
        self._flight = flight 
        self._seat_map = {}
        self._creation_date = creation_date 
        self._status = status 
    
    def fetch_reservation_details(self, reservation_number):
        pass 

    def get_passengers(self):
        pass 


class Itinerary: 
    def __init__(self, customer_id, starting_airport, final_airport, creation_date):
        self._customer_id = customer_id 
        self._strating_airport = starting_airport 
        self._final_airport = final_airport 
        self._creation_date = creation_date 
        self._reservations = []

    def get_reservations(self):
        pass 

    def make_reservation(self):
        pass 

    def make_payment(self):
        pass 


################################################
# Hotel Management System
################################################

# Hotel, HotelLocation
# Room
# Account
# RoomBooking
# RoomHouseKeeping, RoomCharge, RoomKey

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self._street_address = street
        self._city = city
        self._state = state 
        self._zip_code = zip_code 
        self._country = country 
    
# account, person, guest, receptionist, server 
class Account: 
    def __init__(self, id, password, status=AccountStatus.Active):
        self._id = id 
        self._password = password 
        self._status = status 
    
# from abc import ABC, abstractmethod 
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self._name = name 
        self._address = address 
        self._email = email 
        self._phone = phone 
        self._account = account 

class Guest(Person):
    def __init__(self):
        self._total_rooms_checked_in = 0 
    
    def get_bookings(self):
        pass 

class Receptionist(Person):
    def search_member(self, name):
        pass 

    def create_booking(self):
        pass 

class Server(Person):
    def add_room_charge(self, room, room_charge):
        pass 

# hotel and hotel location 
class HotelLocation:
    def __init__(self, name, address):
        self._name = name 
        self._location = address 
    
    def get_rooms(self):
        pass 

class Hotel:
    def __init__(self, name):
        self._name = name 
        self._locations = []
    
    def add_location(self, location):
        pass 

class Search(ABC):
    def search(self, style, start_date, duration):
        pass 

class Room(Search):
    def __init__(self, room_number, room_style, status, price, is_smoking):
        self._room_number = room_number 
        self._style = room_style
        self._status = status 
        self._booking_price = price 
        self._is_smoking = is_smoking 
        self._keys = []
        self._housing_keeping_log = []
    
    def is_room_available(self):
        pass 

    def check_in(self):
        pass 

    def check_out(self):
        pass 

    def search(self, style, start_date, duration):
        pass 


class RoomBooking:
    def __init__(self, reservation_number, start_date, duration_in_days, booking_status):
        self._reservation_number = reservation_number
        self._start_date = start_date 
        self._duration_in_days = duration_in_days 
        self._status = booking_status 
        self._checkin = None 
        self._checkout = None 
        self._guest_id = 0 
        self._room = None 
        self._invoice = None 
        self._notifications = []
    
    def fetch_details(self, reservation_number):
        pass 

