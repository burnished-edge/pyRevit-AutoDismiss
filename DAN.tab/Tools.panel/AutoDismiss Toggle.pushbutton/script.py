from pyrevit import script, forms

# Access the config file
my_config = script.get_config("AutoDismiss")

# Get the current state (pass True as a positional argument)
current_state = my_config.get_option('is_active', True)

# Flip the state
new_state = not current_state

# Save the new state
my_config.is_active = new_state
script.save_config()

# Visual feedback
if new_state:
    forms.alert("Auto-Dismiss is now ON", title="Tool Status", warn_icon=False)
else:
    forms.alert("Auto-Dismiss is now OFF. Revit will show warnings normally.", title="Tool Status", warn_icon=False)
