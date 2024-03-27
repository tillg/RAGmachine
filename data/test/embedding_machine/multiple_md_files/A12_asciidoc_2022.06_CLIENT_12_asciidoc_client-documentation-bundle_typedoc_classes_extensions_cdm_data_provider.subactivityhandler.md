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
  * [extensions/cdm/data-provider](../modules/extensions_cdm_data_provider.html)
  * [SubActivityHandler](extensions_cdm_data_provider.subactivityhandler.html)

# Class SubActivityHandler

### Hierarchy

  * SubActivityHandler

### Implements

  * [CddDataHandler](../interfaces/extensions_cdm_data_provider.cdddatahandler.html)

## Index

### Constructors

  * [constructor](extensions_cdm_data_provider.subactivityhandler.html#constructor)

### Methods

  * [load](extensions_cdm_data_provider.subactivityhandler.html#load)
  * [save](extensions_cdm_data_provider.subactivityhandler.html#save)

## Constructors

### constructor

  * new SubActivityHandler(activity: [Activity](../modules/core_activity.activity-1.html), initiatingActivity: [Activity](../modules/core_activity.activity-1.html), documentModel: DocumentModel): [SubActivityHandler](extensions_cdm_data_provider.subactivityhandler.html)

  *     * Defined in src/extensions/cdm/dataProvider/internal/subactivity/SubActivityHandler.ts:45

#### Parameters

    * ##### activity: [Activity](../modules/core_activity.activity-1.html)

    * ##### initiatingActivity: [Activity](../modules/core_activity.activity-1.html)

    * ##### documentModel: DocumentModel

#### Returns
[SubActivityHandler](extensions_cdm_data_provider.subactivityhandler.html)

## Methods

### load

  * load(loadType: [LoadType](../modules/extensions_cdm_data_provider.html#loadtype)): SagaIterator<void>

  * Implementation of [CddDataHandler](../interfaces/extensions_cdm_data_provider.cdddatahandler.html).[load](../interfaces/extensions_cdm_data_provider.cdddatahandler.html#load)

    * Defined in src/extensions/cdm/dataProvider/internal/subactivity/SubActivityHandler.ts:52

#### Parameters

    * ##### loadType: [LoadType](../modules/extensions_cdm_data_provider.html#loadtype)

#### Returns SagaIterator<void>

### save

  * save(config: [SaveConfig](../interfaces/core_data.dataprovider-1.saveconfig.html)): SagaIterator<void>

  * Implementation of [CddDataHandler](../interfaces/extensions_cdm_data_provider.cdddatahandler.html).[save](../interfaces/extensions_cdm_data_provider.cdddatahandler.html#save)

    * Defined in src/extensions/cdm/dataProvider/internal/subactivity/SubActivityHandler.ts:60

#### Parameters

    * ##### config: [SaveConfig](../interfaces/core_data.dataprovider-1.saveconfig.html)

#### Returns SagaIterator<void>

  * [_Globals_](../globals.html)
  * [extensions/cdm/data-provider](../modules/extensions_cdm_data_provider.html)

  * [StandaloneActivityHandler](extensions_cdm_data_provider.standaloneactivityhandler.html)

  * [SubActivityHandler](extensions_cdm_data_provider.subactivityhandler.html)
    * [constructor](extensions_cdm_data_provider.subactivityhandler.html#constructor)
    * [load](extensions_cdm_data_provider.subactivityhandler.html#load)
    * [save](extensions_cdm_data_provider.subactivityhandler.html#save)

  * [CDDQuery](../interfaces/extensions_cdm_data_provider.cddquery.html)
  * [CddDataHandler](../interfaces/extensions_cdm_data_provider.cdddatahandler.html)
  * [CdmRelationship](../interfaces/extensions_cdm_data_provider.cdmrelationship.html)
  * [DirectedRelationships](../interfaces/extensions_cdm_data_provider.directedrelationships.html)
  * [DocModelReference](../interfaces/extensions_cdm_data_provider.docmodelreference.html)
  * [NewLinkDescriptorSpecs](../interfaces/extensions_cdm_data_provider.newlinkdescriptorspecs.html)
  * [LinkDocumentModelProvider](../modules/extensions_cdm_data_provider.html#linkdocumentmodelprovider)
  * [LoadType](../modules/extensions_cdm_data_provider.html#loadtype)
  * [ModelProvider](../modules/extensions_cdm_data_provider.html#modelprovider)
  * [ModelTypeGuard](../modules/extensions_cdm_data_provider.html#modeltypeguard)
  * [EXPERIMENTAL](../modules/extensions_cdm_data_provider.html#experimental)
  * [cddDataProvider](../modules/extensions_cdm_data_provider.html#cdddataprovider)
  * [disableHandlingMiddleware](../modules/extensions_cdm_data_provider.html#disablehandlingmiddleware)
  * [cdmToGraph](../modules/extensions_cdm_data_provider.html#cdmtograph)
  * [computeSubActivityData](../modules/extensions_cdm_data_provider.html#computesubactivitydata)
  * [convertMutations](../modules/extensions_cdm_data_provider.html#convertmutations)
  * [createCandidateDataHoldersSaga](../modules/extensions_cdm_data_provider.html#createcandidatedataholderssaga)
  * [createInitialDataHolderData](../modules/extensions_cdm_data_provider.html#createinitialdataholderdata)
  * [dgForNewEntity](../modules/extensions_cdm_data_provider.html#dgfornewentity)
  * [extractPureDocument](../modules/extensions_cdm_data_provider.html#extractpuredocument)
  * [isParentCdmActivity](../modules/extensions_cdm_data_provider.html#isparentcdmactivity)
  * [isSetCddInActivity](../modules/extensions_cdm_data_provider.html#issetcddinactivity)
  * [linkedActivities](../modules/extensions_cdm_data_provider.html#linkedactivities)
  * [load](../modules/extensions_cdm_data_provider.html#load)
  * [loadDG](../modules/extensions_cdm_data_provider.html#loaddg)
  * [loadSubDG](../modules/extensions_cdm_data_provider.html#loadsubdg)
  * [resolveDocumentModel](../modules/extensions_cdm_data_provider.html#resolvedocumentmodel)
  * [toCddChanges](../modules/extensions_cdm_data_provider.html#tocddchanges)

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

