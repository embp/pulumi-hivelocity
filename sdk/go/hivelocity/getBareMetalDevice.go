// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hivelocity

import (
	"context"
	"reflect"

	"github.com/embp/pulumi-hivelocity/sdk/go/hivelocity/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupBareMetalDevice(ctx *pulumi.Context, args *LookupBareMetalDeviceArgs, opts ...pulumi.InvokeOption) (*LookupBareMetalDeviceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBareMetalDeviceResult
	err := ctx.Invoke("hivelocity:index/getBareMetalDevice:getBareMetalDevice", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBareMetalDevice.
type LookupBareMetalDeviceArgs struct {
	DeviceId       *int                       `pulumi:"deviceId"`
	Filters        []GetBareMetalDeviceFilter `pulumi:"filters"`
	First          *bool                      `pulumi:"first"`
	Hostname       *string                    `pulumi:"hostname"`
	LastUpdated    *string                    `pulumi:"lastUpdated"`
	LocationName   *string                    `pulumi:"locationName"`
	OrderId        *int                       `pulumi:"orderId"`
	OsName         *string                    `pulumi:"osName"`
	Period         *string                    `pulumi:"period"`
	PowerStatus    *string                    `pulumi:"powerStatus"`
	PrimaryIp      *string                    `pulumi:"primaryIp"`
	ProductId      *int                       `pulumi:"productId"`
	ProductName    *string                    `pulumi:"productName"`
	PublicSshKeyId *int                       `pulumi:"publicSshKeyId"`
	Script         *string                    `pulumi:"script"`
	ServiceId      *int                       `pulumi:"serviceId"`
	Tags           []string                   `pulumi:"tags"`
	VlanId         *int                       `pulumi:"vlanId"`
}

// A collection of values returned by getBareMetalDevice.
type LookupBareMetalDeviceResult struct {
	DeviceId int                        `pulumi:"deviceId"`
	Filters  []GetBareMetalDeviceFilter `pulumi:"filters"`
	First    *bool                      `pulumi:"first"`
	Hostname string                     `pulumi:"hostname"`
	// The provider-assigned unique ID for this managed resource.
	Id             string   `pulumi:"id"`
	LastUpdated    string   `pulumi:"lastUpdated"`
	LocationName   string   `pulumi:"locationName"`
	OrderId        int      `pulumi:"orderId"`
	OsName         string   `pulumi:"osName"`
	Period         string   `pulumi:"period"`
	PowerStatus    string   `pulumi:"powerStatus"`
	PrimaryIp      string   `pulumi:"primaryIp"`
	ProductId      int      `pulumi:"productId"`
	ProductName    string   `pulumi:"productName"`
	PublicSshKeyId *int     `pulumi:"publicSshKeyId"`
	Script         string   `pulumi:"script"`
	ServiceId      int      `pulumi:"serviceId"`
	Tags           []string `pulumi:"tags"`
	VlanId         *int     `pulumi:"vlanId"`
}

func LookupBareMetalDeviceOutput(ctx *pulumi.Context, args LookupBareMetalDeviceOutputArgs, opts ...pulumi.InvokeOption) LookupBareMetalDeviceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBareMetalDeviceResult, error) {
			args := v.(LookupBareMetalDeviceArgs)
			r, err := LookupBareMetalDevice(ctx, &args, opts...)
			var s LookupBareMetalDeviceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBareMetalDeviceResultOutput)
}

// A collection of arguments for invoking getBareMetalDevice.
type LookupBareMetalDeviceOutputArgs struct {
	DeviceId       pulumi.IntPtrInput                 `pulumi:"deviceId"`
	Filters        GetBareMetalDeviceFilterArrayInput `pulumi:"filters"`
	First          pulumi.BoolPtrInput                `pulumi:"first"`
	Hostname       pulumi.StringPtrInput              `pulumi:"hostname"`
	LastUpdated    pulumi.StringPtrInput              `pulumi:"lastUpdated"`
	LocationName   pulumi.StringPtrInput              `pulumi:"locationName"`
	OrderId        pulumi.IntPtrInput                 `pulumi:"orderId"`
	OsName         pulumi.StringPtrInput              `pulumi:"osName"`
	Period         pulumi.StringPtrInput              `pulumi:"period"`
	PowerStatus    pulumi.StringPtrInput              `pulumi:"powerStatus"`
	PrimaryIp      pulumi.StringPtrInput              `pulumi:"primaryIp"`
	ProductId      pulumi.IntPtrInput                 `pulumi:"productId"`
	ProductName    pulumi.StringPtrInput              `pulumi:"productName"`
	PublicSshKeyId pulumi.IntPtrInput                 `pulumi:"publicSshKeyId"`
	Script         pulumi.StringPtrInput              `pulumi:"script"`
	ServiceId      pulumi.IntPtrInput                 `pulumi:"serviceId"`
	Tags           pulumi.StringArrayInput            `pulumi:"tags"`
	VlanId         pulumi.IntPtrInput                 `pulumi:"vlanId"`
}

func (LookupBareMetalDeviceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBareMetalDeviceArgs)(nil)).Elem()
}

// A collection of values returned by getBareMetalDevice.
type LookupBareMetalDeviceResultOutput struct{ *pulumi.OutputState }

func (LookupBareMetalDeviceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBareMetalDeviceResult)(nil)).Elem()
}

func (o LookupBareMetalDeviceResultOutput) ToLookupBareMetalDeviceResultOutput() LookupBareMetalDeviceResultOutput {
	return o
}

func (o LookupBareMetalDeviceResultOutput) ToLookupBareMetalDeviceResultOutputWithContext(ctx context.Context) LookupBareMetalDeviceResultOutput {
	return o
}

func (o LookupBareMetalDeviceResultOutput) DeviceId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) int { return v.DeviceId }).(pulumi.IntOutput)
}

func (o LookupBareMetalDeviceResultOutput) Filters() GetBareMetalDeviceFilterArrayOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) []GetBareMetalDeviceFilter { return v.Filters }).(GetBareMetalDeviceFilterArrayOutput)
}

func (o LookupBareMetalDeviceResultOutput) First() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) *bool { return v.First }).(pulumi.BoolPtrOutput)
}

func (o LookupBareMetalDeviceResultOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.Hostname }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupBareMetalDeviceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) LastUpdated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.LastUpdated }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) LocationName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.LocationName }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) OrderId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) int { return v.OrderId }).(pulumi.IntOutput)
}

func (o LookupBareMetalDeviceResultOutput) OsName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.OsName }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) Period() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.Period }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) PowerStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.PowerStatus }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) PrimaryIp() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.PrimaryIp }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) ProductId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) int { return v.ProductId }).(pulumi.IntOutput)
}

func (o LookupBareMetalDeviceResultOutput) ProductName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.ProductName }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) PublicSshKeyId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) *int { return v.PublicSshKeyId }).(pulumi.IntPtrOutput)
}

func (o LookupBareMetalDeviceResultOutput) Script() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) string { return v.Script }).(pulumi.StringOutput)
}

func (o LookupBareMetalDeviceResultOutput) ServiceId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) int { return v.ServiceId }).(pulumi.IntOutput)
}

func (o LookupBareMetalDeviceResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o LookupBareMetalDeviceResultOutput) VlanId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupBareMetalDeviceResult) *int { return v.VlanId }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBareMetalDeviceResultOutput{})
}
