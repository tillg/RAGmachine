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
  * [SignalRequestFilter](extensions_platform_server_connectors.signalrequestfilter-1.html)

# Class SignalRequestFilter

experimental

    

This filter adds the {@link AbortSignal} from the
`payload.extendedData.signal` to the fetch request itself in order to be able
to cancel requests.

IMPORTANT: This filter is required in order to cancel uploads of the provided
`AttachmentHandler` by `extensions/platform-server-connectors` on network
level.

### Hierarchy

  * SignalRequestFilter

### Implements

  * RequestFilter

## Index

### Methods

  * [canHandleRequest](extensions_platform_server_connectors.signalrequestfilter-1.html#canhandlerequest)
  * [doRequestFilter](extensions_platform_server_connectors.signalrequestfilter-1.html#dorequestfilter)

## Methods

### canHandleRequest

  * canHandleRequest(__namedParameters: { payload: { extendedData: any } }): boolean

  *     * Defined in src/extensions/platform-server-connectors/internal/filters.ts:34

#### Parameters

    * ##### __namedParameters: { payload: { extendedData: any } }

      * ##### payload: { extendedData: any }

        * ##### extendedData: any

#### Returns boolean

### doRequestFilter

  * doRequestFilter(__namedParameters: { payload: {} & { extendedData: { signal: AbortSignal } }; request: RequestInit }): RequestFilterResult

  *     * Defined in src/extensions/platform-server-connectors/internal/filters.ts:38

#### Parameters

    * ##### __namedParameters: { payload: {} & { extendedData: { signal: AbortSignal } }; request: RequestInit }

      * ##### payload: {} & { extendedData: { signal: AbortSignal } }

      * ##### request: RequestInit

#### Returns RequestFilterResult

  * [_Globals_](../globals.html)
  * [extensions/platform-server-connectors](../modules/extensions_platform_server_connectors.html)

  * [Configuration](../modules/extensions_platform_server_connectors.html#configuration)
  * [PlatformServerConnectors](../modules/extensions_platform_server_connectors.html#platformserverconnectors)
  * [SignalRequestFilter](../modules/extensions_platform_server_connectors.html#signalrequestfilter)
  * [configure](../modules/extensions_platform_server_connectors.html#configure)
  * [PlatformDocumentListDataLoader](extensions_platform_server_connectors.platformdocumentlistdataloader.html)
  * [PlatformSingleDocumentDataLoader](extensions_platform_server_connectors.platformsingledocumentdataloader.html)

  * [SignalRequestFilter](extensions_platform_server_connectors.signalrequestfilter-1.html)
    * [canHandleRequest](extensions_platform_server_connectors.signalrequestfilter-1.html#canhandlerequest)
    * [doRequestFilter](extensions_platform_server_connectors.signalrequestfilter-1.html#dorequestfilter)

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

