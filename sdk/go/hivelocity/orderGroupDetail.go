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

type OrderGroupDetail struct {
	pulumi.CustomResourceState

	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupDetailBareMetalDeviceArrayOutput `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name pulumi.StringOutput `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack pulumi.BoolOutput `pulumi:"sameRack"`
}

// NewOrderGroupDetail registers a new resource with the given unique name, arguments, and options.
func NewOrderGroupDetail(ctx *pulumi.Context,
	name string, args *OrderGroupDetailArgs, opts ...pulumi.ResourceOption) (*OrderGroupDetail, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BareMetalDevices == nil {
		return nil, errors.New("invalid value for required argument 'BareMetalDevices'")
	}
	if args.SameRack == nil {
		return nil, errors.New("invalid value for required argument 'SameRack'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("hivelocity:index/orderGroup:orderGroup"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrderGroupDetail
	err := ctx.RegisterResource("hivelocity:index/orderGroupDetail:OrderGroupDetail", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrderGroupDetail gets an existing OrderGroupDetail resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrderGroupDetail(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrderGroupDetailState, opts ...pulumi.ResourceOption) (*OrderGroupDetail, error) {
	var resource OrderGroupDetail
	err := ctx.ReadResource("hivelocity:index/orderGroupDetail:OrderGroupDetail", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrderGroupDetail resources.
type orderGroupDetailState struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices []OrderGroupDetailBareMetalDevice `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name *string `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack *bool `pulumi:"sameRack"`
}

type OrderGroupDetailState struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupDetailBareMetalDeviceArrayInput
	// Name of this Order Group
	Name pulumi.StringPtrInput
	// Devices will be placed in the same rack
	SameRack pulumi.BoolPtrInput
}

func (OrderGroupDetailState) ElementType() reflect.Type {
	return reflect.TypeOf((*orderGroupDetailState)(nil)).Elem()
}

type orderGroupDetailArgs struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices []OrderGroupDetailBareMetalDevice `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name *string `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack bool `pulumi:"sameRack"`
}

// The set of arguments for constructing a OrderGroupDetail resource.
type OrderGroupDetailArgs struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupDetailBareMetalDeviceArrayInput
	// Name of this Order Group
	Name pulumi.StringPtrInput
	// Devices will be placed in the same rack
	SameRack pulumi.BoolInput
}

func (OrderGroupDetailArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*orderGroupDetailArgs)(nil)).Elem()
}

type OrderGroupDetailInput interface {
	pulumi.Input

	ToOrderGroupDetailOutput() OrderGroupDetailOutput
	ToOrderGroupDetailOutputWithContext(ctx context.Context) OrderGroupDetailOutput
}

func (*OrderGroupDetail) ElementType() reflect.Type {
	return reflect.TypeOf((**OrderGroupDetail)(nil)).Elem()
}

func (i *OrderGroupDetail) ToOrderGroupDetailOutput() OrderGroupDetailOutput {
	return i.ToOrderGroupDetailOutputWithContext(context.Background())
}

func (i *OrderGroupDetail) ToOrderGroupDetailOutputWithContext(ctx context.Context) OrderGroupDetailOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupDetailOutput)
}

// OrderGroupDetailArrayInput is an input type that accepts OrderGroupDetailArray and OrderGroupDetailArrayOutput values.
// You can construct a concrete instance of `OrderGroupDetailArrayInput` via:
//
//	OrderGroupDetailArray{ OrderGroupDetailArgs{...} }
type OrderGroupDetailArrayInput interface {
	pulumi.Input

	ToOrderGroupDetailArrayOutput() OrderGroupDetailArrayOutput
	ToOrderGroupDetailArrayOutputWithContext(context.Context) OrderGroupDetailArrayOutput
}

type OrderGroupDetailArray []OrderGroupDetailInput

func (OrderGroupDetailArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrderGroupDetail)(nil)).Elem()
}

func (i OrderGroupDetailArray) ToOrderGroupDetailArrayOutput() OrderGroupDetailArrayOutput {
	return i.ToOrderGroupDetailArrayOutputWithContext(context.Background())
}

func (i OrderGroupDetailArray) ToOrderGroupDetailArrayOutputWithContext(ctx context.Context) OrderGroupDetailArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupDetailArrayOutput)
}

