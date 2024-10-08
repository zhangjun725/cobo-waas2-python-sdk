# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.custodial_transfer_source import CustodialTransferSource


class TestCustodialTransferSource(unittest.TestCase):
    """CustodialTransferSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustodialTransferSource:
        """Test CustodialTransferSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustodialTransferSource`
        """
        model = CustodialTransferSource()
        if include_optional:
            return CustodialTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return CustodialTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testCustodialTransferSource(self):
        """Test CustodialTransferSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
