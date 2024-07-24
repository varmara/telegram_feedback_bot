# Possible user states:
# User activity:
# - new user - default state
# - active user (session within a month)
# - inactive user
# Ban status:
# - shadowbanned
# - banned

from aiogram.fsm.state import State, StatesGroup

# Define states
class UserState(StatesGroup):
    ACTIVE = State()      # Active user
    INACTIVE = State()    # Inactive user
    SHADOWBANNED = State() # Shadowbanned user
    BANNED = State()      # Banned user
