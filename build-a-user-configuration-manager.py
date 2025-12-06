** start of main.py **

test_settings = {
    "theme" : "light",
    "language": "ind",
    "notifications": "high"
}


def add_setting(test_settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name." 
    
    test_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(test_settings, up_setting):
    key, value = up_setting
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"


def view_settings(test_settings):
    output = "Current User Settings:\n"
    if test_settings == {}:
        return "No settings available."
    for key, value in test_settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output


** end of main.py **

