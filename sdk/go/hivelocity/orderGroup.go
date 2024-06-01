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

// Deprecated: hivelocity.index/ordergroup.orderGroup has been deprecated in favor of hivelocity.index/ordergroupdetail.OrderGroupDetail
type OrderGroup struct {
	pulumi.CustomResourceState

	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupBareMetalDeviceArrayOutput `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name pulumi.StringOutput `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack pulumi.BoolOutput `pulumi:"sameRack"`
}

// NewOrderGroup registers a new resource with the given unique name, arguments, and options.
func NewOrderGroup(ctx *pulumi.Context,
	name string, args *OrderGroupArgs, opts ...pulumi.ResourceOption) (*OrderGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BareMetalDevices == nil {
		return nil, errors.New("invalid value for required argument 'BareMetalDevices'")
	}
	if args.SameRack == nil {
		return nil, errors.New("invalid value for required argument 'SameRack'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrderGroup
	err := ctx.RegisterResource("hivelocity:index/orderGroup:orderGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrderGroup gets an existing OrderGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrderGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrderGroupState, opts ...pulumi.ResourceOption) (*OrderGroup, error) {
	var resource OrderGroup
	err := ctx.ReadResource("hivelocity:index/orderGroup:orderGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrderGroup resources.
type orderGroupState struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices []OrderGroupBareMetalDevice `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name *string `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack *bool `pulumi:"sameRack"`
}

type OrderGroupState struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupBareMetalDeviceArrayInput
	// Name of this Order Group
	Name pulumi.StringPtrInput
	// Devices will be placed in the same rack
	SameRack pulumi.BoolPtrInput
}

func (OrderGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*orderGroupState)(nil)).Elem()
}

type orderGroupArgs struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices []OrderGroupBareMetalDevice `pulumi:"bareMetalDevices"`
	// Name of this Order Group
	Name *string `pulumi:"name"`
	// Devices will be placed in the same rack
	SameRack bool `pulumi:"sameRack"`
}

// The set of arguments for constructing a OrderGroup resource.
type OrderGroupArgs struct {
	// A list of Bare Metal Devices to deploy
	BareMetalDevices OrderGroupBareMetalDeviceArrayInput
	// Name of this Order Group
	Name pulumi.StringPtrInput
	// Devices will be placed in the same rack
	SameRack pulumi.BoolInput
}

func (OrderGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*orderGroupArgs)(nil)).Elem()
}

type OrderGroupInput interface {
	pulumi.Input

	ToOrderGroupOutput() OrderGroupOutput
	ToOrderGroupOutputWithContext(ctx context.Context) OrderGroupOutput
}

func (*OrderGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**OrderGroup)(nil)).Elem()
}

func (i *OrderGroup) ToOrderGroupOutput() OrderGroupOutput {
	return i.ToOrderGroupOutputWithContext(context.Background())
}

func (i *OrderGroup) ToOrderGroupOutputWithContext(ctx context.Context) OrderGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupOutput)
}

// OrderGroupArrayInput is an input type that accepts OrderGroupArray and OrderGroupArrayOutput values.
// You can construct a concrete instance of `OrderGroupArrayInput` via:
//
//	OrderGroupArray{ OrderGroupArgs{...} }
type OrderGroupArrayInput interface {
	pulumi.Input

	ToOrderGroupArrayOutput() OrderGroupArrayOutput
	ToOrderGroupArrayOutputWithContext(context.Context) OrderGroupArrayOutput
}

type OrderGroupArray []OrderGroupInput

func (OrderGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrderGroup)(nil)).Elem()
}

func (i OrderGroupArray) ToOrderGroupArrayOutput() OrderGroupArrayOutput {
	return i.ToOrderGroupArrayOutputWithContext(context.Background())
}

func (i OrderGroupArray) ToOrderGroupArrayOutputWithContext(ctx context.Context) OrderGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupArrayOutput)
}

// OrderGroupMapInput is an input type that accepts OrderGroupMap and OrderGroupMapOutput values.
// You can construct a concrete instance of `OrderGroupMapInput` via:
//
//	OrderGroupMap{ "key": OrderGroupArgs{...} }
type OrderGroupMapInput interface {
	pulumi.Input

	ToOrderGroupMapOutput() OrderGroupMapOutput
	ToOrderGroupMapOutputWithContext(context.Context) OrderGroupMapOutput
}

type OrderGroupMap map[string]OrderGroupInput

func (OrderGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrderGroup)(nil)).Elem()
}

func (i OrderGroupMap) ToOrderGroupMapOutput() OrderGroupMapOutput {
	return i.ToOrderGroupMapOutputWithContext(context.Background())
}

func (i OrderGroupMap) ToOrderGroupMapOutputWithContext(ctx context.Context) OrderGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrderGroupMapOutput)
}

type OrderGroupOutput struct{ *pulumi.OutputState }

func (OrderGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrderGroup)(nil)).Elem()
}

func (o OrderGroupOutput) ToOrderGroupOutput() OrderGroupOutput {
	return o
}

func (o OrderGroupOutput) ToOrderGroupOutputWithContext(ctx context.Context) OrderGroupOutput {
	return o
}

// A list of Bare Metal Devices to deploy
func (o OrderGroupOutput) BareMetalDevices() OrderGroupBareMetalDeviceArrayOutput {
	return o.ApplyT(func(v *OrderGroup) OrderGroupBareMetalDeviceArrayOutput { return v.BareMetalDevices }).(OrderGroupBareMetalDeviceArrayOutput)
}

// Name of this Order Group
func (o OrderGroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OrderGroup) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Devices will be placed in the same rack
func (o OrderGroupOutput) SameRack() pulumi.BoolOutput {
	return o.ApplyT(func(v *OrderGroup) pulumi.BoolOutput { return v.SameRack }).(pulumi.BoolOutput)
}

type OrderGroupArrayOutput struct{ *pulumi.OutputState }

func (OrderGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrderGroup)(nil)).Elem()
}

func (o OrderGroupArrayOutput) ToOrderGroupArrayOutput() OrderGroupArrayOutput {
	return o
}

func (o OrderGroupArrayOutput) ToOrderGroupArrayOutputWithContext(ctx context.Context) OrderGroupArrayOutput {
	return o
}

func (o OrderGroupArrayOutput) Index(i pulumi.IntInput) OrderGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OrderGroup {
		return vs[0].([]*OrderGroup)[vs[1].(int)]
	}).(OrderGroupOutput)
}

type OrderGroupMapOutput struct{ *pulumi.OutputState }

func (OrderGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrderGroup)(nil)).Elem()
}

func (o OrderGroupMapOutput) ToOrderGroupMapOutput() OrderGroupMapOutput {
	return o
}

func (o OrderGroupMapOutput) ToOrderGroupMapOutputWithContext(ctx context.Context) OrderGroupMapOutput {
	return o
}

func (o OrderGroupMapOutput) MapIndex(k pulumi.StringInput) OrderGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OrderGroup {
		return vs[0].(map[string]*OrderGroup)[vs[1].(string)]
	}).(OrderGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupInput)(nil)).Elem(), &OrderGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupArrayInput)(nil)).Elem(), OrderGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrderGroupMapInput)(nil)).Elem(), OrderGroupMap{})
	pulumi.RegisterOutputType(OrderGroupOutput{})
	pulumi.RegisterOutputType(OrderGroupArrayOutput{})
	pulumi.RegisterOutputType(OrderGroupMapOutput{})
}
