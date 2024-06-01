// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    [Obsolete(@"hivelocity.index/ignition.ignition has been deprecated in favor of hivelocity.index/ignitiondetail.IgnitionDetail")]
    [HivelocityResourceType("hivelocity:index/ignition:ignition")]
    public partial class Ignition : global::Pulumi.CustomResource
    {
        /// <summary>
        /// String of the JSON contents of the ignition file
        /// </summary>
        [Output("contents")]
        public Output<string> Contents { get; private set; } = null!;

        /// <summary>
        /// Name of ignition file resource
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Ignition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Ignition(string name, IgnitionArgs args, CustomResourceOptions? options = null)
            : base("hivelocity:index/ignition:ignition", name, args ?? new IgnitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Ignition(string name, Input<string> id, IgnitionState? state = null, CustomResourceOptions? options = null)
            : base("hivelocity:index/ignition:ignition", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Ignition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Ignition Get(string name, Input<string> id, IgnitionState? state = null, CustomResourceOptions? options = null)
        {
            return new Ignition(name, id, state, options);
        }
    }

    public sealed class IgnitionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// String of the JSON contents of the ignition file
        /// </summary>
        [Input("contents", required: true)]
        public Input<string> Contents { get; set; } = null!;

        /// <summary>
        /// Name of ignition file resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public IgnitionArgs()
        {
        }
        public static new IgnitionArgs Empty => new IgnitionArgs();
    }

    public sealed class IgnitionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// String of the JSON contents of the ignition file
        /// </summary>
        [Input("contents")]
        public Input<string>? Contents { get; set; }

        /// <summary>
        /// Name of ignition file resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public IgnitionState()
        {
        }
        public static new IgnitionState Empty => new IgnitionState();
    }
}