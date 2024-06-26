# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetProductResult',
    'AwaitableGetProductResult',
    'get_product',
    'get_product_output',
]

@pulumi.output_type
class GetProductResult:
    """
    A collection of values returned by getProduct.
    """
    def __init__(__self__, annually_location_premium=None, biennial_location_premium=None, core=None, data_center=None, edge=None, filters=None, first=None, hourly_location_premium=None, id=None, monthly_location_premium=None, product_annually_price=None, product_bandwidth=None, product_biennial_price=None, product_cpu=None, product_cpu_cores=None, product_disabled_billing_periods=None, product_display_price=None, product_drive=None, product_gpu=None, product_hourly_price=None, product_id=None, product_memory=None, product_monthly_price=None, product_name=None, product_on_sale=None, product_original_price=None, product_quarterly_price=None, product_semi_annually_price=None, product_triennial_price=None, quarterly_location_premium=None, semi_annually_location_premium=None, stock=None, triennial_location_premium=None):
        if annually_location_premium and not isinstance(annually_location_premium, float):
            raise TypeError("Expected argument 'annually_location_premium' to be a float")
        pulumi.set(__self__, "annually_location_premium", annually_location_premium)
        if biennial_location_premium and not isinstance(biennial_location_premium, float):
            raise TypeError("Expected argument 'biennial_location_premium' to be a float")
        pulumi.set(__self__, "biennial_location_premium", biennial_location_premium)
        if core and not isinstance(core, bool):
            raise TypeError("Expected argument 'core' to be a bool")
        pulumi.set(__self__, "core", core)
        if data_center and not isinstance(data_center, str):
            raise TypeError("Expected argument 'data_center' to be a str")
        pulumi.set(__self__, "data_center", data_center)
        if edge and not isinstance(edge, bool):
            raise TypeError("Expected argument 'edge' to be a bool")
        pulumi.set(__self__, "edge", edge)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if first and not isinstance(first, bool):
            raise TypeError("Expected argument 'first' to be a bool")
        pulumi.set(__self__, "first", first)
        if hourly_location_premium and not isinstance(hourly_location_premium, float):
            raise TypeError("Expected argument 'hourly_location_premium' to be a float")
        pulumi.set(__self__, "hourly_location_premium", hourly_location_premium)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if monthly_location_premium and not isinstance(monthly_location_premium, float):
            raise TypeError("Expected argument 'monthly_location_premium' to be a float")
        pulumi.set(__self__, "monthly_location_premium", monthly_location_premium)
        if product_annually_price and not isinstance(product_annually_price, float):
            raise TypeError("Expected argument 'product_annually_price' to be a float")
        pulumi.set(__self__, "product_annually_price", product_annually_price)
        if product_bandwidth and not isinstance(product_bandwidth, str):
            raise TypeError("Expected argument 'product_bandwidth' to be a str")
        pulumi.set(__self__, "product_bandwidth", product_bandwidth)
        if product_biennial_price and not isinstance(product_biennial_price, float):
            raise TypeError("Expected argument 'product_biennial_price' to be a float")
        pulumi.set(__self__, "product_biennial_price", product_biennial_price)
        if product_cpu and not isinstance(product_cpu, str):
            raise TypeError("Expected argument 'product_cpu' to be a str")
        pulumi.set(__self__, "product_cpu", product_cpu)
        if product_cpu_cores and not isinstance(product_cpu_cores, str):
            raise TypeError("Expected argument 'product_cpu_cores' to be a str")
        pulumi.set(__self__, "product_cpu_cores", product_cpu_cores)
        if product_disabled_billing_periods and not isinstance(product_disabled_billing_periods, list):
            raise TypeError("Expected argument 'product_disabled_billing_periods' to be a list")
        pulumi.set(__self__, "product_disabled_billing_periods", product_disabled_billing_periods)
        if product_display_price and not isinstance(product_display_price, float):
            raise TypeError("Expected argument 'product_display_price' to be a float")
        pulumi.set(__self__, "product_display_price", product_display_price)
        if product_drive and not isinstance(product_drive, str):
            raise TypeError("Expected argument 'product_drive' to be a str")
        pulumi.set(__self__, "product_drive", product_drive)
        if product_gpu and not isinstance(product_gpu, str):
            raise TypeError("Expected argument 'product_gpu' to be a str")
        pulumi.set(__self__, "product_gpu", product_gpu)
        if product_hourly_price and not isinstance(product_hourly_price, float):
            raise TypeError("Expected argument 'product_hourly_price' to be a float")
        pulumi.set(__self__, "product_hourly_price", product_hourly_price)
        if product_id and not isinstance(product_id, int):
            raise TypeError("Expected argument 'product_id' to be a int")
        pulumi.set(__self__, "product_id", product_id)
        if product_memory and not isinstance(product_memory, str):
            raise TypeError("Expected argument 'product_memory' to be a str")
        pulumi.set(__self__, "product_memory", product_memory)
        if product_monthly_price and not isinstance(product_monthly_price, float):
            raise TypeError("Expected argument 'product_monthly_price' to be a float")
        pulumi.set(__self__, "product_monthly_price", product_monthly_price)
        if product_name and not isinstance(product_name, str):
            raise TypeError("Expected argument 'product_name' to be a str")
        pulumi.set(__self__, "product_name", product_name)
        if product_on_sale and not isinstance(product_on_sale, bool):
            raise TypeError("Expected argument 'product_on_sale' to be a bool")
        pulumi.set(__self__, "product_on_sale", product_on_sale)
        if product_original_price and not isinstance(product_original_price, float):
            raise TypeError("Expected argument 'product_original_price' to be a float")
        pulumi.set(__self__, "product_original_price", product_original_price)
        if product_quarterly_price and not isinstance(product_quarterly_price, float):
            raise TypeError("Expected argument 'product_quarterly_price' to be a float")
        pulumi.set(__self__, "product_quarterly_price", product_quarterly_price)
        if product_semi_annually_price and not isinstance(product_semi_annually_price, float):
            raise TypeError("Expected argument 'product_semi_annually_price' to be a float")
        pulumi.set(__self__, "product_semi_annually_price", product_semi_annually_price)
        if product_triennial_price and not isinstance(product_triennial_price, float):
            raise TypeError("Expected argument 'product_triennial_price' to be a float")
        pulumi.set(__self__, "product_triennial_price", product_triennial_price)
        if quarterly_location_premium and not isinstance(quarterly_location_premium, float):
            raise TypeError("Expected argument 'quarterly_location_premium' to be a float")
        pulumi.set(__self__, "quarterly_location_premium", quarterly_location_premium)
        if semi_annually_location_premium and not isinstance(semi_annually_location_premium, float):
            raise TypeError("Expected argument 'semi_annually_location_premium' to be a float")
        pulumi.set(__self__, "semi_annually_location_premium", semi_annually_location_premium)
        if stock and not isinstance(stock, str):
            raise TypeError("Expected argument 'stock' to be a str")
        pulumi.set(__self__, "stock", stock)
        if triennial_location_premium and not isinstance(triennial_location_premium, float):
            raise TypeError("Expected argument 'triennial_location_premium' to be a float")
        pulumi.set(__self__, "triennial_location_premium", triennial_location_premium)

    @property
    @pulumi.getter(name="annuallyLocationPremium")
    def annually_location_premium(self) -> float:
        return pulumi.get(self, "annually_location_premium")

    @property
    @pulumi.getter(name="biennialLocationPremium")
    def biennial_location_premium(self) -> float:
        return pulumi.get(self, "biennial_location_premium")

    @property
    @pulumi.getter
    def core(self) -> bool:
        return pulumi.get(self, "core")

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> str:
        return pulumi.get(self, "data_center")

    @property
    @pulumi.getter
    def edge(self) -> bool:
        return pulumi.get(self, "edge")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetProductFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def first(self) -> Optional[bool]:
        return pulumi.get(self, "first")

    @property
    @pulumi.getter(name="hourlyLocationPremium")
    def hourly_location_premium(self) -> float:
        return pulumi.get(self, "hourly_location_premium")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="monthlyLocationPremium")
    def monthly_location_premium(self) -> float:
        return pulumi.get(self, "monthly_location_premium")

    @property
    @pulumi.getter(name="productAnnuallyPrice")
    def product_annually_price(self) -> float:
        return pulumi.get(self, "product_annually_price")

    @property
    @pulumi.getter(name="productBandwidth")
    def product_bandwidth(self) -> str:
        return pulumi.get(self, "product_bandwidth")

    @property
    @pulumi.getter(name="productBiennialPrice")
    def product_biennial_price(self) -> float:
        return pulumi.get(self, "product_biennial_price")

    @property
    @pulumi.getter(name="productCpu")
    def product_cpu(self) -> str:
        return pulumi.get(self, "product_cpu")

    @property
    @pulumi.getter(name="productCpuCores")
    def product_cpu_cores(self) -> str:
        return pulumi.get(self, "product_cpu_cores")

    @property
    @pulumi.getter(name="productDisabledBillingPeriods")
    def product_disabled_billing_periods(self) -> Sequence[str]:
        return pulumi.get(self, "product_disabled_billing_periods")

    @property
    @pulumi.getter(name="productDisplayPrice")
    def product_display_price(self) -> float:
        return pulumi.get(self, "product_display_price")

    @property
    @pulumi.getter(name="productDrive")
    def product_drive(self) -> str:
        return pulumi.get(self, "product_drive")

    @property
    @pulumi.getter(name="productGpu")
    def product_gpu(self) -> str:
        return pulumi.get(self, "product_gpu")

    @property
    @pulumi.getter(name="productHourlyPrice")
    def product_hourly_price(self) -> float:
        return pulumi.get(self, "product_hourly_price")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> int:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productMemory")
    def product_memory(self) -> str:
        return pulumi.get(self, "product_memory")

    @property
    @pulumi.getter(name="productMonthlyPrice")
    def product_monthly_price(self) -> float:
        return pulumi.get(self, "product_monthly_price")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> str:
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="productOnSale")
    def product_on_sale(self) -> bool:
        return pulumi.get(self, "product_on_sale")

    @property
    @pulumi.getter(name="productOriginalPrice")
    def product_original_price(self) -> float:
        return pulumi.get(self, "product_original_price")

    @property
    @pulumi.getter(name="productQuarterlyPrice")
    def product_quarterly_price(self) -> float:
        return pulumi.get(self, "product_quarterly_price")

    @property
    @pulumi.getter(name="productSemiAnnuallyPrice")
    def product_semi_annually_price(self) -> float:
        return pulumi.get(self, "product_semi_annually_price")

    @property
    @pulumi.getter(name="productTriennialPrice")
    def product_triennial_price(self) -> float:
        return pulumi.get(self, "product_triennial_price")

    @property
    @pulumi.getter(name="quarterlyLocationPremium")
    def quarterly_location_premium(self) -> float:
        return pulumi.get(self, "quarterly_location_premium")

    @property
    @pulumi.getter(name="semiAnnuallyLocationPremium")
    def semi_annually_location_premium(self) -> float:
        return pulumi.get(self, "semi_annually_location_premium")

    @property
    @pulumi.getter
    def stock(self) -> str:
        return pulumi.get(self, "stock")

    @property
    @pulumi.getter(name="triennialLocationPremium")
    def triennial_location_premium(self) -> float:
        return pulumi.get(self, "triennial_location_premium")


