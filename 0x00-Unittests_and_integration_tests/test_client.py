#!/usr/bin/env python3
"""Module for testing client functions
"""

import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    Tests for client.GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', MagicMock(return_value={'key', 'value'}))
    def test_org(self, org):
        """ Tests utils.get_json for expected value """
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org, {'key', 'value'})
