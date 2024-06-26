// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    [HivelocityResourceType("hivelocity:index/vlanDetail:VlanDetail")]
    public partial class VlanDetail : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Location where to create this VLAN
        /// </summary>
        [Output("facilityCode")]
        public Output<string> FacilityCode { get; private set; } = null!;

        /// <summary>
        /// IDs of ports to include in this VLAN
        /// </summary>
        [Output("portIds")]
        public Output<ImmutableArray<int>> PortIds { get; private set; } = null!;

        /// <summary>
        /// Tag ID of VLAN
        /// </summary>
        [Output("tagId")]
        public Output<int> TagId { get; private set; } = null!;

        /// <summary>
        /// Type of VLAN to be created, can be either `private` or `public`
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a VlanDetail resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VlanDetail(string name, VlanDetailArgs args, CustomResourceOptions? options = null)
            : base("hivelocity:index/vlanDetail:VlanDetail", name, args ?? new VlanDetailArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VlanDetail(string name, Input<string> id, VlanDetailState? state = null, CustomResourceOptions? options = null)
            : base("hivelocity:index/vlanDetail:VlanDetail", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "hivelocity:index/vlan:vlan" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VlanDetail resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VlanDetail Get(string name, Input<string> id, VlanDetailState? state = null, CustomResourceOptions? options = null)
        {
            return new VlanDetail(name, id, state, options);
        }
    }

    public sealed class VlanDetailArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Location where to create this VLAN
        /// </summary>
        [Input("facilityCode", required: true)]
        public Input<string> FacilityCode { get; set; } = null!;

        [Input("portIds", required: true)]
        private InputList<int>? _portIds;

        /// <summary>
        /// IDs of ports to include in this VLAN
        /// </summary>
        public InputList<int> PortIds
        {
            get => _portIds ?? (_portIds = new InputList<int>());
            set => _portIds = value;
        }

        /// <summary>
        /// Type of VLAN to be created, can be either `private` or `public`
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public VlanDetailArgs()
        {
        }
        public static new VlanDetailArgs Empty => new VlanDetailArgs();
    }

    public sealed class VlanDetailState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Location where to create this VLAN
        /// </summary>
        [Input("facilityCode")]
        public Input<string>? FacilityCode { get; set; }

        [Input("portIds")]
        private InputList<int>? _portIds;

        /// <summary>
        /// IDs of ports to include in this VLAN
        /// </summary>
        public InputList<int> PortIds
        {
            get => _portIds ?? (_portIds = new InputList<int>());
            set => _portIds = value;
        }

        /// <summary>
        /// Tag ID of VLAN
        /// </summary>
        [Input("tagId")]
        public Input<int>? TagId { get; set; }

        /// <summary>
        /// Type of VLAN to be created, can be either `private` or `public`
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public VlanDetailState()
        {
        }
        public static new VlanDetailState Empty => new VlanDetailState();
    }
}
