import unittest
from src.core.lock_controller import LockController

class TestLockController(unittest.TestCase):

    def setUp(self):
        self.lock_controller = LockController()

    def test_initial_lock_status(self):
        self.assertEqual(self.lock_controller.get_lock_status(), 'unlocked')

    def test_lock_mechanism(self):
        self.lock_controller.lock()
        self.assertEqual(self.lock_controller.get_lock_status(), 'locked')

    def test_unlock_mechanism(self):
        self.lock_controller.lock()
        self.lock_controller.unlock()
        self.assertEqual(self.lock_controller.get_lock_status(), 'unlocked')

    def test_pin_verification_success(self):
        self.lock_controller.set_pin('1234')
        self.assertTrue(self.lock_controller.verify_pin('1234'))

    def test_pin_verification_failure(self):
        self.lock_controller.set_pin('1234')
        self.assertFalse(self.lock_controller.verify_pin('4321'))

if __name__ == '__main__':
    unittest.main()