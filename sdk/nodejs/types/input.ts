// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface GetBareMetalDeviceFilter {
    name: string;
    values: string[];
}

export interface GetBareMetalDeviceFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetDeviceFilter {
    name: string;
    values: string[];
}

export interface GetDeviceFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetDevicePortFilter {
    name: string;
    values: string[];
}

export interface GetDevicePortFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetHivelocityDevicePortFilter {
    name: string;
    values: string[];
}

export interface GetHivelocityDevicePortFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetProductFilter {
    name: string;
    values: string[];
}

export interface GetProductFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetSshKeyFilter {
    name: string;
    values: string[];
}

export interface GetSshKeyFilterArgs {
    name: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface OrderGroupBareMetalDevice {
    /**
     * When set, prefer only bonded devices
     */
    bonded?: pulumi.Input<boolean>;
    /**
     * Device ID
     */
    deviceId?: pulumi.Input<number>;
    /**
     * Force deployment of this Device ID (internal use only)
     */
    forceDeviceId?: pulumi.Input<number>;
    /**
     * Hostname for this device
     */
    hostname: pulumi.Input<string>;
    /**
     * IgnitionConfig ID
     */
    ignitionId?: pulumi.Input<number>;
    /**
     * Last time this device was updated
     */
    lastUpdated?: pulumi.Input<string>;
    /**
     * Deploy device in this location
     */
    locationName: pulumi.Input<string>;
    /**
     * Order ID
     */
    orderId?: pulumi.Input<number>;
    /**
     * Operating system to install on device
     */
    osName: pulumi.Input<string>;
    /**
     * Billing period for device
     */
    period?: pulumi.Input<string>;
    /**
     * Power status
     */
    powerStatus?: pulumi.Input<string>;
    /**
     * Primary IP of device
     */
    primaryIp?: pulumi.Input<string>;
    /**
     * Product ID to pick from the stock
     */
    productId: pulumi.Input<number>;
    /**
     * Product Name
     */
    productName?: pulumi.Input<string>;
    /**
     * ID of a SSH Key to apply for device
     */
    publicSshKeyId?: pulumi.Input<number>;
    /**
     * Post-install script for device
     */
    script?: pulumi.Input<string>;
    /**
     * Service ID
     */
    serviceId?: pulumi.Input<number>;
    /**
     * Tags to apply for device
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VLAN ID
     *
     * @deprecated This field is deprecated. Please use a hivelocity.VlanDetail resource instead.
     */
    vlanId?: pulumi.Input<number>;
}

export interface OrderGroupDetailBareMetalDevice {
    /**
     * When set, prefer only bonded devices
     */
    bonded?: pulumi.Input<boolean>;
    /**
     * Device ID
     */
    deviceId?: pulumi.Input<number>;
    /**
     * Force deployment of this Device ID (internal use only)
     */
    forceDeviceId?: pulumi.Input<number>;
    /**
     * Hostname for this device
     */
    hostname: pulumi.Input<string>;
    /**
     * IgnitionConfig ID
     */
    ignitionId?: pulumi.Input<number>;
    /**
     * Last time this device was updated
     */
    lastUpdated?: pulumi.Input<string>;
    /**
     * Deploy device in this location
     */
    locationName: pulumi.Input<string>;
    /**
     * Order ID
     */
    orderId?: pulumi.Input<number>;
    /**
     * Operating system to install on device
     */
    osName: pulumi.Input<string>;
    /**
     * Billing period for device
     */
    period?: pulumi.Input<string>;
    /**
     * Power status
     */
    powerStatus?: pulumi.Input<string>;
    /**
     * Primary IP of device
     */
    primaryIp?: pulumi.Input<string>;
    /**
     * Product ID to pick from the stock
     */
    productId: pulumi.Input<number>;
    /**
     * Product Name
     */
    productName?: pulumi.Input<string>;
    /**
     * ID of a SSH Key to apply for device
     */
    publicSshKeyId?: pulumi.Input<number>;
    /**
     * Post-install script for device
     */
    script?: pulumi.Input<string>;
    /**
     * Service ID
     */
    serviceId?: pulumi.Input<number>;
    /**
     * Tags to apply for device
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VLAN ID
     *
     * @deprecated This field is deprecated. Please use a hivelocity.VlanDetail resource instead.
     */
    vlanId?: pulumi.Input<number>;
}
