from unittest import TestCase

from core.utils.env_picker import pick_env_variable
from core.utils.env_picker import load_env_file_in_memory


class TestEnvPicker(TestCase):
    
    def setUp(self) -> None:
        """Create a fake .env file for testing."""
        with open(".test_env", "w") as file:
            file.write("TEST_KEY=TEST_VALUE")
        return super().setUp()

    def test_load_env_file_in_memory(self):
        load_env_file_in_memory(".test_env")
        self.assertEqual(pick_env_variable("TEST_KEY"), "TEST_VALUE")
    
    def test_load_env_file_in_memory_file_not_found(self):
        with self.assertRaises(Exception) as context:
            load_env_file_in_memory("non_existent_file")
        self.assertTrue("No such file or directory" in str(context.exception))
        
    def test_pick_env_variable(self):
        self.assertEqual(pick_env_variable("TEST_KEY"), "TEST_VALUE")
    
    def test_pick_env_variable_default(self):
        self.assertEqual(pick_env_variable("NON_EXISTENT_KEY", "DEFAULT_VALUE"), "DEFAULT_VALUE")
        
    def tearDown(self) -> None:
        """Remove the fake .env file."""
        import os
        os.remove(".test_env")
        return super().tearDown()