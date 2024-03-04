import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_string_method(self, category_factory):
        x = category_factory()
        assert x.__str__() == "test_category"


class TestBrandModel:
    def test_string_method(self, brand_factory):
        obj = brand_factory()
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_string_method(self, product_factory):
        obj = product_factory(name="test_product")
        assert obj.__str__() == "test_product"