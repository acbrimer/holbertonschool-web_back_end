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
        """ Tests client.GithubOrgClient.org for expected value """
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org, {'key', 'value'})

    @patch('client.GithubOrgClient.org',
           MagicMock(return_value={'repos_url', 'www'}))
    def test_public_repos_url(self):
        """Tests client.GithubOrgClient._public_repos_url """
        github_org_client = GithubOrgClient('test_org')
        self.assertEqual(github_org_client._public_repos_url, 'www')

    @patch('client.get_json', MagicMock(return_value={'repos_url', 'www'}))
    def test_public_repos(self):
        """Tests client.GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient.public_repos',
                   MagicMock(return_value='www')) as repo:
            github_org_client = GithubOrgClient('test_org')
            self.assertEqual(github_org_client.public_repos, 'www')
            repo.assert_called_once()
