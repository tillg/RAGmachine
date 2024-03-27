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
  * [core/application](../modules/core_application.html)
  * [ModuleRegistryImpl](core_application.moduleregistryimpl.html)

# Class ModuleRegistryImpl

### Hierarchy

  * ModuleRegistryImpl

### Implements

  * [ModuleRegistry](../interfaces/core_application.moduleregistry.html)

## Index

### Constructors

  * [constructor](core_application.moduleregistryimpl.html#constructor)

### Methods

  * [addModule](core_application.moduleregistryimpl.html#addmodule)
  * [getAllModules](core_application.moduleregistryimpl.html#getallmodules)
  * [removeModule](core_application.moduleregistryimpl.html#removemodule)
  * [removeModuleById](core_application.moduleregistryimpl.html#removemodulebyid)
  * [subscribe](core_application.moduleregistryimpl.html#subscribe)

## Constructors

### constructor

  * new ModuleRegistryImpl(interceptor: [ModuleRegistryEventInterceptor](../interfaces/core_application.moduleregistryeventinterceptor.html)): [ModuleRegistryImpl](core_application.moduleregistryimpl.html)

  *     * Defined in src/core/application/internal/factories/moduleRegistry.ts:117

Sets an interceptor function that is called before a module is added or
removed. Module Events are only executed if the interceptor returns false.

#### Parameters

    * ##### interceptor: [ModuleRegistryEventInterceptor](../interfaces/core_application.moduleregistryeventinterceptor.html)

#### Returns [ModuleRegistryImpl](core_application.moduleregistryimpl.html)

## Methods

### addModule

  * addModule(module: [Module](../interfaces/core_application.module-1.html)): void

  * Implementation of [ModuleRegistry](../interfaces/core_application.moduleregistry.html).[addModule](../interfaces/core_application.moduleregistry.html#addmodule)

    * Defined in src/core/application/internal/factories/moduleRegistry.ts:147

#### Parameters

    * ##### module: [Module](../interfaces/core_application.module-1.html)

#### Returns void

### getAllModules

  * getAllModules(): ReadonlyArray<[Module](../interfaces/core_application.module-1.html)>

  * Implementation of [ModuleRegistry](../interfaces/core_application.moduleregistry.html).[getAllModules](../interfaces/core_application.moduleregistry.html#getallmodules)

    * Defined in src/core/application/internal/factories/moduleRegistry.ts:183

#### Returns
ReadonlyArray<[Module](../interfaces/core_application.module-1.html)>

### removeModule

  * removeModule(module: [Module](../interfaces/core_application.module-1.html)): void

  * Implementation of [ModuleRegistry](../interfaces/core_application.moduleregistry.html).[removeModule](../interfaces/core_application.moduleregistry.html#removemodule)

    * Defined in src/core/application/internal/factories/moduleRegistry.ts:169

#### Parameters

    * ##### module: [Module](../interfaces/core_application.module-1.html)

#### Returns void

### removeModuleById

  * removeModuleById(id: string): void

  * Implementation of [ModuleRegistry](../interfaces/core_application.moduleregistry.html).[removeModuleById](../interfaces/core_application.moduleregistry.html#removemodulebyid)

    * Defined in src/core/application/internal/factories/moduleRegistry.ts:161

#### Parameters

    * ##### id: string

#### Returns void

### subscribe

  * subscribe(eventListener: [ModuleRegistryEventListener](../interfaces/core_application.moduleregistryeventlistener.html)): () => void

  *     * Defined in src/core/application/internal/factories/moduleRegistry.ts:137

Subscribe to Module events This is used by some extensions to react on module
events.

#### Parameters

    * ##### eventListener: [ModuleRegistryEventListener](../interfaces/core_application.moduleregistryeventlistener.html)

#### Returns () => void

    *       * (): void
      * #### Returns void

  * [_Globals_](../globals.html)
  * [core/application](../modules/core_application.html)
    * [ApplicationActions](../modules/core_application.applicationactions-1.html)
    * [ApplicationFactories](../modules/core_application.applicationfactories-1.html)
    * [ApplicationReducers](../modules/core_application.applicationreducers-1.html)
    * [ApplicationSaga](../modules/core_application.applicationsaga-1.html)
    * [ApplicationSelectors](../modules/core_application.applicationselectors-1.html)
    * [ModuleRegistryProvider](../modules/core_application.moduleregistryprovider-1.html)

  * [ModuleRegistryImpl](core_application.moduleregistryimpl.html)
    * [constructor](core_application.moduleregistryimpl.html#constructor)
    * [addModule](core_application.moduleregistryimpl.html#addmodule)
    * [getAllModules](core_application.moduleregistryimpl.html#getallmodules)
    * [removeModule](core_application.moduleregistryimpl.html#removemodule)
    * [removeModuleById](core_application.moduleregistryimpl.html#removemodulebyid)
    * [subscribe](core_application.moduleregistryimpl.html#subscribe)

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