// OrderGroupDetailMapInput is an input type that accepts OrderGroupDetailMap and OrderGroupDetailMapOutput values.
// You can construct a concrete instance of `OrderGroupDetailMapInput` via:
//
//	OrderGroupDetailMap{ "key": OrderGroupDetailArgs{...} }
type OrderGroupDetailMapInput interface {
	pulumi.Input

	ToOrderGroupDetailMapOutput() OrderGroupDetailMapOutput
	ToOrderGroupDetailMapOutputWithContext(context.Context) OrderGroupDetailMapOutput
}

type OrderGroupDetailMap map[string]OrderGroupDetailInput

func (OrderGroupDetailMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrderGroupDetail)(nil)).Elem()
}

func (i OrderGroupDetailMap) ToOrderGroupDetailMapOutput() OrderGroupDetailMapOutput {
	return i.ToOrderGroupDetailMapOutputWithContext(context.Background())
}

func (i OrderGroupDetailMap) ToOrderGroupDetailMapOutputWithContext(ctx context.Context) OrderGroupDetailMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupDetailMapOutput)
}

type OrderGroupDetailOutput struct{ *pulumi.OutputState }

func (OrderGroupDetailOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrderGroupDetail)(nil)).Elem()
}

func (o OrderGroupDetailOutput) ToOrderGroupDetailOutput() OrderGroupDetailOutput {
	return o
}

func (o OrderGroupDetailOutput) ToOrderGroupDetailOutputWithContext(ctx context.Context) OrderGroupDetailOutput {
	return o
}

// A list of Bare Metal Devices to deploy
func (o OrderGroupDetailOutput) BareMetalDevices() OrderGroupDetailBareMetalDeviceArrayOutput {
	return o.ApplyT(func(v *OrderGroupDetail) OrderGroupDetailBareMetalDeviceArrayOutput { return v.BareMetalDevices }).(OrderGroupDetailBareMetalDeviceArrayOutput)
}

// Name of this Order Group
func (o OrderGroupDetailOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OrderGroupDetail) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Devices will be placed in the same rack
func (o OrderGroupDetailOutput) SameRack() pulumi.BoolOutput {
	return o.ApplyT(func(v *OrderGroupDetail) pulumi.BoolOutput { return v.SameRack }).(pulumi.BoolOutput)
}

type OrderGroupDetailArrayOutput struct{ *pulumi.OutputState }

func (OrderGroupDetailArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrderGroupDetail)(nil)).Elem()
}

func (o OrderGroupDetailArrayOutput) ToOrderGroupDetailArrayOutput() OrderGroupDetailArrayOutput {
	return o
}

func (o OrderGroupDetailArrayOutput) ToOrderGroupDetailArrayOutputWithContext(ctx context.Context) OrderGroupDetailArrayOutput {
	return o
}

func (o OrderGroupDetailArrayOutput) Index(i pulumi.IntInput) OrderGroupDetailOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OrderGroupDetail {
		return vs[0].([]*OrderGroupDetail)[vs[1].(int)]
	}).(OrderGroupDetailOutput)
}

type OrderGroupDetailMapOutput struct{ *pulumi.OutputState }

func (OrderGroupDetailMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrderGroupDetail)(nil)).Elem()
}

func (o OrderGroupDetailMapOutput) ToOrderGroupDetailMapOutput() OrderGroupDetailMapOutput {
	return o
}

func (o OrderGroupDetailMapOutput) ToOrderGroupDetailMapOutputWithContext(ctx context.Context) OrderGroupDetailMapOutput {
	return o
}

func (o OrderGroupDetailMapOutput) MapIndex(k pulumi.StringInput) OrderGroupDetailOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OrderGroupDetail {
		return vs[0].(map[string]*OrderGroupDetail)[vs[1].(string)]
	}).(OrderGroupDetailOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupDetailInput)(nil)).Elem(), &OrderGroupDetail{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupDetailArrayInput)(nil)).Elem(), OrderGroupDetailArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupDetailMapInput)(nil)).Elem(), OrderGroupDetailMap{})
	pulumi.RegisterOutputType(OrderGroupDetailOutput{})
	pulumi.RegisterOutputType(OrderGroupDetailArrayOutput{})
	pulumi.RegisterOutputType(OrderGroupDetailMapOutput{})
}