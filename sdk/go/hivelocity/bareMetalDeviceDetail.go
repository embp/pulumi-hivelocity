// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hivelocity

import (
	"context"
	"reflect"

	"errors"
	"github.com/embp/pulumi-hivelocity/sdk/go/hivelocity/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type BareMetalDeviceDetail struct {
	pulumi.CustomResourceState

	// When set, prefer only bonded devices
	Bonded pulumi.BoolPtrOutput `pulumi:"bonded"`
	// Device ID
	DeviceId pulumi.IntOutput `pulumi:"deviceId"`
	// Force deployment of this Device ID (internal use only)
	ForceDeviceId pulumi.IntPtrOutput `pulumi:"forceDeviceId"`
	// Hostname for this device
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// IgnitionConfig ID
	IgnitionId pulumi.IntPtrOutput `pulumi:"ignitionId"`
	// Last time this device was updated
	LastUpdated pulumi.StringOutput `pulumi:"lastUpdated"`
	// Deploy device in this location
	LocationName pulumi.StringOutput `pulumi:"locationName"`
	// Order ID
	OrderId pulumi.IntOutput `pulumi:"orderId"`
	// Operating system to install on device
	OsName pulumi.StringOutput `pulumi:"osName"`
	// Billing period for device
	Period pulumi.StringOutput `pulumi:"period"`
	// Power status
	PowerStatus pulumi.StringOutput `pulumi:"powerStatus"`
	// Primary IP of device
	PrimaryIp pulumi.StringOutput `pulumi:"primaryIp"`
	// Product ID to pick from the stock
	ProductId pulumi.IntOutput `pulumi:"productId"`
	// Product Name
	ProductName pulumi.StringOutput `pulumi:"productName"`
	// ID of a SSH Key to apply for device
	PublicSshKeyId pulumi.IntPtrOutput `pulumi:"publicSshKeyId"`
	// Post-install script for device
	Script pulumi.StringPtrOutput `pulumi:"script"`
	// Service ID
	ServiceId pulumi.IntOutput `pulumi:"serviceId"`
	// Tags to apply for device
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// VLAN ID
	//
	// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
	VlanId pulumi.IntPtrOutput `pulumi:"vlanId"`
}

