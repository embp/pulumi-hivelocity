// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getEffectiveIgnition(args: GetEffectiveIgnitionArgs, opts?: pulumi.InvokeOptions): Promise<GetEffectiveIgnitionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("hivelocity:index/getEffectiveIgnition:getEffectiveIgnition", {
        "deviceId": args.deviceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getEffectiveIgnition.
 */
export interface GetEffectiveIgnitionArgs {
    deviceId: number;
}

/**
 * A collection of values returned by getEffectiveIgnition.
 */
export interface GetEffectiveIgnitionResult {
    readonly contents: string;
    readonly deviceId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
export function getEffectiveIgnitionOutput(args: GetEffectiveIgnitionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEffectiveIgnitionResult> {
    return pulumi.output(args).apply((a: any) => getEffectiveIgnition(a, opts))
}

/**
 * A collection of arguments for invoking getEffectiveIgnition.
 */
export interface GetEffectiveIgnitionOutputArgs {
    deviceId: pulumi.Input<number>;
}
