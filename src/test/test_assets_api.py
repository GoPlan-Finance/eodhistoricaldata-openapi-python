"""
    EOD Historical Data API

    EOD Historical Data API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sam@sddproductions.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.assets_api import AssetsApi  # noqa: E501


class TestAssetsApi(unittest.TestCase):
    """AssetsApi unit test stubs"""

    def setUp(self):
        self.api = AssetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_asset_fundamentals(self):
        """Test case for asset_fundamentals

        Get Asset fundamentals  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Search symbols  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()