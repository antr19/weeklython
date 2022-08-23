from database.functions import *
from database.sqlite_db1 import *

users = []
admins = []

# #event
# insert_db('event', ['user_id', 'type', 'title', 'description', 'seats_number', 'data_start', 'data_end'], ['1', 'online', '##########2', '3', '4', '2022-08-23 10:00', '2021-08-23 14:00'])
# insert_db('event', ['user_id', 'type', 'title', 'description', 'seats_number', 'data_start', 'data_end'], ['1', 'Moscow', '111party_title', 'description', '40', '2021-08-23 10:00', '2021-08-23 14:00'])
# insert_db('event', ['user_id', 'type', 'title', 'description', 'seats_number', 'data_start', 'data_end'], ['1', 'lesson', 'lesson_title', 'description', '56', '2022-07-23 10:00', '2022-09-23 14:00'])
#
# # registration
# insert_db('registration', ['user_id', 'event_id', 'registration_time'], ['1', '1', '2022-07-23 10:00'])
# insert_db('registration', ['user_id', 'event_id', 'registration_time'], ['1', '2', '2022-07-23 10:00'])
# insert_db('registration', ['user_id', 'event_id', 'registration_time'], ['1', '3', '2022-07-23 10:00'])
# insert_db('registration', ['user_id', 'event_id', 'registration_time'], ['2', '3', '2022-07-23 10:00'])
# register_user(7, 8)
# unregister_user(7, 8)
#
# #checkins
# insert_db('checkins', ['user_id', 'event_id', 'time'], ['1', '2', '2022-07-23 10:00'])
# insert_db('checkins', ['user_id', 'event_id', 'time'], ['1', '2', '2022-07-23 10:00'])
# user_checkined(7, 8)

#users
# insert_db('users', ['id', 'login', 'campus', 'time'], ['10', 'login_custom_10', 'Moscow', '2022-07-23 10:00'])

# print(select_db('event', ['*']))
# print(get_relevant_events(1))

# leave_feedback(1, 1, 1, "1")
# print(if_left_feedback(1, 1))
# print(if_left_feedback(1, 1111))

user_checkined(301784271, 6)
update_db('event', 'data_end', '0', 'id=6')
import deeplink.deeplink as dd
import utils.utils as ut

# dd.get_qrcode(ut.get_deeplink("eventid_2"), "qrcode.png")
