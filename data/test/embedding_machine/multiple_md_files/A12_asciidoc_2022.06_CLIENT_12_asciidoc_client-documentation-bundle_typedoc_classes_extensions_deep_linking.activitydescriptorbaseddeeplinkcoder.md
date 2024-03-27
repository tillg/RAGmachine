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
  * [extensions/deep-linking](../modules/extensions_deep_linking.html)
  * [ActivityDescriptorBasedDeepLinkCoder](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html)

# Class ActivityDescriptorBasedDeepLinkCoder

### Hierarchy

  * ActivityDescriptorBasedDeepLinkCoder

### Implements

  * [DeepLinkCoder](../interfaces/extensions_deep_linking.deeplinkcoder.html)

## Index

### Methods

  * [decode](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html#decode)
  * [encode](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html#encode)

## Methods

### decode

  * decode(deepLink: string): Action<[PushPayload](../interfaces/core_activity.activityactions-1.pushpayload.html)>[]

  * Implementation of [DeepLinkCoder](../interfaces/extensions_deep_linking.deeplinkcoder.html).[decode](../interfaces/extensions_deep_linking.deeplinkcoder.html#decode)

    * Defined in src/extensions/deep-linking/internal/deepLinkCoder.ts:67

#### Parameters

    * ##### deepLink: string

#### Returns
Action<[PushPayload](../interfaces/core_activity.activityactions-1.pushpayload.html)>[]

### encode

  * encode(activity: [Activity](../modules/core_activity.activity-1.html), sourceActivities: [Activity](../modules/core_activity.activity-1.html)[]): string

  * Implementation of [DeepLinkCoder](../interfaces/extensions_deep_linking.deeplinkcoder.html).[encode](../interfaces/extensions_deep_linking.deeplinkcoder.html#encode)

    * Defined in src/extensions/deep-linking/internal/deepLinkCoder.ts:60

#### Parameters

    * ##### activity: [Activity](../modules/core_activity.activity-1.html)

    * ##### sourceActivities: [Activity](../modules/core_activity.activity-1.html)[]

#### Returns string

  * [_Globals_](../globals.html)
  * [extensions/deep-linking](../modules/extensions_deep_linking.html)
    * [DeepLinkingFactories](../modules/extensions_deep_linking.deeplinkingfactories-1.html)

  * [DeepLinkingFactories](../modules/extensions_deep_linking.html#deeplinkingfactories)

  * [ActivityDescriptorBasedDeepLinkCoder](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html)
    * [decode](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html#decode)
    * [encode](extensions_deep_linking.activitydescriptorbaseddeeplinkcoder.html#encode)

  * [Configuration](../interfaces/extensions_deep_linking.configuration.html)
  * [CurrentActivityLocationManager](../interfaces/extensions_deep_linking.currentactivitylocationmanager.html)
  * [DeepLinkCoder](../interfaces/extensions_deep_linking.deeplinkcoder.html)
  * [applyDeepLink](../modules/extensions_deep_linking.html#applydeeplink)
  * [clearDeepLink](../modules/extensions_deep_linking.html#cleardeeplink)
  * [handleApplyDeepLink](../modules/extensions_deep_linking.html#handleapplydeeplink)
  * [handleLoadWelcomePage](../modules/extensions_deep_linking.html#handleloadwelcomepage)
  * [handleUpdateDeepLink](../modules/extensions_deep_linking.html#handleupdatedeeplink)
  * [loadWelcomePage](../modules/extensions_deep_linking.html#loadwelcomepage)
  * [updateDeepLink](../modules/extensions_deep_linking.html#updatedeeplink)
  * [browserLocationManager](../modules/extensions_deep_linking.html#browserlocationmanager)

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