// NewBareMetalDeviceDetail registers a new resource with the given unique name, arguments, and options.
func NewBareMetalDeviceDetail(ctx *pulumi.Context,
	name string, args *BareMetalDeviceDetailArgs, opts ...pulumi.ResourceOption) (*BareMetalDeviceDetail, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Hostname == nil {
		return nil, errors.New("invalid value for required argument 'Hostname'")
	}
	if args.LocationName == nil {
		return nil, errors.New("invalid value for required argument 'LocationName'")
	}
	if args.OsName == nil {
		return nil, errors.New("invalid value for required argument 'OsName'")
	}
	if args.ProductId == nil {
		return nil, errors.New("invalid value for required argument 'ProductId'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("hivelocity:index/bareMetalDevice:bareMetalDevice"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BareMetalDeviceDetail
	err := ctx.RegisterResource("hivelocity:index/bareMetalDeviceDetail:BareMetalDeviceDetail", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBareMetalDeviceDetail gets an existing BareMetalDeviceDetail resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBareMetalDeviceDetail(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BareMetalDeviceDetailState, opts ...pulumi.ResourceOption) (*BareMetalDeviceDetail, error) {
	var resource BareMetalDeviceDetail
	err := ctx.ReadResource("hivelocity:index/bareMetalDeviceDetail:BareMetalDeviceDetail", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BareMetalDeviceDetail resources.
type bareMetalDeviceDetailState struct {
	// When set, prefer only bonded devices
	Bonded *bool `pulumi:"bonded"`
	// Device ID
	DeviceId *int `pulumi:"deviceId"`
	// Force deployment of this Device ID (internal use only)
	ForceDeviceId *int `pulumi:"forceDeviceId"`
	// Hostname for this device
	Hostname *string `pulumi:"hostname"`
	// IgnitionConfig ID
	IgnitionId *int `pulumi:"ignitionId"`
	// Last time this device was updated
	LastUpdated *string `pulumi:"lastUpdated"`
	// Deploy device in this location
	LocationName *string `pulumi:"locationName"`
	// Order ID
	OrderId *int `pulumi:"orderId"`
	// Operating system to install on device
	OsName *string `pulumi:"osName"`
	// Billing period for device
	Period *string `pulumi:"period"`
	// Power status
	PowerStatus *string `pulumi:"powerStatus"`
	// Primary IP of device
	PrimaryIp *string `pulumi:"primaryIp"`
	// Product ID to pick from the stock
	ProductId *int `pulumi:"productId"`
	// Product Name
	ProductName *string `pulumi:"productName"`
	// ID of a SSH Key to apply for device
	PublicSshKeyId *int `pulumi:"publicSshKeyId"`
	// Post-install script for device
	Script *string `pulumi:"script"`
	// Service ID
	ServiceId *int `pulumi:"serviceId"`
	// Tags to apply for device
	Tags []string `pulumi:"tags"`
	// VLAN ID
	//
	// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
	VlanId *int `pulumi:"vlanId"`
}

type BareMetalDeviceDetailState struct {
	// When set, prefer only bonded devices
	Bonded pulumi.BoolPtrInput
	// Device ID
	DeviceId pulumi.IntPtrInput
	// Force deployment of this Device ID (internal use only)
	ForceDeviceId pulumi.IntPtrInput
	// Hostname for this device
	Hostname pulumi.StringPtrInput
	// IgnitionConfig ID
	IgnitionId pulumi.IntPtrInput
	// Last time this device was updated
	LastUpdated pulumi.StringPtrInput
	// Deploy device in this location
	LocationName pulumi.StringPtrInput
	// Order ID
	OrderId pulumi.IntPtrInput
	// Operating system to install on device
	OsName pulumi.StringPtrInput
	// Billing period for device
	Period pulumi.StringPtrInput
	// Power status
	PowerStatus pulumi.StringPtrInput
	// Primary IP of device
	PrimaryIp pulumi.StringPtrInput
	// Product ID to pick from the stock
	ProductId pulumi.IntPtrInput
	// Product Name
	ProductName pulumi.StringPtrInput
	// ID of a SSH Key to apply for device
	PublicSshKeyId pulumi.IntPtrInput
	// Post-install script for device
	Script pulumi.StringPtrInput
	// Service ID
	ServiceId pulumi.IntPtrInput
	// Tags to apply for device
	Tags pulumi.StringArrayInput
	// VLAN ID
	//
	// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
	VlanId pulumi.IntPtrInput
}

func (BareMetalDeviceDetailState) ElementType() reflect.Type {
	return reflect.TypeOf((*bareMetalDeviceDetailState)(nil)).Elem()
}

type bareMetalDeviceDetailArgs struct {
	// When set, prefer only bonded devices
	Bonded *bool `pulumi:"bonded"`
	// Device ID
	DeviceId *int `pulumi:"deviceId"`
	// Force deployment of this Device ID (internal use only)
	ForceDeviceId *int `pulumi:"forceDeviceId"`
	// Hostname for this device
	Hostname string `pulumi:"hostname"`
	// IgnitionConfig ID
	IgnitionId *int `pulumi:"ignitionId"`
	// Last time this device was updated
	LastUpdated *string `pulumi:"lastUpdated"`
	// Deploy device in this location
	LocationName string `pulumi:"locationName"`
	// Order ID
	OrderId *int `pulumi:"orderId"`
	// Operating system to install on device
	OsName string `pulumi:"osName"`
	// Billing period for device
	Period *string `pulumi:"period"`
	// Power status
	PowerStatus *string `pulumi:"powerStatus"`
	// Primary IP of device
	PrimaryIp *string `pulumi:"primaryIp"`
	// Product ID to pick from the stock
	ProductId int `pulumi:"productId"`
	// Product Name
	ProductName *string `pulumi:"productName"`
	// ID of a SSH Key to apply for device
	PublicSshKeyId *int `pulumi:"publicSshKeyId"`
	// Post-install script for device
	Script *string `pulumi:"script"`
	// Service ID
	ServiceId *int `pulumi:"serviceId"`
	// Tags to apply for device
	Tags []string `pulumi:"tags"`
	// VLAN ID
	//
	// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
	VlanId *int `pulumi:"vlanId"`
}

// The set of arguments for constructing a BareMetalDeviceDetail resource.
type BareMetalDeviceDetailArgs struct {
	// When set, prefer only bonded devices
	Bonded pulumi.BoolPtrInput
	// Device ID
	DeviceId pulumi.IntPtrInput
	// Force deployment of this Device ID (internal use only)
	ForceDeviceId pulumi.IntPtrInput
	// Hostname for this device
	Hostname pulumi.StringInput
	// IgnitionConfig ID
	IgnitionId pulumi.IntPtrInput
	// Last time this device was updated
	LastUpdated pulumi.StringPtrInput
	// Deploy device in this location
	LocationName pulumi.StringInput
	// Order ID
	OrderId pulumi.IntPtrInput
	// Operating system to install on device
	OsName pulumi.StringInput
	// Billing period for device
	Period pulumi.StringPtrInput
	// Power status
	PowerStatus pulumi.StringPtrInput
	// Primary IP of device
	PrimaryIp pulumi.StringPtrInput
	// Product ID to pick from the stock
	ProductId pulumi.IntInput
	// Product Name
	ProductName pulumi.StringPtrInput
	// ID of a SSH Key to apply for device
	PublicSshKeyId pulumi.IntPtrInput
	// Post-install script for device
	Script pulumi.StringPtrInput
	// Service ID
	ServiceId pulumi.IntPtrInput
	// Tags to apply for device
	Tags pulumi.StringArrayInput
	// VLAN ID
	//
	// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
	VlanId pulumi.IntPtrInput
}

func (BareMetalDeviceDetailArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bareMetalDeviceDetailArgs)(nil)).Elem()
}

type BareMetalDeviceDetailInput interface {
	pulumi.Input

	ToBareMetalDeviceDetailOutput() BareMetalDeviceDetailOutput
	ToBareMetalDeviceDetailOutputWithContext(ctx context.Context) BareMetalDeviceDetailOutput
}

func (*BareMetalDeviceDetail) ElementType() reflect.Type {
	return reflect.TypeOf((**BareMetalDeviceDetail)(nil)).Elem()
}

func (i *BareMetalDeviceDetail) ToBareMetalDeviceDetailOutput() BareMetalDeviceDetailOutput {
	return i.ToBareMetalDeviceDetailOutputWithContext(context.Background())
}

func (i *BareMetalDeviceDetail) ToBareMetalDeviceDetailOutputWithContext(ctx context.Context) BareMetalDeviceDetailOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BareMetalDeviceDetailOutput)
}

// BareMetalDeviceDetailArrayInput is an input type that accepts BareMetalDeviceDetailArray and BareMetalDeviceDetailArrayOutput values.
// You can construct a concrete instance of `BareMetalDeviceDetailArrayInput` via:
//
//	BareMetalDeviceDetailArray{ BareMetalDeviceDetailArgs{...} }
type BareMetalDeviceDetailArrayInput interface {
	pulumi.Input

	ToBareMetalDeviceDetailArrayOutput() BareMetalDeviceDetailArrayOutput
	ToBareMetalDeviceDetailArrayOutputWithContext(context.Context) BareMetalDeviceDetailArrayOutput
}

type BareMetalDeviceDetailArray []BareMetalDeviceDetailInput

func (BareMetalDeviceDetailArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BareMetalDeviceDetail)(nil)).Elem()
}

