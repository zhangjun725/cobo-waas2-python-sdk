# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response


class TestCreateTransferTransaction201Response(unittest.TestCase):
    """CreateTransferTransaction201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTransferTransaction201Response:
        """Test CreateTransferTransaction201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTransferTransaction201Response`
        """
        model = CreateTransferTransaction201Response()
        if include_optional:
            return CreateTransferTransaction201Response(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                transaction_id = 'c986cb3b-1301-412f-9450-13a52c43a95f',
                status = 'Submitted'
            )
        else:
            return CreateTransferTransaction201Response(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                transaction_id = 'c986cb3b-1301-412f-9450-13a52c43a95f',
                status = 'Submitted',
        )
        """

    def testCreateTransferTransaction201Response(self):
        """Test CreateTransferTransaction201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
