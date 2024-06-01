// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class VlanDetail extends pulumi.CustomResource {
    /**
     * Get an existing VlanDetail resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VlanDetailState, opts?: pulumi.CustomResourceOptions): VlanDetail {
        return new VlanDetail(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hivelocity:index/vlanDetail:VlanDetail';

    /**
     * Returns true if the given object is an instance of VlanDetail.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VlanDetail {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VlanDetail.__pulumiType;
    }

    /**
     * Location where to create this VLAN
     */
    public readonly facilityCode!: pulumi.Output<string>;
    /**
     * IDs of ports to include in this VLAN
     */
    public readonly portIds!: pulumi.Output<number[]>;
    /**
     * Tag ID of VLAN
     */
    public /*out*/ readonly tagId!: pulumi.Output<number>;
    /**
     * Type of VLAN to be created, can be either `private` or `public`
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a VlanDetail resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VlanDetailArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VlanDetailArgs | VlanDetailState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VlanDetailState | undefined;
            resourceInputs["facilityCode"] = state ? state.facilityCode : undefined;
            resourceInputs["portIds"] = state ? state.portIds : undefined;
            resourceInputs["tagId"] = state ? state.tagId : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as VlanDetailArgs | undefined;
            if ((!args || args.facilityCode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'facilityCode'");
            }
            if ((!args || args.portIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'portIds'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["facilityCode"] = args ? args.facilityCode : undefined;
            resourceInputs["portIds"] = args ? args.portIds : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["tagId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "hivelocity:index/vlan:vlan" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(VlanDetail.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VlanDetail resources.
 */
export interface VlanDetailState {
    /**
     * Location where to create this VLAN
     */
    facilityCode?: pulumi.Input<string>;
    /**
     * IDs of ports to include in this VLAN
     */
    portIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Tag ID of VLAN
     */
    tagId?: pulumi.Input<number>;
    /**
     * Type of VLAN to be created, can be either `private` or `public`
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VlanDetail resource.
 */
export interface VlanDetailArgs {
    /**
     * Location where to create this VLAN
     */
    facilityCode: pulumi.Input<string>;
    /**
     * IDs of ports to include in this VLAN
     */
    portIds: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Type of VLAN to be created, can be either `private` or `public`
     */
    type: pulumi.Input<string>;
}
