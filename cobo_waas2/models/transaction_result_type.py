# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionResultType(str, Enum):
    """
    The transaction result type. Possible values include:   - `Signature`: An EVM EIP-191 or EVM EIP-712 signature. 
    """

    """
    allowed enum values
    """
    SIGNATURE = 'Signature'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionResultType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


