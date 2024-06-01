// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    public static class GetDevice
    {
        public static Task<GetDeviceResult> InvokeAsync(GetDeviceArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDeviceResult>("hivelocity:index/getDevice:getDevice", args ?? new GetDeviceArgs(), options.WithDefaults());

        public static Output<GetDeviceResult> Invoke(GetDeviceInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDeviceResult>("hivelocity:index/getDevice:getDevice", args ?? new GetDeviceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDeviceArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetDeviceFilterArgs>? _filters;
        public List<Inputs.GetDeviceFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetDeviceFilterArgs>());
            set => _filters = value;
        }

        [Input("first")]
        public bool? First { get; set; }

        public GetDeviceArgs()
        {
        }
        public static new GetDeviceArgs Empty => new GetDeviceArgs();
    }

    public sealed class GetDeviceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetDeviceFilterInputArgs>? _filters;
        public InputList<Inputs.GetDeviceFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetDeviceFilterInputArgs>());
            set => _filters = value;
        }

        [Input("first")]
        public Input<bool>? First { get; set; }

        public GetDeviceInvokeArgs()
        {
        }
        public static new GetDeviceInvokeArgs Empty => new GetDeviceInvokeArgs();
    }


    [OutputType]
    public sealed class GetDeviceResult
    {
        public readonly int DeviceId;
        public readonly string DeviceType;
        public readonly ImmutableArray<Outputs.GetDeviceFilterResult> Filters;
        public readonly bool? First;
        public readonly string Hostname;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<string> IpAddresses;
        public readonly string IpmiAddress;
        public readonly bool IpmiEnabled;
        public readonly ImmutableDictionary<string, string> Location;
        public readonly ImmutableDictionary<string, string> Metadata;
        public readonly string Name;
        public readonly string PowerStatus;
        public readonly int ServicePlan;
        public readonly string Status;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetDeviceResult(
            int deviceId,

            string deviceType,

            ImmutableArray<Outputs.GetDeviceFilterResult> filters,

            bool? first,

            string hostname,

            string id,

            ImmutableArray<string> ipAddresses,

            string ipmiAddress,

            bool ipmiEnabled,

            ImmutableDictionary<string, string> location,

            ImmutableDictionary<string, string> metadata,

            string name,

            string powerStatus,

            int servicePlan,

            string status,

            ImmutableArray<string> tags)
        {
            DeviceId = deviceId;
            DeviceType = deviceType;
            Filters = filters;
            First = first;
            Hostname = hostname;
            Id = id;
            IpAddresses = ipAddresses;
            IpmiAddress = ipmiAddress;
            IpmiEnabled = ipmiEnabled;
            Location = location;
            Metadata = metadata;
            Name = name;
            PowerStatus = powerStatus;
            ServicePlan = servicePlan;
            Status = status;
            Tags = tags;
        }
    }
}