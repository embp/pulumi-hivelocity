// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class SshKeyDetail extends pulumi.CustomResource {
    /**
     * Get an existing SshKeyDetail resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SshKeyDetailState, opts?: pulumi.CustomResourceOptions): SshKeyDetail {
        return new SshKeyDetail(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hivelocity:index/sshKeyDetail:SshKeyDetail';

    /**
     * Returns true if the given object is an instance of SshKeyDetail.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SshKeyDetail {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SshKeyDetail.__pulumiType;
    }

    public readonly name!: pulumi.Output<string>;
    public readonly publicKey!: pulumi.Output<string>;
    public readonly sshKeyId!: pulumi.Output<number>;

    /**
     * Create a SshKeyDetail resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SshKeyDetailArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SshKeyDetailArgs | SshKeyDetailState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SshKeyDetailState | undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["publicKey"] = state ? state.publicKey : undefined;
            resourceInputs["sshKeyId"] = state ? state.sshKeyId : undefined;
        } else {
            const args = argsOrState as SshKeyDetailArgs | undefined;
            if ((!args || args.publicKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicKey'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["sshKeyId"] = args ? args.sshKeyId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "hivelocity:index/sshKey:sshKey" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(SshKeyDetail.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SshKeyDetail resources.
 */
export interface SshKeyDetailState {
    name?: pulumi.Input<string>;
    publicKey?: pulumi.Input<string>;
    sshKeyId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a SshKeyDetail resource.
 */
export interface SshKeyDetailArgs {
    name?: pulumi.Input<string>;
    publicKey: pulumi.Input<string>;
    sshKeyId?: pulumi.Input<number>;
}