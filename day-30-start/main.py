try:
    new_doct = {"key": "value"}
    print(new_doct["mike"])
except KeyError as error_message:
    print(f"{error_message} caused error")