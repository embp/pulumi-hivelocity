# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BareMetalDeviceDetailArgs', 'BareMetalDeviceDetail']

@pulumi.input_type
class BareMetalDeviceDetailArgs:
    def __init__(__self__, *,
                 hostname: pulumi.Input[str],
                 location_name: pulumi.Input[str],
                 os_name: pulumi.Input[str],
                 product_id: pulumi.Input[int],
                 bonded: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 force_device_id: Optional[pulumi.Input[int]] = None,
                 ignition_id: Optional[pulumi.Input[int]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[int]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 power_status: Optional[pulumi.Input[str]] = None,
                 primary_ip: Optional[pulumi.Input[str]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 public_ssh_key_id: Optional[pulumi.Input[int]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a BareMetalDeviceDetail resource.
        :param pulumi.Input[str] hostname: Hostname for this device
        :param pulumi.Input[str] location_name: Deploy device in this location
        :param pulumi.Input[str] os_name: Operating system to install on device
        :param pulumi.Input[int] product_id: Product ID to pick from the stock
        :param pulumi.Input[bool] bonded: When set, prefer only bonded devices
        :param pulumi.Input[int] device_id: Device ID
        :param pulumi.Input[int] force_device_id: Force deployment of this Device ID (internal use only)
        :param pulumi.Input[int] ignition_id: IgnitionConfig ID
        :param pulumi.Input[str] last_updated: Last time this device was updated
        :param pulumi.Input[int] order_id: Order ID
        :param pulumi.Input[str] period: Billing period for device
        :param pulumi.Input[str] power_status: Power status
        :param pulumi.Input[str] primary_ip: Primary IP of device
        :param pulumi.Input[str] product_name: Product Name
        :param pulumi.Input[int] public_ssh_key_id: ID of a SSH Key to apply for device
        :param pulumi.Input[str] script: Post-install script for device
        :param pulumi.Input[int] service_id: Service ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to apply for device
        :param pulumi.Input[int] vlan_id: VLAN ID
        """
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "location_name", location_name)
        pulumi.set(__self__, "os_name", os_name)
        pulumi.set(__self__, "product_id", product_id)
        if bonded is not None:
            pulumi.set(__self__, "bonded", bonded)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if force_device_id is not None:
            pulumi.set(__self__, "force_device_id", force_device_id)
        if ignition_id is not None:
            pulumi.set(__self__, "ignition_id", ignition_id)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if order_id is not None:
            pulumi.set(__self__, "order_id", order_id)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if power_status is not None:
            pulumi.set(__self__, "power_status", power_status)
        if primary_ip is not None:
            pulumi.set(__self__, "primary_ip", primary_ip)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)
        if public_ssh_key_id is not None:
            pulumi.set(__self__, "public_ssh_key_id", public_ssh_key_id)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vlan_id is not None:
            warnings.warn("""This field is deprecated. Please use a VlanDetail resource instead.""", DeprecationWarning)
            pulumi.log.warn("""vlan_id is deprecated: This field is deprecated. Please use a VlanDetail resource instead.""")
        if vlan_id is not None:
            pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        Hostname for this device
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> pulumi.Input[str]:
        """
        Deploy device in this location
        """
        return pulumi.get(self, "location_name")

    @location_name.setter
    def location_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "location_name", value)

    @property
    @pulumi.getter(name="osName")
    def os_name(self) -> pulumi.Input[str]:
        """
        Operating system to install on device
        """
        return pulumi.get(self, "os_name")

    @os_name.setter
    def os_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "os_name", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[int]:
        """
        Product ID to pick from the stock
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter
    def bonded(self) -> Optional[pulumi.Input[bool]]:
        """
        When set, prefer only bonded devices
        """
        return pulumi.get(self, "bonded")

    @bonded.setter
    def bonded(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bonded", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[int]]:
        """
        Device ID
        """
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="forceDeviceId")
    def force_device_id(self) -> Optional[pulumi.Input[int]]:
        """
        Force deployment of this Device ID (internal use only)
        """
        return pulumi.get(self, "force_device_id")

    @force_device_id.setter
    def force_device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "force_device_id", value)

    @property
    @pulumi.getter(name="ignitionId")
    def ignition_id(self) -> Optional[pulumi.Input[int]]:
        """
        IgnitionConfig ID
        """
        return pulumi.get(self, "ignition_id")

    @ignition_id.setter
    def ignition_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ignition_id", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        """
        Last time this device was updated
        """
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> Optional[pulumi.Input[int]]:
        """
        Order ID
        """
        return pulumi.get(self, "order_id")

    @order_id.setter
    def order_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order_id", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[str]]:
        """
        Billing period for device
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> Optional[pulumi.Input[str]]:
        """
        Power status
        """
        return pulumi.get(self, "power_status")

    @power_status.setter
    def power_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "power_status", value)

    @property
    @pulumi.getter(name="primaryIp")
    def primary_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Primary IP of device
        """
        return pulumi.get(self, "primary_ip")

    @primary_ip.setter
    def primary_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_ip", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[str]]:
        """
        Product Name
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_name", value)

    @property
    @pulumi.getter(name="publicSshKeyId")
    def public_ssh_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of a SSH Key to apply for device
        """
        return pulumi.get(self, "public_ssh_key_id")

    @public_ssh_key_id.setter
    def public_ssh_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "public_ssh_key_id", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        Post-install script for device
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[int]]:
        """
        Service ID
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags to apply for device
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[pulumi.Input[int]]:
        """
        VLAN ID
        """
        warnings.warn("""This field is deprecated. Please use a VlanDetail resource instead.""", DeprecationWarning)
        pulumi.log.warn("""vlan_id is deprecated: This field is deprecated. Please use a VlanDetail resource instead.""")

        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan_id", value)


@pulumi.input_type
class _BareMetalDeviceDetailState:
    def __init__(__self__, *,
                 bonded: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 force_device_id: Optional[pulumi.Input[int]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignition_id: Optional[pulumi.Input[int]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location_name: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[int]] = None,
                 os_name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 power_status: Optional[pulumi.Input[str]] = None,
                 primary_ip: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[int]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 public_ssh_key_id: Optional[pulumi.Input[int]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering BareMetalDeviceDetail resources.
        :param pulumi.Input[bool] bonded: When set, prefer only bonded devices
        :param pulumi.Input[int] device_id: Device ID
        :param pulumi.Input[int] force_device_id: Force deployment of this Device ID (internal use only)
        :param pulumi.Input[str] hostname: Hostname for this device
        :param pulumi.Input[int] ignition_id: IgnitionConfig ID
        :param pulumi.Input[str] last_updated: Last time this device was updated
        :param pulumi.Input[str] location_name: Deploy device in this location
        :param pulumi.Input[int] order_id: Order ID
        :param pulumi.Input[str] os_name: Operating system to install on device
        :param pulumi.Input[str] period: Billing period for device
        :param pulumi.Input[str] power_status: Power status
        :param pulumi.Input[str] primary_ip: Primary IP of device
        :param pulumi.Input[int] product_id: Product ID to pick from the stock
        :param pulumi.Input[str] product_name: Product Name
        :param pulumi.Input[int] public_ssh_key_id: ID of a SSH Key to apply for device
        :param pulumi.Input[str] script: Post-install script for device
        :param pulumi.Input[int] service_id: Service ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to apply for device
        :param pulumi.Input[int] vlan_id: VLAN ID
        """
        if bonded is not None:
            pulumi.set(__self__, "bonded", bonded)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if force_device_id is not None:
            pulumi.set(__self__, "force_device_id", force_device_id)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ignition_id is not None:
            pulumi.set(__self__, "ignition_id", ignition_id)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if location_name is not None:
            pulumi.set(__self__, "location_name", location_name)
        if order_id is not None:
            pulumi.set(__self__, "order_id", order_id)
        if os_name is not None:
            pulumi.set(__self__, "os_name", os_name)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if power_status is not None:
            pulumi.set(__self__, "power_status", power_status)
        if primary_ip is not None:
            pulumi.set(__self__, "primary_ip", primary_ip)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)
        if public_ssh_key_id is not None:
            pulumi.set(__self__, "public_ssh_key_id", public_ssh_key_id)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vlan_id is not None:
            warnings.warn("""This field is deprecated. Please use a VlanDetail resource instead.""", DeprecationWarning)
            pulumi.log.warn("""vlan_id is deprecated: This field is deprecated. Please use a VlanDetail resource instead.""")
        if vlan_id is not None:
            pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter
    def bonded(self) -> Optional[pulumi.Input[bool]]:
        """
        When set, prefer only bonded devices
        """
        return pulumi.get(self, "bonded")

    @bonded.setter
    def bonded(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bonded", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[int]]:
        """
        Device ID
        """
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="forceDeviceId")
    def force_device_id(self) -> Optional[pulumi.Input[int]]:
        """
        Force deployment of this Device ID (internal use only)
        """
        return pulumi.get(self, "force_device_id")

    @force_device_id.setter
    def force_device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "force_device_id", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Hostname for this device
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="ignitionId")
    def ignition_id(self) -> Optional[pulumi.Input[int]]:
        """
        IgnitionConfig ID
        """
        return pulumi.get(self, "ignition_id")

    @ignition_id.setter
    def ignition_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ignition_id", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        """
        Last time this device was updated
        """
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> Optional[pulumi.Input[str]]:
        """
        Deploy device in this location
        """
        return pulumi.get(self, "location_name")

    @location_name.setter
    def location_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location_name", value)

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> Optional[pulumi.Input[int]]:
        """
        Order ID
        """
        return pulumi.get(self, "order_id")

    @order_id.setter
    def order_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order_id", value)

    @property
    @pulumi.getter(name="osName")
    def os_name(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system to install on device
        """
        return pulumi.get(self, "os_name")

    @os_name.setter
    def os_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_name", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[str]]:
        """
        Billing period for device
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> Optional[pulumi.Input[str]]:
        """
        Power status
        """
        return pulumi.get(self, "power_status")

    @power_status.setter
    def power_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "power_status", value)

    @property
    @pulumi.getter(name="primaryIp")
    def primary_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Primary IP of device
        """
        return pulumi.get(self, "primary_ip")

    @primary_ip.setter
    def primary_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_ip", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[int]]:
        """
        Product ID to pick from the stock
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[str]]:
        """
        Product Name
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_name", value)

    @property
    @pulumi.getter(name="publicSshKeyId")
    def public_ssh_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of a SSH Key to apply for device
        """
        return pulumi.get(self, "public_ssh_key_id")

    @public_ssh_key_id.setter
    def public_ssh_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "public_ssh_key_id", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        Post-install script for device
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[int]]:
        """
        Service ID
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags to apply for device
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[pulumi.Input[int]]:
        """
        VLAN ID
        """
        warnings.warn("""This field is deprecated. Please use a VlanDetail resource instead.""", DeprecationWarning)
        pulumi.log.warn("""vlan_id is deprecated: This field is deprecated. Please use a VlanDetail resource instead.""")

        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan_id", value)


class BareMetalDeviceDetail(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bonded: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 force_device_id: Optional[pulumi.Input[int]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignition_id: Optional[pulumi.Input[int]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location_name: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[int]] = None,
                 os_name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 power_status: Optional[pulumi.Input[str]] = None,
                 primary_ip: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[int]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 public_ssh_key_id: Optional[pulumi.Input[int]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a BareMetalDeviceDetail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bonded: When set, prefer only bonded devices
        :param pulumi.Input[int] device_id: Device ID
        :param pulumi.Input[int] force_device_id: Force deployment of this Device ID (internal use only)
        :param pulumi.Input[str] hostname: Hostname for this device
        :param pulumi.Input[int] ignition_id: IgnitionConfig ID
        :param pulumi.Input[str] last_updated: Last time this device was updated
        :param pulumi.Input[str] location_name: Deploy device in this location
        :param pulumi.Input[int] order_id: Order ID
        :param pulumi.Input[str] os_name: Operating system to install on device
        :param pulumi.Input[str] period: Billing period for device
        :param pulumi.Input[str] power_status: Power status
        :param pulumi.Input[str] primary_ip: Primary IP of device
        :param pulumi.Input[int] product_id: Product ID to pick from the stock
        :param pulumi.Input[str] product_name: Product Name
        :param pulumi.Input[int] public_ssh_key_id: ID of a SSH Key to apply for device
        :param pulumi.Input[str] script: Post-install script for device
        :param pulumi.Input[int] service_id: Service ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to apply for device
        :param pulumi.Input[int] vlan_id: VLAN ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BareMetalDeviceDetailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BareMetalDeviceDetail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BareMetalDeviceDetailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BareMetalDeviceDetailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bonded: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 force_device_id: Optional[pulumi.Input[int]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignition_id: Optional[pulumi.Input[int]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location_name: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[int]] = None,
                 os_name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 power_status: Optional[pulumi.Input[str]] = None,
                 primary_ip: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[int]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 public_ssh_key_id: Optional[pulumi.Input[int]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BareMetalDeviceDetailArgs.__new__(BareMetalDeviceDetailArgs)

            __props__.__dict__["bonded"] = bonded
            __props__.__dict__["device_id"] = device_id
            __props__.__dict__["force_device_id"] = force_device_id
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__.__dict__["hostname"] = hostname
            __props__.__dict__["ignition_id"] = ignition_id
            __props__.__dict__["last_updated"] = last_updated
            if location_name is None and not opts.urn:
                raise TypeError("Missing required property 'location_name'")
            __props__.__dict__["location_name"] = location_name
            __props__.__dict__["order_id"] = order_id
            if os_name is None and not opts.urn:
                raise TypeError("Missing required property 'os_name'")
            __props__.__dict__["os_name"] = os_name
            __props__.__dict__["period"] = period
            __props__.__dict__["power_status"] = power_status
            __props__.__dict__["primary_ip"] = primary_ip
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            __props__.__dict__["product_name"] = product_name
            __props__.__dict__["public_ssh_key_id"] = public_ssh_key_id
            __props__.__dict__["script"] = script
            __props__.__dict__["service_id"] = service_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vlan_id"] = vlan_id
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="hivelocity:index/bareMetalDevice:bareMetalDevice")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BareMetalDeviceDetail, __self__).__init__(
            'hivelocity:index/bareMetalDeviceDetail:BareMetalDeviceDetail',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bonded: Optional[pulumi.Input[bool]] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            force_device_id: Optional[pulumi.Input[int]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            ignition_id: Optional[pulumi.Input[int]] = None,
            last_updated: Optional[pulumi.Input[str]] = None,
            location_name: Optional[pulumi.Input[str]] = None,
            order_id: Optional[pulumi.Input[int]] = None,
            os_name: Optional[pulumi.Input[str]] = None,
            period: Optional[pulumi.Input[str]] = None,
            power_status: Optional[pulumi.Input[str]] = None,
            primary_ip: Optional[pulumi.Input[str]] = None,
            product_id: Optional[pulumi.Input[int]] = None,
            product_name: Optional[pulumi.Input[str]] = None,
            public_ssh_key_id: Optional[pulumi.Input[int]] = None,
            script: Optional[pulumi.Input[str]] = None,
            service_id: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            vlan_id: Optional[pulumi.Input[int]] = None) -> 'BareMetalDeviceDetail':
        """
        Get an existing BareMetalDeviceDetail resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bonded: When set, prefer only bonded devices
        :param pulumi.Input[int] device_id: Device ID
        :param pulumi.Input[int] force_device_id: Force deployment of this Device ID (internal use only)
        :param pulumi.Input[str] hostname: Hostname for this device
        :param pulumi.Input[int] ignition_id: IgnitionConfig ID
        :param pulumi.Input[str] last_updated: Last time this device was updated
        :param pulumi.Input[str] location_name: Deploy device in this location
        :param pulumi.Input[int] order_id: Order ID
        :param pulumi.Input[str] os_name: Operating system to install on device
        :param pulumi.Input[str] period: Billing period for device
        :param pulumi.Input[str] power_status: Power status
        :param pulumi.Input[str] primary_ip: Primary IP of device
        :param pulumi.Input[int] product_id: Product ID to pick from the stock
        :param pulumi.Input[str] product_name: Product Name
        :param pulumi.Input[int] public_ssh_key_id: ID of a SSH Key to apply for device
        :param pulumi.Input[str] script: Post-install script for device
        :param pulumi.Input[int] service_id: Service ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to apply for device
        :param pulumi.Input[int] vlan_id: VLAN ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BareMetalDeviceDetailState.__new__(_BareMetalDeviceDetailState)

        __props__.__dict__["bonded"] = bonded
        __props__.__dict__["device_id"] = device_id
        __props__.__dict__["force_device_id"] = force_device_id
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["ignition_id"] = ignition_id
        __props__.__dict__["last_updated"] = last_updated
        __props__.__dict__["location_name"] = location_name
        __props__.__dict__["order_id"] = order_id
        __props__.__dict__["os_name"] = os_name
        __props__.__dict__["period"] = period
        __props__.__dict__["power_status"] = power_status
        __props__.__dict__["primary_ip"] = primary_ip
        __props__.__dict__["product_id"] = product_id
        __props__.__dict__["product_name"] = product_name
        __props__.__dict__["public_ssh_key_id"] = public_ssh_key_id
        __props__.__dict__["script"] = script
        __props__.__dict__["service_id"] = service_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["vlan_id"] = vlan_id
        return BareMetalDeviceDetail(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bonded(self) -> pulumi.Output[Optional[bool]]:
        """
        When set, prefer only bonded devices
        """
        return pulumi.get(self, "bonded")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[int]:
        """
        Device ID
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="forceDeviceId")
    def force_device_id(self) -> pulumi.Output[Optional[int]]:
        """
        Force deployment of this Device ID (internal use only)
        """
        return pulumi.get(self, "force_device_id")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        Hostname for this device
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="ignitionId")
    def ignition_id(self) -> pulumi.Output[Optional[int]]:
        """
        IgnitionConfig ID
        """
        return pulumi.get(self, "ignition_id")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        """
        Last time this device was updated
        """
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> pulumi.Output[str]:
        """
        Deploy device in this location
        """
        return pulumi.get(self, "location_name")

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> pulumi.Output[int]:
        """
        Order ID
        """
        return pulumi.get(self, "order_id")

    @property
    @pulumi.getter(name="osName")
    def os_name(self) -> pulumi.Output[str]:
        """
        Operating system to install on device
        """
        return pulumi.get(self, "os_name")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[str]:
        """
        Billing period for device
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> pulumi.Output[str]:
        """
        Power status
        """
        return pulumi.get(self, "power_status")

    @property
    @pulumi.getter(name="primaryIp")
    def primary_ip(self) -> pulumi.Output[str]:
        """
        Primary IP of device
        """
        return pulumi.get(self, "primary_ip")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[int]:
        """
        Product ID to pick from the stock
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Output[str]:
        """
        Product Name
        """
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="publicSshKeyId")
    def public_ssh_key_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of a SSH Key to apply for device
        """
        return pulumi.get(self, "public_ssh_key_id")

    @property
    @pulumi.getter
    def script(self) -> pulumi.Output[Optional[str]]:
        """
        Post-install script for device
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[int]:
        """
        Service ID
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Tags to apply for device
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[Optional[int]]:
        """
        VLAN ID
        """
        warnings.warn("""This field is deprecated. Please use a VlanDetail resource instead.""", DeprecationWarning)
        pulumi.log.warn("""vlan_id is deprecated: This field is deprecated. Please use a VlanDetail resource instead.""")

        return pulumi.get(self, "vlan_id")

