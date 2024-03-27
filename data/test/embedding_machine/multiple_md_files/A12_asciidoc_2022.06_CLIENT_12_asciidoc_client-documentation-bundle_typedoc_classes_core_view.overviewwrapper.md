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
  * [core/view](../modules/core_view.html)
  * [OverviewWrapper](core_view.overviewwrapper.html)

# Class OverviewWrapper<S, SS>

### Type parameters

  * #### S

  * #### SS

### Hierarchy

  * PureComponent<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>
    * OverviewWrapper

## Index

### Properties

  * [context](core_view.overviewwrapper.html#context)
  * [contextType](core_view.overviewwrapper.html#contexttype)

### Methods

  * [UNSAFE_componentWillMount](core_view.overviewwrapper.html#unsafe_componentwillmount)
  * [UNSAFE_componentWillReceiveProps](core_view.overviewwrapper.html#unsafe_componentwillreceiveprops)
  * [UNSAFE_componentWillUpdate](core_view.overviewwrapper.html#unsafe_componentwillupdate)
  * [componentDidCatch](core_view.overviewwrapper.html#componentdidcatch)
  * [componentDidMount](core_view.overviewwrapper.html#componentdidmount)
  * [componentDidUpdate](core_view.overviewwrapper.html#componentdidupdate)
  * [componentWillMount](core_view.overviewwrapper.html#componentwillmount)
  * [componentWillReceiveProps](core_view.overviewwrapper.html#componentwillreceiveprops)
  * [componentWillUnmount](core_view.overviewwrapper.html#componentwillunmount)
  * [componentWillUpdate](core_view.overviewwrapper.html#componentwillupdate)
  * [getNextSortingState](core_view.overviewwrapper.html#getnextsortingstate)
  * [getRowLoadingStatus](core_view.overviewwrapper.html#getrowloadingstatus)
  * [getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)
  * [onColumnClick](core_view.overviewwrapper.html#oncolumnclick)
  * [onFilterChange](core_view.overviewwrapper.html#onfilterchange)
  * [onLoadMoreRows](core_view.overviewwrapper.html#onloadmorerows)
  * [onMultiSelectionClear](core_view.overviewwrapper.html#onmultiselectionclear)
  * [onOverallMultiSelectionButtonClick](core_view.overviewwrapper.html#onoverallmultiselectionbuttonclick)
  * [onPageChange](core_view.overviewwrapper.html#onpagechange)
  * [onRowButtonClick](core_view.overviewwrapper.html#onrowbuttonclick)
  * [onRowClick](core_view.overviewwrapper.html#onrowclick)
  * [onRowSelect](core_view.overviewwrapper.html#onrowselect)
  * [onRowsRendered](core_view.overviewwrapper.html#onrowsrendered)
  * [onSearch](core_view.overviewwrapper.html#onsearch)
  * [render](core_view.overviewwrapper.html#render)
  * [setListRef](core_view.overviewwrapper.html#setlistref)
  * [setLoaderRef](core_view.overviewwrapper.html#setloaderref)
  * [shouldComponentUpdate](core_view.overviewwrapper.html#shouldcomponentupdate)

## Properties

### context

context: React.ContextType<typeof LocalizerContext> | undefined

  * Defined in src/core/view/internal/components/overview-engine.tsx:89

### Static contextType

contextType: Context<L10nContext> = LocalizerContext

  * Defined in src/core/view/internal/components/overview-engine.tsx:88

## Methods

### Optional UNSAFE_componentWillMount

  * UNSAFE_componentWillMount(): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[UNSAFE_componentWillMount](core_view.overviewwrapper.html#unsafe_componentwillmount)

    * Defined in node_modules/@types/react/index.d.ts:717

Called immediately before mounting occurs, and before `Component#render`.
Avoid introducing any side-effects or subscriptions in this method.

This method will not stop working in React 17.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use componentDidMount or the constructor instead

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-
rendering.html#initializing-state>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Returns void

### Optional UNSAFE_componentWillReceiveProps

  * UNSAFE_componentWillReceiveProps(nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, nextContext: any): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[UNSAFE_componentWillReceiveProps](core_view.overviewwrapper.html#unsafe_componentwillreceiveprops)

    * Defined in node_modules/@types/react/index.d.ts:749

Called when the component may be receiving new props. React may call this even
if props have not changed, so be sure to compare new and existing props if you
only want to handle changes.

Calling `Component#setState` generally does not trigger this method.

This method will not stop working in React 17.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use static getDerivedStateFromProps instead

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#updating-
state-based-on-props>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Parameters

    * ##### nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### nextContext: any

#### Returns void

### Optional UNSAFE_componentWillUpdate

  * UNSAFE_componentWillUpdate(nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, nextState: Readonly<S>, nextContext: any): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[UNSAFE_componentWillUpdate](core_view.overviewwrapper.html#unsafe_componentwillupdate)

    * Defined in node_modules/@types/react/index.d.ts:777

Called immediately before rendering when new props or state is received. Not
called for the initial render.

Note: You cannot call `Component#setState` here.

This method will not stop working in React 17.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use getSnapshotBeforeUpdate instead

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#reading-
dom-properties-before-an-update>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Parameters

    * ##### nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### nextState: Readonly<S>

    * ##### nextContext: any

#### Returns void

### Optional componentDidCatch

  * componentDidCatch(error: Error, errorInfo: ErrorInfo): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentDidCatch](core_view.overviewwrapper.html#componentdidcatch)

    * Defined in node_modules/@types/react/index.d.ts:646

Catches exceptions generated in descendant components. Unhandled exceptions
will cause the entire component tree to unmount.

#### Parameters

    * ##### error: Error

    * ##### errorInfo: ErrorInfo

#### Returns void

### Optional componentDidMount

  * componentDidMount(): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentDidMount](core_view.overviewwrapper.html#componentdidmount)

    * Defined in node_modules/@types/react/index.d.ts:625

Called immediately after a component is mounted. Setting state here will
trigger re-rendering.

#### Returns void

### componentDidUpdate

  * componentDidUpdate(): void

  * Overrides [ErrorBoundary](core_frame.errorboundary.html).[componentDidUpdate](core_frame.errorboundary.html#componentdidupdate)

    * Defined in src/core/view/internal/components/overview-engine.tsx:97

#### Returns void

### Optional componentWillMount

  * componentWillMount(): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentWillMount](core_view.overviewwrapper.html#componentwillmount)

    * Defined in node_modules/@types/react/index.d.ts:703

Called immediately before mounting occurs, and before `Component#render`.
Avoid introducing any side-effects or subscriptions in this method.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use componentDidMount or the constructor instead; will stop working in
React 17

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-
rendering.html#initializing-state>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Returns void

### Optional componentWillReceiveProps

  * componentWillReceiveProps(nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, nextContext: any): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentWillReceiveProps](core_view.overviewwrapper.html#componentwillreceiveprops)

    * Defined in node_modules/@types/react/index.d.ts:732

Called when the component may be receiving new props. React may call this even
if props have not changed, so be sure to compare new and existing props if you
only want to handle changes.

Calling `Component#setState` generally does not trigger this method.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use static getDerivedStateFromProps instead; will stop working in React
17

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#updating-
state-based-on-props>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Parameters

    * ##### nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### nextContext: any

#### Returns void

### Optional componentWillUnmount

  * componentWillUnmount(): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentWillUnmount](core_view.overviewwrapper.html#componentwillunmount)

    * Defined in node_modules/@types/react/index.d.ts:641

Called immediately before a component is destroyed. Perform any necessary
cleanup in this method, such as cancelled network requests, or cleaning up any
DOM elements created in `componentDidMount`.

#### Returns void

### Optional componentWillUpdate

  * componentWillUpdate(nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, nextState: Readonly<S>, nextContext: any): void

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[componentWillUpdate](core_view.overviewwrapper.html#componentwillupdate)

    * Defined in node_modules/@types/react/index.d.ts:762

Called immediately before rendering when new props or state is received. Not
called for the initial render.

Note: You cannot call `Component#setState` here.

Note: the presence of getSnapshotBeforeUpdate or getDerivedStateFromProps
prevents this from being invoked.

deprecated

    

16.3, use getSnapshotBeforeUpdate instead; will stop working in React 17

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#reading-
dom-properties-before-an-update>

see

    

<https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html#gradual-
migration-path>

#### Parameters

    * ##### nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### nextState: Readonly<S>

    * ##### nextContext: any

#### Returns void

### getNextSortingState

  * getNextSortingState(column: Column, initialSorting?: ColumnRef): { order: "ASC" | "DESC" | "NONE"; path: string }

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:198

#### Parameters

    * ##### column: Column

    * ##### Optional initialSorting: ColumnRef

#### Returns { order: "ASC" | "DESC" | "NONE"; path: string }

    * ##### order: "ASC" | "DESC" | "NONE"

    * ##### path: string

### Protected getRowLoadingStatus

  * getRowLoadingStatus(rowIndex: number): RowLoadingStatus

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:113

#### Parameters

    * ##### rowIndex: number

#### Returns RowLoadingStatus

### Optional getSnapshotBeforeUpdate

  * getSnapshotBeforeUpdate(prevProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, prevState: Readonly<S>): SS | null

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)

    * Defined in node_modules/@types/react/index.d.ts:682

Runs before React applies the result of `render` to the document, and returns
an object to be given to componentDidUpdate. Useful for saving things such as
scroll position before `render` causes changes to it.

Note: the presence of getSnapshotBeforeUpdate prevents any of the deprecated
lifecycle events from running.

#### Parameters

    * ##### prevProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### prevState: Readonly<S>

#### Returns SS | null

### Protected onColumnClick

  * onColumnClick(columnIndex: number): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:184

#### Parameters

    * ##### columnIndex: number

#### Returns void

### Protected onFilterChange

  * onFilterChange(fieldBasedFilters: FilterMap): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:161

#### Parameters

    * ##### fieldBasedFilters: FilterMap

#### Returns void

### Protected onLoadMoreRows

  * onLoadMoreRows(start: number, numberOfRows: number): Promise<void>

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:119

#### Parameters

    * ##### start: number

    * ##### numberOfRows: number

#### Returns Promise<void>

### Protected onMultiSelectionClear

  * onMultiSelectionClear(): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:258

#### Returns void

### Protected onOverallMultiSelectionButtonClick

  * onOverallMultiSelectionButtonClick(params: { affectedRowIds: string[]; selected: boolean }): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:264

#### Parameters

    * ##### params: { affectedRowIds: string[]; selected: boolean }

      * ##### affectedRowIds: string[]

      * ##### selected: boolean

#### Returns void

### Protected onPageChange

  * onPageChange(pageNumber: number): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:168

#### Parameters

    * ##### pageNumber: number

#### Returns void

### Protected onRowButtonClick

  * onRowButtonClick(params: { documentId: string; rowActionModel: RowAction }): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:236

#### Parameters

    * ##### params: { documentId: string; rowActionModel: RowAction }

      * ##### documentId: string

      * ##### rowActionModel: RowAction

#### Returns void

### Protected onRowClick

  * onRowClick(params: { customEvent?: undefined | string; documentId: string }): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:225

#### Parameters

    * ##### params: { customEvent?: undefined | string; documentId: string }

      * ##### Optional customEvent?: undefined | string

      * ##### documentId: string

#### Returns void

### Protected onRowSelect

  * onRowSelect(params: { documentId: string; selected: boolean }): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:250

#### Parameters

    * ##### params: { documentId: string; selected: boolean }

      * ##### documentId: string

      * ##### selected: boolean

#### Returns void

### Protected onRowsRendered

  * onRowsRendered(__namedParameters: { overscanStartIndex: number; overscanStopIndex: number }): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:103

#### Parameters

    * ##### __namedParameters: { overscanStartIndex: number; overscanStopIndex: number }

      * ##### overscanStartIndex: number

      * ##### overscanStopIndex: number

#### Returns void

### Protected onSearch

  * onSearch(filter: string): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:151

#### Parameters

    * ##### filter: string

#### Returns void

### render

  * render(): React.ReactNode

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:275

#### Returns React.ReactNode

### Protected setListRef

  * setListRef(ref: List | null): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:147

#### Parameters

    * ##### ref: List | null

#### Returns void

### Protected setLoaderRef

  * setLoaderRef(ref: InfiniteLoader | null): void

  *     * Defined in src/core/view/internal/components/overview-engine.tsx:143

#### Parameters

    * ##### ref: InfiniteLoader | null

#### Returns void

### Optional shouldComponentUpdate

  * shouldComponentUpdate(nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>, nextState: Readonly<S>, nextContext: any): boolean

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[shouldComponentUpdate](core_view.overviewwrapper.html#shouldcomponentupdate)

    * Defined in node_modules/@types/react/index.d.ts:636

Called to determine whether the change in props and state should trigger a re-
render.

`Component` always returns true. `PureComponent` implements a shallow
comparison on props and state and returns true if any props or states have
changed.

If false is returned, `Component#render`, `componentWillUpdate` and
`componentDidUpdate` will not be called.

#### Parameters

    * ##### nextProps: Readonly<[OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)>

    * ##### nextState: Readonly<S>

    * ##### nextContext: any

#### Returns boolean

  * [_Globals_](../globals.html)
  * [core/view](../modules/core_view.html)
    * [View](../modules/core_view.view-1.html)
    * [ViewSelectors](../modules/core_view.viewselectors-1.html)
    * [ViewViews](../modules/core_view.viewviews-1.html)

  * [OverviewEngineActions](../modules/core_view.html#overviewengineactions)
  * [OverviewEngineReducers](../modules/core_view.html#overviewenginereducers)
  * [OverviewEngineSelectors](../modules/core_view.html#overviewengineselectors)
  * [OverviewEngineState](../modules/core_view.html#overviewenginestate)
  * [View](../modules/core_view.html#view)
  * [ViewSelectors](../modules/core_view.html#viewselectors)
  * [ViewViews](../modules/core_view.html#viewviews)

  * [OverviewWrapper](core_view.overviewwrapper.html)
    * [context](core_view.overviewwrapper.html#context)
    * [contextType](core_view.overviewwrapper.html#contexttype)
    * [UNSAFE_componentWillMount](core_view.overviewwrapper.html#unsafe_componentwillmount)
    * [UNSAFE_componentWillReceiveProps](core_view.overviewwrapper.html#unsafe_componentwillreceiveprops)
    * [UNSAFE_componentWillUpdate](core_view.overviewwrapper.html#unsafe_componentwillupdate)
    * [componentDidCatch](core_view.overviewwrapper.html#componentdidcatch)
    * [componentDidMount](core_view.overviewwrapper.html#componentdidmount)
    * [componentDidUpdate](core_view.overviewwrapper.html#componentdidupdate)
    * [componentWillMount](core_view.overviewwrapper.html#componentwillmount)
    * [componentWillReceiveProps](core_view.overviewwrapper.html#componentwillreceiveprops)
    * [componentWillUnmount](core_view.overviewwrapper.html#componentwillunmount)
    * [componentWillUpdate](core_view.overviewwrapper.html#componentwillupdate)
    * [getNextSortingState](core_view.overviewwrapper.html#getnextsortingstate)
    * [getRowLoadingStatus](core_view.overviewwrapper.html#getrowloadingstatus)
    * [getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)
    * [onColumnClick](core_view.overviewwrapper.html#oncolumnclick)
    * [onFilterChange](core_view.overviewwrapper.html#onfilterchange)
    * [onLoadMoreRows](core_view.overviewwrapper.html#onloadmorerows)
    * [onMultiSelectionClear](core_view.overviewwrapper.html#onmultiselectionclear)
    * [onOverallMultiSelectionButtonClick](core_view.overviewwrapper.html#onoverallmultiselectionbuttonclick)
    * [onPageChange](core_view.overviewwrapper.html#onpagechange)
    * [onRowButtonClick](core_view.overviewwrapper.html#onrowbuttonclick)
    * [onRowClick](core_view.overviewwrapper.html#onrowclick)
    * [onRowSelect](core_view.overviewwrapper.html#onrowselect)
    * [onRowsRendered](core_view.overviewwrapper.html#onrowsrendered)
    * [onSearch](core_view.overviewwrapper.html#onsearch)
    * [render](core_view.overviewwrapper.html#render)
    * [setListRef](core_view.overviewwrapper.html#setlistref)
    * [setLoaderRef](core_view.overviewwrapper.html#setloaderref)
    * [shouldComponentUpdate](core_view.overviewwrapper.html#shouldcomponentupdate)

  * [OverviewWrapperProps](../modules/core_view.html#overviewwrapperprops)
  * [OwnProps](../modules/core_view.html#ownprops)
  * [ConnectedOverviewWrapper](../modules/core_view.html#connectedoverviewwrapper)
  * [BaseProgressIndicator](../modules/core_view.html#baseprogressindicator)
  * [createRenderGuardComponent](../modules/core_view.html#createrenderguardcomponent)
  * [debounce](../modules/core_view.html#debounce)
  * [memoize](../modules/core_view.html#memoize)
  * [DocumentModelUtils](../modules/core_view.html#documentmodelutils)

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

