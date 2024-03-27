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
  * [extensions/relationship](../modules/extensions_relationship.html)
  * [StandaloneFormEngine](extensions_relationship.standaloneformengine.html)

# Class StandaloneFormEngine<S, SS, S>

### Type parameters

  * #### S

  * #### SS

  * #### S

### Hierarchy

  * Component<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>
    * StandaloneFormEngine

## Index

### Constructors

  * [constructor](extensions_relationship.standaloneformengine.html#constructor)

### Properties

  * [context](extensions_relationship.standaloneformengine.html#context)
  * [props](extensions_relationship.standaloneformengine.html#props)
  * [refs](extensions_relationship.standaloneformengine.html#refs)
  * [state](extensions_relationship.standaloneformengine.html#state)
  * [contextType](extensions_relationship.standaloneformengine.html#contexttype)

### Methods

  * [UNSAFE_componentWillMount](extensions_relationship.standaloneformengine.html#unsafe_componentwillmount)
  * [UNSAFE_componentWillReceiveProps](extensions_relationship.standaloneformengine.html#unsafe_componentwillreceiveprops)
  * [UNSAFE_componentWillUpdate](extensions_relationship.standaloneformengine.html#unsafe_componentwillupdate)
  * [componentDidCatch](extensions_relationship.standaloneformengine.html#componentdidcatch)
  * [componentDidMount](extensions_relationship.standaloneformengine.html#componentdidmount)
  * [componentDidUpdate](extensions_relationship.standaloneformengine.html#componentdidupdate)
  * [componentWillMount](extensions_relationship.standaloneformengine.html#componentwillmount)
  * [componentWillReceiveProps](extensions_relationship.standaloneformengine.html#componentwillreceiveprops)
  * [componentWillUnmount](extensions_relationship.standaloneformengine.html#componentwillunmount)
  * [componentWillUpdate](extensions_relationship.standaloneformengine.html#componentwillupdate)
  * [forceUpdate](extensions_relationship.standaloneformengine.html#forceupdate)
  * [getSnapshotBeforeUpdate](extensions_relationship.standaloneformengine.html#getsnapshotbeforeupdate)
  * [render](extensions_relationship.standaloneformengine.html#render)
  * [setState](extensions_relationship.standaloneformengine.html#setstate)
  * [shouldComponentUpdate](extensions_relationship.standaloneformengine.html#shouldcomponentupdate)

## Constructors

### constructor

  * new StandaloneFormEngine(props: [FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)): [StandaloneFormEngine](extensions_relationship.standaloneformengine.html)

  * Overrides [ErrorBoundary](core_frame.errorboundary.html).[constructor](core_frame.errorboundary.html#constructor)

    * Defined in src/extensions/relationship/internal/ui/components/StandaloneFormEngine.tsx:76

#### Parameters

    * ##### props: [FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)

#### Returns
[StandaloneFormEngine](extensions_relationship.standaloneformengine.html)

## Properties

### context

context: any

Inherited from
[ErrorBoundary](core_frame.errorboundary.html).[context](core_frame.errorboundary.html#context)

  * Defined in node_modules/@types/react/index.d.ts:479

If using the new style context, re-declare this in your class to be the
`React.ContextType` of your `static contextType`. Should be used with type
annotation or static contextType.

    
    
    static contextType = MyContext
    // For TS pre-3.7:
    context!: React.ContextType<typeof MyContext>
    // For TS 3.7 and above:
    declare context: React.ContextType<typeof MyContext>

see

    

<https://reactjs.org/docs/context.html>

### props

props: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)> & Readonly<{ children?: ReactNode | undefined }>

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

state: Readonly<S>

Inherited from
[ApplicationFrameLayout](core_frame.applicationframelayout.html).[state](core_frame.applicationframelayout.html#state)

  * Defined in node_modules/@types/react/index.d.ts:505

### Static Optional contextType

contextType: Context<any> | undefined

Inherited from
[ErrorBoundary](core_frame.errorboundary.html).[contextType](core_frame.errorboundary.html#contexttype)

  * Defined in node_modules/@types/react/index.d.ts:461

If set, `this.context` will be set at runtime to the current value of the
given Context.

Usage:

    
    
    type MyContext = number
    const Ctx = React.createContext<MyContext>(0)
    
    class Foo extends React.Component {
      static contextType = Ctx
      context!: React.ContextType<typeof Ctx>
      render () {
        return <>My context's value: {this.context}</>;
      }
    }

see

    

<https://reactjs.org/docs/context.html#classcontexttype>

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

  * UNSAFE_componentWillReceiveProps(nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, nextContext: any): void

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

    * ##### nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

    * ##### nextContext: any

#### Returns void

### Optional UNSAFE_componentWillUpdate

  * UNSAFE_componentWillUpdate(nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, nextState: Readonly<S>, nextContext: any): void

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

    * ##### nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

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

### Optional componentDidUpdate

  * componentDidUpdate(prevProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, prevState: Readonly<S>, snapshot?: [SS]()): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[componentDidUpdate](core_frame.errorboundary.html#componentdidupdate)

    * Defined in node_modules/@types/react/index.d.ts:688

Called immediately after updating occurs. Not called for the initial render.

The snapshot is only present if getSnapshotBeforeUpdate is present and returns
non-null.

#### Parameters

    * ##### prevProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

    * ##### prevState: Readonly<S>

    * ##### Optional snapshot: [SS]()

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

  * componentWillReceiveProps(nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, nextContext: any): void

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

    * ##### nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

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

  * componentWillUpdate(nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, nextState: Readonly<S>, nextContext: any): void

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

    * ##### nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

    * ##### nextState: Readonly<S>

    * ##### nextContext: any

#### Returns void

### forceUpdate

  * forceUpdate(callback?: undefined | (() => void)): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[forceUpdate](core_frame.errorboundary.html#forceupdate)

    * Defined in node_modules/@types/react/index.d.ts:496

#### Parameters

    * ##### Optional callback: undefined | (() => void)

#### Returns void

### Optional getSnapshotBeforeUpdate

  * getSnapshotBeforeUpdate(prevProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, prevState: Readonly<S>): SS | null

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)

    * Defined in node_modules/@types/react/index.d.ts:682

Runs before React applies the result of `render` to the document, and returns
an object to be given to componentDidUpdate. Useful for saving things such as
scroll position before `render` causes changes to it.

Note: the presence of getSnapshotBeforeUpdate prevents any of the deprecated
lifecycle events from running.

#### Parameters

    * ##### prevProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

    * ##### prevState: Readonly<S>

#### Returns SS | null

### render

  * render(): Element

  * Overrides Component.render

    * Defined in src/extensions/relationship/internal/ui/components/StandaloneFormEngine.tsx:95

#### Returns Element

### setState

  * setState<K>(state: ((prevState: Readonly<S>, props: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>) => null | S | {}) | (null | S | {}), callback?: undefined | (() => void)): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[setState](core_frame.errorboundary.html#setstate)

    * Defined in node_modules/@types/react/index.d.ts:491

#### Type parameters

    * #### K: keyof S

#### Parameters

    * ##### state: ((prevState: Readonly<S>, props: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>) => null | S | {}) | (null | S | {})

    * ##### Optional callback: undefined | (() => void)

#### Returns void

### Optional shouldComponentUpdate

  * shouldComponentUpdate(nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>, nextState: Readonly<S>, nextContext: any): boolean

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

    * ##### nextProps: Readonly<[FormEngineProps](../interfaces/extensions_relationship.formengineprops.html)>

    * ##### nextState: Readonly<S>

    * ##### nextContext: any

#### Returns boolean

  * [_Globals_](../globals.html)
  * [extensions/relationship](../modules/extensions_relationship.html)
    * [AdapterLink](../modules/extensions_relationship.adapterlink.html)
    * [Relationship](../modules/extensions_relationship.relationship-1.html)
    * [RelationshipActions](../modules/extensions_relationship.relationshipactions-1.html)
    * [RelationshipFactories](../modules/extensions_relationship.relationshipfactories-1.html)
    * [RelationshipReducers](../modules/extensions_relationship.relationshipreducers-1.html)
    * [RelationshipSelectors](../modules/extensions_relationship.relationshipselectors-1.html)
    * [RelationshipViews](../modules/extensions_relationship.relationshipviews-1.html)

  * [StandaloneFormEngine](extensions_relationship.standaloneformengine.html)
    * [constructor](extensions_relationship.standaloneformengine.html#constructor)
    * [context](extensions_relationship.standaloneformengine.html#context)
    * [props](extensions_relationship.standaloneformengine.html#props)
    * [refs](extensions_relationship.standaloneformengine.html#refs)
    * [state](extensions_relationship.standaloneformengine.html#state)
    * [contextType](extensions_relationship.standaloneformengine.html#contexttype)
    * [UNSAFE_componentWillMount](extensions_relationship.standaloneformengine.html#unsafe_componentwillmount)
    * [UNSAFE_componentWillReceiveProps](extensions_relationship.standaloneformengine.html#unsafe_componentwillreceiveprops)
    * [UNSAFE_componentWillUpdate](extensions_relationship.standaloneformengine.html#unsafe_componentwillupdate)
    * [componentDidCatch](extensions_relationship.standaloneformengine.html#componentdidcatch)
    * [componentDidMount](extensions_relationship.standaloneformengine.html#componentdidmount)
    * [componentDidUpdate](extensions_relationship.standaloneformengine.html#componentdidupdate)
    * [componentWillMount](extensions_relationship.standaloneformengine.html#componentwillmount)
    * [componentWillReceiveProps](extensions_relationship.standaloneformengine.html#componentwillreceiveprops)
    * [componentWillUnmount](extensions_relationship.standaloneformengine.html#componentwillunmount)
    * [componentWillUpdate](extensions_relationship.standaloneformengine.html#componentwillupdate)
    * [forceUpdate](extensions_relationship.standaloneformengine.html#forceupdate)
    * [getSnapshotBeforeUpdate](extensions_relationship.standaloneformengine.html#getsnapshotbeforeupdate)
    * [render](extensions_relationship.standaloneformengine.html#render)
    * [setState](extensions_relationship.standaloneformengine.html#setstate)
    * [shouldComponentUpdate](extensions_relationship.standaloneformengine.html#shouldcomponentupdate)

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

