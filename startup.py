from pyrevit import HOST_APP, framework, script
from Autodesk.Revit.UI.Events import DialogBoxShowingEventArgs

# We need to import the ViewSchedule class from the Revit API
from Autodesk.Revit.DB import ViewSchedule 

def dismiss_type_warning(sender, args):
    try:
        # 1. Check if the tool is toggled ON in the config
        my_config = script.get_config("AutoDismiss")
        if not my_config.get_option('is_active', True):
            return 

        # 2. Drill down to the Active View
        uiapp = sender
        uidoc = uiapp.ActiveUIDocument
        
        # We must check if uidoc exists, otherwise this will throw an error 
        # if a dialog pops up when no project files are open (e.g., at the home screen)
        if uidoc:
            active_view = uidoc.ActiveView
            
            # 3. Check if the active view is specifically a Schedule
            if not isinstance(active_view, ViewSchedule):
                # If it's a floor plan, 3D view, sheet, etc., stop the script right here.
                return 

        # 4. If we are in a schedule, proceed with checking the warning message
        if hasattr(args, 'Message'):
            target_texts = (
                "MESSAGE TO BE DISMISSED - MUST BE PHRASED VERBATIM",
            )
            
            if args.Message.startswith(target_texts):
                args.OverrideResult(1)
                
    except Exception:
        pass # Fail silently in the background

# Safely unregister and register the event hook
try:
    HOST_APP.uiapp.DialogBoxShowing -= framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)
except Exception:
    pass

HOST_APP.uiapp.DialogBoxShowing += framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)
