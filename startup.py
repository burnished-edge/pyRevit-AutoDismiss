from pyrevit import HOST_APP, framework, script
from Autodesk.Revit.UI.Events import DialogBoxShowingEventArgs

def dismiss_type_warning(sender, args):
    try:
        my_config = script.get_config("AutoDismiss")
        
        # Pass True as a positional argument here too
        if not my_config.get_option('is_active', True):
            return 

        if hasattr(args, 'Message'):
            target_texts = (
                "This change will be applied to all elements of type",
            )
            
            if args.Message.startswith(target_texts):
                args.OverrideResult(1)
    except Exception:
        pass 

try:
    HOST_APP.uiapp.DialogBoxShowing -= framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)
except Exception:
    pass

HOST_APP.uiapp.DialogBoxShowing += framework.EventHandler[DialogBoxShowingEventArgs](dismiss_type_warning)