func (i BareMetalDeviceDetailArray) ToBareMetalDeviceDetailArrayOutput() BareMetalDeviceDetailArrayOutput {
	return i.ToBareMetalDeviceDetailArrayOutputWithContext(context.Background())
}

func (i BareMetalDeviceDetailArray) ToBareMetalDeviceDetailArrayOutputWithContext(ctx context.Context) BareMetalDeviceDetailArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BareMetalDeviceDetailArrayOutput)
}

// BareMetalDeviceDetailMapInput is an input type that accepts BareMetalDeviceDetailMap and BareMetalDeviceDetailMapOutput values.
// You can construct a concrete instance of `BareMetalDeviceDetailMapInput` via:
//
//	BareMetalDeviceDetailMap{ "key": BareMetalDeviceDetailArgs{...} }
type BareMetalDeviceDetailMapInput interface {
	pulumi.Input

	ToBareMetalDeviceDetailMapOutput() BareMetalDeviceDetailMapOutput
	ToBareMetalDeviceDetailMapOutputWithContext(context.Context) BareMetalDeviceDetailMapOutput
}

type BareMetalDeviceDetailMap map[string]BareMetalDeviceDetailInput

func (BareMetalDeviceDetailMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BareMetalDeviceDetail)(nil)).Elem()
}

