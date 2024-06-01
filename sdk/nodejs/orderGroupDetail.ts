// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class OrderGroupDetail extends pulumi.CustomResource {
    /**
     * Get an existing OrderGroupDetail resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrderGroupDetailState, opts?: pulumi.CustomResourceOptions): OrderGroupDetail {
        return new OrderGroupDetail(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hivelocity:index/orderGroupDetail:OrderGroupDetail';

    /**
     * Returns true if the given object is an instance of OrderGroupDetail.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrderGroupDetail {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrderGroupDetail.__pulumiType;
    }

    /**
     * A list of Bare Metal Devices to deploy
     */
    public readonly bareMetalDevices!: pulumi.Output<outputs.OrderGroupDetailBareMetalDevice[]>;
    /**
     * Name of this Order Group
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Devices will be placed in the same rack
     */
    public readonly sameRack!: pulumi.Output<boolean>;

    /**
     * Create a OrderGroupDetail resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OrderGroupDetailArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrderGroupDetailArgs | OrderGroupDetailState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrderGroupDetailState | undefined;
            resourceInputs["bareMetalDevices"] = state ? state.bareMetalDevices : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["sameRack"] = state ? state.sameRack : undefined;
        } else {
            const args = argsOrState as OrderGroupDetailArgs | undefined;
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
        const aliasOpts = { aliases: [{ type: "hivelocity:index/orderGroup:orderGroup" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(OrderGroupDetail.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OrderGroupDetail resources.
 */
export interface OrderGroupDetailState {
    /**
     * A list of Bare Metal Devices to deploy
     */
    bareMetalDevices?: pulumi.Input<pulumi.Input<inputs.OrderGroupDetailBareMetalDevice>[]>;
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
 * The set of arguments for constructing a OrderGroupDetail resource.
 */
export interface OrderGroupDetailArgs {
    /**
     * A list of Bare Metal Devices to deploy
     */
    bareMetalDevices: pulumi.Input<pulumi.Input<inputs.OrderGroupDetailBareMetalDevice>[]>;
    /**
     * Name of this Order Group
     */
    name?: pulumi.Input<string>;
    /**
     * Devices will be placed in the same rack
     */
    sameRack: pulumi.Input<boolean>;
}