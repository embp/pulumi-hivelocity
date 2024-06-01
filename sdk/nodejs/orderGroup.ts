// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * @deprecated hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail
 */
export class OrderGroup extends pulumi.CustomResource {
    /**
     * Get an existing OrderGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrderGroupState, opts?: pulumi.CustomResourceOptions): OrderGroup {
        pulumi.log.warn("OrderGroup is deprecated: hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail")
        return new OrderGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hivelocity:index/orderGroup:orderGroup';

    /**
     * Returns true if the given object is an instance of OrderGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrderGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrderGroup.__pulumiType;
    }

    /**
     * A list of Bare Metal Devices to deploy
     */
    public readonly bareMetalDevices!: pulumi.Output<outputs.OrderGroupBareMetalDevice[]>;
    /**
     * Name of this Order Group
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Devices will be placed in the same rack
     */
    public readonly sameRack!: pulumi.Output<boolean>;

    /**
     * Create a OrderGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail */
    constructor(name: string, args: OrderGroupArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail */
    constructor(name: string, argsOrState?: OrderGroupArgs | OrderGroupState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("OrderGroup is deprecated: hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrderGroupState | undefined;
            resourceInputs["bareMetalDevices"] = state ? state.bareMetalDevices : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["sameRack"] = state ? state.sameRack : undefined;
        } else {
            const args = argsOrState as OrderGroupArgs | undefined;
            if ((!args || args.bareMetalDevices === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bareMetalDevices'");
            }
            if ((!args || args.sameRack === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sameRack'");
            }
            resourceInputs["bareMetalDevices"] = args ? args.bareMetalDevices : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["sameRack"] = args ? args.sameRack : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OrderGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering orderGroup resources.
 */
export interface OrderGroupState {
    /**
     * A list of Bare Metal Devices to deploy
     */
    bareMetalDevices?: pulumi.Input<pulumi.Input<inputs.OrderGroupBareMetalDevice>[]>;
    /**
     * Name of this Order Group
     */
    name?: pulumi.Input<string>;
    /**
     * Devices will be placed in the same rack
     */
    sameRack?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a OrderGroup resource.
 */
export interface OrderGroupArgs {
    /**
     * A list of Bare Metal Devices to deploy
     */
    bareMetalDevices: pulumi.Input<pulumi.Input<inputs.OrderGroupBareMetalDevice>[]>;
    /**
     * Name of this Order Group
     */
    name?: pulumi.Input<string>;
    /**
     * Devices will be placed in the same rack
     */
    sameRack: pulumi.Input<boolean>;
}
