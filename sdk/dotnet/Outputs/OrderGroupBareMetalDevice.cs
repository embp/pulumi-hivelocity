// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity.Outputs
{

    [OutputType]
    public sealed class OrderGroupBareMetalDevice
    {
        /// <summary>
        /// When set, prefer only bonded devices
        /// </summary>
        public readonly bool? Bonded;
        /// <summary>
        /// Device ID
        /// </summary>
        public readonly int? DeviceId;
        /// <summary>
        /// Force deployment of this Device ID (internal use only)
        /// </summary>
        public readonly int? ForceDeviceId;
        /// <summary>
        /// Hostname for this device
        /// </summary>
        public readonly string Hostname;
        /// <summary>
        /// IgnitionConfig ID
        /// </summary>
        public readonly int? IgnitionId;
        /// <summary>
        /// Last time this device was updated
        /// </summary>
        public readonly string? LastUpdated;
        /// <summary>
        /// Deploy device in this location
        /// </summary>
        public readonly string LocationName;
        /// <summary>
        /// Order ID
        /// </summary>
        public readonly int? OrderId;
        /// <summary>
        /// Operating system to install on device
        /// </summary>
        public readonly string OsName;
        /// <summary>
        /// Billing period for device
        /// </summary>
        public readonly string? Period;
        /// <summary>
        /// Power status
        /// </summary>
        public readonly string? PowerStatus;
        /// <summary>
        /// Primary IP of device
        /// </summary>
        public readonly string? PrimaryIp;
        /// <summary>
        /// Product ID to pick from the stock
        /// </summary>
        public readonly int ProductId;
        /// <summary>
        /// Product Name
        /// </summary>
        public readonly string? ProductName;
        /// <summary>
        /// ID of a SSH Key to apply for device
        /// </summary>
        public readonly int? PublicSshKeyId;
        /// <summary>
        /// Post-install script for device
        /// </summary>
        public readonly string? Script;
        /// <summary>
        /// Service ID
        /// </summary>
        public readonly int? ServiceId;
        /// <summary>
        /// Tags to apply for device
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// VLAN ID
        /// </summary>
        public readonly int? VlanId;

        [OutputConstructor]
        private OrderGroupBareMetalDevice(
            bool? bonded,

            int? deviceId,

            int? forceDeviceId,

            string hostname,

            int? ignitionId,

            string? lastUpdated,

            string locationName,

            int? orderId,

            string osName,

            string? period,

            string? powerStatus,

            string? primaryIp,

            int productId,

            string? productName,

            int? publicSshKeyId,

            string? script,

            int? serviceId,

            ImmutableArray<string> tags,

            int? vlanId)
        {
            Bonded = bonded;
            DeviceId = deviceId;
            ForceDeviceId = forceDeviceId;
            Hostname = hostname;
            IgnitionId = ignitionId;
            LastUpdated = lastUpdated;
            LocationName = locationName;
            OrderId = orderId;
            OsName = osName;
            Period = period;
            PowerStatus = powerStatus;
            PrimaryIp = primaryIp;
            ProductId = productId;
            ProductName = productName;
            PublicSshKeyId = publicSshKeyId;
            Script = script;
            ServiceId = serviceId;
            Tags = tags;
            VlanId = vlanId;
        }
    }
}
