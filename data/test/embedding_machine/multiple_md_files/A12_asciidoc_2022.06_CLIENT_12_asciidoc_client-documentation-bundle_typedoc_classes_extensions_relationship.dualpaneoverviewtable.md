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
  * [DualPaneOverviewTable](extensions_relationship.dualpaneoverviewtable.html)

# Class DualPaneOverviewTable<SS>

### Type parameters

  * #### SS

### Hierarchy

  * Component<DualPaneOverviewTableProps, DualPaneOverviewTableState>
    * DualPaneOverviewTable

## Index

### Constructors

  * [constructor](extensions_relationship.dualpaneoverviewtable.html#constructor)

### Properties

  * [context](extensions_relationship.dualpaneoverviewtable.html#context)
  * [props](extensions_relationship.dualpaneoverviewtable.html#props)
  * [refs](extensions_relationship.dualpaneoverviewtable.html#refs)
  * [state](extensions_relationship.dualpaneoverviewtable.html#state)
  * [contextType](extensions_relationship.dualpaneoverviewtable.html#contexttype)

### Methods

  * [FilterButton](extensions_relationship.dualpaneoverviewtable.html#filterbutton)
  * [Footer](extensions_relationship.dualpaneoverviewtable.html#footer)
  * [Heading](extensions_relationship.dualpaneoverviewtable.html#heading)
  * [RowActionGroup](extensions_relationship.dualpaneoverviewtable.html#rowactiongroup)
  * [TableBody](extensions_relationship.dualpaneoverviewtable.html#tablebody)
  * [TableBodyCell](extensions_relationship.dualpaneoverviewtable.html#tablebodycell)
  * [UNSAFE_componentWillMount](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillmount)
  * [UNSAFE_componentWillReceiveProps](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillreceiveprops)
  * [UNSAFE_componentWillUpdate](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillupdate)
  * [componentDidCatch](extensions_relationship.dualpaneoverviewtable.html#componentdidcatch)
  * [componentDidMount](extensions_relationship.dualpaneoverviewtable.html#componentdidmount)
  * [componentDidUpdate](extensions_relationship.dualpaneoverviewtable.html#componentdidupdate)
  * [componentWillMount](extensions_relationship.dualpaneoverviewtable.html#componentwillmount)
  * [componentWillReceiveProps](extensions_relationship.dualpaneoverviewtable.html#componentwillreceiveprops)
  * [componentWillUnmount](extensions_relationship.dualpaneoverviewtable.html#componentwillunmount)
  * [componentWillUpdate](extensions_relationship.dualpaneoverviewtable.html#componentwillupdate)
  * [forceUpdate](extensions_relationship.dualpaneoverviewtable.html#forceupdate)
  * [getSnapshotBeforeUpdate](extensions_relationship.dualpaneoverviewtable.html#getsnapshotbeforeupdate)
  * [handleColumnClick](extensions_relationship.dualpaneoverviewtable.html#handlecolumnclick)
  * [render](extensions_relationship.dualpaneoverviewtable.html#render)
  * [setState](extensions_relationship.dualpaneoverviewtable.html#setstate)
  * [shouldComponentUpdate](extensions_relationship.dualpaneoverviewtable.html#shouldcomponentupdate)

## Constructors

### constructor

  * new DualPaneOverviewTable(props: DualPaneOverviewTableProps): [DualPaneOverviewTable](extensions_relationship.dualpaneoverviewtable.html)

  * Overrides [ErrorBoundary](core_frame.errorboundary.html).[constructor](core_frame.errorboundary.html#constructor)

    * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:408

#### Parameters

    * ##### props: DualPaneOverviewTableProps

#### Returns
[DualPaneOverviewTable](extensions_relationship.dualpaneoverviewtable.html)

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

props: Readonly<DualPaneOverviewTableProps> & Readonly<{ children?: ReactNode | undefined }>

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

state: Readonly<DualPaneOverviewTableState>

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

### FilterButton

  * FilterButton(props: PropsType & { children?: ReactNode | undefined }): null | Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:494

#### Parameters

    * ##### props: PropsType & { children?: ReactNode | undefined }

#### Returns null | Element

### Footer

  * Footer(): Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:464

#### Returns Element

### Heading

  * Heading(props: PropsType & { children?: ReactNode | undefined }): Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:446

#### Parameters

    * ##### props: PropsType & { children?: ReactNode | undefined }

#### Returns Element

### RowActionGroup

  * RowActionGroup(props: Props & { children?: ReactNode | undefined }): Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:479

#### Parameters

    * ##### props: Props & { children?: ReactNode | undefined }

#### Returns Element

### TableBody

  * TableBody(props: Props & { children?: ReactNode | undefined }): Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:498

#### Parameters

    * ##### props: Props & { children?: ReactNode | undefined }

#### Returns Element

### TableBodyCell

  * TableBodyCell(props: Props & { children?: ReactNode | undefined }): null | Element

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:484

#### Parameters

    * ##### props: Props & { children?: ReactNode | undefined }

#### Returns null | Element

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

  * UNSAFE_componentWillReceiveProps(nextProps: Readonly<DualPaneOverviewTableProps>, nextContext: any): void

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

    * ##### nextProps: Readonly<DualPaneOverviewTableProps>

    * ##### nextContext: any

#### Returns void

### Optional UNSAFE_componentWillUpdate

  * UNSAFE_componentWillUpdate(nextProps: Readonly<DualPaneOverviewTableProps>, nextState: Readonly<DualPaneOverviewTableState>, nextContext: any): void

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

    * ##### nextProps: Readonly<DualPaneOverviewTableProps>

    * ##### nextState: Readonly<DualPaneOverviewTableState>

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

  * componentDidUpdate(prevProps: Readonly<DualPaneOverviewTableProps>, prevState: Readonly<DualPaneOverviewTableState>, snapshot?: [SS]()): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[componentDidUpdate](core_frame.errorboundary.html#componentdidupdate)

    * Defined in node_modules/@types/react/index.d.ts:688

Called immediately after updating occurs. Not called for the initial render.

The snapshot is only present if getSnapshotBeforeUpdate is present and returns
non-null.

#### Parameters

    * ##### prevProps: Readonly<DualPaneOverviewTableProps>

    * ##### prevState: Readonly<DualPaneOverviewTableState>

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

  * componentWillReceiveProps(nextProps: Readonly<DualPaneOverviewTableProps>, nextContext: any): void

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

    * ##### nextProps: Readonly<DualPaneOverviewTableProps>

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

  * componentWillUpdate(nextProps: Readonly<DualPaneOverviewTableProps>, nextState: Readonly<DualPaneOverviewTableState>, nextContext: any): void

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

    * ##### nextProps: Readonly<DualPaneOverviewTableProps>

    * ##### nextState: Readonly<DualPaneOverviewTableState>

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

  * getSnapshotBeforeUpdate(prevProps: Readonly<DualPaneOverviewTableProps>, prevState: Readonly<DualPaneOverviewTableState>): SS | null

  * Inherited from [OverviewWrapper](core_view.overviewwrapper.html).[getSnapshotBeforeUpdate](core_view.overviewwrapper.html#getsnapshotbeforeupdate)

    * Defined in node_modules/@types/react/index.d.ts:682

Runs before React applies the result of `render` to the document, and returns
an object to be given to componentDidUpdate. Useful for saving things such as
scroll position before `render` causes changes to it.

Note: the presence of getSnapshotBeforeUpdate prevents any of the deprecated
lifecycle events from running.

#### Parameters

    * ##### prevProps: Readonly<DualPaneOverviewTableProps>

    * ##### prevState: Readonly<DualPaneOverviewTableState>

#### Returns SS | null

### handleColumnClick

  * handleColumnClick(columnIndex: number): void

  *     * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:435

#### Parameters

    * ##### columnIndex: number

#### Returns void

### render

  * render(): React.ReactNode

  * Overrides Component.render

    * Defined in src/extensions/relationship/internal/ui/components/DualPaneSelection.tsx:506

#### Returns React.ReactNode

### setState

  * setState<K>(state: ((prevState: Readonly<DualPaneOverviewTableState>, props: Readonly<DualPaneOverviewTableProps>) => null | S | {}) | (null | S | {}), callback?: undefined | (() => void)): void

  * Inherited from [ErrorBoundary](core_frame.errorboundary.html).[setState](core_frame.errorboundary.html#setstate)

    * Defined in node_modules/@types/react/index.d.ts:491

#### Type parameters

    * #### K: keyof DualPaneOverviewTableState

#### Parameters

    * ##### state: ((prevState: Readonly<DualPaneOverviewTableState>, props: Readonly<DualPaneOverviewTableProps>) => null | S | {}) | (null | S | {})

    * ##### Optional callback: undefined | (() => void)

#### Returns void

### Optional shouldComponentUpdate

  * shouldComponentUpdate(nextProps: Readonly<DualPaneOverviewTableProps>, nextState: Readonly<DualPaneOverviewTableState>, nextContext: any): boolean

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

    * ##### nextProps: Readonly<DualPaneOverviewTableProps>

    * ##### nextState: Readonly<DualPaneOverviewTableState>

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

  * [DualPaneOverviewTable](extensions_relationship.dualpaneoverviewtable.html)
    * [constructor](extensions_relationship.dualpaneoverviewtable.html#constructor)
    * [context](extensions_relationship.dualpaneoverviewtable.html#context)
    * [props](extensions_relationship.dualpaneoverviewtable.html#props)
    * [refs](extensions_relationship.dualpaneoverviewtable.html#refs)
    * [state](extensions_relationship.dualpaneoverviewtable.html#state)
    * [contextType](extensions_relationship.dualpaneoverviewtable.html#contexttype)
    * [FilterButton](extensions_relationship.dualpaneoverviewtable.html#filterbutton)
    * [Footer](extensions_relationship.dualpaneoverviewtable.html#footer)
    * [Heading](extensions_relationship.dualpaneoverviewtable.html#heading)
    * [RowActionGroup](extensions_relationship.dualpaneoverviewtable.html#rowactiongroup)
    * [TableBody](extensions_relationship.dualpaneoverviewtable.html#tablebody)
    * [TableBodyCell](extensions_relationship.dualpaneoverviewtable.html#tablebodycell)
    * [UNSAFE_componentWillMount](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillmount)
    * [UNSAFE_componentWillReceiveProps](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillreceiveprops)
    * [UNSAFE_componentWillUpdate](extensions_relationship.dualpaneoverviewtable.html#unsafe_componentwillupdate)
    * [componentDidCatch](extensions_relationship.dualpaneoverviewtable.html#componentdidcatch)
    * [componentDidMount](extensions_relationship.dualpaneoverviewtable.html#componentdidmount)
    * [componentDidUpdate](extensions_relationship.dualpaneoverviewtable.html#componentdidupdate)
    * [componentWillMount](extensions_relationship.dualpaneoverviewtable.html#componentwillmount)
    * [componentWillReceiveProps](extensions_relationship.dualpaneoverviewtable.html#componentwillreceiveprops)
    * [componentWillUnmount](extensions_relationship.dualpaneoverviewtable.html#componentwillunmount)
    * [componentWillUpdate](extensions_relationship.dualpaneoverviewtable.html#componentwillupdate)
    * [forceUpdate](extensions_relationship.dualpaneoverviewtable.html#forceupdate)
    * [getSnapshotBeforeUpdate](extensions_relationship.dualpaneoverviewtable.html#getsnapshotbeforeupdate)
    * [handleColumnClick](extensions_relationship.dualpaneoverviewtable.html#handlecolumnclick)
    * [render](extensions_relationship.dualpaneoverviewtable.html#render)
    * [setState](extensions_relationship.dualpaneoverviewtable.html#setstate)
    * [shouldComponentUpdate](extensions_relationship.dualpaneoverviewtable.html#shouldcomponentupdate)

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

