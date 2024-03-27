Search

  * Preparing search index...
  * The search index is not available

[Client API Documentation](../index.html)

Options

All

  * Public
  * Public/Protected
  * All

Menu

  * [Globals](../globals.html)
  * [extensions/http-connectors](../modules/extensions_http_connectors.html)
  * [DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)

# Class DocumentModelLoader

### Hierarchy

  * DocumentModelLoader

## Index

### Constructors

  * [constructor](extensions_http_connectors.documentmodelloader.html#constructor)

### Properties

  * [modelFetcher](extensions_http_connectors.documentmodelloader.html#modelfetcher)
  * [name](extensions_http_connectors.documentmodelloader.html#name)

### Methods

  * [canHandle](extensions_http_connectors.documentmodelloader.html#canhandle)
  * [load](extensions_http_connectors.documentmodelloader.html#load)

## Constructors

### constructor

  * new DocumentModelLoader(modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)): [DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)

  *     * Defined in src/extensions/http-connectors/internal/DocumentModelLoader.ts:25

#### Parameters

    * ##### modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

#### Returns
[DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)

## Properties

### Protected modelFetcher

modelFetcher:
[ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

  * Defined in src/extensions/http-connectors/internal/DocumentModelLoader.ts:27

### name

name: string = "DocumentModelLoader"

  * Defined in src/extensions/http-connectors/internal/DocumentModelLoader.ts:25

## Methods

### canHandle

  * canHandle(__namedParameters: { modelType: string }): boolean

  *     * Defined in src/extensions/http-connectors/internal/DocumentModelLoader.ts:29

#### Parameters

    * ##### __namedParameters: { modelType: string }

      * ##### modelType: string

#### Returns boolean

### load

  * load(descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)): Promise<[DocumentAndValidationModel](../interfaces/core_model.model-1.documentandvalidationmodel.html)>

  *     * Defined in src/extensions/http-connectors/internal/DocumentModelLoader.ts:33

#### Parameters

    * ##### descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)

#### Returns
Promise<[DocumentAndValidationModel](../interfaces/core_model.model-1.documentandvalidationmodel.html)>

  * [_Globals_](../globals.html)
  * [extensions/http-connectors](../modules/extensions_http_connectors.html)

  * [ModelFetcher](../modules/extensions_http_connectors.html#modelfetcher)
  * [createHttpModelFetcher](../modules/extensions_http_connectors.html#createhttpmodelfetcher)

  * [DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)
    * [constructor](extensions_http_connectors.documentmodelloader.html#constructor)
    * [modelFetcher](extensions_http_connectors.documentmodelloader.html#modelfetcher)
    * [name](extensions_http_connectors.documentmodelloader.html#name)
    * [canHandle](extensions_http_connectors.documentmodelloader.html#canhandle)
    * [load](extensions_http_connectors.documentmodelloader.html#load)

  * [FormModelLoader](extensions_http_connectors.formmodelloader.html)
  * [GenericModelLoader](extensions_http_connectors.genericmodelloader.html)
  * [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)
  * [createHttpModelFetcher](../modules/extensions_http_connectors.html#createhttpmodelfetcher-1)
  * [createHttpModelLoaders](../modules/extensions_http_connectors.html#createhttpmodelloaders)
  * [createNotFoundError](../modules/extensions_http_connectors.html#createnotfounderror)
  * [createPostProcessingFailedError](../modules/extensions_http_connectors.html#createpostprocessingfailederror)
  * [createUnexpectedTypeError](../modules/extensions_http_connectors.html#createunexpectedtypeerror)

## Legend

  * Module
  * Object literal
  * Variable
  * Function
  * Function with type parameter
  * Index signature
  * Type alias
  * Type alias with type parameter

  * Enumeration
  * Enumeration member
  * Property
  * Method

  * Interface
  * Interface with type parameter
  * Constructor
  * Property
  * Method
  * Index signature

  * Class
  * Class with type parameter
  * Constructor
  * Property
  * Method
  * Accessor
  * Index signature

  * Inherited constructor
  * Inherited property
  * Inherited method
  * Inherited accessor

  * Protected property
  * Protected method
  * Protected accessor

  * Private property
  * Private method
  * Private accessor

  * Static property
  * Static method

Generated using [TypeDoc](https://typedoc.org/)

