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
  * [GenericModelLoader](extensions_http_connectors.genericmodelloader.html)

# Class GenericModelLoader

### Hierarchy

  * GenericModelLoader

### Implements

  * [ModelLoader](../interfaces/core_model.modelloader-1.html)

## Index

### Constructors

  * [constructor](extensions_http_connectors.genericmodelloader.html#constructor)

### Properties

  * [modelFetcher](extensions_http_connectors.genericmodelloader.html#modelfetcher)
  * [name](extensions_http_connectors.genericmodelloader.html#name)

### Methods

  * [canHandle](extensions_http_connectors.genericmodelloader.html#canhandle)
  * [load](extensions_http_connectors.genericmodelloader.html#load)

## Constructors

### constructor

  * new GenericModelLoader(modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)): [GenericModelLoader](extensions_http_connectors.genericmodelloader.html)

  *     * Defined in src/extensions/http-connectors/internal/GenericModelLoader.ts:22

#### Parameters

    * ##### modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

#### Returns
[GenericModelLoader](extensions_http_connectors.genericmodelloader.html)

## Properties

### Protected modelFetcher

modelFetcher:
[ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

  * Defined in src/extensions/http-connectors/internal/GenericModelLoader.ts:24

### name

name: string = "GenericModelLoader"

Implementation of
[ModelLoader](../interfaces/core_model.modelloader-1.html).[name](../interfaces/core_model.modelloader-1.html#name)

  * Defined in src/extensions/http-connectors/internal/GenericModelLoader.ts:22

## Methods

### canHandle

  * canHandle(descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)): boolean

  * Implementation of [ModelLoader](../interfaces/core_model.modelloader-1.html).[canHandle](../interfaces/core_model.modelloader-1.html#canhandle)

    * Defined in src/extensions/http-connectors/internal/GenericModelLoader.ts:26

#### Parameters

    * ##### descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)

#### Returns boolean

### load

  * load(descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html), getReferencedModel: (referencedModel: ModelReference) => Promise<ModelAPI>): Promise<ModelAPI>

  *     * Defined in src/extensions/http-connectors/internal/GenericModelLoader.ts:30

#### Parameters

    * ##### descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)

    * ##### getReferencedModel: (referencedModel: ModelReference) => Promise<ModelAPI>

      *         * (referencedModel: ModelReference): Promise<ModelAPI>
        * #### Parameters

          * ##### referencedModel: ModelReference

#### Returns Promise<ModelAPI>

#### Returns Promise<ModelAPI>

  * [_Globals_](../globals.html)
  * [extensions/http-connectors](../modules/extensions_http_connectors.html)

  * [ModelFetcher](../modules/extensions_http_connectors.html#modelfetcher)
  * [createHttpModelFetcher](../modules/extensions_http_connectors.html#createhttpmodelfetcher)
  * [DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)
  * [FormModelLoader](extensions_http_connectors.formmodelloader.html)

  * [GenericModelLoader](extensions_http_connectors.genericmodelloader.html)
    * [constructor](extensions_http_connectors.genericmodelloader.html#constructor)
    * [modelFetcher](extensions_http_connectors.genericmodelloader.html#modelfetcher)
    * [name](extensions_http_connectors.genericmodelloader.html#name)
    * [canHandle](extensions_http_connectors.genericmodelloader.html#canhandle)
    * [load](extensions_http_connectors.genericmodelloader.html#load)

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

