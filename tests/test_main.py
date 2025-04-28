import unittest
from src.secure_env import secure_load_env

class TestSecureEnv(unittest.TestCase):
    def test_secure_env_load(self):
        result = secure_load_env()
        self.assertTrue(isinstance(result, dict))
        for k, v in result.items():
            self.assertTrue(k.endswith("_SALT") or k.endswith("_HASH"))

if __name__ == "__main__":
    unittest.main()
