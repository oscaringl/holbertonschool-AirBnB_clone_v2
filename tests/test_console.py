#!/usr/bin/python3
"""Class TestConsoleDocs"""

import console
from contextlib import redirect_stdout
import inspect
import io
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation"""
    def test_pep8_conformance_console(self):
        """Test that console.py"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_console_module_docstring(self):
        """Test for the console.py"""
        self.assertIsNot(console.__doc__, None,
                         "console.py")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class")


class TestConsoleCommands(unittest.TestCase):
    """Class to test functionality of console"""
    @classmethod
    def setUpClass(cls):
        """Create command console to test with"""
        cls.cmdcon = HBNBCommand()

    def setUp(self):
        """Create in memory buffer to capture stdout"""
        self.output = io.StringIO()

    def tearDown(self):
        """Close in memory buffer after test"""
        self.output.close()

    def test_do_create(self):
        """Test do_create method of console"""
        with redirect_stdout(self.output):
            self.cmdcon.onecmd('create')
            self.assertEqual(self.output.getvalue(),
                             "** class name missing **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create blah')
            self.assertEqual(self.output.getvalue(),
                             "** class doesn't exist **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State name="California"')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
