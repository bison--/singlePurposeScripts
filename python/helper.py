import os

def bool_conversion(user_input):
    valid_true = {'true', 'True', 'y', 'yes', 'j', 'ja'}
    return user_input in valid_true


def valid_input(question, _type=str, use_default=False, default=None):
    need_input = True
    result = None
    while need_input:
        user_input = input(question)
        if user_input == '' and use_default:
            result = default
            break

        if _type == bool:
            user_input = bool_conversion(user_input)

        try:
            result = _type(user_input)
            need_input = False
        except Exception as ex:
            print(ex)

    return result

def get_full_path_without_extension(file_path):
    file_path_without_extension, _ = os.path.splitext(file_path)
    return file_path_without_extension