func (i BareMetalDeviceDetailMap) ToBareMetalDeviceDetailMapOutput() BareMetalDeviceDetailMapOutput {
	return i.ToBareMetalDeviceDetailMapOutputWithContext(context.Background())
}

func (i BareMetalDeviceDetailMap) ToBareMetalDeviceDetailMapOutputWithContext(ctx context.Context) BareMetalDeviceDetailMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BareMetalDeviceDetailMapOutput)
}

type BareMetalDeviceDetailOutput struct{ *pulumi.OutputState }

func (BareMetalDeviceDetailOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BareMetalDeviceDetail)(nil)).Elem()
}

func (o BareMetalDeviceDetailOutput) ToBareMetalDeviceDetailOutput() BareMetalDeviceDetailOutput {
	return o
}

func (o BareMetalDeviceDetailOutput) ToBareMetalDeviceDetailOutputWithContext(ctx context.Context) BareMetalDeviceDetailOutput {
	return o
}

// When set, prefer only bonded devices
func (o BareMetalDeviceDetailOutput) Bonded() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.BoolPtrOutput { return v.Bonded }).(pulumi.BoolPtrOutput)
}

// Device ID
func (o BareMetalDeviceDetailOutput) DeviceId() pulumi.IntOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntOutput { return v.DeviceId }).(pulumi.IntOutput)
}

// Force deployment of this Device ID (internal use only)
func (o BareMetalDeviceDetailOutput) ForceDeviceId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntPtrOutput { return v.ForceDeviceId }).(pulumi.IntPtrOutput)
}

// Hostname for this device
func (o BareMetalDeviceDetailOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.Hostname }).(pulumi.StringOutput)
}

// IgnitionConfig ID
func (o BareMetalDeviceDetailOutput) IgnitionId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntPtrOutput { return v.IgnitionId }).(pulumi.IntPtrOutput)
}

// Last time this device was updated
func (o BareMetalDeviceDetailOutput) LastUpdated() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.LastUpdated }).(pulumi.StringOutput)
}

// Deploy device in this location
func (o BareMetalDeviceDetailOutput) LocationName() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.LocationName }).(pulumi.StringOutput)
}

// Order ID
func (o BareMetalDeviceDetailOutput) OrderId() pulumi.IntOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntOutput { return v.OrderId }).(pulumi.IntOutput)
}

// Operating system to install on device
func (o BareMetalDeviceDetailOutput) OsName() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.OsName }).(pulumi.StringOutput)
}

// Billing period for device
func (o BareMetalDeviceDetailOutput) Period() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.Period }).(pulumi.StringOutput)
}

// Power status
func (o BareMetalDeviceDetailOutput) PowerStatus() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.PowerStatus }).(pulumi.StringOutput)
}

