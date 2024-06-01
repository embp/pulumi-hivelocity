// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hivelocity
{
    public static class GetSshKey
    {
        public static Task<GetSshKeyResult> InvokeAsync(GetSshKeyArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSshKeyResult>("hivelocity:index/getSshKey:getSshKey", args ?? new GetSshKeyArgs(), options.WithDefaults());

        public static Output<GetSshKeyResult> Invoke(GetSshKeyInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSshKeyResult>("hivelocity:index/getSshKey:getSshKey", args ?? new GetSshKeyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSshKeyArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetSshKeyFilterArgs>? _filters;
        public List<Inputs.GetSshKeyFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetSshKeyFilterArgs>());
            set => _filters = value;
        }

        [Input("first")]
        public bool? First { get; set; }

        public GetSshKeyArgs()
        {
        }
        public static new GetSshKeyArgs Empty => new GetSshKeyArgs();
    }

    public sealed class GetSshKeyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetSshKeyFilterInputArgs>? _filters;
        public InputList<Inputs.GetSshKeyFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetSshKeyFilterInputArgs>());
            set => _filters = value;
        }

        [Input("first")]
        public Input<bool>? First { get; set; }

        public GetSshKeyInvokeArgs()
        {
        }
        public static new GetSshKeyInvokeArgs Empty => new GetSshKeyInvokeArgs();
    }


    [OutputType]
    public sealed class GetSshKeyResult
    {
        public readonly ImmutableArray<Outputs.GetSshKeyFilterResult> Filters;
        public readonly bool? First;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string PublicKey;
        public readonly int SshKeyId;

        [OutputConstructor]
        private GetSshKeyResult(
            ImmutableArray<Outputs.GetSshKeyFilterResult> filters,

            bool? first,

            string id,

            string name,

            string publicKey,

            int sshKeyId)
        {
            Filters = filters;
            First = first;
            Id = id;
            Name = name;
            PublicKey = publicKey;
            SshKeyId = sshKeyId;
        }
    }
}