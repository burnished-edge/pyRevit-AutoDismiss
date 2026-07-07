from pyrevit import script, forms

# Access the exact same config file that startup.py is looking at
my_config = script.get_config("AutoDismiss")

# Get the current state (defaults to True)
current_state = my_config.get_option('is_active', default=True)

# Flip the state (If True, make False. If False, make True)
new_state = not current_state

# Save the new state back to the config file
my_config.is_active = new_state
script.save_config()

# Give the user visual feedback so they know what happened
if new_state:
    forms.alert("Auto-Dismiss is now ON", title="Tool Status", warn_icon=False)
else:
    forms.alert("Auto-Dismiss is now OFF. Revit will show warnings normally.", title="Tool Status", warn_icon=False)