// Primary IP of device
func (o BareMetalDeviceDetailOutput) PrimaryIp() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.PrimaryIp }).(pulumi.StringOutput)
}

// Product ID to pick from the stock
func (o BareMetalDeviceDetailOutput) ProductId() pulumi.IntOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntOutput { return v.ProductId }).(pulumi.IntOutput)
}

// Product Name
func (o BareMetalDeviceDetailOutput) ProductName() pulumi.StringOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringOutput { return v.ProductName }).(pulumi.StringOutput)
}

// ID of a SSH Key to apply for device
func (o BareMetalDeviceDetailOutput) PublicSshKeyId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntPtrOutput { return v.PublicSshKeyId }).(pulumi.IntPtrOutput)
}

// Post-install script for device
func (o BareMetalDeviceDetailOutput) Script() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringPtrOutput { return v.Script }).(pulumi.StringPtrOutput)
}

// Service ID
func (o BareMetalDeviceDetailOutput) ServiceId() pulumi.IntOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntOutput { return v.ServiceId }).(pulumi.IntOutput)
}

// Tags to apply for device
func (o BareMetalDeviceDetailOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.StringArrayOutput { return v.Tags }).(pulumi.StringArrayOutput)
}

// VLAN ID
//
// Deprecated: This field is deprecated. Please use a VlanDetail resource instead.
func (o BareMetalDeviceDetailOutput) VlanId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *BareMetalDeviceDetail) pulumi.IntPtrOutput { return v.VlanId }).(pulumi.IntPtrOutput)
}

type BareMetalDeviceDetailArrayOutput struct{ *pulumi.OutputState }

func (BareMetalDeviceDetailArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BareMetalDeviceDetail)(nil)).Elem()
}

func (o BareMetalDeviceDetailArrayOutput) ToBareMetalDeviceDetailArrayOutput() BareMetalDeviceDetailArrayOutput {
	return o
}

func (o BareMetalDeviceDetailArrayOutput) ToBareMetalDeviceDetailArrayOutputWithContext(ctx context.Context) BareMetalDeviceDetailArrayOutput {
	return o
}

func (o BareMetalDeviceDetailArrayOutput) Index(i pulumi.IntInput) BareMetalDeviceDetailOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *BareMetalDeviceDetail {
		return vs[0].([]*BareMetalDeviceDetail)[vs[1].(int)]
	}).(BareMetalDeviceDetailOutput)
}

type BareMetalDeviceDetailMapOutput struct{ *pulumi.OutputState }

func (BareMetalDeviceDetailMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BareMetalDeviceDetail)(nil)).Elem()
}

func (o BareMetalDeviceDetailMapOutput) ToBareMetalDeviceDetailMapOutput() BareMetalDeviceDetailMapOutput {
	return o
}

func (o BareMetalDeviceDetailMapOutput) ToBareMetalDeviceDetailMapOutputWithContext(ctx context.Context) BareMetalDeviceDetailMapOutput {
	return o
}

func (o BareMetalDeviceDetailMapOutput) MapIndex(k pulumi.StringInput) BareMetalDeviceDetailOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *BareMetalDeviceDetail {
		return vs[0].(map[string]*BareMetalDeviceDetail)[vs[1].(string)]
	}).(BareMetalDeviceDetailOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BareMetalDeviceDetailInput)(nil)).Elem(), &BareMetalDeviceDetail{})
	pulumi.RegisterInputType(reflect.TypeOf((*BareMetalDeviceDetailArrayInput)(nil)).Elem(), BareMetalDeviceDetailArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BareMetalDeviceDetailMapInput)(nil)).Elem(), BareMetalDeviceDetailMap{})
	pulumi.RegisterOutputType(BareMetalDeviceDetailOutput{})
	pulumi.RegisterOutputType(BareMetalDeviceDetailArrayOutput{})
	pulumi.RegisterOutputType(BareMetalDeviceDetailMapOutput{})
}
