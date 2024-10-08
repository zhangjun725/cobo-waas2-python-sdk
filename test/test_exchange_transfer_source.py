# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.exchange_transfer_source import ExchangeTransferSource


class TestExchangeTransferSource(unittest.TestCase):
    """ExchangeTransferSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeTransferSource:
        """Test ExchangeTransferSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeTransferSource`
        """
        model = ExchangeTransferSource()
        if include_optional:
            return ExchangeTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                trading_account_type = 'Asset'
            )
        else:
            return ExchangeTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                trading_account_type = 'Asset',
        )
        """

    def testExchangeTransferSource(self):
        """Test ExchangeTransferSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
