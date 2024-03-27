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
  * [FormModelLoader](extensions_http_connectors.formmodelloader.html)

# Class FormModelLoader

### Hierarchy

  * FormModelLoader

## Index

### Constructors

  * [constructor](extensions_http_connectors.formmodelloader.html#constructor)

### Properties

  * [modelFetcher](extensions_http_connectors.formmodelloader.html#modelfetcher)
  * [name](extensions_http_connectors.formmodelloader.html#name)

### Methods

  * [canHandle](extensions_http_connectors.formmodelloader.html#canhandle)
  * [load](extensions_http_connectors.formmodelloader.html#load)

## Constructors

### constructor

  * new FormModelLoader(modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)): [FormModelLoader](extensions_http_connectors.formmodelloader.html)

  *     * Defined in src/extensions/http-connectors/internal/FormModelLoader.ts:28

#### Parameters

    * ##### modelFetcher: [ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

#### Returns
[FormModelLoader](extensions_http_connectors.formmodelloader.html)

## Properties

### Protected modelFetcher

modelFetcher:
[ModelFetcher](../interfaces/extensions_http_connectors.modelfetcher-1.html)

  * Defined in src/extensions/http-connectors/internal/FormModelLoader.ts:30

### name

name: string = "FormModelLoader"

  * Defined in src/extensions/http-connectors/internal/FormModelLoader.ts:28

## Methods

### canHandle

  * canHandle(__namedParameters: { modelType: string }): boolean

  *     * Defined in src/extensions/http-connectors/internal/FormModelLoader.ts:32

#### Parameters

    * ##### __namedParameters: { modelType: string }

      * ##### modelType: string

#### Returns boolean

### load

  * load(descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html), getReferencedModel: (referencedModel: ModelReference) => Promise<ModelAPI>): Promise<FormModel>

  *     * Defined in src/extensions/http-connectors/internal/FormModelLoader.ts:36

#### Parameters

    * ##### descriptor: [Descriptor](../interfaces/core_model.model-1.descriptor.html)

    * ##### getReferencedModel: (referencedModel: ModelReference) => Promise<ModelAPI>

      *         * (referencedModel: ModelReference): Promise<ModelAPI>
        * #### Parameters

          * ##### referencedModel: ModelReference

#### Returns Promise<ModelAPI>

#### Returns Promise<FormModel>

  * [_Globals_](../globals.html)
  * [extensions/http-connectors](../modules/extensions_http_connectors.html)

  * [ModelFetcher](../modules/extensions_http_connectors.html#modelfetcher)
  * [createHttpModelFetcher](../modules/extensions_http_connectors.html#createhttpmodelfetcher)
  * [DocumentModelLoader](extensions_http_connectors.documentmodelloader.html)

  * [FormModelLoader](extensions_http_connectors.formmodelloader.html)
    * [constructor](extensions_http_connectors.formmodelloader.html#constructor)
    * [modelFetcher](extensions_http_connectors.formmodelloader.html#modelfetcher)
    * [name](extensions_http_connectors.formmodelloader.html#name)
    * [canHandle](extensions_http_connectors.formmodelloader.html#canhandle)
    * [load](extensions_http_connectors.formmodelloader.html#load)

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

