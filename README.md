# Hivelocity Resource Provider

Pulumi conversion of the [Terraform Hivelocity provider](https://registry.terraform.io/providers/hivelocity/hivelocity/latest/docs).

The Hivelocity provider provides resources to interact with the Hivelocity API.

This provider is untested and not production ready.

This repo was forked from Pulumi's [provider template repo](https://github.com/pulumi/pulumi-tf-provider-boilerplate).

# Local Development

Use the VS Code Dev Containers plugin to use the included `Dockerfile` located in the .devcontainer directory. This will create the development environment needed to build and generate the sdk.

Hivelocity's Terraform [provider](https://github.com/hivelocity/terraform-provider-hivelocity) imports the `github.com/hivelocity/terraform-provider-hivelocity/hivelocity-client-go` generated directory. If targeting the github repo as the import source the provider will fail to build. To get around it this provider expects a local version of the [Hivelocity Terraform provider](https://github.com/hivelocity/terraform-provider-hivelocity) that has been built to generate the client files.

The pulumi provider uses a replace to replace imports with a local path in `provider/go.mod`, line 7:

`replace github.com/hivelocity/terraform-provider-hivelocity v0.7.9 => ../../terraform-provider-hivelocity`

Once the local version of the terraform provider has been built, use the below commands to generate:

- Generating schema = `make tfgen`
- Build the sdks = `make build_sdks`
- Ensure sdk is built correctly = `cd sdk && go mod tidy`
- Lint the provider = `make lint_provider`

If any updates are made you'll need to re-run `make tfgen` to re-generate the schema.

For more info on commands and process for bridging a terraform provider to Pulumi see the [provider template boilerplate repo](https://github.com/pulumi/pulumi-tf-provider-boilerplate).