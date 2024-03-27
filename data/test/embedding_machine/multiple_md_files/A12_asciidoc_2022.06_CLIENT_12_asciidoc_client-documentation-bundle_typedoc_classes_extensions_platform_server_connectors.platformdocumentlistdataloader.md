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
  * [extensions/platform-server-connectors](../modules/extensions_platform_server_connectors.html)
  * [PlatformDocumentListDataLoader](extensions_platform_server_connectors.platformdocumentlistdataloader.html)

# Class PlatformDocumentListDataLoader

### Hierarchy

  * PlatformDocumentListDataLoader

### Implements

  * [DataLoader](../modules/core_data.dataloader-1.html)<[Data](../modules/core_activity.activity-1.data.html)>

## Index

### Constructors

  * [constructor](extensions_platform_server_connectors.platformdocumentlistdataloader.html#constructor)

### Properties

  * [localeProvider](extensions_platform_server_connectors.platformdocumentlistdataloader.html#localeprovider)
  * [name](extensions_platform_server_connectors.platformdocumentlistdataloader.html#name)

### Methods

  * [canHandle](extensions_platform_server_connectors.platformdocumentlistdataloader.html#canhandle)
  * [delete](extensions_platform_server_connectors.platformdocumentlistdataloader.html#delete)
  * [load](extensions_platform_server_connectors.platformdocumentlistdataloader.html#load)
  * [save](extensions_platform_server_connectors.platformdocumentlistdataloader.html#save)

## Constructors

### constructor

  * new PlatformDocumentListDataLoader(localeProvider: () => Locale): [PlatformDocumentListDataLoader](extensions_platform_server_connectors.platformdocumentlistdataloader.html)

  *     * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:41

#### Parameters

    * ##### localeProvider: () => Locale

      *         * (): Locale
        * #### Returns Locale

#### Returns
[PlatformDocumentListDataLoader](extensions_platform_server_connectors.platformdocumentlistdataloader.html)

## Properties

### Protected localeProvider

localeProvider: () => Locale

  * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:43

#### Type declaration

  *     * (): Locale
    * #### Returns Locale

### name

name: string = "PlatformDocumentListDataLoader"

  * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:39

## Methods

### canHandle

  * canHandle(activityDescriptor: [Descriptor](../modules/core_activity.activity-1.descriptor.html)): boolean

  *     * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:45

#### Parameters

    * ##### activityDescriptor: [Descriptor](../modules/core_activity.activity-1.descriptor.html)

#### Returns boolean

### delete

  * delete(activityDescriptor: [Descriptor](../modules/core_activity.activity-1.descriptor.html)): Promise<void>

  *     * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:158

#### Parameters

    * ##### activityDescriptor: [Descriptor](../modules/core_activity.activity-1.descriptor.html)

#### Returns Promise<void>

### load

  * load(activity: [Activity](../modules/core_activity.activity-1.html), _documentModel: DocumentModel | undefined, models: ModelAPI[]): Promise<[Data](../modules/core_activity.activity-1.data.html)>

  *     * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:49

#### Parameters

    * ##### activity: [Activity](../modules/core_activity.activity-1.html)

    * ##### _documentModel: DocumentModel | undefined

    * ##### models: ModelAPI[]

#### Returns Promise<[Data](../modules/core_activity.activity-1.data.html)>

### save

  * save(): Promise<[Data](../modules/core_activity.activity-1.data.html)>

  *     * Defined in src/extensions/platform-server-connectors/internal/loaders/PlatformDocumentListDataLoader.ts:154

#### Returns Promise<[Data](../modules/core_activity.activity-1.data.html)>

  * [_Globals_](../globals.html)
  * [extensions/platform-server-connectors](../modules/extensions_platform_server_connectors.html)

  * [Configuration](../modules/extensions_platform_server_connectors.html#configuration)
  * [PlatformServerConnectors](../modules/extensions_platform_server_connectors.html#platformserverconnectors)
  * [SignalRequestFilter](../modules/extensions_platform_server_connectors.html#signalrequestfilter)
  * [configure](../modules/extensions_platform_server_connectors.html#configure)

  * [PlatformDocumentListDataLoader](extensions_platform_server_connectors.platformdocumentlistdataloader.html)
    * [constructor](extensions_platform_server_connectors.platformdocumentlistdataloader.html#constructor)
    * [localeProvider](extensions_platform_server_connectors.platformdocumentlistdataloader.html#localeprovider)
    * [name](extensions_platform_server_connectors.platformdocumentlistdataloader.html#name)
    * [canHandle](extensions_platform_server_connectors.platformdocumentlistdataloader.html#canhandle)
    * [delete](extensions_platform_server_connectors.platformdocumentlistdataloader.html#delete)
    * [load](extensions_platform_server_connectors.platformdocumentlistdataloader.html#load)
    * [save](extensions_platform_server_connectors.platformdocumentlistdataloader.html#save)

  * [PlatformSingleDocumentDataLoader](extensions_platform_server_connectors.platformsingledocumentdataloader.html)
  * [SignalRequestFilter](extensions_platform_server_connectors.signalrequestfilter-1.html)
  * [Configuration](../interfaces/extensions_platform_server_connectors.configuration-1.html)
  * [Loaders](../interfaces/extensions_platform_server_connectors.loaders.html)
  * [PlatformServerConnectors](../interfaces/extensions_platform_server_connectors.platformserverconnectors-1.html)
  * [configure](../modules/extensions_platform_server_connectors.html#configure-1)
  * [configure](../modules/extensions_platform_server_connectors.html#configure-2)
  * [configure](../modules/extensions_platform_server_connectors.html#configure-3)
  * [mergeDocuments](../modules/extensions_platform_server_connectors.html#mergedocuments)
  * [platformModelFetcher](../modules/extensions_platform_server_connectors.html#platformmodelfetcher)
  * [JsonRpc2Dispatcher](../modules/extensions_platform_server_connectors.html#jsonrpc2dispatcher)
  * [RequestBuilder](../modules/extensions_platform_server_connectors.html#requestbuilder)
  * [RestRequestDispatcher](../modules/extensions_platform_server_connectors.html#restrequestdispatcher)

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

