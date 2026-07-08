# pyRevit AutoDismiss

A background pyRevit extension designed to automatically dismiss disruptive Revit warnings during heavy modeling tasks. This tool intercepts Revit's `DialogBoxShowing` event to silently click "OK" on specific, pre-defined warning messages—such as the warning triggered when bulk-editing type parameters in a non-itemized schedule.

It utilizes a background listener to operate completely silently without interrupting your workflow, while providing a ribbon-based kill switch to instantly toggle the automation on or off as needed.

---

## Features

* **Silent Background Listener**: Initializes automatically when Revit starts via a `startup.py` script. It sits in the background and evaluates dialog boxes the millisecond they appear.
* **Instant Kill Switch**: Includes a native ribbon button to toggle the auto-dismiss feature ON or OFF on the fly, without needing to restart Revit or uninstall the tool.
* **Easily Expandable Blocklist**: Built using a simple Python tuple, allowing users or BIM managers to quickly add new warning phrases to the auto-dismiss blocklist with just a text editor.
* **State Persistence**: Remembers whether you left the tool armed or disarmed across different Revit sessions using pyRevit's built-in configuration manager.

---

## Installation & Setup Workflow

Please complete the following steps to get the plugin installed and configured.

1. [Step 1: Install via pyRevit Extension Manager](#step-1-install-via-pyrevit-extension-manager)
2. [Step 2: First Run & Initialization](#step-2-first-run--initialization)
3. [Keeping the Tool Updated](#keeping-the-tool-updated)

---

### Step 1: Install via pyRevit Extension Manager

You can install this extension directly from this GitHub repository using pyRevit's built-in tools.

1. Open Revit and navigate to the `pyRevit` tab on the ribbon.
2. Click the `pyRevit` drop-down menu (small triangle icon next to "pyRevit") and select `Extensions`.
3. In the Extension Manager window, paste this repository's Git URL into the GIT URL field:
   `https://github.com/burnished-edge/pyRevit-AutoDismiss.git` *(Note: Replace with actual URL if different)*
4. Provide a name for the tool if prompted, then click `Add and install`. 
5. Once the installation completes, close the Extension Manager.

---

### Step 2: First Run & Initialization

Because this tool relies on a background listener rather than a standard push-button script, it needs to be initialized into Revit's application framework.

1. After installing the extension, click `Reload` in the main pyRevit ribbon menu. 
2. pyRevit will recompile, and the background listener (`startup.py`) will automatically hook into Revit's dialog event handler.
3. A new ribbon tab/panel will generate on your screen containing the `Toggle Dismiss` button. The tool is now active and armed by default.

---

## Keeping the Tool Updated

Because the extension is linked directly to GitHub via pyRevit, applying future updates is effortless. Whenever a new version or new set of blocked warnings is pushed to this repository:

1. Open the `pyRevit Extension Manager`.
2. Locate AutoDismiss in your installed list.
3. Click `Update`. pyRevit will automatically pull the latest source code from GitHub and apply the changes. 
4. Reload pyRevit to see the updates take effect.

---

## How To Use

1. Proceed with your standard Revit workflows (e.g., editing type parameters in a non-itemized schedule). If a warning matches the blocklist, the dialog box will flash and dismiss itself instantly.
2. To pause the tool, click the `Toggle Dismiss` button on your custom ribbon panel. 
3. A prompt will appear confirming that **Auto-Dismiss is now OFF**. Revit will display all warnings normally.
4. Click the button again to re-arm the listener. 

![AutoDismiss Ribbon Toggle UI](docs/images/autodismiss_toggle_ui.png)

---

## How to Add New Warnings to the Blocklist

Revit warnings can have varying verbiage depending on the exact context. If you encounter a new dialog box that you want the script to automatically click "OK" on, you can add it to the codebase.

1. Open the `startup.py` file located at the root of this installed extension folder.
2. Locate the `target_texts` variable inside the `dismiss_type_warning` function.
3. Type the exact starting text of the new warning into the list.

> ⚠️ **PYTHON SYNTAX REQUIREMENT**: You **must** wrap the new warning phrase in quotation marks (`" "`) and you **must** include a comma (`,`) at the end of the line, even if it is the last item in the list.

### Code Example:
```python
            target_texts = (
                "This change will be applied to all elements of type", # Original warning
                "Elements have duplicate Mark values",                 # New warning added
                "Line is slightly off axis",                           # Another warning added
            )
