from pyrevit import HOST_APP, framework, script
from Autodesk.Revit.UI.Events import DialogBoxShowingEventArgs

def dismiss_type_warning(sender, args):
    try:
        # 1. Check our custom configuration file first
        my_config = script.get_config("AutoDismiss")
        
        # If 'is_active' is set to False, stop here and do nothing.
        # (It defaults to True if the setting doesn't exist yet)
        if not my_config.get_option('is_active', default=True):
            return 

        # 2. If it is active, proceed with checking the message
        if hasattr(args, 'Message'):
            target_texts = (
                "This change will be applied to all elements of type",
            )
            
            if args.Message.startswith(target_texts):
                args.OverrideResult(1)
    except Exception:
        pass 

# Unregister and register the event
try:
    HOST_APP.uiapp.DialogBoxShowing -= framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)
except Exception:
    pass

HOST_APP.uiapp.DialogBoxShowing += framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)