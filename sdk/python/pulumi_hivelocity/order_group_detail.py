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

__all__ = ['OrderGroupDetailArgs', 'OrderGroupDetail']

@pulumi.input_type
class OrderGroupDetailArgs:
    def __init__(__self__, *,
                 bare_metal_devices: pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]],
                 same_rack: pulumi.Input[bool],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrderGroupDetail resource.
        :param pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]] bare_metal_devices: A list of Bare Metal Devices to deploy
        :param pulumi.Input[bool] same_rack: Devices will be placed in the same rack
        :param pulumi.Input[str] name: Name of this Order Group
        """
        pulumi.set(__self__, "bare_metal_devices", bare_metal_devices)
        pulumi.set(__self__, "same_rack", same_rack)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="bareMetalDevices")
    def bare_metal_devices(self) -> pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]]:
        """
        A list of Bare Metal Devices to deploy
        """
        return pulumi.get(self, "bare_metal_devices")

    @bare_metal_devices.setter
    def bare_metal_devices(self, value: pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]]):
        pulumi.set(self, "bare_metal_devices", value)

    @property
    @pulumi.getter(name="sameRack")
    def same_rack(self) -> pulumi.Input[bool]:
        """
        Devices will be placed in the same rack
        """
        return pulumi.get(self, "same_rack")

    @same_rack.setter
    def same_rack(self, value: pulumi.Input[bool]):
        pulumi.set(self, "same_rack", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this Order Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _OrderGroupDetailState:
    def __init__(__self__, *,
                 bare_metal_devices: Optional[pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 same_rack: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering OrderGroupDetail resources.
        :param pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]] bare_metal_devices: A list of Bare Metal Devices to deploy
        :param pulumi.Input[str] name: Name of this Order Group
        :param pulumi.Input[bool] same_rack: Devices will be placed in the same rack
        """
        if bare_metal_devices is not None:
            pulumi.set(__self__, "bare_metal_devices", bare_metal_devices)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if same_rack is not None:
            pulumi.set(__self__, "same_rack", same_rack)

    @property
    @pulumi.getter(name="bareMetalDevices")
    def bare_metal_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]]]:
        """
        A list of Bare Metal Devices to deploy
        """
        return pulumi.get(self, "bare_metal_devices")

    @bare_metal_devices.setter
    def bare_metal_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrderGroupDetailBareMetalDeviceArgs']]]]):
        pulumi.set(self, "bare_metal_devices", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this Order Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sameRack")
    def same_rack(self) -> Optional[pulumi.Input[bool]]:
        """
        Devices will be placed in the same rack
        """
        return pulumi.get(self, "same_rack")

    @same_rack.setter
    def same_rack(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "same_rack", value)


class OrderGroupDetail(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bare_metal_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrderGroupDetailBareMetalDeviceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 same_rack: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a OrderGroupDetail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrderGroupDetailBareMetalDeviceArgs']]]] bare_metal_devices: A list of Bare Metal Devices to deploy
        :param pulumi.Input[str] name: Name of this Order Group
        :param pulumi.Input[bool] same_rack: Devices will be placed in the same rack
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrderGroupDetailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OrderGroupDetail resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OrderGroupDetailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrderGroupDetailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bare_metal_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrderGroupDetailBareMetalDeviceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 same_rack: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrderGroupDetailArgs.__new__(OrderGroupDetailArgs)

            if bare_metal_devices is None and not opts.urn:
                raise TypeError("Missing required property 'bare_metal_devices'")
            __props__.__dict__["bare_metal_devices"] = bare_metal_devices
            __props__.__dict__["name"] = name
            if same_rack is None and not opts.urn:
                raise TypeError("Missing required property 'same_rack'")
            __props__.__dict__["same_rack"] = same_rack
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="hivelocity:index/orderGroup:orderGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OrderGroupDetail, __self__).__init__(
            'hivelocity:index/orderGroupDetail:OrderGroupDetail',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bare_metal_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrderGroupDetailBareMetalDeviceArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            same_rack: Optional[pulumi.Input[bool]] = None) -> 'OrderGroupDetail':
        """
        Get an existing OrderGroupDetail resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrderGroupDetailBareMetalDeviceArgs']]]] bare_metal_devices: A list of Bare Metal Devices to deploy
        :param pulumi.Input[str] name: Name of this Order Group
        :param pulumi.Input[bool] same_rack: Devices will be placed in the same rack
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrderGroupDetailState.__new__(_OrderGroupDetailState)

        __props__.__dict__["bare_metal_devices"] = bare_metal_devices
        __props__.__dict__["name"] = name
        __props__.__dict__["same_rack"] = same_rack
        return OrderGroupDetail(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bareMetalDevices")
    def bare_metal_devices(self) -> pulumi.Output[Sequence['outputs.OrderGroupDetailBareMetalDevice']]:
        """
        A list of Bare Metal Devices to deploy
        """
        return pulumi.get(self, "bare_metal_devices")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of this Order Group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sameRack")
    def same_rack(self) -> pulumi.Output[bool]:
        """
        Devices will be placed in the same rack
        """
        return pulumi.get(self, "same_rack")

