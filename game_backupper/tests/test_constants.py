# Tests
# Settings
TEST_SETTINGS_LOAD_SETTINGS_EXCESSIVE_PARAMS = """\
{
\"BACKUP_SAVE_FOLDER\":\"backup_folder\",\n\"N_SAVE_LIMIT\":10,\n\"SETTINGS_INI_ROOT\":\"folder\",\n\"test_field\":\"test_value\" 
}"""
TEST_SETTINGS_LOAD_SETTINGS_INSUFFICIENT_PARAMS = """\
{
\"BACKUP_SAVE_FOLDER\":\"backup_folder\",\n\"N_SAVE_LIMIT\":10 
}"""