class AwaitableGetProductResult(GetProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductResult(
            annually_location_premium=self.annually_location_premium,
            biennial_location_premium=self.biennial_location_premium,
            core=self.core,
            data_center=self.data_center,
            edge=self.edge,
            filters=self.filters,
            first=self.first,
            hourly_location_premium=self.hourly_location_premium,
            id=self.id,
            monthly_location_premium=self.monthly_location_premium,
            product_annually_price=self.product_annually_price,
            product_bandwidth=self.product_bandwidth,
            product_biennial_price=self.product_biennial_price,
            product_cpu=self.product_cpu,
            product_cpu_cores=self.product_cpu_cores,
            product_disabled_billing_periods=self.product_disabled_billing_periods,
            product_display_price=self.product_display_price,
            product_drive=self.product_drive,
            product_gpu=self.product_gpu,
            product_hourly_price=self.product_hourly_price,
            product_id=self.product_id,
            product_memory=self.product_memory,
            product_monthly_price=self.product_monthly_price,
            product_name=self.product_name,
            product_on_sale=self.product_on_sale,
            product_original_price=self.product_original_price,
            product_quarterly_price=self.product_quarterly_price,
            product_semi_annually_price=self.product_semi_annually_price,
            product_triennial_price=self.product_triennial_price,
            quarterly_location_premium=self.quarterly_location_premium,
            semi_annually_location_premium=self.semi_annually_location_premium,
            stock=self.stock,
            triennial_location_premium=self.triennial_location_premium)


def get_product(filters: Optional[Sequence[pulumi.InputType['GetProductFilterArgs']]] = None,
                first: Optional[bool] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['first'] = first
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hivelocity:index/getProduct:getProduct', __args__, opts=opts, typ=GetProductResult).value

    return AwaitableGetProductResult(
        annually_location_premium=pulumi.get(__ret__, 'annually_location_premium'),
        biennial_location_premium=pulumi.get(__ret__, 'biennial_location_premium'),
        core=pulumi.get(__ret__, 'core'),
        data_center=pulumi.get(__ret__, 'data_center'),
        edge=pulumi.get(__ret__, 'edge'),
        filters=pulumi.get(__ret__, 'filters'),
        first=pulumi.get(__ret__, 'first'),
        hourly_location_premium=pulumi.get(__ret__, 'hourly_location_premium'),
        id=pulumi.get(__ret__, 'id'),
        monthly_location_premium=pulumi.get(__ret__, 'monthly_location_premium'),
        product_annually_price=pulumi.get(__ret__, 'product_annually_price'),
        product_bandwidth=pulumi.get(__ret__, 'product_bandwidth'),
        product_biennial_price=pulumi.get(__ret__, 'product_biennial_price'),
        product_cpu=pulumi.get(__ret__, 'product_cpu'),
        product_cpu_cores=pulumi.get(__ret__, 'product_cpu_cores'),
        product_disabled_billing_periods=pulumi.get(__ret__, 'product_disabled_billing_periods'),
        product_display_price=pulumi.get(__ret__, 'product_display_price'),
        product_drive=pulumi.get(__ret__, 'product_drive'),
        product_gpu=pulumi.get(__ret__, 'product_gpu'),
        product_hourly_price=pulumi.get(__ret__, 'product_hourly_price'),
        product_id=pulumi.get(__ret__, 'product_id'),
        product_memory=pulumi.get(__ret__, 'product_memory'),
        product_monthly_price=pulumi.get(__ret__, 'product_monthly_price'),
        product_name=pulumi.get(__ret__, 'product_name'),
        product_on_sale=pulumi.get(__ret__, 'product_on_sale'),
        product_original_price=pulumi.get(__ret__, 'product_original_price'),
        product_quarterly_price=pulumi.get(__ret__, 'product_quarterly_price'),
        product_semi_annually_price=pulumi.get(__ret__, 'product_semi_annually_price'),
        product_triennial_price=pulumi.get(__ret__, 'product_triennial_price'),
        quarterly_location_premium=pulumi.get(__ret__, 'quarterly_location_premium'),
        semi_annually_location_premium=pulumi.get(__ret__, 'semi_annually_location_premium'),
        stock=pulumi.get(__ret__, 'stock'),
        triennial_location_premium=pulumi.get(__ret__, 'triennial_location_premium'))


@_utilities.lift_output_func(get_product)
def get_product_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetProductFilterArgs']]]]] = None,
                       first: Optional[pulumi.Input[Optional[bool]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
