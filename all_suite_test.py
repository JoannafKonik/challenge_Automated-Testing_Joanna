import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginToTheScoutsPanel
from test_cases.login_to_the_system import TestLoginToTheScoutsPanel_invalid_password
from test_cases.sign_out import TestSignOut
from test_cases.remind_password import TestRemindPassword
from test_cases.add_new_player import TestAddNewPlayer
from test_cases.add_new_player import TestAddNewPlayer_clear_form

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginToTheScoutsPanel))
   test_suite.addTest(makeSuite(TestLoginToTheScoutsPanel_invalid_password))
   test_suite.addTest(makeSuite(TestSignOut))
   test_suite.addTest(makeSuite(TestRemindPassword))
   test_suite.addTest(makeSuite(TestAddNewPlayer))
   test_suite.addTest(makeSuite(TestAddNewPlayer_clear_form))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())