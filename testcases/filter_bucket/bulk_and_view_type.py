from pages.filter_bucket.bulk_and_view_type import FilterBucket
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Bucket(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.buck = FilterBucket(self.driver)

    def test_01VerifyAccessoryAddedInViewList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in view by type listing")
        self.log.info("*#" * 20)
        self.buck.AddingAccessoryProduct_VerifyAddedInViewByType()

    def test_02VerifyAccessoryShowingInBulkCopyList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in bulk copy button listing on the top")
        self.log.info("*#" * 20)
        self.buck.BulkCopyButton_VerifyAccessoryShowingTopOfList()

    def test_03VerifyFurnitureAddedInViewList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in view by type listing -- Furniture")
        self.log.info("*#" * 20)
        self.buck.AddingFurnitureProduct_VerifyAddedInViewByType()

    def test_04VerifyFurnitureShowingInBulkCopyList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in bulk copy button listing on the top -- Furniture")
        self.log.info("*#" * 20)
        self.buck.BulkCopyButton_VerifyFurnitureShowingTopOfList()

    def test_05VerifyOfficeFurnitureAddedInViewList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in view by type listing -- office Furniture")
        self.log.info("*#" * 20)
        self.buck.AddingOfficeFurnitureProduct_VerifyAddedInViewByType()

    def test_06VerifyOfficeFurnitureShowingInBulkCopyList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in bulk copy button listing on the top -- Office Furniture")
        self.log.info("*#" * 20)
        self.buck.BulkCopyButton_VerifyOfficeFurnitureShowingTopOfList()

    def test_07VerifyOpsAssetFurnitureAddedInViewList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in view by type listing -- OPS Asset")
        self.log.info("*#" * 20)
        self.buck.AddingOpsAssetProduct_VerifyAddedInViewByType()

    def test_08VerifyOpsAssetFurnitureShowingInBulkCopyList(self):
        self.log.info("*#" * 20)
        self.log.info("Add product showing in bulk copy button listing on the top -- OPS ASSET")
        self.log.info("*#" * 20)
        self.buck.BulkCopyButton_VerifyOpsAssetFurnitureShowingTopOfList()



