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
  * [core/frame](../modules/core_frame.html)
  * [ApplicationFrameLayout](core_frame.applicationframelayout.html)

# Class ApplicationFrameLayout<SS>

### Type parameters

  * #### SS

### Hierarchy

  * Component<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }, ApplicationFrameLayoutState>
    * ApplicationFrameLayout

## Index

### Constructors

  * [constructor](core_frame.applicationframelayout.html#constructor)

### Properties

  * [context](core_frame.applicationframelayout.html#context)
  * [props](core_frame.applicationframelayout.html#props)
  * [refs](core_frame.applicationframelayout.html#refs)
  * [state](core_frame.applicationframelayout.html#state)
  * [contextType](core_frame.applicationframelayout.html#contexttype)

### Methods

  * [UNSAFE_componentWillMount](core_frame.applicationframelayout.html#unsafe_componentwillmount)
  * [UNSAFE_componentWillReceiveProps](core_frame.applicationframelayout.html#unsafe_componentwillreceiveprops)
  * [UNSAFE_componentWillUpdate](core_frame.applicationframelayout.html#unsafe_componentwillupdate)
  * [componentDidCatch](core_frame.applicationframelayout.html#componentdidcatch)
  * [componentDidMount](core_frame.applicationframelayout.html#componentdidmount)
  * [componentDidUpdate](core_frame.applicationframelayout.html#componentdidupdate)
  * [componentWillMount](core_frame.applicationframelayout.html#componentwillmount)
  * [componentWillReceiveProps](core_frame.applicationframelayout.html#componentwillreceiveprops)
  * [componentWillUnmount](core_frame.applicationframelayout.html#componentwillunmount)
  * [componentWillUpdate](core_frame.applicationframelayout.html#componentwillupdate)
  * [evaluateMobileNavigationBackButtonAction](core_frame.applicationframelayout.html#evaluatemobilenavigationbackbuttonaction)
  * [forceUpdate](core_frame.applicationframelayout.html#forceupdate)
  * [getSnapshotBeforeUpdate](core_frame.applicationframelayout.html#getsnapshotbeforeupdate)
  * [onSetMainMenuExpanded](core_frame.applicationframelayout.html#onsetmainmenuexpanded)
  * [onSetSubExpanded](core_frame.applicationframelayout.html#onsetsubexpanded)
  * [render](core_frame.applicationframelayout.html#render)
  * [setState](core_frame.applicationframelayout.html#setstate)
  * [shouldComponentUpdate](core_frame.applicationframelayout.html#shouldcomponentupdate)
  * [shouldSidebarCollapse](core_frame.applicationframelayout.html#shouldsidebarcollapse)
  * [shouldSidebarExpand](core_frame.applicationframelayout.html#shouldsidebarexpand)
  * [getDerivedStateFromProps](core_frame.applicationframelayout.html#getderivedstatefromprops)

## Constructors

### constructor

  * new ApplicationFrameLayout(props: StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps): [ApplicationFrameLayout](core_frame.applicationframelayout.html)

  * Overrides [ErrorBoundary](core_frame.errorboundary.html).[constructor](core_frame.errorboundary.html#constructor)

    * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:259

#### Parameters

    * ##### props: StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps

#### Returns [ApplicationFrameLayout](core_frame.applicationframelayout.html)

## Properties

### context

context: React.ContextType<typeof SizeContext> | undefined

Overrides
[ErrorBoundary](core_frame.errorboundary.html).[context](core_frame.errorboundary.html#context)

  * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:259

### props

props: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }> & Readonly<{ children?: ReactNode | undefined }>

Inherited from
[ErrorBoundary](core_frame.errorboundary.html).[props](core_frame.errorboundary.html#props)

  * Defined in node_modules/@types/react/index.d.ts:504

### refs

refs: {}

Inherited from
[ErrorBoundary](core_frame.errorboundary.html).[refs](core_frame.errorboundary.html#refs)

  * Defined in node_modules/@types/react/index.d.ts:510

deprecated

    

<https://reactjs.org/docs/refs-and-the-dom.html#legacy-api-string-refs>

#### Type declaration

  * ##### [key: string]: ReactInstance

### state

state: Readonly<ApplicationFrameLayoutState>

Inherited from
[ApplicationFrameLayout](core_frame.applicationframelayout.html).[state](core_frame.applicationframelayout.html#state)

  * Defined in node_modules/@types/react/index.d.ts:505

### Static contextType

contextType: Context<SizeContextProps> = SizeContext

Overrides
[ErrorBoundary](core_frame.errorboundary.html).[contextType](core_frame.errorboundary.html#contexttype)

  * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:258

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

  * UNSAFE_componentWillReceiveProps(nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, nextContext: any): void

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

    * ##### nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

    * ##### nextContext: any

#### Returns void

### Optional UNSAFE_componentWillUpdate

  * UNSAFE_componentWillUpdate(nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, nextState: Readonly<ApplicationFrameLayoutState>, nextContext: any): void

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

    * ##### nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

    * ##### nextState: Readonly<ApplicationFrameLayoutState>

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

  * componentDidUpdate(prevProps: StateProps & { currentSize?: SizeDetectorProps.Size }): void

  * Overrides [ErrorBoundary](core_frame.errorboundary.html).[componentDidUpdate](core_frame.errorboundary.html#componentdidupdate)

    * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:286

Collapse the sidebar and remember the old state when the size changed under
the small device threshold.

Recover the sidebar state when the size changed above the small device
threshold again.

If the current device size is a small device: Expand the sidebar, if there are
new activities which added a view to the sidebar OR If there are only views in
the sidebar.

Collapse the sidebar if activities got cancelled.

#### Parameters

    * ##### prevProps: StateProps & { currentSize?: SizeDetectorProps.Size }

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

  * componentWillReceiveProps(nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, nextContext: any): void

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

    * ##### nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

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

  * componentWillUpdate(nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, nextState: Readonly<ApplicationFrameLayoutState>, nextContext: any): void

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

    * ##### nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

    * ##### nextState: Readonly<ApplicationFrameLayoutState>

    * ##### nextContext: any

#### Returns void

### evaluateMobileNavigationBackButtonAction

  * evaluateMobileNavigationBackButtonAction(visibleRegion: [Reference](../modules/core_model.applicationmodel-1.region.reference.html)): [MobileNavigationAction](../modules/core_frame.html#mobilenavigationaction) | undefined

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:579

#### Parameters

    * ##### visibleRegion: [Reference](../modules/core_model.applicationmodel-1.region.reference.html)

#### Returns [MobileNavigationAction](../modules/core_frame.html#mobilenavigationaction) | undefined

### forceUpdate

  * forceUpdate(callback?: undefined | (() => void)): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[forceUpdate](core_frame.errorboundary.html#forceupdate)

    * Defined in node_modules/@types/react/index.d.ts:496

#### Parameters

    * ##### Optional callback: undefined | (() => void)

#### Returns void

### Optional getSnapshotBeforeUpdate

  * getSnapshotBeforeUpdate(prevProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, prevState: Readonly<ApplicationFrameLayoutState>): SS | null

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)

    * Defined in node_modules/@types/react/index.d.ts:682

Runs before React applies the result of `render` to the document, and returns
an object to be given to componentDidUpdate. Useful for saving things such as
scroll position before `render` causes changes to it.

Note: the presence of getSnapshotBeforeUpdate prevents any of the deprecated
lifecycle events from running.

#### Parameters

    * ##### prevProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

    * ##### prevState: Readonly<ApplicationFrameLayoutState>

#### Returns SS | null

### onSetMainMenuExpanded

  * onSetMainMenuExpanded(expanded: boolean): void

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:575

#### Parameters

    * ##### expanded: boolean

#### Returns void

### onSetSubExpanded

  * onSetSubExpanded(expanded: boolean): void

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:571

#### Parameters

    * ##### expanded: boolean

#### Returns void

### render

  * render(): React.ReactNode

  * Overrides Component.render

    * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:366

#### Returns React.ReactNode

### setState

  * setState<K>(state: ((prevState: Readonly<ApplicationFrameLayoutState>, props: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>) => null | S | {}) | (null | S | {}), callback?: undefined | (() => void)): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[setState](core_frame.errorboundary.html#setstate)

    * Defined in node_modules/@types/react/index.d.ts:491

#### Type parameters

    * #### K: keyof ApplicationFrameLayoutState

#### Parameters

    * ##### state: ((prevState: Readonly<ApplicationFrameLayoutState>, props: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>) => null | S | {}) | (null | S | {})

    * ##### Optional callback: undefined | (() => void)

#### Returns void

### Optional shouldComponentUpdate

  * shouldComponentUpdate(nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>, nextState: Readonly<ApplicationFrameLayoutState>, nextContext: any): boolean

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

    * ##### nextProps: Readonly<StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }>

    * ##### nextState: Readonly<ApplicationFrameLayoutState>

    * ##### nextContext: any

#### Returns boolean

### shouldSidebarCollapse

  * shouldSidebarCollapse(prevProps: StateProps): boolean

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:331

#### Parameters

    * ##### prevProps: StateProps

#### Returns boolean

### shouldSidebarExpand

  * shouldSidebarExpand(prevProps: StateProps): boolean

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:310

#### Parameters

    * ##### prevProps: StateProps

#### Returns boolean

### Static getDerivedStateFromProps

  * getDerivedStateFromProps(nextProps: StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }, prevState: ApplicationFrameLayoutState): Partial<ApplicationFrameLayoutState> | null

  *     * Defined in src/core/frame/internal/layout/ApplicationFrameLayout.tsx:344

This is used to set subExpandedState and subExpanded in state to the value
from the props when this changes due to a scene change with new settings.

#### Parameters

    * ##### nextProps: StateProps & [OwnProps](../interfaces/core_frame.ownprops.html) & DispatchProps & { currentSize?: SizeDetectorProps.Size }

    * ##### prevState: ApplicationFrameLayoutState

#### Returns Partial<ApplicationFrameLayoutState> | null

  * [_Globals_](../globals.html)
  * [core/frame](../modules/core_frame.html)
    * [FrameFactories](../modules/core_frame.framefactories-1.html)
    * [FrameViews](../modules/core_frame.frameviews-1.html)

  * [ApplicationFrameLayout](core_frame.applicationframelayout.html)
    * [constructor](core_frame.applicationframelayout.html#constructor)
    * [context](core_frame.applicationframelayout.html#context)
    * [props](core_frame.applicationframelayout.html#props)
    * [refs](core_frame.applicationframelayout.html#refs)
    * [state](core_frame.applicationframelayout.html#state)
    * [contextType](core_frame.applicationframelayout.html#contexttype)
    * [UNSAFE_componentWillMount](core_frame.applicationframelayout.html#unsafe_componentwillmount)
    * [UNSAFE_componentWillReceiveProps](core_frame.applicationframelayout.html#unsafe_componentwillreceiveprops)
    * [UNSAFE_componentWillUpdate](core_frame.applicationframelayout.html#unsafe_componentwillupdate)
    * [componentDidCatch](core_frame.applicationframelayout.html#componentdidcatch)
    * [componentDidMount](core_frame.applicationframelayout.html#componentdidmount)
    * [componentDidUpdate](core_frame.applicationframelayout.html#componentdidupdate)
    * [componentWillMount](core_frame.applicationframelayout.html#componentwillmount)
    * [componentWillReceiveProps](core_frame.applicationframelayout.html#componentwillreceiveprops)
    * [componentWillUnmount](core_frame.applicationframelayout.html#componentwillunmount)
    * [componentWillUpdate](core_frame.applicationframelayout.html#componentwillupdate)
    * [evaluateMobileNavigationBackButtonAction](core_frame.applicationframelayout.html#evaluatemobilenavigationbackbuttonaction)
    * [forceUpdate](core_frame.applicationframelayout.html#forceupdate)
    * [getSnapshotBeforeUpdate](core_frame.applicationframelayout.html#getsnapshotbeforeupdate)
    * [onSetMainMenuExpanded](core_frame.applicationframelayout.html#onsetmainmenuexpanded)
    * [onSetSubExpanded](core_frame.applicationframelayout.html#onsetsubexpanded)
    * [render](core_frame.applicationframelayout.html#render)
    * [setState](core_frame.applicationframelayout.html#setstate)
    * [shouldComponentUpdate](core_frame.applicationframelayout.html#shouldcomponentupdate)
    * [shouldSidebarCollapse](core_frame.applicationframelayout.html#shouldsidebarcollapse)
    * [shouldSidebarExpand](core_frame.applicationframelayout.html#shouldsidebarexpand)
    * [getDerivedStateFromProps](core_frame.applicationframelayout.html#getderivedstatefromprops)

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

