#!/usr/bin/env python3.6

import os
import markdown

import obspython as obs

__version__ = "0.0.1"
__author__ = "nossebro"
__website__ = "https://github.com/nossebro/obs-template"


def script_description():
    """Function expected to return a character string containing the description of the script."""

    desc = "<!doctype html>\n\n<html lang=\"en\">\n<body>\n"
    filename = next((x for x in ["{}.md".format(
        __name__), "README.md"] if x in os.listdir(script_path())), None)
    if filename:
        with open(os.path.join(script_path(), filename), "r", encoding="utf-8") as f:
            try:
                desc += markdown.markdown(f.read(), extensions=["tables"])
            except Exception as e:
                print(e)
        f.close()
    desc += "\n<h2>Script Information</h2>\n<p>\n<table width=\"90%\">\n<tbody>\n"
    for x in ["__version__", "__author__"]:
        desc += "<tr>\n<td>{}:</td>\n<td>{}</td>\n</tr>\n".format(
            x.replace("__", "").title(), eval(x))
    desc += "<tr>\n<td>{0}:</td>\n<td><a href=\"{1}\">{1}</a></td>\n</tr>\n".format(
        "Website", __website__)
    desc += "</tbody>\n</table>\n</p>\n</body>\n</html>\n"
    return desc


def script_load(settings):
    """Called on script startup with specific settings associated with the script.

    The settings parameter provided is not typically used for settings that are set by the user; instead the parameter is used for any extra internal settings data that may be used in the script.

    Parameters:
    settings – Settings associated with the script."""

    pass


def script_unload():
    """Called when the script is being unloaded."""

    pass


def script_save(settings):
    """Called when the script is being saved.

    This is not necessary for settings that are set by the user; instead this is used for any extra internal settings data that may be used in the script.

    Parameters:
    settings – Settings associated with the script."""

    pass


def script_defaults(settings):
    """Called to set default settings (if any) associated with the script.

    You would typically call Default Value Functions for the on the settings in order to set its default values.

    Parameters:
    settings – Settings associated with the script."""

    pass


def script_update(settings):
    """Called when the script’s settings (if any) have been changed by the user.

    Parameters:
    settings – Settings associated with the script."""

    pass


def script_properties() -> object:
    """Called to define user properties associated with the script.

    These properties are used to define how to show settings properties to a user.

    Returns:
    obs_properties_t object created via obs_properties_create()."""

    return obs.obs_properties_create()


def script_tick(seconds):
    """Called every frame in case per-frame processing is needed.

    If a timer is needed, please use Script Timers instead, as timers are more efficient if all that’s needed is basic timer functionality. Using this function in Python is not recommended due to the global interpreter lock of Python.

    Parameters:
    seconds – Seconds passed since previous frame."""

    pass
