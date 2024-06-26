// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    [HivelocityResourceType("hivelocity:index/ignitionDetail:IgnitionDetail")]
    public partial class IgnitionDetail : global::Pulumi.CustomResource
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
        /// Create a IgnitionDetail resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IgnitionDetail(string name, IgnitionDetailArgs args, CustomResourceOptions? options = null)
            : base("hivelocity:index/ignitionDetail:IgnitionDetail", name, args ?? new IgnitionDetailArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IgnitionDetail(string name, Input<string> id, IgnitionDetailState? state = null, CustomResourceOptions? options = null)
            : base("hivelocity:index/ignitionDetail:IgnitionDetail", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "hivelocity:index/ignition:ignition" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing IgnitionDetail resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IgnitionDetail Get(string name, Input<string> id, IgnitionDetailState? state = null, CustomResourceOptions? options = null)
        {
            return new IgnitionDetail(name, id, state, options);
        }
    }

    public sealed class IgnitionDetailArgs : global::Pulumi.ResourceArgs
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

        public IgnitionDetailArgs()
        {
        }
        public static new IgnitionDetailArgs Empty => new IgnitionDetailArgs();
    }

    public sealed class IgnitionDetailState : global::Pulumi.ResourceArgs
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

        public IgnitionDetailState()
        {
        }
        public static new IgnitionDetailState Empty => new IgnitionDetailState();
    }
}
