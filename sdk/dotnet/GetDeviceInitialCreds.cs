// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    public static class GetDeviceInitialCreds
    {
        public static Task<GetDeviceInitialCredsResult> InvokeAsync(GetDeviceInitialCredsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDeviceInitialCredsResult>("hivelocity:index/getDeviceInitialCreds:getDeviceInitialCreds", args ?? new GetDeviceInitialCredsArgs(), options.WithDefaults());

        public static Output<GetDeviceInitialCredsResult> Invoke(GetDeviceInitialCredsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDeviceInitialCredsResult>("hivelocity:index/getDeviceInitialCreds:getDeviceInitialCreds", args ?? new GetDeviceInitialCredsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDeviceInitialCredsArgs : global::Pulumi.InvokeArgs
    {
        [Input("deviceId", required: true)]
        public int DeviceId { get; set; }

        public GetDeviceInitialCredsArgs()
        {
        }
        public static new GetDeviceInitialCredsArgs Empty => new GetDeviceInitialCredsArgs();
    }

    public sealed class GetDeviceInitialCredsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("deviceId", required: true)]
        public Input<int> DeviceId { get; set; } = null!;

        public GetDeviceInitialCredsInvokeArgs()
        {
        }
        public static new GetDeviceInitialCredsInvokeArgs Empty => new GetDeviceInitialCredsInvokeArgs();
    }


    [OutputType]
    public sealed class GetDeviceInitialCredsResult
    {
        public readonly int DeviceId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string LockerUrl;
        public readonly string Password;
        public readonly int Port;
        public readonly string User;

        [OutputConstructor]
        private GetDeviceInitialCredsResult(
            int deviceId,

            string id,

            string lockerUrl,

            string password,

            int port,

            string user)
        {
            DeviceId = deviceId;
            Id = id;
            LockerUrl = lockerUrl;
            Password = password;
            Port = port;
            User = user;
        }
    }
}