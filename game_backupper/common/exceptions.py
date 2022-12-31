class SettingParseException(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class SettingTypeFuncInvalidAttribute(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class SettingTypeFuncInvalidPath(SettingTypeFuncInvalidAttribute):
    def __init__(self, message=None):
        super().__init__(message)


class SettingTypeFuncInvalidString(SettingTypeFuncInvalidAttribute):
    def __init__(self, message=None):
        super().__init__(message)


class SettingTypeFuncInvalidFloat(SettingTypeFuncInvalidAttribute):
    def __init__(self, message=None):
        super().__init__(message)


class SettingTypeFuncInvalidInt(SettingTypeFuncInvalidAttribute):
    def __init__(self, message=None):
        super().__init__(message)


class NonexistentPathException:
    pass
