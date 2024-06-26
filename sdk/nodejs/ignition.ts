// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * @deprecated hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail
 */
export class Ignition extends pulumi.CustomResource {
    /**
     * Get an existing Ignition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IgnitionState, opts?: pulumi.CustomResourceOptions): Ignition {
        pulumi.log.warn("Ignition is deprecated: hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail")
        return new Ignition(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hivelocity:index/ignition:ignition';

    /**
     * Returns true if the given object is an instance of Ignition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ignition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ignition.__pulumiType;
    }

    /**
     * String of the JSON contents of the ignition file
     */
    public readonly contents!: pulumi.Output<string>;
    /**
     * Name of ignition file resource
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a Ignition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail */
    constructor(name: string, args: IgnitionArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail */
    constructor(name: string, argsOrState?: IgnitionArgs | IgnitionState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Ignition is deprecated: hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IgnitionState | undefined;
            resourceInputs["contents"] = state ? state.contents : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as IgnitionArgs | undefined;
            if ((!args || args.contents === undefined) && !opts.urn) {
                throw new Error("Missing required property 'contents'");
            }
            resourceInputs["contents"] = args ? args.contents : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Ignition.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ignition resources.
 */
export interface IgnitionState {
    /**
     * String of the JSON contents of the ignition file
     */
    contents?: pulumi.Input<string>;
    /**
     * Name of ignition file resource
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Ignition resource.
 */
export interface IgnitionArgs {
    /**
     * String of the JSON contents of the ignition file
     */
    contents: pulumi.Input<string>;
    /**
     * Name of ignition file resource
     */
    name?: pulumi.Input<string>;
}
