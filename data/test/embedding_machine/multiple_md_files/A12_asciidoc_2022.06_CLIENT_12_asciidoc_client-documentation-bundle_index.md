# Client Developer Documentation

CLIENT Product Team  

Client Developer Documentation12.5.0

  * 1\. Introduction
    * 1.1. Technologies
    * 1.2. Principles
  * 2\. Getting Started
    * 2.1. Prerequisites
      * 2.1.1. Useful Tools
        * A12 Modeling Tools
        * IDE with TypeScript support
        * React and Redux Developer Tools
    * 2.2. Template Project
      * 2.2.1. Download
      * 2.2.2. Installation
      * 2.2.3. Build Process
        * Watch Mode
        * Testing
      * 2.2.4. Files and Directories
  * 3\. Basic Concepts
    * 3.1. Application Frame
      * 3.1.1. Elements of the Application Frame
    * 3.2. Views
      * 3.2.1. Arranging UIs
        * Match Conditions
        * Directives
        * Regions
        * Cases
      * 3.2.2. Views are identifiable Content Parts
        * Master/Detail
        * Nested Details
          * View Assignment
          * Layout
          * Summary
        * Changing Context in the Sidebar Region
          * Thinking in View Directives
          * Summary
      * 3.2.3. Example: Cosmo Design Study
        * Clearing a Region
    * 3.3. Activity
      * 3.3.1. Activity Data Structure
        * Activity Descriptor
          * Pre-defined Key
        * Properties
        * Data Holder
          * Example
        * Operations on Activities
          * Creating an Activity
        * Data Loading
        * Linking Activities
          * The Initiating Activity
          * The Source Activity
      * 3.3.2. Work with Business Data
        * Activity Descriptor
        * Activity Data
          * Document Related Data
        * Activity Relations
        * Data Reducers
    * 3.4. From Activities to Views to Engines
      * 3.4.1. Creating the First Activity (Overview)
      * 3.4.2. Creating the Second Activity (Detail)
      * 3.4.3. Changing the Selected Row in the Overview
    * 3.5. Application Model
      * 3.5.1. Overview
        * Application
        * Module
        * Flow
        * Scene
        * Case
        * Scene Change
      * 3.5.2. Configuration of Regions
        * Region Layout
      * 3.5.3. Locales
      * 3.5.4. Modules
        * Bottom-up Development
        * Starting an initial activity through the menu
      * 3.5.5. Flows
        * Starting a Flow
        * Multiple Flows (outlook)
      * 3.5.6. Scenes
        * Scene Match
          * Required Prior Scene
          * Initial Scene for a Flow
        * Example
          * UI State 0: No Scene
          * UI State 1: In Offer List
          * UI State 2: In Edit Offer
      * 3.5.7. Scene Changes
        * The Replay Algorithm
        * Layout changes
      * 3.5.8. Cases
        * Cases versus traditional "tabs"
    * 3.6. Data Loading
      * 3.6.1. Data Handlers
        * Registration and order of execution
        * Data Loader and Data Editor
        * Data Provider
          * Empty Document Data Provider
          * Example
    * 3.7. Data Reducers
      * 3.7.1. Adding a Data Reducer
    * 3.8. Summary
  * 4\. Features
    * 4.1. Configuration
      * 4.1.1. Usage
      * 4.1.2. UI Settings
    * 4.2. Engines
      * 4.2.1. Form-Engine Component
      * 4.2.2. Overview-Engine Component
      * 4.2.3. Form-Engine
        * Integration
          * Appsetup
          * View
        * State Integration
          * Initializing of an Activity
          * Updating of an Activity
        * Actions
        * Customization
          * View
          * Middlewares or Sagas
          * DataFormats
          * Engine State Selector
    * 4.3. Platform Server Connectors
      * 4.3.1. Important to Know
      * 4.3.2. Note on Attachments
      * 4.3.3. Providing Custom Server Connector
    * 4.4. HTTP Connectors
      * 4.4.1. HTTP Model Loading
      * 4.4.2. Platform Model Loading
      * 4.4.3. Implementing a custom ModelLoader
      * 4.4.4. Custom Model Loading
    * 4.5. Layouts
      * 4.5.1. MasterDetail
      * 4.5.2. Dashboard
      * 4.5.3. ApplicationFrame
        * Header
        * Main Menu
          * Mobile Navigation
          * MainMenuContext
        * SidebarContext
        * Layout Settings
      * 4.5.4. Stack
      * 4.5.5. Null
      * 4.5.6. Custom Layouts
      * 4.5.7. Progress Indication
        * Conditionally hide Progress Indicator
      * 4.5.8. Error Boundaries
    * 4.6. CRUD
      * 4.6.1. Customizing not supported
    * 4.7. Localization
      * 4.7.1. Current Locale
      * 4.7.2. Available Locales
      * 4.7.3. Localizer
      * 4.7.4. Localization Keys
        * Static Resources
        * Application Model
          * Menu Entries
          * Cases
      * 4.7.5. Single Locale Setup
      * 4.7.6. Hidden Accessibility Texts
    * 4.8. Modularization
      * 4.8.1. Motivation
      * 4.8.2. ModuleRegistry
      * 4.8.3. Using the API
      * 4.8.4. Implementing custom extension points
      * 4.8.5. Modules and the Main Menu
    * 4.9. Dirty Handling
    * 4.10. Notifications
      * 4.10.1. Mobile
    * 4.11. Static Pages
    * 4.12. Deep Linking
      * 4.12.1. Default Codec
      * 4.12.2. Setup
        * URL Encoding
        * Activity Restoration
      * 4.12.3. Configuration
      * 4.12.4. Customization
      * 4.12.5. Limitations
      * 4.12.6. Welcome Page
        * Modularization
    * 4.13. Model Graph
    * 4.14. Heterogeneity
      * 4.14.1. Subtype Dependency
      * 4.14.2. Model Graph Loading
      * 4.14.3. Heterogeneous Overviews
      * 4.14.4. Creating new Documents
      * 4.14.5. Document Model-Dependent Forms
      * 4.14.6. Example Setup (Simple CRUD)
        * Modeling
        * Application Setup
      * 4.14.7. Example Setup (Detailed)
        * Variant selection mapper
    * 4.15. Relationships
      * 4.15.1. Relationship Engine
        * Relationship UI configuration
      * 4.15.2. Views
        * Drop Down Selection
        * Dual Pane Selection
        * Quadro Pane Selection
        * Table List
          * Custom Localization
      * 4.15.3. Link Form
      * 4.15.4. Form-Engine integration
      * 4.15.5. Model Overview
    * 4.16. Accessibility Support
      * 4.16.1. ARIA in built-in Layouts
        * ApplicationFrameLayout
        * DashboardLayout
        * MasterDetailLayout
        * StackRegionLayout
      * 4.16.2. ARIA in built-in Components
        * Engines
        * ErrorBoundary
      * 4.16.3. ARIA in custom Layouts and Views
        * Custom Layouts
        * Custom Views
      * 4.16.4. Focus handling between views
    * 4.17. SCDM - Simple Composed Data Model
      * 4.17.1. Preparation
      * 4.17.2. Application setup
        * Middlewares / Sagas
        * Reducers
        * Data Provider
    * 4.18. Client Chrome Extension
      * 4.18.1. Installation
      * 4.18.2. Usage
    * 4.19. Asynchronous flows with Redux Saga
      * 4.19.1. Implementation of sagas in Client
        * Connecting sagas directly to middleware
        * Connecting sagas to the dispatcher
        * Providing own dispatcher
      * 4.19.2. Error handling in sagas
      * 4.19.3. Built-in sagas which get triggered by an action
        * Models and Documents
        * CRUD Demo
        * Cancellation of Activities
      * 4.19.4. ActivitySagas
        * acquireActivityLock
      * 4.19.5. StoreSagas
        * waitForStateChange
    * 4.20. Responsive Application Layout Optimization
    * 4.21. Mobile Navigation
      * 4.21.1. General Overview
      * 4.21.2. Mobile Navigation Project setup
        * Application
        * Views
        * Title
        * Custom layouts
          * One view in mobile mode
          * Multiple views in mobile mode
  * 5\. Architecture
    * 5.1. Walkthrough
      * 5.1.1. Activity / Scene / View cascade
  * 6\. Tutorials
    * 6.1. Prerequisites
    * 6.2. Adding a Static Page
      * 6.2.1. Create a new static page
      * 6.2.2. Register a new module in the Application Model
      * 6.2.3. Summary
    * 6.3. Working with A12 Models
      * 6.3.1. Adding A12 Models to the Template Project
        * Download Example Models
          * Storing models in template project
        * Generate validation file and copy models to target directory
          * Add a `build.gradle` file
          * Integrate the model conversion into the build process
        * Summary
      * 6.3.2. Using JSON Loader for Models and Documents
        * Create document provider functions for example data
        * Register Model and Data Loader
        * Summary
      * 6.3.3. Using overview and form components
        * Create a new module in the Application Model
        * Register the views and middlewares in the template project
        * Summary
    * 6.4. Using the Client with the A12 Server
      * 6.4.1. Configuration of the A12 Server
        * Adapt the scripts in the `package.json`
        * Download the A12 server configuration
        * Summary
      * 6.4.2. Enable the application to load models and documents from the A12 Server
        * Restart the application in `platform_server` mode
    * 6.5. Using Relationships between Models
      * 6.5.1. Before you start
      * 6.5.2. Goal of this tutorial
      * 6.5.3. Set up the models
        * Base and Relationship models
        * Application Model
      * 6.5.4. Provide some sample products and brands
      * 6.5.5. Configure the Server
      * 6.5.6. About the relationship
      * 6.5.7. UI configuration for the relationship between product and brand
      * 6.5.8. Register the relationship extension in the appsetup
        * Setup the view for a relationship Form-Engine
        * Register relationship extension in application setup
        * Setting the Model Graph
    * 6.6. Adding a New Locale
      * 6.6.1. Configuring a New Locale
      * 6.6.2. Initial Locale
      * 6.6.3. Working with Custom Localization Resources
        * Creating a Custom LocalizationTreeMap
        * Provide the Custom Resources to the Localizer
      * 6.6.4. Menu and case labels
      * 6.6.5. Static pages
      * 6.6.6. Custom components
      * 6.6.7. Forms and Overviews
      * 6.6.8. Relationship extension
    * 6.7. Implementing a timer with Redux Saga
      * 6.7.1. Create a new folder
      * 6.7.2. Implement the timer actions
      * 6.7.3. Implement the timer reducer
      * 6.7.4. Create the timer view component
      * 6.7.5. Create a `runTimer()` saga
      * 6.7.6. Register the timer reducer and saga in the application setup
      * 6.7.7. Register the timer view in the `viewFactory.tsx`
      * 6.7.8. Create a timer module in the application model
      * 6.7.9. Summary
  * 7\. Recipes
    * 7.1. Writing Tests for the Client
      * 7.1.1. React Components
      * 7.1.2. ActionCreators / Reducers
        * Example
      * 7.1.3. DataEditor / DataLoader / ModelLoader
      * 7.1.4. Sagas
        * Example
  * 8\. Frequently Asked Questions
    * 8.1. General
      * 8.1.1. How to define the initial locale of the application?
      * 8.1.2. How to connect a different Backend?
      * 8.1.3. How to enable Redux DevTools in the Client?
    * 8.2. Engines
      * 8.2.1. How to render a UI engine?
      * 8.2.2. How to render two UI engines for distinct document models?
        * DO NOT add another `VIEW_ADD` directive for a different UI engine
      * 8.2.3. How to compute values / modify document with Form-Engine?
    * 8.3. Miscellaneous
      * 8.3.1. How to get access to the Client git repository?
  * 9\. Troubleshooting
    * 9.1. Redux DevTools out of sync for some Activity properties
    * 9.2. Views are remounting on every render
  * 10\. Migration
    * 10.1. Migration to JSON Application Models and the latest Application Model Version
      * 10.1.1. TS Code to JSON Migration
      * 10.1.2. Align SME Application Models
      * 10.1.3. Application Model Migration to Version 1.0.0
      * 10.1.4. Import Application Model from JSON in Your Project
    * 10.2. Migration to new Kernel API
      * 10.2.1. NPM Dependencies
      * 10.2.2. DocumentLoader and DataProvider
      * 10.2.3. Models in Store
    * 10.3. Form-Engine Migration
      * 10.3.1. Prerequisites
        * NPM Dependencies
        * New Kernel-API
      * 10.3.2. AppSetup
      * 10.3.3. ViewViews.FormEngine
        * additionalOptions
        * readonly
        * Events
          * onEvent
          * onRowEvent
          * onValueChanged
          * onValidationStateChanged
      * 10.3.4. CRUD
    * 10.4. Overview-Engine Migration
      * 10.4.1. Prerequisites
        * New Kernel-API
      * 10.4.2. ViewViews.OverviewEngine
      * 10.4.3. CRUD
  * 11\. API Documentation
  * 12\. Migration Instructions
    * 12.1. 2022.06
      * 12.1.1. Breaking Changes
        * Integration of dependencies
        * Appmodel migration
          * New localization API
          * Improved typing of ApplicationModel.Menu
          * Main Menu optional for Modules
          * Clarified use of View and Container
        * New features
          * Removal of ContentBoxRenderMap
          * Removal of stylus
          * Form Engine UI State moved
          * Amount of filtered entries displayed
        * Development
          * Redux DevTools Integration
          * RESOURCE_KEYS removed from breaking change management
      * 12.1.2. Deprecation
        * Form Engine UI State moved
    * 12.2. Application Model Migration Tool

## 1\. Introduction

__ |  You can download this documentation as pdf [here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/3794d7056a85e5470af9ae60861b2f91/client-documentation.pdf).  
---|---  
  
A number of A12 initiatives stream together into this new solution for client
side application development:

  * The Form-Engine and Overview-Engine are written as reusable React components.

  * A12 Client Application Frame (CAF) was a rough predecessor. It has a focus of showing a three-pane layout (search filter, Overview-Engines, and Form-Engine) in Angular 1 frame.

  * Plasma for Business Apps drove the concepts and design for the entire screen of business applications along with support for one central main interaction - master/detail. Today it manifests as layouts and widgets in the A12 Widgets project.

  * A12 Model & Document APIs for accessing the platform server via TypeScript interfaces.

With the Client we pursuit a model-driven solution for building the client-
side of business applications.

![frame](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/588ce2d01b92bb8749a5cd9e67c5046b/frame.png)

The Client uses the same model based approach like the Engines, i.e., an
**application model** along with an interpreter that describes the UI
structure and the user interaction behavior of the client application.
Therefore, the model introduces high-level concepts that are independent of
the underlying client technologies.

It can also be seen as an orchestrator for the Engines and Widgets. The A12
team **hides a lot of complexity within the engines** and the Services (like
validation/computation), so that the Client runtime can be focused and lean.

![building-
blocks](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/c08bf65850bfd76d791a347e870af622/building-
blocks.png)

Further, features for the Client are:

  * Support for desktop and mobile devices out of the box. Note that while Plasma is not mobile-first, it ensures usability and consistency across device classes.

  * Flexible UI frame according to guidelines by A12 UI/UX team. Client has the concept of frame regions (in which views live) that improve upon the rigid three-pane layout of former UX approaches.

  * Extensible by various mechanisms like factories and inversion of control. The documented public API is here key, and its introduction was from lessons-learned of former project work.

  * Modern and lean technology stack: just TypeScript, React, Redux, Redux-Saga as well as Engines, Widgets, and Services.

### 1.1. Technologies

Client is a front-end platform based on [React](https://reactjs.org/)
libraries, written in [TypeScript](https://www.typescriptlang.org/), and built
via [Node.js](https://nodejs.org/). More on Client can be found in the [mgm
wiki](https://wiki.mgm-tp.com/confluence/x/z9AKBw) (mgm internal only).

Please also consider reading the wiki page [Redux-based
Architectures](https://wiki.mgm-tp.com/confluence/x/XLLDBg) (mgm internal
only), since it introduces you to the evolution and key concepts of modern
React and Redux applications.

![stack-with-
react](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/4b9f21d0ae243c09de5572da914dccba/stack-
with-react.svg)

The Client architecture invests fully in the React ecosystem. We have chosen
the following technologies:

  * **TypeScript** : It's static typed (but weak typed) with features that allow for truly scalable (code-wise) application development. Although React and Redux are JavaScript, we use the available TypeScript typings, so it becomes even safer to use these libraries.

  * **React** : efficient rendering of the UI component tree ("virtual DOM") without caring about current DOM state, i.e., no data binding required. React is also at the core of the Engines and Widgets.

  * We have applied best practices like functional rendering, separation of container and presentational components, and extensions through wrapping with higher order components (HOCs).

  * **Redux** : easy-to-understand unidirectional data flow. It follows heavily the functional paradigm instead of object-orientated. Redux enables the [Immutable App Architecture](https://medium.com/react-weekly/embracing-immutable-architecture-dc04e3f08543), which is the core of the Client architecture.

  * **Sagas** : make complex asynchronous control flows look like synchronous code. Sagas are elegant for any kind of background work that you would put into threads in Java.

Please understand the Redux concepts like store, state, reducer, middleware,
action, action creator; and also how connecting React components works via
provider and the `connect` functions of the "react-redux" library.

![redux-unidir-ui-
arch](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/215244f9bd9c8d40bf7c661f23fbea72/redux-
unidir-ui-arch.jpg)

Figure 1. [Source](https://staltz.com/unidirectional-user-interface-
architectures.html)

Sagas are, like middleware and specially
[thunks](https://github.com/reduxjs/redux-thunk), a way to introduce impure
effects into the pure functional world of Redux, like asynchronous I/O.
However, unlike thunks, sagas express these asynchronous steps in conventional
sequential manner (by utilizing JavaScript generators combined with async and
await).

With Redux-Saga, the situation changes slightly:

![redux-
saga](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/f08dd045864292a01f1ee0bb67e916fb/redux-
saga.jpg)

Figure 2. [Source](https://staltz.com/)

Sagas are background generator functions that typically are triggered by
incoming actions and then start off complex steps.

Note that the `take` effect (and any variants), that waits for an action in a
saga, returns **only after the store changes happened** and all middlewares
and reducers are already executed for a specific action. Meaning that a saga
can only react but not change or discard actions (unlike middleware).

### 1.2. Principles

The following diagram shows the principal structuring of the Client into
modules and their responsibilities in the architecture.

![key-
concepts](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/33851c56ce9a5479f295dd86cd5e5c7b/key-
concepts.svg)

The Client modules fall in one of these categories:

  * State Management

  * Application Model

  * Store

  * Supporting Sagas

  * Data I/O

  * Data Hub with the Data Loaders/Editors

  * Data Provider Principles

  * Presentation

  * Abstract UI Structures

  * Views

  * Business Logic

## 2\. Getting Started

This chapter gives a quick guide to start developing you own application with
the Client.

### 2.1. Prerequisites

In order to use the Client library no special software dependencies are
necessary. The Client library is delivered as an npm package, that is
available in the [mgm Artifactory](https://artifacts.mgm-
tp.com/artifactory/webapp/#/home) (mgm internal only). Further information can
be found in the [mgm Wiki](https://wiki.mgm-
tp.com/confluence/display/TECHHELP) (mgm internal only).

#### 2.1.1. Useful Tools

##### A12 Modeling Tools

The A12 SME and A12 UI Designer are tools to create the data and UI models.
The A12 UI Designer is the easiest way to upload these models to the server.
It is of advantage when you are aware of how to use these tools. Be aware that
the A12 modeling tools version has to fit to the version of the backend (i.e.
Services and Engines).

Please check the [A12 Releases](https://wiki.mgm-
tp.com/confluence/display/A12/Releases) page (mgm internal only) to find out
about compatible versions of different A12 products.

##### IDE with TypeScript support

In general, you can use your favorite IDE of choice. However, we recommend to
use [Visual Studio Code](https://code.visualstudio.com/) for the following
reasons:

  * We only provide project settings for vscode.

  * It has very good and up-to-date TypeScript support.

  * It is open source.

If you use Visual Studio Code, we recommend some extensions for it which help
e.g. to find linting errors during development or to maintain the A12 code
style. You will get a notification about them in VS Code the first time you
open the template project.

We also recommend using the TypeScript version of the workspace instead of the
one bundled with VS Code.

##### React and Redux Developer Tools

As with the IDE, you can use any browser, but we use Chrome. Familiarize
yourself with the React and Redux extensions. They are essential to inspect
your application's UI and backend state.

### 2.2. Template Project

The Client comes with a minimal, empty project. You can use it to create a new
application. It is intentionally kept as small as possible, so that you can
include only the functionality that you need.

You can find examples of how to integrate additional functionality in the
source code of the Client Sample-Application.

__ |  The included webpack configuration serves as a starting point for building and developing with the Client template. It should not be used as a reference for a production ready build. It is necessary to adapt the build to the projects requirements. Furthermore, some security aspects are totally ignored in order to keep it simple and maintainable.  
---|---  
  
#### 2.2.1. Download

Template project can be downloaded
[here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/f81c422a9d514390e5147745bfd3ee39/a12-client-
template.zip) (mgm internal only).

Extract it in a new directory:

    
    
    mkdir <NEW-PROJECT-NAME>
    unzip a12-client-template.zip -d <NEW-PROJECT-NAME>

#### 2.2.2. Installation

Navigate into the project directory and build the application

    
    
    cd <NEW-PROJECT-NAME>
    
    npm install
    npm run initialize
    npm run compile

Run the application with

    
    
    npm start

The application should be accessible at <http://localhost:8080>.

You should see the application frame with the application header and one menu
entry `WELCOME`.

![Initial landing page of template
project](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/b444eba7cd6611bb62e9e22e67ebb867/template_start.png)

Figure 3. Application frame of the template project after the first log-in

#### 2.2.3. Build Process

To build the application your run

    
    
    npm install          # Only needed to run once
    npm run initialize   # Only needed to run once
    npm run compile

##### Watch Mode

In order to have changes in the code immediately compiled, start the `tsc`
watcher running in the background. This can be done in your IDE as a task or
by starting the watch mode in your terminal by running the following npm
script.

    
    
    npm run typescript:watch

##### Testing

We use [mocha](https://mochajs.org/) as a pre-configured testing framework in
the template project.

To start the tests you need to execute

    
    
    npm test

#### 2.2.4. Files and Directories

This document describes the structure of the project template that can be used
as a starting point for projects that are based on products.

Directory / File | Description  
---|---  
`.vscode/` |  This directory contains Visual Studio Code specific editor settings.  
`node_modules/` |  All packages that are defined in the `package.json` as dependencies are installed and dropped locally in this directory. The TypeScript files may use these packages via the `import` statement.  
`resources/` |  The directory contains the main page of the application **(index.html)** , where React components are rendered, and some static resources. When working with A12 models, we will create more directories in the `resources` directory, one for storing the A12 document and UI models, and another one for storing the server configuration.  
`src/config/dev.config.ts` |  Binds services to the IoC (Inversion of Control) container (implemented by Inversify). This file is named after the environment that it configures: in this case it is a development environment configuration - a configuration for the production environment would have a name `prod.config.ts`. There is no implicit naming convention, at least in the project template. This file is explicitly imported by `index.ts`. Projects need to provide their own mechanism if they need to set the environment in a more customizable way (for example at runtime, based on some environment variable, or similar).  
`src/main/config/resources.ts` |  Contains localized texts.  
`src/main/static/` |  This directory contains code for static pages.  
`src/main/appmodel.json` |  Defines the application model with one example use case for static pages.  
`src/main/appsetup.ts` |  Exports the **setup** -function that returns the objects used to initialize the Client application, like Redux store or data coming from the application model (views, menu). It delegates to the platform, whose **setup** -function requires two mandatory, project-specific arguments:

  * model (`ApplicationModel`): contains the model of the application, which is defined in the file `appmodel.json`.
  * data handlers (`DataHandler`): implementation of the DataHandlers - the component that is responsible for loading and saving data and models.

  
`src/main/viewFactory.tsx` |  Exports the function viewFactory returning the implementation of a React component by its name as defined in the application model.  
`src/main/index.tsx` |  This is the entry point to the application. It uses the Redux provider component to provide the Redux store to all Client components. It also renders the `RegionUI` component which acts as the main component of the Client application. One additional prop of the `RegionUI` component is the `viewProvider` which has been setup in the `viewFactory.tsx`.  
`target/` |  The target directory contains all transpiled JavaScript files and additional output files that result from the build process, e.g. linting and test reports.  
`src/test/` |  This directory contains examples of unit tests.  
`src/test/unit/example.test.ts` |  A template of a unit test suite.  
`.gitignore` |  Contains all files and directories that should be ignored by the git versioning system.  
`.mocharc.json` |  This file contains the options for the test execution with mocha.  
`.nycrc.json` |  This file configures code coverage settings for the template project. More information about the coverage can be found on the official [istanbul](https://istanbul.js.org/) homepage.  
`package.json` |  All npm packages contain a file, usually in the project root, called package.json - this file holds various metadata relevant to the project. This file is used to give information to npm that allows it to identify the project as well as handle the project's dependencies.  
`README.md` |  Markdown file providing general information about the project to be developed. This file should typically contain information about how to build and run the application.  
`tsconfig.json` |  TypeScript compiler settings for the whole template project.  
`.eslintrc.json` |  Options for the linting tool eslint.  
`webpack.config.js` |  The webpack config `webpack.config.js` is already pre-configured with two profiles: `dev` and `platform_server`. This tutorial won't cover the details of this configuration, but it enables us to use the A12 models and documents in a client-only mode and with the Services implementation.  
  
## 3\. Basic Concepts

This chapter gives an introduction to the basic concepts of the A12 Client.

### 3.1. Application Frame

#### 3.1.1. Elements of the Application Frame

The A12 UI/UX team has defined a specific structure for the Plasma design that
is called application frame. It consists of four distinguished elements:

  * **Application Header** : contains e.g. logo, selected locale, user, and role information

  * **Navigation** : shows the main menu

  * **Context (Sidebar)** : displays additional information, context-related actions, and allows for sub navigation

  * **Content** : shows for example the Engines in specific layouts, e.g., a master-detail layout.

![Elements of the Application
Frame](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/6e8e05567581230994ac5371b25925f4/application-
frame.png)

### 3.2. Views

#### 3.2.1. Arranging UIs

The Application Model is an A12 UI Model for defining the "macroscopic" UI
aspects of applications based on [Plasma for Business
Applications](../../../../../../content/2022.06/PLASMA/1/asciidoc/plasma-
concept-documentation/index.html). This includes

  * main menu

  * regions

  * views

Inner parts of the UI can also be created using A12, but this is done using
other A12 components, e.g. Engines based on Form and Overview Model.

Each Application Model consists of _Modules_. A Module is a high level
building block of the application and directly accessible via the main menu.
It consists mainly of:

  * (optional) menu entry

  * flows with scenes

Menu defines the main menu entry of the Module and which Activity is started
when it is selected.

The scenes define the actual functionality of the Module. Each scene consists
of

  * match conditions

  * enter and leave directives

  * cases

##### Match Conditions

Match conditions define when the scene applies. They always refer to the
Activity Descriptor. The application model supports the following matching
strategies:

  * **mustEqual:** a property must equal a (constant) value

  * **isSet:** a property must be set

##### Directives

If the scene applies, the respective scene is "entered" and the enter
directives are executed. If the scene no longer applies, the respective
"leave" directives are executed.

The available directives are

  * _VIEW_ADD_

  * _REGION_CLEAR_

The VIEW_ADD directive has the following parameters:

  * **Region:** Defines to which Region the view should be added. The default region is defined in the layout.

  * **Name:** Defines the name of the React/Redux ui component that is responsible for visualizing the view.

__ |  In addition, make sure that the ui component is provided by the _View Factory_ configured in the application setup.  
---|---  
  
  * **Constraints:** Contains configurable constraints for the current layout. There are the following pre-defined properties:

    * `type`: refers to the layout to be configured. Some properties can only be specified for certain types. Currently the only built-in type is "MasterDetail"

    * `preferredWidth`: only available for type "MasterDetail". Determines the preferred width of the most right view. If another view is visible on the left hand side, this other view will take up the remaining space.

    * `label`: only available for type "MasterDetail". Can be used to specify the multilingual label of the view added by the directive. The label is used for the view navigation, when the view is currently hidden.

  * **Configuration:** Contains configurable constraints for the current view. There are the following pre-defined properties:

    * `bindings`: an array of bindings which are used for relationship ui configurations

  * **models:** an optional array of model descriptor objects. Each of them describes an A12 model to be loaded. Whenever this array is defined, the runtime automatically triggers model and data loading for this scene

  * **loadData:** an optional boolean flag. When set to true, the runtime automatically triggers data loading for this scene. This flag is only required, if you want to load data without having any A12 models.

__ |  Setting `loadData` to false will not prevent data loading, if there are models defined for the current view (see Data Loading). However you can prevent data loading by

  * not defining models and setting loadData to false/undefined
  * manually setting the loadingState of the activity to "without"

  
---|---  
  
The REGION_CLEAR directive has the following parameters:

  * **Region:** Defines which Region should be cleared. The default region is CONTENT.

  * **Layout:** Sets the layout for the Region. The default layout is Master-Detail.

##### Regions

Regions are visual locations inside the page. Currently, there are three
regions available: _CONTENT_ , _SIDEBAR_ and _MODAL_.

  * Views placed in _CONTENT_ will appear in the content area of the application frame widget.

  * Views placed in _SIDEBAR_ will appear in the sidebar of the application frame widget.

  * Views placed in _MODAL_ will appear in a modal dialog.

##### Cases

_Cases_ are an advanced feature to switch between different UIs without
changing Activities.

#### 3.2.2. Views are identifiable Content Parts

The A12 UI UX team has analyzed several layouts and UI flows from existing
projects. Below are shown the most common ones.

##### Master/Detail

The most simple is the master/detail layout. Here's an illustration:

![concept1-master-
detail](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/680d148178c1541c285d159df20c5743/concept1-master-
detail.png)

The master is here denoted as "View A" and is typically a data-browser, i.e.,
a list of business objects in rows. A12 calls this an "**overview** ". The
controls for filtering, sorting and search criteria are here part of View A
for simplicity, but search criteria can also be a view on its own. Also note
the sidebar with optional information about the overview. By selecting a row
you open and edit the details of the corresponding business object, here
represented as "View A.B". For example, this is a form with all attributes as
fields and input controls.

This example uses two content parts, which we will denote "**views** ": the
overview in a first view, the detail view in a second view. Now let's see some
more challenging examples.

##### Nested Details

The role of being a master and a detail is not fixed, meaning that a detail
can become master and open a new, nested detail. In the following example:

  1. The overview in "View A" is a master, shown fully maximized.

  2. Selecting a row in the overview brings up the details of the respective business object in "View A.B".

     * Using tabs in the detail view, the information of the business object can be broken down into multiple forms, here "View A.B" (the default view of the business object) and "View A.C". For example let's say that the business object is an insurance policy and "View A.B" is the general data and "View A.C" is the list of terms&conditions, which is shown again as an overview.

  3. Selecting a row in "View A.C" which is a list of terms&conditions as an overview, brings up the details of the corresponding term&condition item in "View A.C.D" as a form. Please note that the term&condition item is seen here as nested (or contained) business object of the policy. Thinking this way, we can apply our concepts in a recursive manner.

![concept2-tabs](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/d4ec5da010468fdd10789b9443aa505d/concept2-tabs.png)

###### View Assignment

Let's break this down into an assignment of views:

  * Overview "View A" is assigned the view #1.

  * "View A.B" and "View A.C" are different "details" of the selected business object, here a policy with the details "general data" (B) and "terms&conditions" (C). Both render their content into a view. Note that switching tabs to change between "View A.B" and "View A.C" does change the view assignment and layout.

  * "View A.C.D" is the detail of the selected term&condition item and is assigned a new view.

###### Layout

Now let's specify the layout with a focus on visibility: For a desktop, the
content area can only show up to two views. That means for our example:

  * view #1 appears maximized if alone.

  * If view #2 appears, view #1 for the overview moves to the left and shrinks.

  * If view #3 appears, view #2 moves to the left and view #1 is minimized and effectively disappears.

![md-layout-for-
views](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/8859fc014aeb51a81b94f475a1d1e82d/md-
layout-for-views.png)

The layout rules can be dependent on device class and available screen space.
For example, a smart phone might only show the latest view and offer
navigation controls, or render views from top to bottom.

![layouts-
variations](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/ad171d5953fc6c069a22c99cfe924afa/layouts-
motivation.png)

###### Summary

In summary, these points are important:

  * Activities open up one (or even multiple) views

  * A view can use tabs internally in order to show different aspects about the business object respective the activity. Another option is to use views and switch between them, as discussed in the subsection below.

  * Layout rules can organize views on screen, like maximizing, minimizing, proportions, max shown views, etc.

##### Changing Context in the Sidebar Region

Usually, each activity is tied to something like a result list (overview) or a
business object. Each view of an activity can have its own context information
in the sidebar. For an insurance policy this e.g. is the title, insured sum
and other key data, but also an action panel with buttons for printing,
progressing the workflow state, etc., is useful.

Until now we have assigned views to the content region only. But the sidebar
region can also contain views. In general, regions contain views, and the
application frame has two standard regions: the content and sidebar areas.

![concept3-cosmo](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/8294aeae2381249b169fce994d7c6605/concept3-cosmo.png)

If we break this down, we can assign views for the example above to the
**sidebar** as follows:

  * "View A" has no sidebar content, thus the sidebar is hidden.

  * For "View A.B" has specific sidebar content, for example "policy info" in "Info" which is assigned view #S1 and an action panel "B" which is assigned view #S2a.

  * For "View A.C" (which is another view of the same activity as "View A.B"), the sidebar continues to show "Info" in view #S1, removes any other view in the sidebar and adds a new view #S2b for the action panel "C" for terms & conditions.

  * For "View A.D" (again another view of the same activity as "View A.B" and "View A.C"), the sidebar again continues to show view #S1, but again removes any other view in the sidebar and adds a new view #S2c for the action panel "E" for coverage.

###### Thinking in View Directives

You might wonder why we focus on the sequence of delta changes when navigating
between the views and not just specify how each view should look. The reason
is that activities and view navigation actually express these delta changes by
using **directives** : "VIEW_ADD" (add view named X to region Y) and
"REGION_CLEAR" (clear region Y, i.e., remove all previously assigned views).
We will learn much more about this in the section about the application model.

###### Summary

In summary, these points are important:

  * The application frame has two regions that contain views: content area and sidebar. Others are possible, but must be added explicitly by the projects.

  * Views can be assigned and removed to achieve view-dependent dynamic content in the regions.

#### 3.2.3. Example: Cosmo Design Study

We now want to apply the ideas to a concrete example. Below is a design study
of the Cosmo UI relaunch, a work in progress. The part of the application we
are focussing on is the policy module. Policies can be listed in an overview
and various details about a policy can be inspected and edited using forms.
The design and layout is also used in production for other applications in the
Cosmo ecosystem: [AGCS DigiPos](https://wiki.mgm-tp.com/confluence/x/ltSABQ)
(mgm internal only) and [MiMaS Online](https://wiki.mgm-
tp.com/confluence/x/dK7dBg) (mgm internal only).

As can be shown below, the application frame shows a menu in the header.
Clicking on the "Policy" menu entry opens the overview. As we have learned,
technically this action does the following:

  * Starts a new overview activity.

  * Allocates a view in the content region.

  * Renders an Overview-Engine with a result list of selectable policy business objects.

![step1](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/2f5ea68eecc019d674a683cb5e2d0327/step1.png)

Selecting a specific row opens up the details about the corresponding policy.
From the technically perspective, this again starts a new activity for editing
the business objects and changes the regions like this:

  * Three views are assigned to the sidebar: an information panel, an action panel, and a view selection menu.

  * One view in the content area with a Form-Engine.

##### Clearing a Region

Please also note that the Form-Engine view is shown maximized even though an
overview view exists. Here's what happened: the view assignment for the
activity specified in the application model (which we will study later on)
that all regions should be _cleared_. Technically this means that even if a
previous activity has assigned views to a certain region, these views are
ignored by the layout manager if the region is cleared on behalf of the
current/active activity.

![step2](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/c954650f39c0214944c10693b67c4849/step2.png)

The screenshot below illustrates the next user interaction: the user switches
from the default view "General Data" of the activity to "Terms&Conditions"
which results in a change in layout:

  * The view with the "General Data" form is _removed_ and replaced by a new view for "Terms&Conditions" which is an overview.

  * Note that the sidebar stays the same.

The "Terms&Conditions" overview shows a list of clause groups. The overview
can be seen as a "master" and a click in a row brings up the details for the
selected Terms&Conditions item (see the blue arrow on the right side of the
illustration below). This starts a new, nested activity.

![step3](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/66b81b9edc87ded62ac5e960f79cc16f/step3.png)

The next screenshot shows the result of this activity:

  * The view for the "Terms&Conditions" overview is _kept_.

  * A new view in the content area region is allocated and shows an overview of "Clause Groups" for the selected Terms&Conditions item.

  * The sidebar stays the same.

![step4](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/623414105eab2a7c2cc182e64cb591fa/step4.png)

### 3.3. Activity

In the previous section, we introduced the concept of "activities" in a
somewhat vague way. Activities are a very important client-side Concept and
are actually quite well specified.

An activity can be seen as a bracket around user interactions, another term
for this bracket is "use case" (taken from requirement engineering). Typical
use cases are:

  * Overview: showing a list of business objects as a result of a search. Typical user interactions are: scrolling/paging, sorting, filtering, refining search criteria.

  * Editing a business object like using a form.

The Client has special support for these typical use cases, but any user
interactions can be managed as an activity. The sample application shows a
variety of activities including showing static FAQ and help pages.

In order to drive the use case, an activity holds all the relevant data and
state, and provides the UI component (indirectly though) for interacting with
the data.

#### 3.3.1. Activity Data Structure

  * Activity Descriptor

  * Properties

  * Operations on Activities

  * Data Loading

  * Linking Activities

Technically, an activity is a data structure in the Redux store that holds all
information of what the runtime and the application UI component need to know
about this use case instance.

    
    
    export interface Activity {
      readonly id: string;
      readonly descriptor: ActivityDescriptor;
      readonly initiatingActivityId?: string;
      // ...
    }
    
    export interface ActivityDescriptor {
      readonly instance?: string; // e.g. „P2"
      readonly [key: string]: string | undefined;
    }

##### Activity Descriptor

The activity descriptor is a key/value-map that specifies what the activity is
doing, e.g., the type of use case and details like the ID of the business
object.

The idea is to separate the intention, i.e., _" What should be done"_ from the
interpretation and implementation of _" How should it be done"_. The _" what"_
is the activity descriptor and it is the responsibility of the activity
creator to specify it. The _" how"_ is specified by "use case matches" in the
application model.

###### Pre-defined Key

There is one key with a pre-defined meaning: The instance key specifies the ID
of the business object, or in A12 context, the A12 data document ID. For
creating a new document the constant `NEW_INSTANCE_IDENTIFIER` (``"__NEW__"``)
from `core/application` should be used.

It is pre-defined in the sense that the provides I/O (loading/saving) and UI
components that interpret this key in the following way: if a form model has
been specified in the matching scene and the instance is set in the
descriptor, e.g., `{ "instance": "P222" }`, this is interpreted as the use
case "Editing data in a form": load the document for the specified business
object and bring up a form. This uses the document model which is referenced
in the specified form model.

##### Properties

Let's break down the most important properties.

  * `id`: each activity needs a unique identifier. The identifier also allows "weak" references to the activity, i.e., without using object references, which are problematic w.r.t. the "immutable state" principle of Redux.

  * `initiatingActivityId` and `sourceActivityId`: see details below.

  * `case`: this relates to the UI and scenes. See Cases for details.

  * `dataHolders`: each activity has a list of data holder objects. Each of them is responsible for one data source and has its own data descriptor see details below.

##### Data Holder

A data holder is responsible for the data of one data source within an
activity. It consists of a `descriptor` to specify what kind of data is being
stored as well as other properties to keep track of the data. The activity
descriptor is then only relevant for determining a matching scene from the
application model.

When an activity is created, it is initialized with one default data holder,
which gets the activity's descriptor as its data holder descriptor. More data
holders can be added to the activity later.

The `error` property of the data holder is intended for tracking `"loading"`
or `"saving"` errors. For tracking other errors it is recommended to store
them inside the `slices` property of the data holder. This can be easily
achieved by creating a custom action and a custom data reducers.

All properties of the data holder are described in more details in the API
reference.

###### Example

Here is an example of an activity that has a list with three data holders.
There is one data holder storing the document data of the activity, and two
other data holders storing link and candidate relationship data.

    
    
    const activity = {
        id: "223",
        descriptor: {
            model: "Product",
            instance: "DomainProduct/15"
        },
        dataHolders: [
            {
                descriptor: { model: "Product", instance: "DomainProduct/15"},
                data: {},
                dirty: "false",
                loadingState: "missing",
                savingState: "not_saved"
            },
            {
                descriptor: { type: "candidate", instance: "1" },
                data: { /*...*/ },
                dirty: "false",
                loadingState: "loaded",
                savingState: "not_saved"
            },
            {
                descriptor: { type: "link", instance: "1" },
                data: { /*...*/ },
                dirty: "false",
                loadingState: "loaded",
                savingState: "not_saved"
            }
        ]
    };

##### Operations on Activities

###### Creating an Activity

There are some pre-defined Redux action factories for working with activities.

Use the `create` function to create the Redux action `PUSH` that creates (or
"pushes") a new activity:

    
    
    function create({ activityId, activityDescriptor, initiatingActivityId, data, loadingState }: CreatePayload): Action<PushPayload> { /*...*/ };

If you want to create a new activity with data already in place, the
recommended way would be to hand in this data via the optional data property
of the params object.

If you still want to update the data of the activity directly after the
creation, e.g. dispatching the `ActivityActions.setData` action directly
afterwards, you need to wait with the dispatch, until the data and models
resulting from dispatching `create` are present in the store. Otherwise, the
data you want to set with setData would be overwritten! This is due to the
asynchronous model and data loading, that happens after dispatching `create`.

##### Data Loading

Most activity types require data and also models, e.g., an overview has the
list of search results and the overview model; the Form-Engine requires the
document data for the business object and also the data and UI models. This
information is kept in the `data` property, which has an internal structure
depending on the activity type.

When an activity is created, like in the examples above, all that is required
is the activity descriptor. Passing data is optional. Typically loading data
and models is and should be delegated to the runtime, specifically to the data
handlers.[1]

The property `loadingState` tracks the progress and gives information about
the outcome:

  * `"without"`: the activity does not require any data, and the `data` property is `undefined`.

  * `"missing"`: the activity requires data and possibly models. The runtime has to load them. Until they are loaded, the `data` property is `undefined`.

  * `"loading"`: the runtime is currently loading data and models.

  * `"loaded"`: the loading of data and models was successful.

  * `"error"`: there was at least one error during the loading of data and models. This information is optional.

An additional property `savingState` is a complementary tracking state for
saving data.

##### Linking Activities

###### The Initiating Activity

This is where nesting of activities comes into play. As we saw in the previous
examples, activities can be easily created, like a selection in an overview
master creates a form detail activity. Creating an activity is always relative
to a **parent activity** (called the "initiating activity") with a reference
by ID as `initiatingActivityId`. Note that the very first activity has no
parent, so the ID is not set (`undefined`).

Linking activities this way creates a tree which is utilized in the Client:

  * Canceling an activity will cancel all linked sub-activities.

  * Committing an activity will commit all linked sub-activities.

![activity-
dependencies](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/0ed786466bcf6512ea12caa90e4f3d26/activity-
dependencies.svg)

###### The Source Activity

There is a second kind of link between activities that is concerned with where
the data comes from. Data can come from an existing activity or from somewhere
else (subject to the selected data loader), typically a server side data
service.[2]

An existing activity is either the direct parent of the activity or any parent
above this parent. The id is kept in the `datasourceActivityId` property. If
data comes from somewhere else, this property is not set (`undefined`).

Consider the example that is illustrated above.

#### 3.3.2. Work with Business Data

Every task that the user is working on is represented as an _activity_. An
activity resembles a (possibly long-running) interaction of the user with the
system, e.g. filling out a (possibly large) form, browsing data, reading a
message, etc.

The main properties of an activity are

  * descriptor

  * data and loading state

  * initiating and source activity

##### Activity Descriptor

The _activity descriptor_ is an outline of the activity. It declares what the
activity is about. Most activities will deal with business data. Because of
this, the notion of a business object is built into the descriptor. Therefore,
it is possible to define an arbitrary number of _string_ properties to
describe the activity. These can augment the business data or be used in
activities that do not deal with business objects.

__ |  Currently, only the property "instance" is reserved for A12 own use.  
---|---  
  
##### Activity Data

Of course, activities can also contain the actual data of the business object.
Data that comes from one data source is typically kept in one data holder. The
data can be of any structure, however in most cases it should be an _A12
Document_. The loading state is also held as a separate property within this
data holder.

In addition to the actual data, there are several properties providing
additional information about the activity's data:

  * **loading and saving state:** tells whether the activity data holder contains data at all and if yes, if the data is missing, loaded or the loading failed. These are usually controlled and used by data handlers and related functionality.

  * **lock:** can be used by business logic to prevent any changes to the data holder - a locked data holder is also considered as "dirty" \- see the dirty handling feature (see below)

  * **dirty information:** can be used by business logic to prevent an accidental cancellation of the activity.

__ |  The feature only works if the "cancel requested" event action is used instead of the "cancel" command action.   
---|---  
  
  * **error state:** Holds information about a `"loading"` or `"saving"` error that is currently present. The error has always an `errorCode` that defines the type of error and - depending on the type - additional, type specific information.

###### Document Related Data

For A12 document related data the Client provides some helper functions to
identify whether an activity contains data that contains a single document
`Activity.Data.SingleDocumentData.isInstance` or a list of document
`Activity.Data.DocumentListData.isInstance`.
`Activity.Data.SingleDocumentData.isInstance` guarantees that the data
contains a document with at least an `id` and a `modelId`.
`Activity.Data.DocumentListData.isInstance` guarantees that the data contains
a list of documents with at least an `id` and a `modelId`.

__ |  If you create A12 documents by yourself, you need to make sure that they fulfill the interface of `Activity.Data.Document`. Next to your data your document needs to contain an `id` and a `modelId`. For new documents you can use the constant `NEW_INSTANCE_IDENTIFIER` as the document id.  
---|---  
  
##### Activity Relations

If an activity has been started by another activity, then that activity is
available as _initiating_ activity. If an activity obtained its data from
another activity, then that activity is available as (data) _source_ activity.

##### Data Reducers

The business data held in an activity can be changed by the user working on a
task like filling out a form or by a system executing a technical task. To
achieve this, the Client provides the concept of Data Reducers which give
fine-grained control over changes to the business data within a data holder.

As an example, the UI state of the Form Engine is handled by a Data Reducer.

### 3.4. From Activities to Views to Engines

Let's bring together the concepts we saw so far -- views, activities, and also
Engines -- and show how they play together to present the UI. We stick to our
insurance policy example (here labelled "offer").

__ |  For simplicity reasons we will focus only on the default application frame layout. The behavior for custom layouts depends mainly on the the region and layout implementation.  
---|---  
  
When the application starts and no menu item is selected, the application
frame is empty or shows the default content for the sidebar and content.

![step1](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/129a97fe0b65159c00286e5cf3f93c96/step1.svg)

#### 3.4.1. Creating the First Activity (Overview)

In the next step the user clicks on the menu item "Offer" and activity 1 is
created with the activity descriptor "{ "model": "offer"}":

We will study the application model only in the next section, but note that
this action is declared in the model.

As a result of creating this activity, scene directives are executed according
to the application model. In this case: first clear the sidebar and the
content regions, then add a view for showing the Overview-Engine.

![step2](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/1b8187284f0ea3f7c82dd8b679735f4a/step2.svg)

Note that until now the activity is only containing the activity descriptor
but no data or models, which is also indicated by the loading state
`"loading"`. As a consequence, the view cannot render much, maybe an animation
to indicate this pending state, but not the Overview-Engine. Loading of data
and models is done through data handlers and orchestrated by the Client
runtime.

The next step begins when the data and models are loaded and the loading state
is changed to `"loaded"`. Now the view has all required parameters for the
Overview-Engine and can instantiate and render it inside the view.

![step3](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/ca96c24d2b55383d7f7facadf9932cc7/step3.svg)

#### 3.4.2. Creating the Second Activity (Detail)

The user now interacts with the overview and clicks on a row in order to edit
the details of the offer. Here's what happens. The view issues a Redux action
to create a second activity. This activity has the first activity as the
initiating activity; but not as source activity, since it will get the offer
document data from the server.

As a result of creating this new activity, directives are executed according
to the application model. In this case:

  * clear the sidebar region (but not the content region),

  * then add a view in the sidebar for the info panel

  * and another view in the content region for showing the Form-Engine

Note again that until now the activity is only containing the activity
descriptor but no data or models. As with the first activity, data and models
are loaded and the loading state is updated accordingly.

As soon as the views have all required parameters, the view contents are
updated with the actual information (sidebar) and Form-Engine (content
region).

![step4](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/abe1f80a4878ce77c031dc210a30ff49/step4.svg)

#### 3.4.3. Changing the Selected Row in the Overview

A typical user interaction in this master/detail situation is the selection of
another row in the master, i.e., overview. One would expect the following to
happen in the UI: the form on the right is cancelled (possibly by asking the
user for permission if the form has changed data) and the form content is
replaced with the document data of the newly selected row. This breaks down
into an action sequence and view changes like this:

  1. We start with just the activity 1 and showing the overview and the user selects a row in the overview.

  2. Just like before the overview view dispatches an action (`create`) in order to create a dependent activity 2.

  3. Now the user selects another row in the overview.

  4. It needs to be checked if there exists a child activity of the overview activity.

     * If no child activity exists, a (`create`) action can be dispatched in order to create a new dependent activity.

     * If a child activity exists, this child activity needs to be cancelled by dispatching the (`cancelRequested`) action. It is possible to provide an activity to the (`cancelRequested`) action that replaces the canceled activity in order to avoid dispatching an additional (`create`) action after the cancellation.

### 3.5. Application Model

So far we have focused on the runtime and understand how starting activities
creates views in regions that show the UI elements. One piece of the puzzle is
missing so far: how exactly do you specify which and how many views are
associated with an activity? This section will explain that this association
is in the application model, specifically in the "scene" descriptions.

#### 3.5.1. Overview

The Application Model is all about the structure of the UI in terms of regions
and layout, and behavior - when and how UI components should be placed in the
UI. The building blocks of the model are summarized in this diagram:

![model-
hierarchy](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/1609b158a503dbddbad963e1ad09b3b2/model-
hierarchy.svg)

Let's go quickly through these elements:

##### Application

  * Header specifies generic model properties like id, supported locales, annotations etc.

  * Specifies the modules

  * Regions configuration specifies the application frame and layouts.

##### Module

  * Functional domain of an application

  * Represented as "Main menu entry", that triggers the creation of the flow's initial activity.

##### Flow

  * UI interaction bracket, i.e. it divides the user interaction into discrete parts. Think of it as a _micro-workflow_ on the client side.

  * In this sense, it is also a closure for a set of connected UI configurations; specifically it breaks down into multiple steps in the flow that we denote _scenes_.

##### Scene

UIs in the Client are modeled using "Scenes", where a scene is "entered" when
some configurable conditions are met. When a scene is entered, its specified
scene change (which in turn contains scene directives) is executed. This, in
turn, reconfigures the UI.

  * Single UI configuration

  * triggered by a change in the activities and activated by an activity descriptor match

  * linked to a (required) prior scene (except initial scenes of a flow)

  * AD match always includes the prior scene implicitly

##### Case

  * Sub-case of an UI arrangement

  * triggered by an explicit case change (manually) / activated by a case menu entry

  * hence, all cases within a scene operate on the same activity!

##### Scene Change

  * Contains directives that should be executed when the scene/case changes

  * onEnter: When the scene/case is entered

  * onExit: When the scene/case is left

Here's an example and break-down the UI and its changes in terms of flows,
scenes and scene changes:

![flow-
illustration](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/e27966f13b4ba10debdd29237250b1d5/flow-
illustration.svg)

#### 3.5.2. Configuration of Regions

We have seen how applications can place contents of ui components in _regions_
, like the content, sidebar and modal region. However, the application model
allows arbitrarily named and even nested regions.

  * In the application model, regions can have any name and there are no "predefined" regions . The semantics of the regions are defined by the layout that is assigned to the region.

  * The tree of regions is defined (statically) in the application model.

  * There is one top-level region - the application (or "app") region. If it has the `ApplicationFrame` layout then it resembles the classical application frame with the content and sidebar regions.

Here's the excerpt from the model that sets up the three regions of the
previous examples:

    
    
    {
      "region": {
        "name": "APP",
        "layout": { "name": "ApplicationFrame" },
        "subRegions": [
          { "name": "CONTENT", "layout": { "name": "MasterDetail" } },
          { "name": "SIDEBAR", "layout": { "name": "Null" } },
          { "name": "MODAL", "layout": { "name": "Stack" } }
        ]
      },
      "defaultRegion": ["CONTENT"]
    }

The resulting region configuration then looks like this:

![region-
configuration](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/e340bdfacc9ea25f0d65b91abdc3afe6/region-
configuration.svg)

##### Region Layout

For each region, the layout must be specified by name with optional settings
data. The provided layouts of the Client are shown here:

![layouts](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/2d9191a80ecdf006c4ecb741489a2e3f/layouts.svg)

Please note that custom layouts can be easily installed and this setup is
discussed further in the customization page.

Layouts for regions can be changed at runtime during a scene change,
specifically by the `CLEAR_REGION` directive. See the page Scene Changes for
further details; this page also shows how to provide extra layout settings
data in the dashboard example.

#### 3.5.3. Locales

The property locales is optional and currently unused. However, it is
recommended to provide here all locales that are used in the application
model.

#### 3.5.4. Modules

The application model is a composition of modules. The modules describe all
the model aspects for a certain domain in your application. For example, an
insurance application can be broken down into modules like partner,
submission, offer and policy.

The idea here is that you can reuse modules and supporting code in different
applications and put together modules to build up an application. This notion
is expressed in the following diagram:

![modules](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/40062a57f93f7d7cfb5ab9414435635d/modules.png)

Modules contain two pieces of information:

  * **Module header including a menu entry** : each module can provide a menu entry that is shown automatically in the menu bar in the header.

  * **Flows** : a flow contains usually many scenes that handle activities in the respective domain and are connection between activities and the view assignments in regions. For example, the offer module might consist of three scenes: the overview (list), editing an offer and adding/editing clauses.

##### Bottom-up Development

The diagram above also shows the supposed bottom-up development process. You
can break up the full application into smaller parts. You begin with single
scene, like showing a search filter with results (an overview in A12 jargon)
or a detail form. Scenes can be assigned to teams and developed and tested in
isolation as a single-scene "application". You now can wire single scenes
together for a user interaction scenario and bundle related scenarios
(typically of the same business entity like offer) into a flow of a module
e.g. "offer". A module is a mini-application that again can be tested in
isolation, and the modules can then finally combined into the full
application.

##### Starting an initial activity through the menu

The application menu is automatically built from the application model. Each
module can specify a menu entry like this:

    
    
    {
      "menu": {
        "name": "offer",
        "label": { "en": "Offer" },
        "activityDescriptor": { "model": "Offer_v3" }
      }
    }

When you click on a menu entry, an activity is started automatically with the
activity descriptor content that is specified in the `activityDescriptor`
property. It is equivalent to `createPushActivityAction({ descriptor: {model:
"Offer_v3"}, …​})`.

The label is localizable by providing different texts in a map. The key is
hereby the string representation of the Locale object. Furthermore, it is
possible to extend and override these texts with a localizer by using the
corresponding localization key. Using a customized localizer does not require
that a label is provided in the application model.

#### 3.5.5. Flows

A flow is a way to group together coupled UI interaction steps, we denote
_scenes_. Examples of multi-step user interactions that could be modeled as
flows are

  * wizards that span multiple steps and involve more than one UI form on the client side[3], e.g. mixing forms, lists/overviews etc.

  * drilling down into a hierarchy of information. Take the example from the Cosmo Design Study: it starts with an overview of policy instances, then entering a specific policy document, and from here listing its general clauses, which are related or embedded information, and looking at various general clause instances of this list.

##### Starting a Flow

Flows are not directly instantiated and have no direct tie to activities.
However, scenes are associated with activities through scene matches. And so
we have a notion of _starting a flow_ by the fact that an activity will match
a first scene in flow. More on this topic in the following section.

##### Multiple Flows (outlook)

Flows are currently limited by the fact, that you can only run one flow at
time: if you click an entry in the main menu, you start off a new flow, and a
possible ongoing flow is stopped by cancelling the activities. However, this
limitation will be lifted in future releases and then multiple flows can be
"started" in parallel. This play nicely together with the fact that activities
form not only a sequence (w.r.t. to the "initiated by" link), but trees and
even forrests. A forrest here means, that Client supports running multiple
top-level activities that each can have tree-like sub activities.

Here's an illustration of the idea of multiple flows spawned by multiple top-
level activities:

![forrest](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/edad5088757bfb3d1d2c8cbd6f6912d9/multiple-
flows.svg)

#### 3.5.6. Scenes

Now we enter the heart of the application model. Scenes are the connection
between activities and the view changes in the UI that are driven by them.

The procedure is roughly as follows:

  1. Selection criterion as **Match Condition** that has to match the activity descriptor of the given activity

  2. Layout changes as **Scene Changes**

The following screenshot shows the UI views that are shown for an activity:

![module-
case](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/209b333cc683026fa0f89d2af74af698/module-
scene.png)

##### Scene Match

Now we address the question of how to choose a scene in the model for the
given activity. All scenes of the model are candidates and are checked via a
scene match as follows.

The match conditions for a scene must evaluate to true. A selector evaluates a
single attribute of the condition and can evaluate it against matches:

Matches | Meaning  
---|---  
`mustEqual: string` | The value must match the string  
`isSet: boolean` | A value for the given key must exist. The value can be anything.  
  
Let's see an example:

    
    
    {
      "matchCondition": [
        { "key": "model", "mustEqual": "Offer" },
        { "key": "instance", "isSet": false }
      ]
    }

These match conditions evaluate to true for an activity descriptor like
`{mode: "Offer" }`, but not for `{mode: "Offer", instance: "433" }`.

###### Required Prior Scene

Actually, there are two conditions that need to be met for a scene to be
matched:

  1. **Required Prior Scene** (optional): The name of the scene within the flow scope that has to be activated "before" (that is, it is the predecessor). It basically just means, that the parent activity of the activity that matches the scene must match this referenced prior scene.

  2. The Match Condition as shown above.

###### Initial Scene for a Flow

A scene that does not have a required prior scene, can be matched by the match
condition alone. This implies that this scene starts the flow, and thus we can
derive the notion of initial scenes of flows. Note that

  * there can be multiple initial scenes,

  * and the ordering of scenes in the model is not relevant.

##### Example

Let's look at the example from the previous Flows page and walk through the
changes that happen:

![scene-match-
example](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/b29a2a887135085ab2684b87e30601da/scene-
match-example.svg)

###### UI State 0: No Scene

  * Let's say there is a module with a main menu entry `AD = {model: "Offer", action: "list"}`.

  * The user clicks on this main menu entry.

  * A new activity with the above AD is created.

  * Note that there is no initiating activity and hence no prior scene. Therefore, only the scene match with the AD properties is conducted among all existing scenes in the model.

  * As result, the scene "Offer List" is matched and thus triggered. The directives in the scene "Offer List" are executed and the respective UI is configured. This effect is not shown in the diagram above but will be illustrated in the following page.

###### UI State 1: In Offer List

  * The user clicks "edit" on the row representing the document "55".

  * A new activity with the AD properties: `{"Offer", instance: "55", action: "edit"}` is created.

  * This time, an initiating activity exists and it matches the AD of "Offer List" (this match is a consequence of the defined required prior scene "Offer List"). Additionally, the newly created activity matches the AD of "Edit Offer".

  * **Mixing Different Model Types** : Now that we have "prior scene" as an additional scene match criteria, we can omit the model match criteria. This allows to edit documents of different types out of a common scene.

  * The scene "Edit Offer" is triggered and the directives in the scene "Edit Offer" are executed (not shown) and the respective UI is configured.

###### UI State 2: In Edit Offer

  * The user selects "edit clause" for clause 5.

  * A new activity with the AD model: `{"Clause", instance: "5", action: "edit"}` is created.

  * Again, an initiating activity exists, and it matches the AD of "Edit Offer". Additionally, the newly created activity matches the AD of "Edit Clause in Offer". Therefore the scene "Edit Clause in Offer" is triggered.

  * The directives in the scene "Edit Clause in Offer" are executed (not shown) and the respective UI is configured.

#### 3.5.7. Scene Changes

Scene changes consists of scene directives that reconfigure the UI,
specifically the contained views and layout of regions.

Let's just continue with the example from the Scene page and refine it with
the specific scene changes:

![flow-
anatomy](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/00852c3e3f90147513edc33e864230f8/scene-
change-example.svg)

Here's an excerpt of directives for a scene change:

    
    
    {
      "onEnter": [
        { "type": "REGION_CLEAR", "region": ["CONTENT"] },
        { "type": "VIEW_ADD", "region": ["CONTENT"], "name": "OverviewCRUD" }
      ],
      "onExit": []
    }

The directives of a scene change are either in the `onEnter` or in the
`onExit` scene changes:

  * `onEnter` directives are executed when a scene is selected.

  * `onExit` directives are executed when a scene is followed by a next one, i.e., when a new activity is created and this causes a new match condition. This group is for preparing a follow-up situation. Note that the scene with the onExit does not end - there is just another scene (change) now on top of it (or you might think of a new nested scene). Example: if you don't want to show the overview/list when a user selects an entry in the list, then you would change the scene example above to the following:

    
    
    {
      "onEnter": [
        { "type": "REGION_CLEAR", "region": ["CONTENT"] },
        { "type": "VIEW_ADD", "region": ["CONTENT"], "name": "OverviewCRUD" }
      ],
      "onExit": [{ "type": "REGION_CLEAR", "region": ["CONTENT"] }]
    }

Scene changes can be given on the scene level but also on the case level.
Scene changes on the scene level are always executed additional and before to
any selected case.

The available directives are:

Directive | Meaning  
---|---  
`REGION_CLEAR` | Changes the layout of a region. It can have (optional) geometry information which can be used by the layout to position its placeholders (into which the views are placed). The structure of the geometry information is therefore layout specific.  
`VIEW_ADD` | Adds a view to a certain region. You must specify a `name` property, which specifies the UI component by name that is to be shown in the view. The name is resolved during view rendering by looking for a match among the registered UI components. Optionally it is possible to specify view specific constraints that effects the layouts.  
  
Here some more sample excerpts:

    
    
    {
      "onEnter": [
        { "type": "REGION_CLEAR", "layout": { "name": "Stack" } },
        {
          "type": "VIEW_ADD",
          "name": "OverviewCRUD",
          "models": [{ "modelType":"overview", "name":"DiveLogOverview" }]
        }
      ]
    }

  1. The `REGION_CLEAR` directive can change the layout of the regions.

  2. The `VIEW_ADD` directive can provide specific model document names to use in the engine of the view. Here the overview model has the very specific "DiveLogOverview" ID.

To better understand the assignment of views to regions, it helps to think of
a region as a container of views:

  * A view is always added to the end of the view list of its region.

  * By clearing a region explicitly with the `REGION_CLEAR` directive, you remove all previous views from the region.

  * Replaying: The view list of a region is rebuilt if any new activity is created or when an activity is finished.

##### The Replay Algorithm

(This section contains very technical information that is optional.)

You might wonder why there is no directive to remove a view or other means for
cleaning up the views that were added. But cleaning up is not required because
it is done automatically. This works like this: if an activity is finished,
the view assignment is reconstructed by the following **replaying algorithm**
:

  1. Let's assume that activity `Ax` has finished and thus is removed from the list of activities `{A1, A2, …​, Ax, …​, An}`

  2. The leftover list `{A1, A2, …​, An}` is replayed

  3. Reset all assignments of views to regions, so that they are empty.

  4. `A_previous := undefined`

  5. Run a loop over `A1` up to `An` with `A_i` as the loop variable:

    1. If `A_previous !== undefined`: execute the directives of the `onNext` group of `A_previous` (including the `onNext` directives of the selected view of `A_previous`).

    2. Find the matching scene for `A_i` and execute the directives of its `onEnter` group (including the `onEnter` directives of the selected view).

    3. `A_previous := A_i`

The replaying algorithm is performed as a Redux selector called `region`.

##### Layout changes

Even though regions are setup in the Region Configuration part of the model,
you can easily reconfigure the layout of any region in a scene change.

Let's illustrate this reconfiguration of the region layout by implementing a
dashboard. The layout "Dashboard" is already provided by the Client. We just
need to set it up with a specific columns/rows configuration, so that the
dashboard's tiles can be positioned properly. The layout setting consists of a
list of rows. Each row contains either a number of views or a list of
container columns.

Let's implement this sample dashboard layout:

![dashboard-
screenshot](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/a2e8218c9ae8611ed76c1027c728fa8e/dashboard-
screenshot.png)

First, we break it down into the rows and columns like this:

![dashboard-
scene](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/4e38ab239d6e1dbf513f07be5a61ada8/dashboard-
layout.svg)

The dashboard should be assigned to a single activity. Thus, we set up the
region for the dashboard with a `REGION_CLEAR` directive and the following
layout setting. Additionally, we add the five views to the region in the right
order. These views will then be placed into dashboard tiles by the dashboard
layout.

    
    
    {
      "sceneChange": {
        "onEnter": [
          {
            "type": "REGION_CLEAR",
            "layout": {
              "name": "Dashboard",
              "settings": {
                "rows": [
                  {
                    "columns": [
                      { "width": { "sm": 3, "md": 4, "lg": 9 } },
                      {
                        "width": { "sm": 1, "md": 2, "lg": 3 },
                        "rows": [
                          { "columns": [ { "width": { "sm": 4, "md": 6, "lg": 12 } } ] },
                          { "columns": [ { "width": { "sm": 4, "md": 6, "lg": 12 } } ] }
                        ]
                      }
                    ]
                  },
                  {
                    "columns": [
                      { "width": { "sm": 4, "md": 2, "lg": 4 } },
                      { "width": { "sm": 4, "md": 4, "lg": 8 } }
                    ]
                  }
                ]
              }
            }
          },
          { "type": "VIEW_ADD", "name": "DashboardIntroTile" },
          { "type": "VIEW_ADD", "name": "DashboardCalendarTile" },
          { "type": "VIEW_ADD", "name": "DashboardNotesTile" },
          { "type": "VIEW_ADD", "name": "DashboardTasksTile" },
          {
            "type": "VIEW_ADD",
            "name": "OverviewCRUD",
            "models": [ { "modelType": "overview", "name": "CRUD-overview" } ]
          }
        ]
      }
    }

Note that the region is not explicitly given in the directives, since the
"CONTENT" region is the default one, as it was specified in the Region
Configuration part of the application model.

In summary, this is how we modelled the dashboard:

![dashboard-single-
activity](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/47510b41e4f8571e7b8777cb501b04c8/dashboard-
single-activity.svg)

To follow up on the dashboard idea, if the user clicks a row in the overview
in view 5, a form should come up. This form is of course a new activity, which
in turn triggers a new scene. Let's assume that the dashboard in the "CONTENT"
region should disappear while the overview is shown, even on desktops with
enough width to show both. Well, discarding the dashboard activity is not an
option. There are two obvious options: using an `REGION_CLEAR` directive in
either the `onExit` scene change of the dashboard scene or the `onEnter` scene
change of the overview scene. The former looks like this:

    
    
    { "onExit": [{ "type": "REGION_CLEAR", "region": ["CONTENT"], "layout": "MasterDetail" }] }

#### 3.5.8. Cases

Cases are an optional feature and can be defined within a scene. Think of them
as mutual exclusive user interface components for editing the data. For
example, when editing an offer, one case is the general data form, another
case is the terms & conditions and yet another one is the coverages list. All
these details are contained in the same offer document, but the designers
broke it down into different cases.

Specifically, a case has

  * A label which is typically shown in the sidebar menu and is localizable by providing different texts in a map. The key is hereby the string representation of the Locale object. Furthermore, it is possible to extend and override these texts with a localizer by using the corresponding localization key. Using a customized localizer does not require that a label is provided in the application model.

  * Scene changes with **directives** : The selected case contains a scene change that is executed after the scene change on the scene level. One typically places view with engines here, while the case agnostic sidebar is setup on the scene level.

Only one case of a scene can be active (thus, a mutual exclusive). This is
tracked by the activity, which has a property `case` for the current case. If
you change this case property, the region is updated (via the replay
algorithm) to update the view assignment to regions.

A menu of available cases can be shown by just adding the standard UI
"GenericCaseMenu" component with a sidebar region. The menu then shows the
name for each case, and with a click on a menu entry, the respective case is
selected and the directives of the case's `onEnter` group are executed.

Here's an example scene that offers three cases and uses the GenericCaseMenu
UI component:

    
    
    {
      "scenes": [
        {
          "name": "Edit Offer",
          "description": "Specific Offer",
          "matchCondition": [
            { "key": "model", "mustEqual": "Offer" },
            { "key": "instance", "isSet": true }
          ],
          "sceneChange": {
            "onEnter": [
              { "type": "VIEW_ADD", "region": "SIDEBAR", "name": "GenericInstanceInfoPanel" },
              { "type": "VIEW_ADD", "region": "SIDEBAR", "name": "OfferActions" },
              { "type": "VIEW_ADD", "region": "SIDEBAR", "name": "GenericCaseMenu" }
            ]
          },
          "defaultCase": "general",
          "cases": [
            {
              "name": "general",
              "label": { "en": "General" },
              "sceneChange": { "onEnter": [ { "type": "VIEW_ADD", "name": "GenericForm" } ] }
            },
            {
              "name": "terms",
              "label": { "en": "Terms & Conditions (General Conditions)" },
              "sceneChange": { "onEnter": [ { "type": "VIEW_ADD", "name": "TermsConditions" } ] }
            },
            {
              "name": "coverages",
              "label": { "en": "Coverages" },
              "sceneChange": { "onEnter": [ { "type": "VIEW_ADD", "name": "GenericOverview" } ] }
            }
          ]
        }
      ]
    }

The following diagram shows the situation where an activity is matched to this
"Offer" scene and the cases are switched from "general" to "terms":

![views](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/4f9e89c47fe16063dc58a3760e67efad/cases-
example.svg)

If the case "general" is selected, the resulting UI looks like this:

![cases](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/07ced9c9764c9f8479b2a1f15afb4f09/anatomy.png)

When the cases are switched from "general" to "terms", the UI adapts like
this:

  1. Removal of the views specified for the previous case "general", i.e., the case with "GenericForm" ui component.

  2. Addition of the view specified for the new view "terms", i.e., the view with "TermsConditions" ui component.

##### Cases versus traditional "tabs"

Some UIs use the "tabs" approach with only one tab being shown at a time.
However, this is very physical. By introducing cases as an abstraction, you
are free to come with any physical rendering you like. And quite easily so, by
means of choosing the right layout (for the tabbed UI, you might can easily
provide a layout the shows views in exclusive tabs) for the "CONTENT" region.

### 3.6. Data Loading

The Client provides a powerful data loading concept. Whenever a scene gets
activated for an activity the Client evaluates if data loading is needed. This
evaluation can be described as the following:

  1. If the matching scene has models defined, e.g. `models: [{ modelType: "form", name: "Product" }]`, the runtime automatically performs model and data loading in parallel.

  2. If the matching scene has no models defined, but the boolean flag `loadData: true`, the runtime automatically performs data loading.

  3. In all other cases, no data loading is performed.

You can always, dispatch an `ActivityActions.loadData` to trigger the data
loading for a specific activity id.

#### 3.6.1. Data Handlers

The Client supports three kinds of data handlers: Data Loader, Data Editor and
Data Provider. They are described in more detail in the upcoming sections.

By using Data Loader or Data Editor, the runtime provides some default
behavior for some data operation.

  * **save:** after saving, it dispatches an ActivityActions.reload of the current activity. If you pass the `updateActivityData` flag to the action's payload of save/commit, the Client updates the activity's data with the response data of the save request.

  * **delete:** before executing the delete request, the Client first tries to cancel all child activities of the current one. After the delete operation, it triggers a reload for the overview activity, if there is one.

If you do not want to have any of these, you should implement the data
operation with a data provider. There is no default behavior for data
provider. The runtime simply calls the `provideData()` function.

##### Registration and order of execution

Data handlers are registered in the application setup. For each data
operation, the runtime tries to find matching data handler in the following
order:

  1. Data Provider

  2. Data Editor

  3. Data Loader

The runtime first evaluates data providers, then data editors and finally data
loaders. The order within each of the arrays is also important. In the
following example, the runtime would first query the `DataProvider`, then the
`DocumentDataEditor` and afterwards the `DataLoader`, if one of them can
handle a data holder of the current activity. The first matching data handler
is going to perform the data operation.

    
    
    const dataHandlers: DataHandlers = {
      dataEditors: [ new DocumentDataEditor() ],
      dataLoaders: [ new DataLoader() ],
      dataProviders: [ new DataProvider() ]
      /* ... */
    }

##### Data Loader and Data Editor

Data Loaders handle the exchange of business data with external systems. Data
Editors on the other hand handle exchange of business data between activities.

Data Loaders support the following actions:

  * load

  * save

  * delete

Data Editors support the following actions:

  * read

  * write

Any number of Data Loaders and Editors can be configured but for every data
action, only one Data Loader or Editor will be used. The selection happens as
follows:

  * Each Data Loader is asked if it can handle the current Activity. The first matching Data Loader is executed .

  * Each Data Editor is checked if it matches the current Activity and an ancestor of it using match conditions. A data editor defines parent and child match conditions. It matches for an activity if all the child match conditions of the editor match the activity descriptor and if all the parent match conditions match an activity descriptor of an ancestor (defined by the initiating activity id) of this activity. The ancestor activities are checked bottom to top (first the direct parent of the activity). The first matching Data Editor is executed and the data is read/written from/to the matched ancestor activity.

Both Data Loaders and Data Editors only handle the data of the activity's
default data holder, which is the one that has the same descriptor as the
activity. Handling the data of additional data holders is supported via Data
Providers.

##### Data Provider

A Data Provider can also handle the exchange of business data with external
systems as well as the exchange of data between activities. Since it is a
wrapper around a redux-saga function, it can fetch data, access the Redux
store via selectors or dispatch actions via action creators.

Data Providers support the following actions:

  * load

  * save

  * delete

Any number of data providers can be registered in the application setup. Every
data provider is asked if it can handle a data holder for the current
activity. A data provider can handle an arbitrary number of data holders, but
each data holder can only be handled by one data provider.

After the selection of all data holders is finished, each data provider gets
its list of data holders to load. Additionally, each provider has access to
the payload of the action that triggered it via the `details` property (see
example below).

If a `"loading"` or `"saving"` error should be set to a specific non-default
data holder, then a custom action and custom data reducers are required.

###### Empty Document Data Provider

In order to enable the creation of empty document by the Client itself, the
Client provides a data provider factory function
(`ApplicationFactories.createEmptyDocumentDataProvider`). This factory returns
a data provider that creates an empty document with initial values and pre-
computed values if a new document should be loaded.

__ |  Without this data provider another data handler has to handle the request for loading a new document.  
---|---  
  
###### Example

The following example shows an implementation of a data provider to load
documents from an API and putting them into the current activity's data
property.

    
    
    const DocumentsDataProvider: DataProvider = {
      name: "DocumentsDataProvider",
      canHandle({ dataHolder, operation }) {
        switch (operation) {
          case "load":
            return dataHolder.descriptor.instance !== undefined;
          case "save":
          case "delete":
            return false;
          default:
            throw new Error(`No support for ${operation}.`);
        }
      },
      *provideData({ activityId, dataHolders, operation, details }) {
        switch (operation) {
          case "load":
            const documents = yield all(
              dataHolders.map(({ descriptor }) =>
                // getDocumentById fetches data from a external source and returns a promise
                call(getDocumentById, `/documents/${descriptor.instance}`)
              ));
            yield put(ActivityActions.setData({ activityId, data: documents }));
            break;
          case "save":
          case "delete":
          default:
            throw new Error(`No support for ${operation}.`);
        }
      }
    };

### 3.7. Data Reducers

A data reducer is a client-specific extension of the reducer concept from
Redux.

Like a standard Redux reducer it is triggered by Redux actions. However, since
data reducers are only concerned with the data slice of an activity, they can
only handle activity-related actions and then, once triggered, calculate the
update of a data holder of the respective activity.

The interface of a data reducer is quite similar to that of a data handler as
it also consists of two methods:

  * canHandle: A function to determine whether the corresponding reducer should handle the given data holder and action.

  * reduce: The reducer function which changes the given data holder in the Redux store.

#### 3.7.1. Adding a Data Reducer

Below is a sample implementation of a data reducer that reacts to a specific
action and then handles its respective payload. The exemplary data reducer
canHandle function is implemented in a way that it will only return true for a
specific data holder of the activity.

    
    
    const actionCreator = actionCreatorFactory("Example");
    
    /** Example action to add a new Todo item to the list of ToDos */
    export const addTodo = actionCreator<AddTodoPayload>("ADD_TODO");
    
    /** The payload of the addTodo action. */
    export interface AddTodoPayload extends ActivityActions.ActivityActionPayload {
      readonly todo: string;
    }
    
    /** Todo list data structure to manage in a data holder */
    export interface TodoList {
      readonly todos: string[];
    }
    
    export const AddTodoDataReducer: ActivityReducers.DataReducer = {
      canHandle(
        dataHolder: Activity.DataHolder<{}>,
        action: ActivityActions.DataReducerAction,
        isDefaultDataHolder?: boolean
      ) {
        return (
          addTodo.match(action) && dataHolder.descriptor["use"] === "todo-list"
        );
      },
      reduce(
        dataHolder: Activity.DataHolder<TodoList>,
        action: Action<AddTodoPayload>
      ) {
        return {
          ...dataHolder,
          data: {
            ...dataHolder.data,
            toDos: [...(dataHolder.data?.todos ?? []), action.payload.todo]
          }
        };
      }
    };

__ |  It is important to note that the trigger action should either extend `ActivityActions.ActivityActionPayload` or `ActivityActions.AsyncActivityActionPayload`. Otherwise, the action payload would not contain the activity identifier and thus would not link it to any activity in the Redux store.  
---|---  
  
The integration of a data reducer can happen in two ways:

  1. The data reducer can be provided with the `ApplicationFactories.Config` object as a part of the general application setup using the `ApplicationFactories.createApplicationSetup` function.

  2. The data reducer can be provided via the Module API as a module-specific data reducer.

### 3.8. Summary

Let's summarize what we've learned so far. Here are the key concepts:

  * Regions: the application frame defines two regions: content area and sidebar. Each region contains views and uses a layout manager to derive which views are visible and how they are arranged.

  * Activity: a user is always engaged in an activity like an overview or editing a form. Activities can be nested in a possible recursive master/detail manner. The next section explains activities further.

  * Case: an activity can offer multiple cases, e.g., a complex business objects like an insurance policy can be broken down into different cases like general data, risks, terms&conditions, etc.

  * Views: The views of a regions are derived by the activities and the current selected scene and case (through a mechanism called _condition matching_ , which is explained in the Application Model section).

![anatomy](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/07ced9c9764c9f8479b2a1f15afb4f09/anatomy.png)

## 4\. Features

This chapter describes the features of the A12 Client in detail.

### 4.1. Configuration

For configuration of technical services, the Client uses dependency injection
based on the [Inversify](http://inversify.io/) library:

  * A12 Model & Document / User API - various services

  * Logging

__ |  It is assumed that the configuration is done once at the initialization. Changes that are done later may cause unintended behavior and are not supported by the Client at the moment!  
---|---  
  
#### 4.1.1. Usage

The main object to interact with the `core/configuration` API is the
Container.

    
    
    import { Container } from "@com.mgmtp.a12.client/client-core/lib/core/configuration";

The difference of this `Container` to the [Inversify](http://inversify.io/)
Container API is that it combines the [Inversify](http://inversify.io/)
Container API (`Container.config`) as well as a map of all identifier
(`Container.identifier`) that are used by the Client.

Identifier | Remarks  
---|---  
LoggingStrategy | Optional  
UISettings | Optional  
  
Please consult the Client API Documentation for more details of the
identifiers.

How to set some configuration

    
    
    import { Container } from "@com.mgmtp.a12.client/client-core/lib/core/configuration";
    
    import { ConsoleLoggingStrategy } from "@com.mgmtp.a12.utils/utils-logging";
    import { LogLevel } from "@com.mgmtp.a12.utils/utils-logging/api";
    
    
    // Initialize an entry
    Container.config
      .bind(Container.identifier.LoggingStrategy)
      .toConstantValue(new ConsoleLoggingStrategy(console, LogLevel.WARN));
    
    // Change an entry
    Container.config
      .rebind(Container.identifier.LoggingStrategy)
      .toConstantValue(new ConsoleLoggingStrategy(console, LogLevel.LOG));

Please consult the [Inversify](http://inversify.io/) Documentation for more
details about using [Inversify](http://inversify.io/) Container API.

#### 4.1.2. UI Settings

With the UI setting it is possible to globally define some UI aspects like the
delay of the progress indicator.

Please refer to the API documentation to get details of the possible settings.

How to set the UI settings

    
    
    import { Container } from "@com.mgmtp.a12.client/client-core/lib/core/configuration";
    
    
    // Change an entry
    Container.config.rebind(Container.identifier.UISettings).toConstantValue({
      /** your settings */
    });

### 4.2. Engines

Several components support the A12 Engines integration:

  * **Form-Engine:** A (base) view for the Form-Engine

  * **Overview-Engine:** A (base) view for the Overview-Engine

Both components receive their models from the store. The data is part of the
activity and provided by the view mechanism.

The provided components require implementation of additional props for
advanced features like attachment handling.

#### 4.2.1. Form-Engine Component

The provided Form-Engine view component is based on the A12 Form-Engine and
can be customized by regular React means using props.

One often required customization of the form engine is to use it in a static
read-only mode, where only read-only operations can be performed in the form.
This can be achieved most easily by providing a preinitialized ui slice (`{
uiState: { readonly: true } }`) to the `slices` property in the payload of the
`create` Redux action, when creating a new activity. Alternatively, you could
set readonly in the ui state in the `mapStateToProps` mapping, when connecting
the form engine component yourself.

When the form activity is already present, you can achive the same thing by
dispatching a `setReadonly` Redux action after the form engine activtiy was
created.

See Form-Engine for more details.

#### 4.2.2. Overview-Engine Component

The provided Overview-Engine view component can also be customized via its
React props.

Furthermore, you can customize the initial state of the Overview Engine by
registering a custom middleware that intercepts `Activity.PUSH` actions and
re-dispatches them with an initial filter configuration. The following code
shows how this can be achieved:

    
    
    import { Middleware } from "redux";
    
    import {
      Activity,
      ActivityActions
    } from "@com.mgmtp.a12.client/client-core/lib/core/activity";
    import {
      OverviewEngineSelectors,
      OverviewEngineState
    } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    
    export const extendPushPayloadMiddleware: Middleware =
      api => next => action => {
        if (ActivityActions.push.match(action)) {
          // filter out those new activities which contain the overview engine that you want to customize
          if (action.payload.activity.descriptor.model !== "my-example-model") {
            return next(action);
          }
    
          let extendedListSlice: Partial<OverviewEngineState> = {};
          const listSlice: Partial<OverviewEngineState> | undefined =
            OverviewEngineSelectors.getStateWithoutDefaults(
              action.payload.activity
            );
          /**
           * Calculate extendedListSlice from listSlice here
           */
          extendedListSlice = listSlice || {};
    
          const defaultDataHolder: Activity.DataHolder<{}> | undefined =
            Activity.findDefaultDataHolder(action.payload.activity);
          if (!action.payload.activity.dataHolders || !defaultDataHolder) {
            throw new Error("The default data holder is missing!");
          }
    
          const remainingDataHolders = action.payload.activity.dataHolders.filter(
            dh => dh !== defaultDataHolder
          );
    
          const extendedPayload: ActivityActions.PushPayload = {
            ...action.payload,
            activity: {
              ...action.payload.activity,
              dataHolders: [
                {
                  ...defaultDataHolder,
                  slices: {
                    ...defaultDataHolder.slices,
                    list: extendedListSlice
                  }
                },
                ...remainingDataHolders
              ]
            }
          };
    
          return next(ActivityActions.push(extendedPayload));
        } else {
          return next(action);
        }
      };

#### 4.2.3. Form-Engine

This chapter will be about:

  * The Setup of Form-Engine in the Client

  * The Integration of the Form-Engine State in Activities

  * Form-Engine actions

  * Customization

It will not cover the CRUD functionality. Please refer to the chapter Working
with A12 models for more information.

It is also recommended to read the [A12 Form Engine
Documentation](../../../../../../content/2022.06/ENGINES/34/asciidoc/formengine-
documentation-bundle/index.html) before to get a better understanding of the
architecture.

##### Integration

This part will explain the steps which are necessary to use the Form-Engine in
a Client application using the Form-Engine extension.

The extension provides different view components:

  * `FormEngineViews.FormEngine`: A connected component that consists of a composition of the FormEngineRenderer, the ContentBoxRenderer and the ScollHandler. You can pass it the engine configuration props and the props of the components in the composition

  * `FormEngineViews.FormEngineTpl`: The same as the FormEngine component above, except it is not connected. This can be used to customize the connection to the redux store.

  * `FormEngineViews.ScrollHandler`: A connected ScrollHandler component that can be used for a custom form engine composition, when the FormEngine component from above is not used.

It also comes with middlewares, sagas, and data reducers to store and modify
the state of the Form-Engine correctly in the Client environment.

###### Appsetup

The following steps are necessary in the appsetup to integrate the extension:

  * call `createFormEngineMiddlewares` and add the returned middlewares to the `additionalMiddlewares`

__ |  If you need to customize your middlewares (like setting up an external enumeration provider or disabling boolean coalescing), you have to pass your `MiddlewareOptions` directly. Do not call `createEngineMiddlewares` separately, as the engine middlewares need to be wrapped to receive the correct state. `createFormEngineMiddlewares` does this automatically.  
---|---  
  
  * add `formEngineSagas` to the `customSagas`

  * add `formEngineDataReducers` to the activity data reducers

Please refer to the API documentation to get further information about the
different parts.

###### View

The Form-Engine view is an already connected component and can be used
directly in the component provider. The view can be customized by using
configuration props. You can also connect the Form-Engine by yourself, which
gives you more possibilities to customize. The chapter Customization contains
more information about how to connect the engine.

The `ScrollHandler` view is also already connected. This view can be used to
activate the scrolling behavior. It is not needed if you use the standard
`FormEngineViews.FormEngine`, but in case you connect the Form-Engine by
yourself you need to wrap the `ScrollHandler` around it.

##### State Integration

###### Initializing of an Activity

The following image shows how an activity, which should be used to display a
Form-Engine, is initialized.

![image](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/4329178681aeb9aa027376284890d65a/initializing_of_an_activity.svg)

  1. The saga from the Form-Engine extension listens to the _push-action_ that belongs to a scene with a modelType `form`.

  2. The saga merges the default initial UI state with the provided partial ui state in the `slices.uiState` property and triggers an internal action to set the UI state.

  3. The internal action is handled by the normal middlewares and reducers.

  4. In the end the newly created activity contains the default data holder, that contains the loaded data and a complete UI state slice.

###### Updating of an Activity

The following image shows the interaction between Form-Engine and the Client.
It is assumed that the activity is already initialized like described in
Initializing of an Activity.

![image](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/daa572dde17208d003f4c46d4c4247bf/bfe_and_activities.svg)

  1. The Client state contains all information which are necessary to render the Form-Engine for a specific form

     * an activity holding the document (data.document prop) and the Form Engine UI state (slices.ui prop) in its default data holder

     * the form model and document model

     * the locale

  2. When connecting the view the internal Form-Engine state is created by using the _FormEngineSelectors_.

  3. The renderer traverses the form model and uses React components to render. Please refer to the `A12 Engines Documentation` for more information.

  4. Event-actions which are dispatched by the Form-Engine are wrapped in a Client action by the _Event-Action Dispatch Adapter_. The new action contains, next to the original event-action, the activity-id. This is necessary to be able to map changes in the back-end to the activity which contains the engine state.

  5. The Client action is handled by the _Middleware-Adapter_. This adapter calls all middlewares from the Form-Engine with the wrapped event-action.

  6. For each event-action, one or more command-actions are dispatched by the Form-Engine middlewares.

  7. If the command-action signals a data change (e.g. `setDocument`) the corresponding _ActivityAction_ is dispatched by the _Middleware-Adapter_.

  8. If the command-action signals a UI-state change a Client action, which wraps the command-action is dispatched by the _Middleware-Adapter_.

  9. The Client action is treated be the _UI-state Reducer Adapter_ , which extracts the wrapped command-action and gives it to the UI-state reducer of the Form-Engine.

  10. The UI-state reducer of the Form-engine changes the given state and returns it to the _engine Reducer Adapter_ which then changes the ui slice in the slices property of the default data holder in the activity.

##### Actions

The Form-Engine extension contains to two actions which are used to wrap
actions coming from the Form-Engine with an activity id. The action
`FormEngineActions.event` is used to wrap event-actions while the action
`FormEngineActions.command` is used to wrap command-actions.

Middlewares that want to handle actions from the Form-Engine need to listen to
both these wrapper actions as well as the actual Engine action which is
contained in the payload of the wrapper action.

The following code shows an example of how to implement a middleware which
handles the event action `Events.eventButton`.

    
    
    export const onEventButtonClickedMiddleware: Middleware<{}, EngineState> =
      api => next => action => {
        if (
          FormEngineActions.event.match(action) &&
          Events.eventButton.match(action.payload.engineEvent)
        ) {
          const event = action.payload
            .engineEvent as Action<Events.EventButtonPayload>;
          handleOnEvent(event.payload.name);
        }
    
        return next(action);
      };

You also need to use these wrapper actions, if you want to dispatch a Form-
Engine action in your code:

    
    
    FormEngineActions.command({
      activityId: formEngineActivityId,
      engineEvent: Commands.setReadonly(true)
    });

##### Customization

This section will describe the different possibilities to customize the Form-
Engine inside the Client. It is recommended to read the chapter about the
interaction of activities and the Form-Engine before.

###### View

####### Customizing the Standard View

The standard view can be customized via props. The props consist of the `View`
props as for every view and in addition the Form-Engine `Config` props.

The `View` props are the standard view props, containing the activity. The
`Config` props come from the Form-Engine and include properties like
`cardView`, `attachmentHandler` and `converters`. Please refer to the [API
documentation of the Form-
Engine](../../../../../../content/2022.06/ENGINES/34/typedoc/formengine-api-
documentation/index.html) for further information.

Via the `Config` props you can also provide custom implementations of the
`FormModelMap`, `InputMap` and `WidgetMap`. This enables you to use custom
widgets. You can find more information about this in the [A12 Form Engine
Documentation](../../../../../../content/2022.06/ENGINES/34/asciidoc/formengine-
documentation-bundle/index.html).

The following code shows a customization example:

    
    
    export function formEngineViewsComponentProvider(props: View): JSX.Element {
      return <FormEngineViews.FormEngine {...props} cardView={true} />;
    }

####### Initial UI Slice

Another high-level way to customize the Form-Engine view is to create the
Form-Engine activity with a preinitialized ui state. This can be achieved by
providing an initial `ui` slice to the `slices` property of the `create`
action payload.

Or you could modify the `slices` property in a data reducer for the form
engine activity default data holder.

In this ui slice values for the Form-Engine's `EngineStore.UIState` properties
can be provided. With this, you can e.g. set the Form-Engine to disabled or
readonly, or you can modify the collapsed state of collapsible sections. You
could even change the initial screen location, i.e. show the detail screen of
a detached repeat as the initial screen. See the [A12 Form Engine API
documentation](../../../../../../content/2022.06/ENGINES/34/typedoc/formengine-
api-documentation/index.html) for all available properties.

Creating the form engine activity with the action shown in the following
example would give you an initially disabled Form-Engine:

    
    
    const initialUiSlice: Partial<EngineStore.UIState> = {
      disabled: true
    };
    
    const createAction = ActivityActions.create({
      activityDescriptor: { model: "form", instance: "1" },
      slices: {
        ui: initialUiSlice
      }
    });

####### Connecting a Custom View

This section describes how you can connect the Form-Engine by yourself. When
you connect the Form-Engine you can use the unconnected
`FormEngineViews.FormEngineTpl` component as a basis.

The Client stores the needed information for the Form-Engine in a different
structure in the state than the Form-Engine requires it. When connecting the
form engine, you need to map the client state to the engine state with a
`mapStateToProps` mapping.

In a `mapDispatchToProps` mapping the UI-events occuring in the form engine
need to be mapped to the respective redux actions.

To connect the component, which means creating and using the mapped props, two
helper functions are provided:

  * `FormEngineStateAdapter.mapStateToProps` to map the state props.

  * `FormEngineActions.mapDispatchToProps` to map the dispatch props. This function internally already uses a dispatch adapter which takes an event-action from the Form-Engine and creates a Client wrapper action which includes next to the event-action the activity id.

Connecting is only necessary if you want to adjust the mapping of state props
or if you want to adjust the handling of UI-events.

######## Complete Example

The following code shows an example of how to connect your form engine.

In this example the ui state of the form engine is statically set to readonly
and the payload of the `Events.navigationButton` is adapted so that the
validate property is always false, independent of the information from the
form model.

    
    
    import * as React from "react";
    import { useDispatch, useSelector } from "react-redux";
    
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import {
      FormEngineActions,
      FormEngineStateAdapter,
      FormEngineViews
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";
    import {
      Config,
      DefaultDispatchProps,
      DefaultStateProps
    } from "@com.mgmtp.a12.formengine/formengine-core/lib/view";
    import { Events } from "@com.mgmtp.a12.formengine/formengine-core/lib/back-end/store";
    
    type StateProps = Partial<DefaultStateProps>;
    
    export type OwnProps = View & Partial<Config>;
    
    export function CustomFormEngineView(
      props: StateProps & DefaultDispatchProps & OwnProps
    ): JSX.Element {
      // default mappings created via helper functions
      const defaultStateProps = useSelector(state =>
        FormEngineStateAdapter.mapStateToProps(state, props)
      );
    
      const dispatch = useDispatch();
      const defaultDispatchProps = FormEngineActions.mapDispatchToProps(
        dispatch,
        props
      );
    
      // customizing the state prop mapping
      const customStateProps: Partial<DefaultStateProps> = {
        ...defaultStateProps,
        state: defaultStateProps.state
          ? {
              ...defaultStateProps.state,
              ui: {
                ...defaultStateProps.state.ui,
                readonly: true // set the form engine readonly
              }
            }
          : undefined
      };
    
      // customizing the dispatch prop mapping
      const customDispatchProps: Partial<DefaultDispatchProps> = {
        ...defaultDispatchProps,
        eventHandlers: {
          ...defaultDispatchProps.eventHandlers,
          onNavigationButton(target: string, validation: "full" | "partial"): void {
            /**
             * Set the validation property always to full instead of taking
             * the information from the form model
             */
            dispatch(
              Events.navigationButton({
                target,
                validation: "full"
              })
            );
          }
        }
      };
    
      // using the mapped props to connect the form engine template
      return (
        <FormEngineViews.FormEngineTpl
          {...props}
          {...customStateProps}
          {...customDispatchProps}
        />
      );
    }

####### Config

Whether you connect your form engine component yourself or use the already
connected one, you can always also adjust the `Config` props, like it is
described here.

###### Middlewares or Sagas

You can register custom middlewares and sagas in your application which react
to actions coming from the Form-Engine. As the client always wraps these
action into a `FormEngineAction`, you need to match them first and then match
the original action.

###### DataFormats

In order to provide custom data formats to the Form-Engine it is necessary to
create your own converter provider that is configured with your data formats.

The example Define DataFormats and Converter Provider below uses the
`defaultConverter` function in order to keep this example as simple as
possible. However, if it is required, it is possible to customize the entire
converter logic here.

Please consult the Kernel documentation for more details about creating
presentation information objects.

Define DataFormats and Converter Provider

    
    
    import {
      Converter,
      defaultConverter,
      defaultLocalizer,
      Provider
    } from "@com.mgmtp.a12.formengine/formengine-core/lib/back-end/store";
    import {
      DataFormats,
      defaultDataFormats,
      Locale,
      PartialLocale
    } from "@com.mgmtp.a12.utils/utils-localization/lib/main";
    
    const dataFormatsProvider: (locale: Locale) => DataFormats = locale => {
      // Provide here your data formats logic
    
      // Below you see an example of a fallback mechanism.
      try {
        return defaultDataFormats(locale);
      } catch {
        return defaultDataFormats({
          language: "en",
          country: "US"
        } as PartialLocale);
      }
    };
    
    export const customConverterProvider: Provider<Converter> = defaultConverter(
      // use the form-engine default localizer provider or
      // implement your own instead if you have a custom localization approach
      defaultLocalizer(dataFormatsProvider),
      dataFormatsProvider
    );

Afterwards, you have to make the new converter provider known to the Form-
Engine view and middleware adapter. This can easily be achieved as shown in
the example Custom Converter Provider Integration.

Custom Converter Provider Integration

    
    
    export function createCustomViewProvider(
      handler?: AttachmentHandler
    ): (componentName: string) => React.ComponentType<View> | undefined {
      const components: { [name: string]: React.ComponentType<View> | undefined } =
        {
          FormView(props) {
            return (
              <FormEngineViews.FormEngine
                {...props}
                converter={customConverterProvider} __**(1)**
                attachmentHandler={handler}
              />
            );
          }
        };
    
      return function customViewProvider(name) {
        return components[name];
      };
    }
    
    // ...
    
    
    export function defaultApplicationLocalizerProvider(state: object): Localizer {
      const locale = LocaleSelectors.locale()(state);
      const documentModelMap = ModelSelectors.allDocumentModels()(state);
      // use the same data formats here as in the customConverterProvider implementation!
      const dataFormats = defaultDataFormats(locale);
    
      return createApplicationLocalizer(locale, documentModelMap, dataFormats);
    }
    
    ApplicationFactories.createApplicationSetup({
      additionalMiddlewares: [
        ...createFormEngineMiddlewares({
          converter: customConverterProvider __**(2)**
        })
      ],
      customSagas: [...formEngineSagas],
      model,
      modelLoaders: [],
      dataHandlers: dataHandlers,
      dataReducers: [...formEngineDataReducers]
    });

__**1** | Provide custom converter provider to the Form-Engine view  
---|---  
__**2** | Provide custom converter provider to the Form-Engine middleware adapter  
  
###### Engine State Selector

If due to some customizations the engine state has to be selected in a
different way, it is necessary to provide a custom engine state selector to
the form engine middleware adapter (`createFormEngineMiddlewares`) and the
view (see Section 4.2.3.4.1.3 for more details).

### 4.3. Platform Server Connectors

The _Platform Server Connectors_ extension provides reading/writing
functionality for the A12 _Form Application_ Server. Note that it depends on
many additional services of the A12 Services product. Please have a look at
the _Sample Application_ source code for an example.

#### 4.3.1. Important to Know

The data loaders of the _Platform Server Connectors_ extension override the
`id` and `modelId` property of any loaded document. This serves the usability
to recognize documents and their models. Typically, this should never be an
issue because the SME enforces a root group. However, if this root group is
called either `id` or `modelId`, this is a critical issue. In this case please
consider to restructure you document model.

#### 4.3.2. Note on Attachments

The _Platform Server Connectors_ extension provides access to the A12 _Form
Application_ Server attachment handling capabilities.

Attachments can be uploaded, replaced, downloaded and removed via the
connectors and preview thumbnails can be provided.

__ |  In contrast to the attachment itself, the preview thumbnails of an attachment can only be retrieved via an unsecured endpoint of the A12 _Form Application_ Server. Security in there is provided by the complexity of the URL which contains the thumbnail UUID. This endpoint is disabled by default, so previews are disabled by default. If the provided security for preview thumbnails is sufficient for your project, the endpoint can be enabled via a server configuration key. See the services documentation for details.  
---|---  
  
#### 4.3.3. Providing Custom Server Connector

The _Platform Server Connectors_ extension respects the Services API and uses
the `ConnectorLocator`. Therefore, it is possible to supply your
implementation following the Simple Example. This can be used to modify the
authentication filters as well as supply a custom server connector.

Simple Example

    
    
    // Configure your server connector e.g. using UAA
    ConnectorLocator.createInstance(serverConnector);

### 4.4. HTTP Connectors

The _HTTP Connectors_ extension provides the functionality to load different
kinds of models from different locations.

We distinguish between loading models directly from the platform server
(Platform Model Loading) or from other locations, e.g. a different server or
you local file system (HTTP Model Loading). Model loading also varies for
different kinds of models, e.g. for a document model it is also necessary to
load the corresponding validation code.

This extension provides three different ModelLoader implementations, which
deal with the different kinds of models:

  * _DocumentModelLoader_ : Loads a document model including the corresponding validation code.

  * _FormModelLoader_ : Loads a form model.

  * _GenericModelLoader_ : Loads a model independently of the model's type.

These model loaders are internally customized with different fetching
mechanisms to be used for both - HTTP Model Loading and Platform Model
Loading.

#### 4.4.1. HTTP Model Loading

With the public factory function _createHttpModelLoaders_ you can retrieve an
array of model loaders for HTTP Model Loading. They use the fetch API for
loading the desired models. The base path from which the models should be
loaded can be configured by passing it to the factory function. If no base
path is given, the root path "/" will be used.

    
    
    const modelLoaders = createHttpModelLoaders("/models/");

#### 4.4.2. Platform Model Loading

Platform Model Loading reuses the model loaders from the _HTTP Connectors_
extension, but sets a different fetching mechanism, which is implemented in
the _Platform Server Connectors_ extension.

#### 4.4.3. Implementing a custom ModelLoader

You can also implement a custom ModelLoader, e.g. to add custom post-
processing steps or a custom fetch logic. To achieve this you first need to
implement the ModelLoader interface as shown in the example below and
afterwards register your custom model loader in the appsetup of your
application.

The ModelLoader interface

    
    
    export interface ModelLoader {
      /**
       * A unique name to identify the loader
       */
      readonly name: string;
    
      /**
       * Determines, if the loader is responsible for an activity
       *
       * @param descriptor of the model that should be loaded
       *
       * @returns true, if the loader is determined responsible or false if not
       */
      canHandle(descriptor: Model.Descriptor): boolean;
    
      /**
       * Load an A12 model. The type of the returned model varies.
       *
       * @param descriptor of the model to be loaded
       * @param getReferencedModel returns a referenced model
       */
      load(
        descriptor: Model.Descriptor,
        getReferencedModel: (descriptor: ModelReference) => Promise<ModelAPI>
      ): Promise<ModelAPI>;
    }

Example of a simple ModelLoader implementation

    
    
    export class CustomModelLoader implements ModelLoader {
      readonly name: string = "CustomModelLoader";
    
      constructor(protected basePath: string = "/") {}
    
      canHandle(descriptor: Model.Descriptor): boolean {
        return true;
      }
    
      async load(
        descriptor: Model.Descriptor,
        getReferencedModel: (referencedModel: ModelReference) => Promise<ModelAPI>
      ): Promise<ModelAPI> {
        return fetch(`${this.basePath}${descriptor.name}.json`)
          .then(response => response.json())
          .then(json => (isModelInstance(json) ? json : Promise.reject("Error!")))
          .catch(error => Promise.reject("Error!"));
      }
    }

#### 4.4.4. Custom Model Loading

Independent of the default model loading of the client it is possible to
handle model loading yourself. In order to prevent interference with the
default model loading only models should be handled that are not referenced by
the application model and their transitive dependencies.

Handling the model loading yourself has some implications, because without the
model descriptors in the application model no automatic data loading will
happen and engines views are not able to resolve their models. Therefore, you
have to provide your own data providers and views.

In the following example you can see a simple custom model loading saga. For
more details about setting models please have a look the
`ModelActions.setModels` action documentation.

Example of a custom model loading saga

    
    
    export function* loadModels(): SagaIterator<void> {
      yield* takeEvery(
        [ActivityActions.push, ActivityActions.cancel],
        function* handlePushAction(action) {
          const activity = ActivityActions.push.match(action)
            ? action.payload.activity
            : action.payload.replacementActivity;
    
          if (
            activity === undefined ||
            !isActivityWithCustomModelLoading(activity) ||
            modelsAreLoaded()
          ) {
            return;
          }
    
          const documentModel = customDocumentModelLoader();
          const formModel = customFormModelLoader();
    
          yield* put(
            ModelActions.setModels({
              [formModel.header.id]: formModel,
              [documentModel.header.id]: documentModel
            })
          );
        }
      );
    }

### 4.5. Layouts

_Layouts_ define how views are visually arranged inside a Region. The
following layouts are provided by default:

#### 4.5.1. MasterDetail

Arrangement of views side-by-side, where only one or two views are visible at
the same time.

Via the VIEW_ADD directive in the application model it is possible to add a
constraint for the preferred width of the right view. The view can take from 1
to 11 of the 12 available layout grid slots, leaving the remaining space for
another view visible on the left. If only one view is visible, it uses all
available space.

For more details, see the [UI/UX concept](https://wiki.mgm-
tp.com/confluence/x/Aq96Bg) (mgm internal only).

#### 4.5.2. Dashboard

All views are arranged in tiles which are positioned in rows and columns.
Please consolidate the widgets documentation for more details.

#### 4.5.3. ApplicationFrame

This layout is only intended to be used for the root region of the
application. It renders

  * a header showing a logo and a title as well as additional header items which can be defined by the project.

  * a sidebar showing the views assigned to the region "SIDEBAR"

  * a content part showing the views assigned to the region "CONTENT"

##### Header

The application frame contains a header which by default shows the title of
the application. It can be adapted by the following props:

  * `logoURL`: The URL to the image which should be shown as logo.

  * `additionalHeaderItems`: Additional header items, defined by a react component and an orientation.

##### Main Menu

The application frame contains the main menu. In order to customize this
aspect a custom main menu component can be provided to the application frame
via its `mainMenuComponent` property. Additionally, the main menu button, that
is rendered in mobile mode, can be customized by providing a custom button
component in the `widgetMap` property.

    
    
    import { ButtonProps } from "@com.mgmtp.a12.widgets/widgets-core/lib/button/main/button.api";
    
    interface PropsType {
      readonly mobileMode: boolean;
      readonly expanded: boolean;
      onMenuItemClick(): void;
    }
    
    function CustomMainMenuComponent(props: PropsType): JSX.Element {
      return <React.Fragment />;
    }
    
    function CustomMainMenuButtonComponent(props: ButtonProps): JSX.Element {
      return <React.Fragment />;
    }
    
    <FrameViews.ApplicationFrameLayout
      {...layoutProps}
      mainMenuComponent={CustomMainMenuComponent}
      widgetMap={{mainMenuButtonComponent: CustomMainMenuButtonComponent}}
    />

__ |  In order to insure correct behavior it is necessary to call `onMenuItemClick` on every menu entry click if a change should occur!  
---|---  
  
###### Mobile Navigation

Mobile Navigation is a build-in feature of the `ApplicationFrameLayout` that
is active by default. It enhances the user experience on mobile devices by
using the available screen space in a more efficient way.

More details are available in Section 4.21.

###### MainMenuContext

On a mobile device the main menu is shown as a sliding menu. It can be toggled
by the user via touching the "hamburger" button shown in the mobile header.

The `ApplicationFrameLayout` wraps its content into the provider of the
`MainMenuContext` in order to allow toggling the menu in a programmatic way.
This React context provides props to get and set the current expansion state
of the mobile main menu. This way a custom component can use the context
anywhere within the application via its Consumer to toggle the mobile main
menu.

A use case is a button in the mobile application header which starts a new
activity and at the same time closes the mobile menu to prevent that the view
of the new activity is hidden from the user.

##### SidebarContext

The ApplicationFrame wraps a React context around the Sidebar region, with
which the current state of the sidebar (collapsed or expanded, minimized or
maximized) can be retrieved and set. Please refer to the [API documentation of
`FrameViews.SidebarContext`](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-bundle/typedoc/modules/core_frame.frameviews-1.html) for more
information.

##### Layout Settings

The `ApplicationModel` contains the following `ApplicationFrame` settings
which can be used to configure the `ApplicationFrame`:

  * disableCollapsingSub: Used to hide the button for triggering the collapsing and expanding of the sidebar

  * initialSubExpanded: Used to set the initial expansion state of the sidebar.

  * initialSubExpandedState: Used to set the initial size of the sidebar.

Please refer to the [API documentation of
`ApplicationModel.ApplicationFrame.Settings`](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-
bundle/typedoc/interfaces/core_model.applicationmodel-1.applicationframe.settings.html)
for more information about these properties.

#### 4.5.4. Stack

Views are "stacked" on top of each other, i.e. only the latest view is
visible. Useful for modals.

#### 4.5.5. Null

All views are rendered without any layout next to each other in the DOM. Use
if you want to output all views without any additional markup.

#### 4.5.6. Custom Layouts

You can define your own layouts by returning them in a custom
`LayoutProvider`. Then you can use them by referencing them in the Application
Model.

Use the same approach to define a custom logo, login image, or version.
Example:

    
    
    import * as React from "react";
    
    import {
      FrameFactories,
      FrameViews
    } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    
    export const customLayoutProvider: FrameViews.LayoutProvider = name => {
      return name === "ApplicationFrame"
        ? { component: CustomAppFrameLayout }
        : FrameFactories.layoutProvider(name);
    };
    
    function CustomAppFrameLayout(
      props: FrameViews.ApplicationFrameLayoutProps
    ): JSX.Element {
      return (
        <FrameViews.ApplicationFrameLayout
          {...props}
          logoURL="/images/my_logo.svg"
        />
      );
    }

You could even implement a fully custom layout component, layouting the view
components as you wish. See the following example:

    
    
    import * as React from "react";
    
    import {
      FrameFactories,
      FrameViews
    } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { LayoutGrid } from "@com.mgmtp.a12.widgets/widgets-core/lib/layout/layout-grid/main/layout-grid.view";
    
    export const customLayoutProvider: FrameViews.LayoutProvider = name => {
      return name === "CustomGridLayout"
        ? { component: CustomGridLayout }
        : FrameFactories.layoutProvider(name);
    };
    
    function CustomGridLayout(props: FrameViews.LayoutProps): JSX.Element {
      const viewComponents = props.views.map(view => props.viewProvider(view.name));
      return (
        <LayoutGrid.Grid>
          <LayoutGrid.Row>
            <LayoutGrid.Column size={{ lg: 12, md: 12, sm: 12 }}>
              {viewComponents[0]}
            </LayoutGrid.Column>
          </LayoutGrid.Row>
          <LayoutGrid.Row>
            <LayoutGrid.Column size={{ lg: 6, md: 6, sm: 6 }}>
              {viewComponents[1]}
            </LayoutGrid.Column>
            <LayoutGrid.Column size={{ lg: 6, md: 6, sm: 6 }}>
              {viewComponents[2]}
            </LayoutGrid.Column>
          </LayoutGrid.Row>
        </LayoutGrid.Grid>
      );
    }

#### 4.5.7. Progress Indication

Every layout renders a progress indicating React component wrapping each view
component. This component is provided by a _Progress Component Provider_.

The default provider can be obtained by using
`FrameFactories.createProgressComponentProvider()`. It delivers a
`ProgressIndicator` widget showing a progress spinner if the flag "busy" of
the default data holder of the related activity is true. This behavior can be
extended by providing additional predicates to the factory function, that
determine when the `ProgressIndicator` is shown. In addition it is also
possible to provide settings by the global UI settings (see Section 4.1.2).

If a different behavior is desired, it is always possible to provide your own
custom progress component provider.

##### Conditionally hide Progress Indicator

To conditionally show or hide the progress indicator from inside the view
component, set `handleProgressIndicator` on the view component. If this flag
is set to `true`, the progress component will be passed to your view
component, where you can show or hide it based on your custom condition.
Example:

For functional components

    
    
    function ConditionalProgressComponent(props: View): JSX.Element {
      const customCondition = true;
      const ViewContent = <div>COMPLEX VIEW COMPONENT</div>;
    
      return props.ProgressComponent && customCondition ? (
        <props.ProgressComponent activity={props.activity}>
          {ViewContent}
        </props.ProgressComponent>
      ) : (
        ViewContent
      );
    }
    
    ConditionalProgressComponent.handleProgressIndicator = true;

For class components

    
    
    class ConditionalProgressComponentClass extends React.Component<View> {
      static handleProgressIndicator = true;
    
      render(): React.ReactNode {
        const customCondition = true;
        const ViewContent = <div>COMPLEX VIEW COMPONENT</div>;
    
        return this.props.ProgressComponent && customCondition ? (
          <this.props.ProgressComponent activity={this.props.activity}>
            {ViewContent}
          </this.props.ProgressComponent>
        ) : (
          ViewContent
        );
      }
    }

Here, the view component provider will set `handleProgressIndicator` only for
the `ConditionalProgress` components, while keeping the default behaviour for
all other components.

__ |  In order to achieve this behaviour when using your own custom layout, you need check for this flag and either wrap your ViewComponent inside of the ProgressComponent (if `false` or not set) or pass it to the ViewComponent as the prop `ProgressComponent`  
---|---  
  
#### 4.5.8. Error Boundaries

Every layout renders an error boundary component wrapping each view component.
Error boundaries are React components that catch JavaScript errors anywhere in
their child component tree, log those errors, and display a fallback UI
instead of the component tree that crashed. Error boundaries catch errors
during rendering, in lifecycle methods, and in constructors of the whole tree
below them.

The error boundary component is provided by an _Error Boundary Provider_. The
default provider `FrameFactories.errorBoundaryProvider` delivers an
`ErrorBoundary` with a default fallback component. This fallback shows a
component with detailed information about the error and a button to cancel the
current activity.

The provider mechanism allows to replace the default error boundary component
for specific views or regions. It is also possible to use the default error
boundary component, but only replace the error boundary fallback component. An
example can be found in the sample application **Error Handling**  __**Error
Boundaries**.

### 4.6. CRUD

The Client provides components to specifically resemble the
[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) UI of
the A12 Form Application. In combination with the Platform Server Connectors
and the A12 Form Application Server, the full CRUD functionality of the Form
Application can be achieved only via A12 Models and without writing any code.

This extension is useful for analysts / modelers during development phase. It
is totally OK to use it in production **as long as it is used as a drop-in
component without any customizing**.

The components which are provided to resemble the CRUD UI are:

  * The Overview-Engine CRUD view from the CRUD extension

  * The Form-Engine view from the form-engine extension

  * CRUD Sagas and a CRUD Middleware from the CRUD extension

The Overview-Engine view is already connected to the store and is pre-
configured for the CRUD functionality. It needs the CRUD Sagas to be
registered in the application setup, which provide CRUD specific Redux backend
functionality.

The Form-Engine view is also provided as a connected component. It requires
the CRUD middleware to be registered in the application setup in order to
provide the CRUD functionality.

For the basic Form-Engine functionality, a middleware, a saga and special
reducers need to be registered in the application setup. See the chapter about
the Form-Engine for more details.

The OverviewCRUD view handles via the CRUD sagas the following CRUD events
from the Overview Model:

  * **add:** Initiate an Activity to add a new document

  * **delete:** Delete the selected document

Clicking on an overview row triggers the default row action of selecting and
opening the document in the Form-Engine view. Custom default row actions are
not supported by the CRUD extension.

The Form-Engine view handles via the CRUD middleware the following CRUD events
from the Form Model:

  * **CRUD::SAVE:** Saves the current data of the Activity

  * **event_submit / event_save:** Commit the current Activity

  * **event_cancel:** Cancel the current Activity

The submit/save events will also trigger a _full validation_ in the A12 Form-
Engine. Note that the further behavior depends on the configured "Data
Providers, Data Loaders and Data Editors".

The CRUD Engines must be used together in order to work correctly.

#### 4.6.1. Customizing not supported

This extension combines a set of Client features to provide a functionality
which is mostly useful for analysts / modelers.

In case you need a different look or behavior, please use the components from
core/view or the form-engine extension for that purpose.

There you will also find constants for event names of the typical crud events
described above and we recommend to use those instead of hard coding the crud
event name strings into your custom component.

### 4.7. Localization

Localization in A12 is done by using the `Localizer`, which is accessible from
a `LocalizerContext` react context. This react context has to wrap all the
react components of the client application that need to localize any texts.
The client library does not create this context itself. The application code
has to add it to the react component tree itself. It is suggested to add this
context as one of the outermost react components of the application.

#### 4.7.1. Current Locale

The current locale is part of the application state and as such managed in the
Redux store. Defining an initial locale of the application is done by
dispatching the `LocaleActions.set` action with the wanted locale during the
setup phase. This can be achieved by adding this action to
`ApplicationFactories.createApplicationSetup`.

#### 4.7.2. Available Locales

The `core/configuration` API uses the entry `Locales` to provide a list of
available locales that is typically used to show a locale selection to the
user. If this entry is not provided, no locale selection will be shown.

#### 4.7.3. Localizer

The localizer is defined by the A12 localization API and represents the core
of it. Please refer the documentation of the `@com.mgmtp.a12.utils/utils-
localization` library for more in-depth information.

    
    
    export interface Localizer {
      (...localizable: Localizable[]): string | undefined;
    }

All A12-related localizations are covered by the default texts that the
`Localizable` objects can contain. I.e. any localizable that is created by
A12-internal logic will always bring the default translations for the English
and German locale. Additional texts to override or extend the A12-default
texts can be passed to e.g. the `defaultLocalizerFactory` when creating an
application-specific `Localizer` function. Please refer to documentation of
the `@com.mgmtp.a12.utils/utils-localization` library for more details on how
this can be achieved.

#### 4.7.4. Localization Keys

The main identification aspect of localizables are the localization keys.
Every `Localizable` that is provided to a localizer must have a localization
key! How the different localization keys are generated depends on their
producer. Therefore, it may be necessary to read the documentation of other
components like Form-Engine and Overview-Engine.

##### Static Resources

For static resources the keys are provided by the constant
`LOCALE_RESOURCE_KEYS` which is located in `core/locale`. This constant
provides the keys as well as the documentation of their usage. For extensions
similar constants exist and are provided by the extensions. Please consult the
documentation of the extensions for more details.

##### Application Model

Please note that you can also provide localization texts directly in the
application model. Every entry is localizable by providing different texts in
a map. The key is hereby the string representation of the `Locale` object.

###### Menu Entries

The key of each menu entry has the pattern `application-model.{application-
model-name}.{module-name}.{menu-name}\(.{sub-menu-name})`* .

###### Cases

The key of each case has the pattern `application-model.{application-model-
name}.{module-name}.{flow-name}.{scene-name}.{case-name}`.

#### 4.7.5. Single Locale Setup

In order to setup the Client with a single locale that is not the default
`en_US`, you have to set the current locale in the Redux store to the desired
locale, e.g. `fr_FR`.

__ |  The Client only provides default texts and configurations for `en` and `de`. For every other locale it is necessary to provide the necessary texts and configurations. This can be achieved by providing the texts in the models (form, overview, document, and application) or by using the A12 localization API.  
---|---  
  
#### 4.7.6. Hidden Accessibility Texts

For the localization of hidden accessibility texts, we rely on the Widgets. In
order to provide your custom localization you have to use the
`A11YLanguageContext` component, which is provided by Widgets. This component
should be used next to the `Provider` component from React-Redux. Please see
the accessibility section in the Widgets documentation for more details.

### 4.8. Modularization

The ModuleRegistry is an API to enable modularization of Client projects. The
API offers extension points to implement dynamic modules in the Client Redux
context. This is not part of the Client template at the moment, neither are
packaging and loading of modules as the build of the client is considered as
project specific. This documentation shows how a modularized Client project
can look like.

#### 4.8.1. Motivation

Modularization is a common requirement in web projects regarding different
aspects:

  * Architecture

    * Clear dependency management

    * Clear relation between frontend and backend code

    * Loose coupling of BE modules

    * API for portal / cross-functionality

  * Infrastructure

    * Possibility to separately release a module (not by default)

    * Possibility to separately deploy a module (not by default)

  * Organization

    * Modules can be developed by another supplier

    * Modules can be easily switched off or de-activated

Different but related aspects are:

  * Keep JS modules in the browser cache for offline usage

  * Partial loading of modules - modules which are not used are not loaded

  * Delta updates in production in order to limit bandwidth

#### 4.8.2. ModuleRegistry

To be able to build up a single page Client application by modules
dynamically, the base or core application itself is not allowed to know the
concrete modules. The modules have to register themselves to any part of the
architecture they want to participate in.

Therefore, the Client architecture provides a central `ModuleRegistry` to add,
remove or retrieve modules. More information about the api can be found in the
respective [API documentation of Module
Registry](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-bundle/typedoc/interfaces/core_application.moduleregistry.html).

To implement a module the API offers different extension points like reducers,
views, sagas, etc. The Client uses the OSGI whiteboard pattern to integrate
the modules: The extension points use a provider to ask all the modules for
specific functions. To enable dynamic implementations of these interfaces,
access to the Redux state is needed.

Modules have to return an unique id. Everything else is optional.

__ |  Module definitions should not interfere and interact with each other to prevent any execution order issue because the execution order is not ensured. This especially applies to fallback solutions for data providers, data editors and data reducers because they prevent the executions of others that are later in the execution chain. Therefore, it is highly recommended that every fallback logic for preventing fatal error should be done in the global definition.  
---|---  
  
The `ModuleRegistry` can be accessed by the `ModuleRegistryProvider`
namespace.

    
    
    export namespace ModuleRegistryProvider {
      export function getInstance(): ModuleRegistry {
        // ...
    
    
      }
    
      export function getViewProvider(
        state: object,
        fallback: View.Provider
      ): View.Provider {
        // ...
    
    
      }
    }

The `ModuleRegistryProvider` also offers the `getViewProvider` function which
can be used in a `RegionUi` to set the `viewProvider` as this an extension
point outside the Client core.

#### 4.8.3. Using the API

To register a module we first need to implement the `Module` interface

    
    
    export const myModule: Module = {
      id: "my-module",
    
      model(state: object): ApplicationModel {
        return myModuleAppModel;
      },
    
      views(
        state: object
      ): (componentName: string) => React.ComponentType<View> | undefined {
        return MyModuleFactories.createRenderer;
      },
    
      middlewares(store: object): Middleware[] {
        return [MyModuleFactories.createCRUDMiddleware()];
      },
    
      reducersMap(state: object): ReducersMapObject {
        return {
          slice1: MyModuleReducers1.slice1,
          slice2: combineReducers({
            slice2_1: MyModuleReducers2.slice2_1
            // ...
          })
        };
      },
    
      sagas(state: object): (() => SagaIterator<void>)[] {
        return [];
      }
    };

Then the module can be registered before or after bootstrapping the Client
Application by `ApplicationSetup`.

    
    
    // Load the moduleAppModel before
    ModuleRegistryProvider.getInstance().addModule(myModule);
    
    const model: ApplicationModel = {
      header: {
        id: "base-application-model",
        locales: [{ code: "en" }],
        modelType: "application",
        modelVersion: "4.0.0"
      },
      content: {
        region: {
          name: "APP",
          layout: { name: "ApplicationFrame" },
          subRegions: [{ name: "CONTENT", layout: { name: "MasterDetail" } }]
        },
        defaultRegion: ["CONTENT"],
        modules: [
          /* Add your flows and scenes here */
        ]
      }
    };
    
    const config: ApplicationSetup = ApplicationFactories.createApplicationSetup({
      model,
      modelLoaders: [],
      dataHandlers: emptyDataHub,
      additionalMiddlewares: []
    });

As you can see we still need to define the application model, the modules
model will be added at runtime. Special care must be taken when removing
modules at runtime and it should be avoided, if possible. If there is an
active View in a module, removing the module will lead to an Error.

If you remove a module at runtime you are responsible for consistency. For
example you may have to stop running sagas or middleware that are doing
processing in the background, or you have to remove state from the store.

#### 4.8.4. Implementing custom extension points

The given extension points may not fit your needs completely, but with the API
it is quite simple to implement new ones on top of it.

In the example we see a `MyAbstractModule` which is the base class for every
project module that offers the new extension `getModuleSpecificRenderer`. The
`MyModuleExtensions.getRenderer()` function provides a renderer to render a
central component that includes module specific parts:

    
    
    export abstract class MyAbstractModule implements Module {
      id = "myAbstractModule";
    
      // ...
    
      moduleSpecificRenderer(): (
        props: ModuleSpecificProps
      ) => JSX.Element | undefined {
        return props => undefined;
      }
    }
    
    export namespace MyModuleExtensions {
      export function getRenderer(): (props: ModuleSpecificProps) => JSX.Element {
        return props => {
          for (const module of ModuleRegistryProvider.getInstance().getAllModules()) {
            if (module instanceof MyAbstractModule) {
              const result = module.moduleSpecificRenderer()(props);
              if (result) {
                return result;
              }
            }
          }
          return <div>{/* ... default View */}</div>;
        };
      }
    }

#### 4.8.5. Modules and the Main Menu

The default main menu of the Client creates one menu item per (App Model)
menu, and the order of the menu items is the same as the appearance / order of
registration in the App Model. When using Modularization, this might not fit
your needs. In this case, please integrate a custom menu component using the
App Frame's mainMenuComponent API.

### 4.9. Dirty Handling

This extension consists of a Dirty Handling saga and a VetoDialog, which can
be wrapped around the application.

The saga can be used instead of the default cancelRequestedHandling saga, to
handle the CANCEL_REQUESTED action.

The CANCEL_REQUESTED action contains in its payload an array of activity ids
and will cancel these activities if they are not dirty or locked. For
evaluating the dirty state the saga takes all data holders of the activity
into account. An activity is dirty if one of the data holders is dirty.

If an activity is dirty or locked, a SET_CANCEL_CONFIRMATION_REQUIRED action
with cancelConfirmationRequired=true is dispatched. The saga then waits until
a RESPONSE_CANCEL_CONFIRMATION action is dispatched. This action contains in
its payload the information about if there was a veto for the cancellation. If
there was no veto the activity gets cancelled by the dirty handling saga. If
there was a veto the activity does not get cancelled and the whole cancelling
process gets aborted.

If all activities got cancelled the Dirty Handling saga dispatches in the end
the RESPONSE_CANCEL_REQUESTED action which contains the payload
"cancelled=true". If not all activities got cancelled, because there was a
veto, the saga dispatches the RESPONSE_CANCEL_REQUESTED action which contains
the payload "cancelled=false". The caller can use the ActivitySaga
`waitForResponseCancelRequested` to wait for the response of the
cancelProcess.

Example usage:

    
    
    const activityIdsWhichShouldBeCancelled = ["A", "B"];
    
    yield put(ActivityActions.cancelRequest({activityIds: activityIdsWhichShouldBeCancelled }));
    
    // wait for the process to finish and take the response
    const cancelled: boolean = yield call(ActivitySagas.waitForResponseCancelRequested);
    
    if(cancelled){
      // all activities where cancelled
    } else {
      // not all activities where cancelled
    }

If the VetoDialog is used, it will listen to any state change and show a
dialog, if there is an activity with "cancelConfirmationRequired=true" . The
dialog offers two options: "Discard changes" and "Abort".

  * The first option dispatches a RESPONSE_CANCEL_CONFIRMATION action with veto=false.

  * The second option dispatches a RESPONSE_CANCEL_CONFIRMATION action with veto=true.

If you do not use the VetoDialog, you have to take care of dispatching a
RESPONSE_CANCEL_CONFIRMATION action, if there are activities which need a
cancelConfirmation, yourself.

### 4.10. Notifications

The `core/notification` API can be used to notify the user about arbitrary
events.

In order to visualize notifications, it is mandatory to wrap the application's
root component with a suitable React component to visualize notifications. The
`core/notification` API provides a default frame component. Without such a
component no notification is shown to the user.

Notifications can be created by dispatching the notification action "add" and
removed again by the corresponding "remove" action.

Notifications can be bound to activities by providing the corresponding
activity id to the notification. Activity bounded notifications will be
removed automatically if the bounded activity is removed by either committing
or canceling. If no activity id is provided then the notification is treated
as a global notification and will not be removed on removing any activity.

Currently, notifications by default are shown as toast messages following the
function and design of the A12 Toast Widget. They can be customized in their
message, position, duration, color, and other options via the properties of
the notification object, that needs to be given to the "add" action as
payload.

It is also possible to create completely custom notifications by providing the
notification frame with a notification renderer, that would return the custom
notification view.

#### 4.10.1. Mobile

On mobile the position is not customizable due to the small available space.
Therefore, only the newest notification is shown on the bottom of the screen.

### 4.11. Static Pages

The static pages extension can be used to include content like contact
information or help pages, that is only loaded on-demand.

Note: Technically, the content is defined as a React component using Widgets.
This makes it very easy to create a consistent look and feel and due to JSX
the resulting source-code is very similar to static HTML.

The extension consists of two parts:

  * **createViewProvider:** A function to create a ready-to-use _View Factory_ \- a provider for the React view components to render static pages

  * **createExternalViewProvider:** A function to create a factory for React view components _by static page name_ , that will fetch the content of the static page via HTTP

The component created by `createExternalViewProvider` will load the code and
create the React component using the naming scheme `"{baseUrl}/{page}.js"`.
_baseUrl_ defaults to "static" and can be set to a different value by using
the respective parameter of the function. _page_ is read from the activity
descriptor property "page" (ultimately derived from the application model).

__ |  To allow static page components to be lazy loaded, the `eval` function is used. `eval` is a potentially dangerous function, as it interprets a given string as JavaScript. In combination with a [Content-Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP), the directive `unsafe-eval` needs to be specified to explicitly allow this feature. This is because `eval` is disabled by default, which essentially breaks this extension feature. If your application uses a CSP which disallows the usage of `eval`, the "static pages" extension can not be used. To remedy that, write your static page components as regular react components instead. This is possible because the main difference between those two is the lazy loading behaviour of static pages.  
---|---  
  
In order to use a different factory for React view components, you can pass it
as an argument to `createViewProvider`.

You can find an example of how to use it in the Tutorials: Adding Static Page.

### 4.12. Deep Linking

The deep linking extension helps to implement URL based (activity) state
restoration, e.g. when a user wants to share a deep link into the application.
Whenever a (relevant) state changes, the encoder is called to update the
location part of the URL. When loading the application, the decoder is called
to restore activity state based on the URL location.

To register this extension you need to call `DeepLinkingFactories.createSagas`
and pass the returned sagas to the `customSagas` property of the
`ApplicationFactories.createApplicationSetup` function.

#### 4.12.1. Default Codec

The extension includes a default codec, that uses the descriptor of the latest
activity. This means that other state of the activity or even other activities
will not be recovered, so the scene might not look the same as at the time of
encoding.

#### 4.12.2. Setup

##### URL Encoding

Registering the sagas is already enough to activate the encoding of the last
started activity into the URL with the default codec.

##### Activity Restoration

To restore the activity encoded in the URL when the app is loading, you need
to setup an action which serves as a trigger for the restoration to be
started.

First, you have to dispatch this action after the initialization code of the
app was executed. This could be e.g. before the first render of the app or
after the user logged in successfully.

Second, the action also needs to be added to the array of apply triggers in
the deep linking sagas configuration. You can hand in the configuration object
to the `DeepLinkingFactories.createSagas` factory function in your app setup.

#### 4.12.3. Configuration

To further customize this extension you can pass more options to the
`DeepLinkingFactories.createSagas` function via the configuration object. This
configuration contains:

  * **updateTriggers** : A list of actions for which the deep link should be updated

  * **applyTriggers** : A list of actions for which the deep link should be applied

If no action is given in `applyTriggers` the deep link will never be applied.
If the `Activity` encoded in the URL is not found, the default page will be
loaded if configured (see Welcome Page).

  * **clearTriggers** : A list of action for which the deep link should be cleared

  * **loadingTimeout** : The time that is waited for the data of a data source activity to be loaded. When it expires and the data is not loaded, the to-be-restored activity will not be created.

#### 4.12.4. Customization

There are other properties in the configuration object which can be used to
replace default implementations:

  * **deepLinkCoder** : Users can provide their own implementation of `DeepLinkCoder`, which decides, what information is encoded in the URL, and how this is done. The default implementation only uses information stored in the `ActivityDescriptor`.

  * **locationManager** : A custom location manager can be provided which allows customizing the handling of the location part of the url. The default implementation only manages setting the '#' character before the location part.

#### 4.12.5. Limitations

__ |  This feature is not meant to provide full URL based navigation through the application (routing). Client applications usually run multiple, nested Activities, but by default only the latest is restored.  
---|---  
  
The URL changes are not saved in the browser history and therefore it is not
possible to navigate to a previous or later `Activity` with the browser
navigation buttons.

It is not sufficient to just change the link in the address bar of a web
browser. The link needs to be opened.

Deep links currently do not work when used in combination with the priorScene
property of Scenes (see Arrange UIs).

#### 4.12.6. Welcome Page

To set a default starting page ("welcome page"), you need to set the property
`initialActivity` in your appmopdel. This contains the descriptor of the
activity that will open as your starting/welcome activity. Additionally, you
need to configure at least one action which indicates that this activity
should be loaded. To do that, you have two possiblities:

If you already configured the deep-linking extension as described above, the
saga that listens to `applyTriggers` will load the activity described by the
`initialActivity` property of your appmodel, when one of these actions gets
dispatched and when the current url does not contain a deep link.

If the appmodel does not contain an `initialActivity` property and the current
url does not contain a deep link, the saga will do nothing.

If you don't want to use the deep-linking functionality, you need to call
`DeepLinkingFactories.loadWelcomePage` and pass its returned saga to the
`customSagas` property of the `ApplicationFactories.createApplicationSetup`
function. Then you need to configure it by adding your action/actions to the
`applyTriggers` list, in the same way as described above.

The saga from `DeepLinkingFactories.loadWelcomePage` will listen for your
configured actions and create the activity described by the `initialActivity`
property of your appmodel.

If no `initialActivity` is set in the appmodel, the saga will do nothing.

Finally, to actually show the view component of your welcome page, you need to
define a scene in your app model matching the descriptor of the
`initialActivity` with its match conditions and which has a VIEW_ADD directive
with your welcome page view.

##### Modularization

If no `initialActivity` is set in the root appmodel and you add appmodels
using the `ModelActions.addModulesApplicationModels` action then the initial
activity is taken from the first appmodel defining one which is merged into
the root appmodel.

### 4.13. Model Graph

The Model Graph provides information about Models during runtime.

If you want to use Client features that require the Model Graph, you need to
load and set it.

You can load the Model Graph yourself from any place, but most probably you
want to use the respective A12 Services API to load it from an A12 Server. A
simple and safe occasion is immediately after the user logged in. Please refer
to the Services documentation for more information.

You can set the Model Graph using `ModelActions.setModelGraph`.

Until you set the Model Graph, an empty Model Graph will be assumed.

### 4.14. Heterogeneity

Heterogeneity is an experimental feature in A12 that allows the handling of
sets of Documents of different types.

For more information about the underlying concepts, please see the
[Heterogeneity Concepts](https://wiki.mgm-tp.com/confluence/x/9AvhBw) Wiki
page (mgm internal only).

__ |  Of the Heterogeneity features envisioned in the above concept, only a small subset has been implemented. This documentation is only about how to use the currently available functionality in the Client.  
---|---  
  
First, the involved parts are described. Then it is shown how to create a
setup using the commerce sample domain.

In the following, the terms _Type_ and _Document Model_ are used synonymously.
However, they serve different purposes. _Document Model_ is the well-known way
in which the inner structure of Documents are defined. _Type_ is a new way to
describe Dependencies between entities without caring about their inner
structure. Types "live" inside the Model Graph.

#### 4.14.1. Subtype Dependency

The Subtype Dependency declares an "is a" relationship from one Document Model
to another. The intention is to instantiate and process Documents which have
an "is a" relationship in a uniform way.

__ |  The Subtype Dependency only declares the relationship. It does **not** imply or even require inheritance of fields/groups/rules. If your business logic requires inheritance, then you have to ensure it yourself, e.g. by using includes or copying fields/groups/rules.  
---|---  
  
You declare a Subtype Dependency by adding an Annotation with name `subTypes`
to the metadata section of the supertype. The value of the Annotation is a
comma separated list of the names of the subtypes.

The following concepts are **not** implemented in the current version:

  * Multiple Inheritance

  * Metadata on subtypes (e.g. to filter subtypes)

#### 4.14.2. Model Graph Loading

With the introduction of heterogeneity, every Client holds a Model Graph
inside its state.

To use heterogeneity, you must load and set the Model Graph.

#### 4.14.3. Heterogeneous Overviews

To list a heterogeneous set of Documents, you can assign the common super type
as the Document Model of the Overview Model. The A12 Server will then take all
Documents of that super type and all sub types into account.

#### 4.14.4. Creating new Documents

In heterogeneous overview, newly created Documents can be of different types.

The CRUD extension detects that the type associated with the Overview Model
has sub types. It then displays a dialog to select the type of the new
Document. The offered types are the same as those used for heterogeneous
overviews.

#### 4.14.5. Document Model-Dependent Forms

When editing a Document from a heterogeneous set, you probably want to define
a single Application Model Scene, but still use different forms for Documents
of different types.

In order to achieve this, you need to limit the usage of a Form Model to a
specific Document type. This can be done by adding a Document Model constraint
to the referenced Form Model in the respective Scene of the Application Model.

Limitations:

  * For each Document type, you must provide a Form Model entry, except if all Document types should share the same Form Model - then you must only provide exactly one Form Model without Document Model.

  * All declared Form Models are loaded on the first usage of the Scene. This can be slow the first time if you have many Sub Types.

#### 4.14.6. Example Setup (Simple CRUD)

The following section describes the necessary changes to make use of
heterogeneity in the A12 sample domain "commerce". You can find the full,
working setup in the Relationships example of the Client Sample Application.

It is a simple setup that makes use of the CRUD component, which contains pre-
configured versions of the heterogeneity building blocks.

__ |  You can find all models in the source code of the Client Sample Application in the folder `core/resources/models/`.  
---|---  
  
##### Modeling

  * In the Document Model `DomainProduct`, set `DomainBundle` as subtype.

  * Setup a Scene using the Overview Model `Product-overview` and the view `OverviewCRUD`.

  * Setup a Scene using the Form Models `Product` and `Brand` (constrained to the respective type) and the view `RelationshipFormEngine`.

##### Application Setup

  * Set the Model Graph. See Model Graph documentation on how to do it.

#### 4.14.7. Example Setup (Detailed)

In order to tailor the heterogeneity functionality to project specific needs,
you can combine the provided building blocks, or replace them with your own
implementation.

All modeling in Document or Application models is done exactly in the same way
as described in the CRUD example above. Therefore, here, only the coding API
is explained.

The currently available building blocks are:

  * Variant selection mapper: a function that maps given types to a tree of selection options

  * Variant selection UI: a component to render an UI to select a type for given selection options

__ |  You can find the fully working example in the source code of the Client Sample Application in the folder `core/src/sample-application/src/modules/data_handling/heterogeneity` of the client repository.  
---|---  
  
##### Variant selection mapper

The provided default variant selection mapper is a function that accepts a
single root type and creates a tree of selection options from it.

The root type defines, which part of the type hierarchy you want to render.

The resulting tree defines the available options, if they are abstract or
concrete, as well as their nesting, order, and labels.

You can pass the result of the mapping to the default variant selection React
component to render a selection UI.

The provided callback of the default selection UI will be invoked with the
name of the selected type, which can then be used to e.g. start a new
Activity.

__ |  When starting a new Activity for a heterogeneous Scene containing Engines, make sure to set the _model_ property in the Descriptor. The Client needs it to pick the right Engine models.  
---|---  
      
    
    const localizer = React.useContext(LocalizerContext).localizer;
    
    const myStartingType = modelGraph.documentModels.find(
      dm => dm.modelId === "MyModel"
    )!;
    
    const options = defaultVariantSelectionMapper(
      modelGraph,
      localizer
    )(myStartingType);
    
    return <VariantSelection variants={options} onSelect={handleSelection} />;

In order to change the enablement, nesting, order or labels of types, you can
replace/compose the default mapper.

In order to change the rendering, you can replace/compose the default React
component.

### 4.15. Relationships

The _Relationship_ extension allows users to manage relationships between
document models in the Client.

A general documentation describing the basic concepts of the Relationship
feature can be found in the mgm A12 overall documentation.

How to integrate the extension into the Client step-by-step is described in a
separate tutorial.

#### 4.15.1. Relationship Engine

The Relationship Engine visualizes links and candidates of a relationship
according to the configuration of the Relationship UI configuration.

##### Relationship UI configuration

The Relationship UI configuration is the melting pot of all models and UI
components used to display a relationship. A typical model looks like the
following:

    
    
    {
      "name": "ProductBrand-UiConfig-1",
      "metaInformation": {
        "version": "1.0.0"
      },
      "relationshipName": "ProductBrand",
      "targetRole": "Brand",
      "components": [
        {
          "id": "1",
          "name": "DropDownSelection",
          "models": [
            {
              "modelType": "overview",
              "name": "ProductBrand-Brand-LinkOverview",
              "use": "link"
            },
            {
              "modelType": "overview",
              "name": "BrandLink-overview",
              "use": "candidate"
            },
            {
              "modelType": "form",
              "name": "ProductBrand-LinkForm",
              "use": "link"
            }
          ]
        }
      ]
    }

It consists of..

  * a unique name

  * the name of the referenced Relationship model

  * the side of the relationship which shall be displayed (called "target role")

  * a list of component configurations used to visualize the relationship

Each component configuration contains..

  * a unique component ID

  * the ID of the View which shall be rendered (see Views)

  * a list of models which are required to render the view

  * additional properties which may be required by individual views

In general only the first component of the list is rendered by the Engine, but
individual views allow a reference to another component (see Table List as an
example).

#### 4.15.2. Views

A relationship can be displayed in several variants. Four views are provided
by default, but projects can define their own UI.

Every default view requires an overview model for links and an overview model
for candidates since the related documents are based on different result
document models.

##### Drop Down Selection

A drop down selection allows the selection of a single link. Candidates are
displayed in a drop down list, the selected link is shown in the input field.

To provide a better modeling experience we have decided to reuse overview
models for this component. The field value of the first overview column is
used to display the link / candidate document.

![Drop Down
Selection](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/9a10d6b7ea36dbe2d27b875d6d2baa3b/drop_down.png)

Use `"name": "DropDownSelection"` in the UI configuration to present your
relationship like this. The view requires the following models:

modelType | use | Description  
---|---|---  
"overview" | "link" | Overview Model to display link documents (the field value of the first overview column is used)  
"overview" | "candidate" | Overview Model to display candidate documents (the field value of the first overview column is used)  
"form" | "link" | Form Model describing the form used to modify the link document. The form is shown when adding new links or by pressing the edit button. If no link document model is specified for the relationship, this form model is not required. Please bind this view to a form control when using the Form Engine integration.  
  
##### Dual Pane Selection

With the dual pane selection users can manage multiple links for a document.
All candidates are shown on the left, links are shown on the right side. Added
links are highlighted green, removed links red. As soon as the changes are
saved, the highlighting will be cleared.

The list of candidates can be filtered, sorted and paginated. This is not
possible for the link table at the moment. Furthermore, it's not possible to
add custom row actions to the overview tables and the content box cannot be
customized using the overview model.

![Dual Pane
Selection](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/b0fc086128eac585ea6c26edee87eef1/dual_pane.png)

Use `"name": "DualPaneSelection"` in the UI configuration to present your
relationship like this. The view requires the following models:

modelType: | use: | Description  
---|---|---  
"overview" | "link" | Overview Model to display link documents  
"overview" | "candidate" | Overview Model to display candidate documents  
"form" | "link" | Form Model describing the form used to modify the link document. The form is shown when adding new links or by pressing the edit button. If no link document model is specified for the relationship, this form model is not required. Please bind this view to a form section when using the Form Engine integration.  
  
##### Quadro Pane Selection

The quadro pane selection provides the same functionality as the dual pane
selection. The main difference is that added, removed and already saved links
are displayed in different tables.

It has been introduced to show the still experimental capabilities to provide
custom UI views handling the same features in a different view. **For this
reason it should not be used in productive applications.**

![Quadro Pane
Selection](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/13bfa7012d30fdcc1572f5833fe87cbf/quadro_pane.png)

Use `"name": "QuadroPaneSelection"` in the UI configuration to present your
relationship like this. The view requires the following models:

modelType | use | Description  
---|---|---  
"overview" | "link" | Overview Model to display link documents  
"overview" | "candidate" | Overview Model to display candidate documents  
"form" | "link" | Form Model describing the form used to modify the link document. The form is shown when adding new links or by pressing the edit button. If no link document model is specified for the relationship, this form model is not required. Please bind this view to a form section when using the Form Engine integration.  
  
##### Table List

Some use cases may focus on a plain table listing the links without modifying
them directly. The table list can be used for these scenarios.

Use `"name": "TableList"` in the UI configuration to present your relationship
like this. The view requires the following models:

modelType | use | Description  
---|---|---  
"overview" | "link" | Overview Model to display link documents  
"overview" | "candidate" | Overview Model to display candidate documents  
  
For the table list an additional property "editComponent" can be specified in
the "props" section of the component configuration. If another component
configuration in the Relationship UI configuration exists with the ID given in
the properties value, an edit button is displayed. When the button is clicked,
the referenced edit component is displayed.

As an example, the following Relationship UI configuration …

    
    
    {
      "name": "ProductBrand-UiConfig-1",
      "metaInformation": {
        "version": "1.0.0"
      },
      "relationshipName": "ProductBrand",
      "targetRole": "Product",
      "components": [
        {
          "id": "1",
          "name": "TableList",
          "models": [
            {
              "modelType": "overview",
              "name": "ProductBrand-Product-LinkOverview",
              "use": "link"
            },
            {
              "modelType": "overview",
              "name": "ProductLink-overview",
              "use": "candidate"
            }
          ],
          "props": {
            "editComponent": "2"
          }
        },
        {
          "id": "2",
          "name": "DualPaneSelection",
          "models": [
            {
              "modelType": "overview",
              "name": "ProductBrand-Product-LinkOverview",
              "use": "link"
            },
            {
              "modelType": "overview",
              "name": "ProductLink-overview",
              "use": "candidate"
            },
            {
              "modelType": "form",
              "name": "ProductBrand-LinkForm",
              "use": "link"
            }
          ],
          "candidatePageSize": 3
        }
      ]
    }

… will show a table list with edit button which will open a dual pane
selection ..

![Table List
Modal](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/dc2519f4ff9e2894576427a7f4409e6d/table_list_modal.png)

Sorting, Filtering and Paging the listed links is not supported in the default
table list.

Please bind this view to a form section when using the Form Engine
integration. === Custom UI (experimental)

In addition to the default views mentioned above, projects can provide their
own UI. To do so, they have to specify an own component provider as
Relationship Engine property. The provider receives a component configuration
and returns a React component providing one of the following interfaces:

  * **ListProps** \- Provides properties required to show links in a readonly list. Views should use this interface to provide a UI similar to the table list.

  * **SingleSelectionProps** \- Provides properties required to render a UI for the selection of a single link. Views should use this interface to provide a UI similar to the drop down selection.

  * **MultiSelectionProps** \- Provides properties required to render a UI for the selection of multiple links at the same time. Views should use this interface to provide a UI similar to the quadro or dual pane selection.

We consider customization of the components to be an experimental feature at
the moment.

###### Custom Localization

All labels rendered by components of the relationship extension can be
localized.

The extension comes with a localizer service, that can be created via a
factory. It has to be configured among the application's localizer services to
localize all multilingual texts defined in the relationship model and UI
configuration.

If a particular label shall be localized independently of the model
definition, the key can be overwritten by defining an own localizer service.
The following keys are available:

  * `relationship.ui-configuration.<name of the ui configuration>.<id of the custom component>.dual-pane.available-items.title` \- Title of the candidate table in Dual Pane

  * `relationship.ui-configuration.<name of the ui configuration>.<id of the custom component>.selected-items.title` \- Title of the link table in Dual Pane

  * `relationship.relationshipModel.<name of the relationship>.<name of the role>.displayLabel` \- The display label of a relationship role

The localization keys of static texts, which are not defined by models, are
provided by the constant `RELATIONSHIP_RESOURCE_KEYS` which is located in
`extensions/relationship`. This constant provides the keys as well as the
documentation of their usage.

#### 4.15.3. Link Form

A link between entities can have its own properties, e.g. the amount of a
product in a bundle or the production site of a product for a brand.

Those properties need to be defined in a link document model and the
respective ui requires a link form model.

If the link form model is provided in the Relationship UI configuration, then
on creating a new link, a Form-Engine will be shown in a modal, where the user
can enter values for the link properties.

![Link Form
Modal](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/9b8b2e5a4ad1e2444a745b29739a7298/link_form_modal.png)

The shown Form-Engine has some limitations, as it cannot be customized via
props and engine options.

#### 4.15.4. Form-Engine integration

In most cases the Relationship Engine shall be integrated into a form. To do
so, a custom form model map (RelationshipFormModelMap) has to be used by the
Form-Engine view.

If the map finds a section or control having a matching binding configuration
of type "relationship", a relationship UI configuration is expected as
configuration. This model is used to render the Relationship Engine. The CRUD
Form Engine view supports this integration by default.

Please note that properties of the bound section / control defined in the form
model (e.g. a section title) are not considered by the Relationship Engine. If
you intend to use the section title to structure your screen, please wrap the
bound element with an additional section having the desired title.

#### 4.15.5. Model Overview

When modeling relationships a lot of models are involved. This section should
provide a short overview to put you back on track. As example we focus on the
Relationship between products and brands. In a brand form assigned products
shall be managed via a dual pane selection.

![Model Overview for
Relationships](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/4b918e517dc108737c95296a0cfd080c/model_overview.png)

Before the introduction of the Relationship feature it was possible to define:

  * A **document model** "Product" describing the properties of a product

  * A **form model** "Product Form" showing a form to enter the product properties

  * An **overview model** "Product Overview" showing products in a table

The same applies to brands.

It was not possible to model a connection between these entities.

From now on we can use a **Relationship Model** "ProductBrand" to define this
connection. In our example the model specifies that multiple products are
assigned to a brand and only one brand can be assigned to a product. If
additional fields shall be defined for this Relationship, another document
model "ProductBrand" can be referenced. It is called **" Link Document
Model"** in this context.

The dual pane selection requires two overview models - one to define the
candidate table (based on the "Product" document model) and one to define the
link table. Link result documents are a combination of fields defined in the
"Product" document model and fields defined in the **Link Document Model**. To
reference this combination in the overview model another document model is
required: The **Link Result Document Model**. It can be generated from the
platform server.

If a **Link Document Model** is referenced in the **Relationship Model** , an
additional form model is required for a form to modify the link document. It
is called "ProductBrand Form" in the overview above.

The **Relationship UI configuration** references the view, the used overview /
form models and the **Relationship Model** to show. To integrate the
relationship directly in the form, the Relationship UI configuration is
defined as a **binding configuration** in the "Brand Form" form model.

### 4.16. Accessibility Support

The Client allows creating applications with accessibility support.

To make the application accessible for a user who uses accessibility tools
like a screen reader, the application requires a clear hierarchical structure
which also is reflected in the application's html.

The user interface of a Client application is structured using regions which
are configured with layouts to display views and other ui components like
menus and headers.

The hierarchical structure within the UI and the underlying html is
established by using unambiguous html-tags like nav for navigation components
and by providing ARIA levels and the role "heading" to the headings and
specific roles to other building blocks of those ui components.

#### 4.16.1. ARIA in built-in Layouts

##### ApplicationFrameLayout

The ApplicationFrameLayout is typically used in the application's root region
to give the application its base structure. It provides an application header
and a main menu and it allows to orchestrate the content for a main content
region, a sidebar region, and a modal region.

The following aria configuration is applied:

  * the application header has the role "banner"

  * the main menu is build with a nav-tag as root html-element, marking it as a navigation for a screen reader

  * the main content view has the role "main", marking it as the application's main content

  * the side bar usually contains project specific custom content, making it a project responsibility to define an appropriate aria structure using nav-tags for a navigation, aria-levels for headings and suitable aria roles.

When the case feature of the Client is used and a navigation to the different
cases is displayed in the side bar, a nav-tag is used.

  * The modal region content again requires project specific configuration.

##### DashboardLayout

The DashboardLayout renders its views as tiles in a grid.

The aria structure is established by

  * rendering a hidden title with aria-level 1 and role "heading" above the tiles

  * handing aria-level 2 to the views in the tiles, so that the views can use this level for their headings.

##### MasterDetailLayout

The MasterDetailLayout allows rendering a list of views, with each view
depending on the previous one which creates a hierarchy of views.

Therefore it hands aria-levels in ascending order starting with 1 to its
visible views, so that the headings of these views can reflect that hierarchy.

##### StackRegionLayout

The StackRegionLayout can manage a list of views but will always only render
the last added one. This view will receive aria-level 1 for its heading.

#### 4.16.2. ARIA in built-in Components

##### Engines

The Engines provide views which render a ContentBox Widget with a title. The
title should be set for good accessibility. It can be defined in the
respective ui model. The title will receive the aria-level determined for the
view by the layout.

Further details about accessibility support of the engines can be found in the
respective engine documentation.

##### ErrorBoundary

When an error is thrown during rendering of a view, the built-in layouts
render the fallback component of the provided ErrorBoundary. It receives the
same aria-level as the view, so that it can be set to the fallback component's
title.

#### 4.16.3. ARIA in custom Layouts and Views

When you are creating custom layouts and views and have to fulfill the
requirement of good accessibility, we have the following recommendations:

##### Custom Layouts

  * The layout should hand aria-levels to its visible views which resemble the hierarchy in which these views stand to each other. Views having the same level in the application hierarchy should get the same aria-level. A view depending on a parent view should get a higher aria-level than that of the parent.

  * If the layout wraps its views in ErrorBoundary components, those should get the same aria-level as the wrapped view.

##### Custom Views

  * The html tag of the view's heading component should have the aria-level which was handed to the view, and the role "heading". This way the heading will integrate into the application's aria heading hierarchy.

  * For a good accessibility structure make sure your custom view has a heading. If you want to make the heading invisible but still accessible for screen readers, you can use the plasma style helper class "-u-unseenButRead" or style your header accordingly.

  * Please do not use aria-level for sub headings inside the view. Only the view's top heading, e.g. the content box title, should have an aria-level.

  * To structure the content of your view use roles on the html containers, e.g. "form" for content with input fields, "document" for text, "heading" for sub headings. Nesting such containers with roles makes the structure transparent for screen readers.

  * Please do not use h-tags for sub headings, since this interferes with the hierarchy created by the aria-levels. Instead use styled div tags with the role "heading".

  * Use a nav-tag as root tag for navigation components or use the role "navigation".

#### 4.16.4. Focus handling between views

In some situations you might want to change the focus from one view to
another. For example, this could happen when adding or removing views in a
layout. How to achieve this focus behavior depends on the concrete requirement
and the specific project setup. The Client sample application provides an
example in the "Examples" section demonstrating a custom focus handling
between an overview and a form.

### 4.17. SCDM - Simple Composed Data Model

This extension is currently an experimental feature that builds on the already
existing relationships extension and the new documentGraph extension.

It provides an optimized UI for editing sets of documents in the context of a
certain use case of the target application.

#### 4.17.1. Preparation

The modeling of SCDM is based on

  * Multiple Document models: Used for the individual entities (domain models) and the aggregate (CDM)

  * A single Form model: Used to model the form UI

  * Multiple Bindings: Configuration of the relationship UI components and placement inside the form

  * Multiple Overview models: Configuration of the links and candidate columns

All models are regular A12 models. The CDM and the form model use annotations
and existing features in a slightly extended way to allow the modeling of a
CDM (form).

Please refer to the Business Analyst documentation for a detailed description
on how to create CDMs.

#### 4.17.2. Application setup

SCDM requires some global configuration. Please check appsetup.ts and
platform_server.devapp.tsx in the sample app for a working example.

##### Middlewares / Sagas

In order to use SCDM, you must pass some new middlewares/sagas to
createApplicationSetup:

  * middlewares: createCdmMiddlewares(createEngineMiddlewares())

    * this one includes and replaces the FE middlewares

    * if you have options for FE middlewares, you must also pass them here!

  * sagas: cdmSagas

##### Reducers

The following sets of reducers have to be added:

  * Document Graph reducers: dgReducerFactory(cddDataHolderReducerExtension)

  * CDD reducers

##### Data Provider

The cddDataProvider has to be added.

### 4.18. Client Chrome Extension

The _Client Chrome Extension_ is an experimental development tool to inspect
the current state of the application. With this tool you can do some low level
interactions with the application which are not possible via the UI. For
example you can always dispatch a commit or cancel action for an activity.

#### 4.18.1. Installation

You can download the extension as a ZIP-archive from the [mgm
Artifactory](https://artifacts.mgm-tp.com:443/artifactory/maven-
releases/com/mgmtp/a12/client/client-chrome-extension) (mgm internal only). In
order to integrate it into Chrome follow these steps:

  1. Unpack the downloaded archive into a new directory

  2. Open the URL `chrome://extensions` in Chrome and enable developer mode

  3. Click on `Load Unpacked` and select the directory from step 1

__ |  To use the extension you need to allow third-party cookies in the Chrome settings.  
---|---  
  
#### 4.18.2. Usage

To use the extension in combination with your application you need to add an
additional middleware in your `appsetup.ts` as shown below:

    
    
    declare var window: Window & { _sampleDevToolMiddleware: Middleware };
    
    const devToolMiddleware = (): Middleware => {
      return window._sampleDevToolMiddleware === undefined ?
      window._sampleDevToolMiddleware = StoreFactories.createMiddleware(
        (api, next, action) => {
          const retVal = next(action);
          return retVal;
        }) : window._sampleDevToolMiddleware;
    };
    
    const config = ApplicationFactories.createApplicationSetup({
        ...
            additionalMiddlewares: devToolMiddleware(),
            ...
    });

### 4.19. Asynchronous flows with Redux Saga

Client uses the JavaScript library Redux Saga for code that involves
asynchronous execution and side effects. This code can be often seen as
defining application flow of some type, like logging-in and -out of a user or
retrieving documents from a server and storing them in the redux store. Redux
Saga allows writing asynchronous code in a synchronous manner, by using
generator functions, called in this context "sagas", that yield descriptions
of what "effects" should occur at any given point in the flow. Those
descriptions are then handled by the saga middleware to perform tasks, like
dispatching actions, waiting for some action to come, calling an asynchronous
function (a function that returns a promise). Effects can be blocking or non-
blocking.

Most sagas use the take-effect (or the helper effects takeLatest or takeEvery)
to wait for an action that matches some pattern. It is important to remember,
that the saga middleware executes after reducers - if some reducer changes the
store in some way on receiving an action, and some saga listens for the same
action, then by the time yield take returns, the store was already modified by
the reducer. If this is not desired, then a new type of action should be
created, that is ignored by reducers.

For general information about Redux Saga, you may want to visit following web
pages:

  * <https://redux-saga.js.org/> \- the project's page

  * <https://www.blog.duomly.com/implement-redux-saga-with-reactjs-and-redux/#redux-saga> \- a tutorial, that also explains some background

  * <http://blog.isquaredsoftware.com/2017/01/idiomatic-redux-thoughts-on-thunks-sagas-abstraction-and-reusability/> \- comparison of Thunks and Sagas, with much background information and links to discussions

  * <https://medium.com/@totaldis/redux-saga-in-action-s-f7d11cffa35a> \- describes an approach that strictly divides actions into signals (that trigger sagas) and deltas (that trigger reducers)

#### 4.19.1. Implementation of sagas in Client

In the standard case, like the one described in the official tutorial (to be
found under the first link above), a saga is a generator function that is
directly connected to the saga middleware. It has all the freedoms allowed by
Redux-Saga and behaves as if it was a separate thread. It is completely
independent of any other sagas. Client allows to define sagas like this, but
the built-in platform-sagas are implemented in a different way.

##### Connecting sagas directly to middleware

Custom sagas can be passed in the customSagas-argument to the factory function
`ApplicationFactories.createApplicationSetup`. Its platform implementation
passes each saga to the run-function defined by the saga middleware. This
function executes each saga right away, so if it contained some blocking code,
it would freeze the application. That's why possibly long running code should
always be run asynchronous and the sagas should always yield effects. Typical
usage is that a saga waits for some action using the take-effect and then
calls some asynchronous code using the call-effect.

##### Connecting sagas to the dispatcher

This method is used for built-in platform-sagas and it allows to overwrite
them. Objects implementing the interface `ApplicationSaga.Descriptor` can be
passed in the overridePlatformSagas-argument to the factory function
`ApplicationFactories.createApplicationSetup`. A descriptor must define
following two functions:

  * canHandle: takes an action as argument and returns true, if the saga should execute

  * handle: calls a generator function (can be seen as a saga), that handles the action matched by canHandle and returns its result, that is, a generator

To use the Descriptor, you need following import:

    
    
    import { ApplicationSaga } from "@com.mgmtp.a12.client/client-core/lib/core/application";

Those descriptors are then used by the dispatcher, a saga that is directly
connected to the middleware, just like in the standard case described before.
The dispatcher receives all actions dispatched to the store and calls
canHandle on every descriptor that it knows. For the first matching
descriptor, the dispatcher yields the generator returned by its handle-
function, that is then processed by the saga middleware. To recapitulate, the
dispatcher dispatches actions to functions, that can handle them.

This mechanism can be used to selectively overwrite built-in sagas - all
descriptors in overridePlatformSagas are checked before built-in sagas, so if
some of them can handle the same action as some built-in saga, then it will be
executed instead.

This mechanism has its restrictions - some concurrency patterns, that are
possible when using sagas in a standard way, are currently not directly
possible, like takeLatest or blocking take. The dispatcher uses takeEvery
under the hood, so an action is always executed, if any of the registered
descriptors can handle it.

For an explanation of takeEvery and takeLatest you may want to visit
<https://redux-saga.js.org/docs/basics/UsingSagaHelpers.html>.

##### Providing own dispatcher

Users of Client can pass the setup function their own implementation of the
dispatcher. It is then executed by the saga middleware, just like provided
dispatcher would be, and receives all registered descriptors as argument.

#### 4.19.2. Error handling in sagas

The circumstance that sagas are implemented as generator functions allows for
easy error handling with the try…catch statement. Inside the catch-block, the
ERROR-action should be created, that is then used by reducers to save the
error and error status in the affected activity. Below are the steps, that
comprise the error handling.

  1. Inside the catch-block in a saga, the ERROR-action should be dispatched. Its payload contains the error and the property operationType, which can be set to "loading" or "saving" \- it is used by reducer to set the value of either loadingState or savingState in the activity.

  2. If the error is of type ApplicationError, then it is saved by reducer as is. Otherwise, the reducer wraps the error in an ApplicationError with the error code of INTERNAL_CLIENT_ERROR.

  3. Based on value of operationType, the reducer sets either loadingState or savingState to "error".

  4. Components can use this information for example to render some kind of indication, that an error occurred.

  5. The error-property can be reset by dispatching the action CLEAR_ERROR.

#### 4.19.3. Built-in sagas which get triggered by an action

Below are listed all actions that are consumed by Client built-in sagas. All
actions that trigger them are in the namespace "Activity", so for example the
action named "PUSH" below has the type "Activity/PUSH". If you want to have a
different behavior, you can register your own implementation in the array
`overridePlatformSagas` in the Client application setup.

##### Models and Documents

Handle loading of A12 documents and models.

Triggering action | Description  
---|---  
`PUSH` | Executes after the reducer already created a new activity. Dispatches the `LOAD_MODELS`\- and `LOAD_DATA`-action if model and/or data loading is required. It also initializes one data holder if it is not already existing. This data holder's descriptor is identical to the activity's descriptor, and we refer to it as the activity data holder. If there is an overview model specified in the scene for the current activity, this saga also initializes the list parameters like pagination, filter and sorting.  
`LOAD_MODELS` | Loads all models into the Redux store which are specified in the scene matching the current activity. All referenced document models are automatically loaded, so there is no need to additionally specify the referenced document model. It only loads models which are not yet in the redux store.  
`LOAD_DATA` | It performs the data loading for all data holders of the current activity whose loading state is `loading`. The loading itself is delegated to the data handlers.<br /><br />If you are using a data loader, there is some default behavior implemented within the Client. After the loading, it dispatches a `SET_DATA` action which sets the data in the activity. When a new document is created and the `preComputeNewDocuments` parameter of the `ApplicationSaga.Configuration` object is set to true, computations will be executed before and the calculated document will be set as data of the activity.<br/><br/>If you are using the data provider, you have the full control about the data loading operation, e.g. you have to write the loaded data back into the activity's data holder.  
`SAVE.STARTED` / `COMMIT.STARTED` | If performs the saving of data for the current activity. The saving itself is delegated to the data handlers.<br /><br />If you are using a data loader, it dispatches the `SET_DATA`-action for the activity after saving with the data from the save result in the payload. If the activity contains a datasourceActivityId, the `SET_DATA`-action is also dispatched for this activity. It also dispatches a `RELOAD` action for related overview activity if it exists.<br/><br/>If you are using a data provider, there is no additional default behavior. The Client simply runs your implemented `provideData` method of the matching data provider.<br/><br/>For the `COMMIT.STARTED` action, the activity is cancelled after the saving operation.  
`REMOVE_DATA` | Calls the delete function of a matching data handler for the current activity.<br /><br />If you are using a data loader, it also dispatches the `RELOAD`-action for the parent overview-activity and its dependents after the delete operation.  
`RELOAD` | Locks the activity (by dispatching the `LOCK`-action), dispatches the `LOAD_DATA`-action and then unlocks the activity (by dispatching the `UNLOCK`-action).  
`QUERY_PARAMETERS_CHANGED` | Executes after reducers already updated the query parameters (filter, sorting and pagination) in the activity. Locks the activity (by dispatching the `LOCK`-action), dispatches the `LOAD_DATA` action and then unlocks the activity (by dispatching the `UNLOCK`-action).  
  
##### CRUD Demo

Triggering action | Description  
---|---  
`CREATE_NEW_DOCUMENT` | Dispatches the PUSH-action with an activity for a new document. A possibly open document gets cancelled before.  
`SELECT_ROW` | Dispatches the PUSH-action with an activity for the selected document. A possibly open document gets cancelled before.  
  
##### Cancellation of Activities

Triggering action | Description  
---|---  
`CANCEL_REQUESTED` | Dispatches a `CANCEL`-action for all activities which are contained in the payload of the action. This saga can be overridden with for example the dirtyHandling-saga which is contained in the extensions of the Client.  
  
#### 4.19.4. ActivitySagas

##### acquireActivityLock

This saga can be used to acquire a lock for an activity. The saga tries to
lock an activity until it has the lock or until the activity is not in the
store anymore. If the activity is already locked by somebody else, the saga
waits for the activity to be unlocked.

The saga has the following signature:

    
    
    function acquireActivityLock(activityId: string, owner: string, details: object): SagaIterator<string | undefined> { /* ... */ }

The locks get a unique id which later has to be used to unlock them.

If the saga acquired a lock it returns the lock id. If the activity gets
deleted from the store in the process the saga returns "undefined". A caller
has to check that the lock id is not undefined before proceeding.

A caller also has to release the lock after it is not needed anymore.

Example usage:

    
    
    const lockId = yield call(ActivitySagas.acquireActivityLock, activityId, owner, details);
    if (lockId === undefined){
      // activity with activityId is not in the store anymore, so it makes sense to stop here..
      return "failed";
    }
    
    // Statements while having the lock
    
    // When you are done, unlock the activity with the lockId
    yield put(ActivityActions.unlock({activityId: activityId, lockId: lockId}));

#### 4.19.5. StoreSagas

##### waitForStateChange

This saga can be used to wait for a specific state change by passing a
selector.

The saga has the following signature:

    
    
    waitForStateChange<T>: (selector: Selector<{stateChanged: boolean, returnValue: T}>) => SagaGenerator<T>;

The function expects as an argument a selector, which returns an object, which
contains the following values:

  * stateChange: specifies that the state changed to the desired outcome

  * returnValue: a value which gets returned by the selector

The waitForStateChange saga calls the selector on the first call and then
after each action which gets dispatched, until the "stateChanged" value is
true. In the end the saga returns the "returnValue" to the caller.

Example usage in another saga:

    
    
    const returnValue = yield call(StoreSagas.waitForStateChange, mySelector(myArguments))

### 4.20. Responsive Application Layout Optimization

There are certain layout optimizations for small window sizes (e.g. an
application is opened on a phone device or the browser window is made
smaller).

These optimizations apply to the following components in the Client:

  * **MasterDetailLayout** : In a large window the MasterDetailLayout shows two panels next to each other, if there is more than one view opened. In a small window the layout shows only one panel.

  * **NotificationFrame** : If the application window is large the notifications are shown separately. Otherwise they are stacked.

  * **ApplicationFrameLayout** : If the application window is small the mobile navigation behavior (Section 4.21) is enabled.

Furthermore, A12 engines and widgets provide layout optimization for small
window sizes for certain components as well.

In order to enable these layout optimizations for the whole application
(including engines and widgets) you need to wrap your application in a React
context provider called `SizeContext`. This provider makes the current window
size available to all underlying React components.

The following code shows an example of how this should look like:

    
    
    const MyApplicationWithSizeDetection = withSizeDetector(MyApplication);
    export function ResizableApplication(props: {}): JSX.Element {
      const [size, setSize] = React.useState<SizeDetectorProps.Size>("lg");
      const onSizeChange = (breakPoint: SizeDetectorProps.BreakPoint): void => {
        setSize(breakPoint.size);
      };
    
      return (
        <SizeContext.Provider value={{ currentSize: size }}>
          <MyApplicationWithSizeDetection {...props} onSizeChange={onSizeChange} />;
        </SizeContext.Provider>
      );
    }

__ |  If you do not wrap your application with the `SizeContext.Provider` there will not be any size detection and a large window will be assumed. There is no fallback to a device detector.  
---|---  
  
### 4.21. Mobile Navigation

#### 4.21.1. General Overview

To be able to navigate backwards in a consistent way on a small device, the
`ApplicationFrameLayout` of the Client provides a navigation mechanism to show
a back button which either cancels the activities belonging to the currently
visible views or expands the sidebar, if it exists.  
The back button will be shown as soon as a nested view (e.g. the detail in a
Master Detail Layout) is shown or a sidebar is collapsed.

The position and rendering of the back button depends on the used layout.

In the case of a layout which shows multiple views in mobile mode (e.g.
DashboardLayout) the ApplicationFrameLayout will render a back button in the
navigation bar above the current content.  

For layouts only showing one view in mobile mode (e.g. Master Detail), a React
context with a `onBackButtonClicked` callback will be created if a back
navigation is possible.  
Each view is responsible of showing a back button if this callback is given.  
More details can be found in Mobile Navigation Project setup

In a multi view layout you also should provide a title for a better navigation
experience. This title needs to be given to the `ApplicationFrameLayout` with
the prop `navigationBarTitle`. You can find an example of this in the Sample-
Application code under "src/components/navigationBarTitle.tsx".

Furthermore, this feature hides the header and footer of the
`ApplicationFrameLayout` as soon as a back-button is shown.

The next section will summarize what you need to do in your project to fully
enable mobile navigation.

__ |  If you do not want this described behavior, you can disable it by setting the prop `disableMobileNavigation` of the `ApplicationFrameLayout` to `true`. Then no back-button will be displayed and the header as well as the footer will be shown the whole time.  
---|---  
  
#### 4.21.2. Mobile Navigation Project setup

##### Application

First of all you need to enable responsive layout optimization for the whole
application. See Section 4.20 for more details.

##### Views

If you use an `ActionContentBox`, you need to set the content box prop
`listenToNavigationContext` to true.  
If you do not use an ActionContentBox for your view, you need to take care of
rendering the button yourself when the `onBackButtonClicked` callback is set.  
For this purpose the A12 Widgets library provides a `BackButton` component.  
The following code shows how to create the back button which you can then put
in the heading of your content box:

    
    
    import * as React from "react";
    
    import { NavigationContentboxContext } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/action-contentbox/action-contentbox.view";
    
    import { ContentBoxElements } from "../static-page/static-page-imports";
    
    export function BackButton(): JSX.Element | null {
      const { onBackButtonClicked } = React.useContext(NavigationContentboxContext);
      return onBackButtonClicked ? (
        <ContentBoxElements.BackButton onBackButtonClicked={onBackButtonClicked} />
      ) : null;
    }

##### Title

If you use a layout which shows more than one view in mobile mode (e.g.
Dashboard or Null layout), you should provide a title for the navigation bar,
which is shown above the visible content in the `ApplicationFrameLayout`.  
You can set the title with the prop `navigationBarTitle` of the
`ApplicationFrameLayout`.

__ |  You do not need to do this, if you do not use the layout in a nested scenario. Meaning there is no sidebar or other parent activity before.   
---|---  
  
##### Custom layouts

In your custom layouts you need to adapt the layout provider. The declaration
of the layout depends on the number of visible views in mobile mode.

###### One view in mobile mode

For this case the layout provider needs to return a Layout object, which sets
`visibleViews` to "single" and `getClearedAfterViewIndex` to "views.length -
2".  
The getClearedAfterViewIndex tells the `ApplicationFrameLayout` after which
view index there is a clear caused by the layout.  
The following code shows an example for such a custom layout declaration

    
    
    import {
      Layout,
      LayoutProps
    } from "@com.mgmtp.a12.client/client-core/lib/core/frame/internal/layout/LayoutProps";
    
    import { CustomLayoutComponent } from "./CustomLayoutComponent";
    
    export const layout: Layout = {
      component: CustomLayoutComponent,
      visibleViews: "single",
      getClearedAfterViewIndex(layoutProps: LayoutProps) {
        return () => {
          if (layoutProps.views.length > 1) {
            return layoutProps.views.length - 2;
          }
    
          return undefined;
        };
      }
    };

The usage of the props `visibleViews` and `getClearedAfterViewIndex` is
described in more detail in the [API documentation of
`Layout`](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-
bundle/typedoc/interfaces/core_model.applicationmodel-1.layout.html).

###### Multiple views in mobile mode

For this case the layout provider needs to return a Layout object, which sets
"visibleViews" to "multiple". Furthermore, if you do not show all available
views with your layout, you need to set getClearedAfterViewIndex as well, to
define the view index after which the layout causes a clear.

## 5\. Architecture

This chapter gives an insight into the A12 Client Architecture.

### 5.1. Walkthrough

This page gives an overview of the key modules and elements of the Client. The
focus is on high-level dependencies and interactions. The following concept
map will guide us:

![client-
architecture](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/3815038008631c75b50892f330319d9e/client-
architecture.svg)

Read the above diagram like this: modules of the Client are in colored boxes.
The box title briefly summarizes the responsibility of the module and also
relevant technologies used. Go back to Principles in the Introduction to see a
collapsed diagram of Clients' modules.

#### 5.1.1. Activity / Scene / View cascade

Activities are not directly related to the UI. Actually, you can create
activities (through Redux actions) in a _headless_ Client application, e.g.,
when testing on the command line. Activities relate to UI only through
indirection with the so-called **Activity/Scene/View** cascade. This page will
give a quick walkthrough of what happens when a new activity is created. The
following sections of this chapter contain other detailed walkthroughs for the
specifics that we are omitting for now.

  1. **Application code** dispatches a Redux action to start a new activity. In the diagram locate the arrow labelled "creates" pointing towards "Activity". For example, when the user clicks on a row in the overview list, the row-selection handler would dispatch this Redux action.

  2. The **activity** is created. It contains, among other things:

     * The **activity descriptor** (a key/value map with the two pre-defined keys "model" and "instance").

       * The activity descriptor is the most relevant part; it denotes the intention of its activity and is then used to select an application model scene that changes the UI.

     * data (which might be missing at this point and loaded later from server - by data loaders - or from a parent activity - by a data editor)

     * Various tracking information like loading state, saving state, processing state, whether the activity is locked or dirty, and also error information.

  3. The activity triggers now two actions: data loading (yellow area in the diagram) and UI updates (the blue and green rest in the diagram).

     * The data loading is handled by so-called data-loading sagas, which is a loop that watches for new activities without loaded data. These sagas are registered during application startup. The default sagas delegate the loading (and saving later on) to registered DataLoaders (load/save from server) and DataEditors (read/write from data of a parent activity). The selection is done by inspecting the activity descriptor.

  4. The **region selector** (in the lower green "frame" module) is called and finds a matching application model scene for the activity descriptor. The scene contains

     * a match condition that has to be matched against the activity descriptor (keys and values to match)

     * a scene change with directives to execute, also an optional default case again with scene changes (not detailed here).

     * Then the directives of the scene change are interpreted and result in a region specification containing the layouts for regions and views in these regions. In the diagram, locate the light blue box "model" just above the green "frame" module.

  5. The derived abstract UI structure is now used to render actual UI components via a provider mechanism, that maps names to actual UI components, e.g., a view with name "CRUDOverview" would map to a specific React component.

     * Note that derived abstract UI structure is agnostic to any technology (even does not know about to React).

  6. The **layout** is a React component for a region that defines the visual structure of this region. The derived views will be rendered according to its specification and the available placeholders in the respective layouts. For example, the master-detail layout has two placeholders on the desktop and one on mobile devices.

     * Views that are not displayed can be accessed through other means, e.g., a dropdown control that is shown by the layout.

     * Applications are free to define their own layouts.

  7. The **UI component** for a view is rendered. There are many predefined views, e.g., for the Engines. Applications are free to define their own views or extend existing ones.

## 6\. Tutorials

The following sections contain tutorials, that teach you about setting up
various features in an A12 Client Application.

You will learn with the help of simple examples:

  * how to add a static page.

  * how to set up a CRUD Workflow using A12 Models.

  * how to set up the A12 Services backend to persist documents.

  * how to set up the relationships feature.

  * how to configure another locale.

  * how to use React, Redux and Redux Sagas in an A12 Client App by creating a timer.

The tutorials build upon the A12 Client template project which also can be
used as a starting point for a new Client project. It is described in more
detail in its own section, which you should read before starting with the
tutorials. There, you will also find a downloadable zip of the template.

Some tutorials build upon the results of other tutorials. This will be
described in detail at the beginning of the respective tutorial. Others are
independent.

### 6.1. Prerequisites

The following dependencies are mandatory in order to follow the tutorial. The
mentioned versions are currently in use and tested, but deviating minor
versions should be working as well.

Tool | Version | Note  
---|---|---  
[JDK](https://www.oracle.com/technetwork/java/javase/overview/index.html) |  `11.0.13` |   
[Gradle](https://docs.gradle.org/)¹ |  `6.5.1` |   
[Node](https://nodejs.org/en/docs/) |  `14.16.0` |   
  
  * npm¹

|  `6.14.6` |   
[Docker](https://hub.docker.com/)¹ |  `19.03.13` |   
  
¹) These dependencies have to be configured to use the [mgm
Artifactory](https://artifacts.mgm-tp.com/artifactory/webapp/#/home) (mgm
internal only). Further information can be found in the [mgm
Wiki](https://wiki.mgm-tp.com/confluence/display/TECHHELP) (mgm internal
only). If you do not want to set up these manually, you might consider using
the Common Development Environment ([CDE](https://wiki.mgm-
tp.com/confluence/pages/viewpage.action?pageId=79806519)) (mgm internal only)
to set up the required dependencies including the necessary configurations for
the Artifactory. However, please be aware that A12 defines the dependency
requirements independently of CDE.

### 6.2. Adding a Static Page

In this tutorial, we will add another simple static page (next to the existing
`Welcome Page`). Content of the page is served as it is defined in the file,
so no additional setup is needed.

Note that it is necessary that the view component provider
`src/main/viewFactory.tsx` contains the `staticPageComponentProvider`. This
will enable static pages (enabled by default in the template).

src/main/viewFactory.tsx

    
    
    import * as React from "react";
    
    import { FrameFactories } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import { StaticPageFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/static-page";
    
    const staticPageComponentProvider = StaticPageFactories.createViewProvider();
    
    function Placeholder(): JSX.Element {
      return <div>ERROR: NO CONTAINER FOUND</div>;
    }
    
    export function viewProvider(componentName: string): React.ComponentType<View> {
      return (
        staticPageComponentProvider(componentName) ||
        FrameFactories.viewProvider(componentName) ||
        Placeholder
      );
    }

#### 6.2.1. Create a new static page

Create a new file `hello_world.tsx` for the static page in the folder
`src/main/static/pages`. The name of the file is important since this is
convention for static pages - it's the URL path which later will be bound to
the page. The file must **export** a React component as **default** that will
represent the static page content. In this example we use the
`ActionContentbox` widget component to wrap our HTML.

src/main/static/pages/hello_world.tsx

    
    
    import {
      React, // Needed for React components
      ContentBoxElements,
      ActionContentbox
    } from "../static-page-imports";
    
    export default function HelloWorldPage(): JSX.Element {
      return (
        <ActionContentbox
          headingElements={<ContentBoxElements.Title text="Hello World" />}
        >
          <p>Greetings from a static page.</p>
        </ActionContentbox>
      );
    }

#### 6.2.2. Register a new module in the Application Model

The application model for the template project is defined in the file
`src/main/appmodel.json`. You need to add a new module for the new static page
to the array of modules in the application model. Note that the name of each
module must be unique.

new module for the new static page

    
    
    {
      "name": "HelloWorld",
      "menu": {
        "name": "hello-world",
        "label": {
          "en": "Hello World"
        },
        "state": {
          "page": "hello_world"
        }
      },
      "flows": [
        {
          "name": "helloFlow",
          "scenes": [
            {
              "name": "hello",
              "matchConditions": [
                {
                  "key": "page",
                  "mustEqual": "hello_world"
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "REGION_CLEAR"
                  },
                  {
                    "type": "VIEW_ADD",
                    "name": "StaticPage"
                  }
                ]
              }
            }
          ]
        }
      ]
    }

#### 6.2.3. Summary

After adding a new static page, we need to compile the added TypeScript files
to JavaScript and then restart the webpack dev server to be able to request it
in the application.

Kill the running webpack dev server in your terminal by hitting `CTRL+C`, and
then run these commands:

    
    
    npm run compile
    npm start

Now, the new page should be accessible through the application menu.

### 6.3. Working with A12 Models

In this tutorial, we will integrate A12 Models into the template project and
use the CRUD views from the Client library to display the models in the
Overview- and Form-Engine.

#### 6.3.1. Adding A12 Models to the Template Project

##### Download Example Models

A set of example models which have been created with the A12 modeling tools
can be downloaded
[here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/30c0989586c9c90363bcc78483eda8bb/example-
models.zip).

Extract and store these models in the `resources` folder of the template
project. It is recommended to use the folder structure shown below, since we
use the same structure in the further steps of the model conversion.

__ |  When using your own A12 models, make sure that all models have the role `admin` defined in the model settings  
---|---  
  
###### Storing models in template project

  * resources

    * html

    * models

      * `DomainPerson.json`

      * `Person-overview.json`

      * `Person.json`

##### Generate validation file and copy models to target directory

The A12 Document, Form and Overview models are created with the A12 modeling
tools in the JSON format which is already sufficient for this tutorial. Those
files just need to be copied over to the target directory.

However, the A12 Document Models which are holding the data structure and
validation rules need also to be converted to a JavaScript file containing the
validation logic, which needs to be copied as well.

To achieve all of this, we have to set up a gradle script which will provide
the tasks to perform the generation of the validation file and to copy the
files to the correct places.

###### Add a `build.gradle` file

The file should be stored in the `resources/models` directory which we created
above.

In order to use `gradle` during the build process, please make sure that it is
correctly installed and configured to work with the _mgm artifactory_ as
described in the Prerequisites.

resources/models/build.gradle

    
    
    /**
     * This gradle script provides tasks for copying, converting and migrating models found in this folder
     * and uses the name schema of the platform server.
     *
     * * `Domain<Name>.json` => `../../target/models/Domain<Name>.json`
     * * `Domain<Name>.json` => `../../target/models/Domain<Name>.validation.js`
     * * `<Name>.json` => `../../target/models/<Name>.json`
     * * `<Name>-overview.json` => `../../target/models/<Name>-overview.json`
     */
    
    buildscript {
        ext {
            Closure<String> getNodeVersion = { new JsonSlurper().parse(project.file("../../node_modules/${it}/package.json")).version }
    
            dependencyVersions = [
                a12: [
                    kernel        : getNodeVersion("@com.mgmtp.a12.kernel/kernel-md-facade"),
                    engines       : getNodeVersion("@com.mgmtp.a12.formengine/formengine-core"),
                    overviewEngine: getNodeVersion("@com.mgmtp.a12.overviewengine/overviewengine-core"),
                    services      : getNodeVersion("@com.mgmtp.a12.dataservices/dataservices-server-connector")
                ]
            ]
    
            println "The following product versions"
            println "Kernel:           " + dependencyVersions.a12.kernel
            println "Engines:          " + dependencyVersions.a12.engines
            println "Overview-Engines: " + dependencyVersions.a12.overviewEngine
            println "Services:         " + dependencyVersions.a12.services
        }
    }
    
    plugins {
        id 'java'
    }
    
    
    import groovy.json.JsonSlurper
    
    configurations {
        form.extendsFrom runtimeOnly
        overview.extendsFrom runtimeOnly
    }
    
    dependencies {
        runtimeOnly "com.mgmtp.a12.kernel:kernel-md-model:${dependencyVersions.a12.kernel}"
        runtimeOnly "com.mgmtp.a12.kernel:kernel-tool-model-migration:${dependencyVersions.a12.kernel}"
        form "com.mgmtp.a12:form-model-migration:${dependencyVersions.a12.engines}"
        overview "com.mgmtp.a12:overview-model-migration:${dependencyVersions.a12.overviewEngine}"
    }
    
    configurations {
        runtimeOnly.exclude group: 'org.slf4j', module: 'slf4j-log4j12'
    }
    
    static boolean isDocumentModel(File file) {
        boolean returnType = false
        if (file.name.endsWith('.json')) {
            for (String line in file.readLines()) {
                if (line.contains('"modelType"')) {
                    if (line.contains('"document"')) {
                        returnType = true
                        break
                    } else {
                        returnType = false
                        break
                    }
                }
            }
        }
        return returnType
    }
    
    static String getFileName(File file) {
        return file.name.take(file.name.lastIndexOf('.'))
    }
    
    task _clean(type: Delete) {
        delete file("${projectDir.path}/../../target/models")
    }
    clean.dependsOn(_clean)
    
    task convertValidation(type: JavaExec) {
    
        classpath sourceSets.main.runtimeClasspath
        main = 'com.mgmtp.a12.kernel.md.model.a12internal.services.codegen.cli.BatchVkValidationCodeGeneratorJs'
    
        fileTree(dir: ".", include: '**/*.json')
            .filter({ file -> isDocumentModel(file) })
            .each { documentModelFile ->
                File outputFile = file("../../target/models/${getFileName(documentModelFile)}.validation.js")
                inputs.file documentModelFile
                outputs.file outputFile
                args documentModelFile.path
                args outputFile.path
            }
    }
    
    task expandIncludes(type: JavaExec) {
    
        dependsOn 'copyModels'
    
        classpath sourceSets.main.runtimeClasspath
        main = 'com.mgmtp.a12.kernel.md.model.a12internal.services.expansion.cli.BatchDocumentModelExpander'
    
        fileTree(dir: ".", include: '**/*.json')
            .filter({ file -> isDocumentModel(file) })
            .each { documentModelFile ->
                File outputFile = file("../../target/models/${getFileName(documentModelFile)}.json")
                inputs.file documentModelFile
                outputs.file outputFile
                args documentModelFile.path
                args outputFile.path
            }
    }
    
    task copyModels(type: Copy) {
        from('.') {
            include '**/*.json'
        }
    
        eachFile {
            path = name
        }
        includeEmptyDirs = false
    
        into file('../../target/models')
    }
    
    task convert {
        dependsOn 'convertValidation', 'copyModels', 'expandIncludes'
    }
    
    task migrateDocumentModels(type: JavaExec) {
        workingDir = new File("${projectDir.path}/../../")
        classpath = sourceSets.main.runtimeClasspath
        main = 'com.mgmtp.a12.kernel.tool.migration.MigratorCli'
        args new File('resources/models').path
    }
    
    task migrateFormModels(type: JavaExec) {
        workingDir = new File("${projectDir.path}/../../")
        classpath = configurations.form
        main = 'com.mgmtp.a12.model.form.migration.MigratorCli'
        args '-o'
        args 'EventButtonFullValidationStep'
        args new File('resources/models').path
    }
    
    task migrateOverviewModels(type: JavaExec) {
        workingDir = new File("${projectDir.path}/../../")
        classpath = configurations.overview
        main = 'com.mgmtp.a12.model.ui.overview.migration.MigratorCli'
        args new File('resources/models').path
    }
    
    task migrate {
        dependsOn 'migrateDocumentModels', 'migrateOverviewModels', 'migrateFormModels'
    }

__ |  `BatchVkValidationCodeGeneratorJs` is a dev tool provided by the kernel. Therefore, please be aware, that it is not subject to the breaking change policy.  
---|---  
  
###### Integrate the model conversion into the build process

Replace the `initialize:models` script in `package.json` with the following
line which will execute the gradle script:

    
    
     "initialize:models": "gradle -b ./resources/models/build.gradle clean convert",

##### Summary

Now, you should be able to run `npm run initialize` to copy the A12 Models for
_Person_ and generate the validation file into the `target` folder of the
project.

In the next section, we setup JSON Loaders for models and documents to be able
to work with the A12 models without having the need for any backend service.

#### 6.3.2. Using JSON Loader for Models and Documents

##### Create document provider functions for example data

We create a new file `DocumentService.ts` inside the `./src/main/mocks` folder
of the project. It contains some fake data for our Person document and two
functions that will provide the appropriate document data:

  * `documentProvider`: provides document data for the Form-Engine for a given document id

  * `documentsProvider`: provides document data for the Overview-Engine for a given model name

src/main/mocks/DocumentService.ts

    
    
    export function documentProvider(id: string): object {
      if (id.startsWith("DomainPerson/")) {
        return DomainPerson.document(Number(id.substring("DomainPerson/".length)));
      }
      throw new Error(`No mock data found for '${id}'.`);
    }
    
    export function documentsProvider(modelName: string): object[] {
      if ("DomainPerson" === modelName) {
        return [0, 1, 2].map(DomainPerson.document);
      }
      return [];
    }
    
    namespace DomainPerson {
      export function document(i: number): object {
        const result = {
          id: `DomainPerson/${i}`,
          Person: {
            PersonalData: {
              FirstName: ["John", "Charlotte", "Kylie"][i],
              LastName: ["Doe", "Brown", "McKane"][i],
              Gender: ["MALE", "FEMALE", "FEMALE"][i],
              DateOfBirth: ["1965-01-15", "1982-07-22", "2001-11-11"][i],
              PlaceOfBirth: ["New York", "London", "Dublin"][i],
              Nationality: ["USA", "England", "Ireland"][i]
            }
          }
        };
        return result;
      }
    }

##### Register Model and Data Loader

In addition, we need to register some model and data loaders in the
application setup in the `./src/main/appsetup.ts`. In this tutorial, we use
the HTTP model loaders from the `http-connectors` package and the JSON Loader
from the `devtools` package of the Client.

First we add imports of model/data loaders which can load models/data from
json files and an import for the document service mock we just created.

    
    
    import { JsonLoaders } from "@com.mgmtp.a12.client/client-core/lib/devtools/models";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    import { createHttpModelLoaders } from "@com.mgmtp.a12.client/client-core/lib/extensions/http-connectors";
    
    import * as model from "./appmodel.json";
    import { documentProvider, documentsProvider } from "./mocks/DocumentService";

Then we have to register the json loaders as DataHandlers in the setup
function:

    
    
    const dataHandlers: DataHandlers = {
      dataEditors: [],
      dataLoaders: [
        new JsonLoaders.OverviewDataLoader(documentsProvider),
        new JsonLoaders.DocumentDataLoader(documentProvider)
      ],
      dataProviders: [ApplicationFactories.createEmptyDocumentDataProvider()]
    };

The two registered DataLoaders are responsible for loading the data to display
the content of the overview and the form. This time they take the mock data
from our mocking DocumentService.

The registered DataProvider is used for creating a new empty document.

Second we add the model loaders which can load models from json files.

src/main/appsetup.ts

    
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: createHttpModelLoaders(),
        dataHandlers,
        customSagas: [],
        additionalMiddlewares: [],
        setupActions: [],
        composeEnhancer: enableReduxDevTools()
      });

The registered ModelLoader loads all necessary A12 Document, Overview, and
Form Models.

In the end the file should look like this:

src/main/appsetup.ts

    
    
    import {
      ApplicationFactories,
      ApplicationSetup,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import { JsonLoaders } from "@com.mgmtp.a12.client/client-core/lib/devtools/models";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    import { createHttpModelLoaders } from "@com.mgmtp.a12.client/client-core/lib/extensions/http-connectors";
    
    import * as model from "./appmodel.json";
    import { documentProvider, documentsProvider } from "./mocks/DocumentService";
    
    export function setup(): ApplicationSetup {
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: [
          new JsonLoaders.OverviewDataLoader(documentsProvider),
          new JsonLoaders.DocumentDataLoader(documentProvider)
        ],
        dataProviders: [ApplicationFactories.createEmptyDocumentDataProvider()]
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: createHttpModelLoaders(),
        dataHandlers,
        customSagas: [],
        additionalMiddlewares: [],
        setupActions: [],
        composeEnhancer: enableReduxDevTools()
      });
    
      return config;
    }
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

##### Summary

We now have done all the necessary preparations to work with A12 models in our
template project. We are able to load models from the `target` folder of our
project and use some fake document data for overviews and forms.

However, after recompiling the application should still work as before. You
won't notice any changes in the UI yet when having a look at the application
in the browser.

In the next step, we will setup everything required to use the prepared A12
Models in the UI.

#### 6.3.3. Using overview and form components

##### Create a new module in the Application Model

At first, we want create a new module `PersonModule` and append it to the list
of modules in the application model `src/main/appmodel.json`.

the new PersonModule

    
    
    {
      "name": "PersonModule",
      "menu": {
        "name": "person",
        "label": {
          "en": "Person"
        },
        "state": {
          "model": "Person"
        }
      },
      "flows": [
        {
          "name": "PersonFlow",
          "scenes": [
            {
              "name": "PersonOverview",
              "description": "Overview of Person Documents",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "Person"
                },
                {
                  "key": "instance",
                  "isSet": false
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "REGION_CLEAR"
                  },
                  {
                    "type": "VIEW_ADD",
                    "name": "OverviewCRUD",
                    "models": [
                      {
                        "modelType": "overview",
                        "name": "Person-overview"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "PersonForm",
              "description": "Form showing on Person Document",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "DomainPerson"
                },
                {
                  "key": "instance",
                  "isSet": true
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "VIEW_ADD",
                    "name": "FormCRUD",
                    "models": [
                      {
                        "modelType": "form",
                        "name": "Person"
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }

We defined a new module with a flow that contains two scenes: `PersonOverview`
and `PersonForm`. Each scene consists of a name, an optional description, some
match conditions and a scene change.

In our example, we want to display the view `OverviewCRUD` for a model of type
`overview` and name `Person-overview` when there is an activity matching the
conditions from the first scene `PersonOverview`.

When there is an activity matching the second scene, we want to show the Form-
Engine via the `FormCRUD` view for the specified form model `Person`.

Both views are created from React components, which are part of the
`extensions` of the Client library and can be used for simple CRUD (Create,
Read, Update, Delete) scenarios. We need to register these CRUD views and also
additional sagas in our template project to make use of them.

##### Register the views and middlewares in the template project

UI Components that act as Views need to be registered in the `viewProvider` in
`src/main/viewFactory.tsx`.

First we need to import the module providing the CRUD views:

    
    
    import { CRUDViews } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";

We create a new provider for the Form-Engine and Overview-Engine views via a
new factory:

    
    
    function createCRUDViewProvider(): (
      componentName: string
    ) => React.ComponentType<View> | undefined {
      const components: { [name: string]: React.ComponentType<View> | undefined } =
        {
          FormCRUD: CRUDViews.FormEngineView,
          OverviewCRUD: CRUDViews.OverviewEngineView
        };
    
      return function provider(name) {
        return components[name];
      };
    }
    
    const crudViewProvider = createCRUDViewProvider();

Then we add the provider to the main viewProvider which is exported to the
application setup:

    
    
    export function viewProvider(componentName: string): React.ComponentType<View> {
      return (
        staticPageComponentProvider(componentName) ||
        // add the new provider here
        crudViewProvider(componentName) ||
        FrameFactories.viewProvider(componentName) ||
        Placeholder
      );
    }

Note, that here only a minimal setup is described. If you want to use the full
feature set of the engines, like handling attachments, a more complex setup is
required which can be studied on the code of the Client Sample Application.

The file in the end should look somehow similar to the following code snippet:

src/main/viewFactory.tsx

    
    
    import * as React from "react";
    
    import { FrameFactories } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import { StaticPageFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/static-page";
    import { CRUDViews } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    
    const staticPageComponentProvider = StaticPageFactories.createViewProvider();
    
    function createCRUDViewProvider(): (
      componentName: string
    ) => React.ComponentType<View> | undefined {
      const components: { [name: string]: React.ComponentType<View> | undefined } =
        {
          FormCRUD: CRUDViews.FormEngineView,
          OverviewCRUD: CRUDViews.OverviewEngineView
        };
    
      return function provider(name) {
        return components[name];
      };
    }
    
    const crudViewProvider = createCRUDViewProvider();
    
    function Placeholder(props: View): JSX.Element {
      return <div>ERROR: NO COMPONENT FOUND</div>;
    }
    
    export function viewProvider(componentName: string): React.ComponentType<View> {
      return (
        staticPageComponentProvider(componentName) ||
        // add the new provider here
        crudViewProvider(componentName) ||
        FrameFactories.viewProvider(componentName) ||
        Placeholder
      );
    }

To setup the Form-Engine which is internally used by the FormCRUD view inside
a Client application, we need to register some sagas, reducers and
middlewares.

In addition, we need to register a CRUD middleware in our application setup
that provides CRUD functionality to the FormCRUD view.

And we need to register a CRUD saga that provides the CRUD functionality to
the OverviewCRUD view.

First, in `src/main/appsetup.ts` let's import all required modules for the
form engine support:

    
    
    import {
      formEngineDataReducers,
      formEngineSagas,
      createFormEngineMiddlewares
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";

And the module for the crud support:

    
    
    import { CRUDFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";

Then the config in the setup function has to be adapted to register the
imported functions:

    
    
    const config = ApplicationFactories.createApplicationSetup({
      model: model as ApplicationModel,
      modelLoaders: createHttpModelLoaders(),
      dataHandlers,
      customSagas: [
        // add the form engine and crud sagas
        ...formEngineSagas,
        ...CRUDFactories.createSagas()
      ],
      additionalMiddlewares: [
        // add the middlewares
        ...createFormEngineMiddlewares(),
        CRUDFactories.createCRUDMiddleware()
      ],
      setupActions: [],
      composeEnhancer: enableReduxDevTools(),
    
      // add the form engine reducer
      dataReducers: formEngineDataReducers
    });

In the end, the file should look similar to this:

src/main/appsetup.ts

    
    
    import {
      ApplicationFactories,
      ApplicationSetup,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import { JsonLoaders } from "@com.mgmtp.a12.client/client-core/lib/devtools/models";
    import { createHttpModelLoaders } from "@com.mgmtp.a12.client/client-core/lib/extensions/http-connectors";
    import {
      formEngineDataReducers,
      formEngineSagas,
      createFormEngineMiddlewares
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";
    import { CRUDFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    
    import * as model from "./appmodel.json";
    import { documentProvider, documentsProvider } from "./mocks/DocumentService";
    
    export function setup(): ApplicationSetup {
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: [
          new JsonLoaders.OverviewDataLoader(documentsProvider),
          new JsonLoaders.DocumentDataLoader(documentProvider)
        ],
        dataProviders: [ApplicationFactories.createEmptyDocumentDataProvider()]
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: createHttpModelLoaders(),
        dataHandlers,
        customSagas: [
          // add the form engine and crud sagas
          ...formEngineSagas,
          ...CRUDFactories.createSagas()
        ],
        additionalMiddlewares: [
          // add the middlewares
          ...createFormEngineMiddlewares(),
          CRUDFactories.createCRUDMiddleware()
        ],
        setupActions: [],
        composeEnhancer: enableReduxDevTools(),
    
        // add the form engine reducer
        dataReducers: formEngineDataReducers
      });
    
      return config;
    }
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

##### Summary

Now, after recompiling, our application should display a new menu item
`Person`. A mouse-click on it opens the Overview-Engine for the `Person-
overview` model with three pre-filled documents.

When selecting the `Add Person` button on the top left corner of the view, the
Client renders the form for a new Person document on the right.

When clicking on a row in the Overview-Engine, it opens the detail form for
the selected person.

By clicking on the save button, we can also verify that the A12 kernel works,
because it reports some validation errors for an empty Person document.

**Remarks:**

  * When you fix the validation error and try to save a valid Person document, you will notice that the save operation has no effect. This is actually the expected behavior of the client-only/mock mode, since the delete and save operations are not implemented for the JSON data loader.

### 6.4. Using the Client with the A12 Server

This tutorial assumes, that you have followed the previous tutorial Working
with A12 models and that you have at least downloaded and converted the
example models, extended the appmodel and configured the viewFactory.

#### 6.4.1. Configuration of the A12 Server

##### Adapt the scripts in the `package.json`

Add the following scripts to the `package.json` in the root of the template
project. They are later required to start the application in server mode,
using the A12 Services backend, also known as A12 platform server.

    
    
    "start:platform_server": "npm-run-all --parallel start:platform_server:*",
    "start:platform_server:server": "npm run server",
    "start:platform_server:webpack": "npm run webpack-dev-server -- --env.profile=platform_server",
    "server": "gradle -b ./resources/server/build.gradle --console=plain clean runJar"

##### Download the A12 server configuration

An A12 server configuration can be downloaded
[here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/422bafd234e6ff0ee556f50db7352340/server.zip).

Unzip it in the `resources` directory of the template project

    
    
    unzip server.zip -d <PROJECT_DIR>/resources/server

The extracted server configuration files should look similar to the following
folder structure:

  * …

  * `node_modules`

  * `resources`

    * `html`

    * `models`

    * **`server`**

      * **`application.properties`**

      * **`build.gradle`**

      * **`index.html`**

      * **`settings.gradle`**

      * **`roles.yaml`**

      * **`users.yaml`**

  * `scripts`

  * `src`

  * …

##### Summary

Now, you should be able to run the server without the client via

    
    
    npm run server

It takes a few seconds until the server startup is finished. You should see
something similar to the following output in your terminal window

    
    
    [INFO ][.a12.services.rest.app.ServerApplication][u:] - Started ServerApplication in 30.6 seconds

Afterwards, make sure to kill the server process by hitting `CTRL+C` in your
terminal. We will restart the server in the upcoming.

Do not mind the error with error code 130 which is expected.

__ |  We describe with this tutorial a simplified way of setting up the platform server. For more details and recommendations please consult the services documentation.  
---|---  
  
#### 6.4.2. Enable the application to load models and documents from the A12
Server

The webpack config and the build process of the template project are pre-
configured to run the application in two different modes: `client-only` with
the in-memory model service and in `server` mode with the A12 Server.

To get both configurations to work, we need to add two additional files:

  * `platform_server.index.tsx`: the entry file for webpack in `server` mode

  * `platform_server.appsetup.ts`: a slightly different application setup for the `server` mode

_Important_ : The pre-configured webpack config only works with these two
entries: `index` (**client-only mode**) or `platform_server.index` (**server
mode**), so make sure that the filenames are identical to the one specified
above.

Now, simply create both files in `src/main` with the following contents. Note
that the content is the minimal configuration you need to run the server mode.

src/main/platform_server.appsetup.ts

    
    
    import {
      ApplicationFactories,
      ApplicationSetup,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    import { LocaleSelectors } from "@com.mgmtp.a12.client/client-core/lib/core/locale";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import {
      formEngineDataReducers,
      formEngineSagas,
      createFormEngineMiddlewares
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";
    import { CRUDFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    import { configure } from "@com.mgmtp.a12.client/client-core/lib/extensions/platform-server-connectors";
    
    import * as model from "./appmodel.json";
    
    export function setup(): ApplicationSetup {
      // Note: ConnectionLocator needs to be configured. This can be achieved e.g. by UAA.
      const platformServerConnectors = configure({
        localeProvider: () => LocaleSelectors.locale()(config.store.getState())
      });
    
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: platformServerConnectors.loaders.dataLoaders,
        dataProviders: [ApplicationFactories.createEmptyDocumentDataProvider()]
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: platformServerConnectors.loaders.modelLoaders,
        dataHandlers,
        additionalMiddlewares: [
          ...createFormEngineMiddlewares(),
          CRUDFactories.createCRUDMiddleware()
        ],
        customSagas: [...formEngineSagas, ...CRUDFactories.createSagas()],
        dataReducers: [...formEngineDataReducers],
        composeEnhancer: enableReduxDevTools()
      });
    
      return config;
    }
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

src/main/platform_server.index.tsx

    
    
    import "./config/dev.config";
    import "./static/static-page-imports";
    
    import * as React from "react";
    import * as ReactDOM from "react-dom";
    import { Provider } from "react-redux";
    
    import { FrameFactories } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { setupServerConnectionForDevelopment } from "@com.mgmtp.a12.client/client-core/lib/devtools/server-connection";
    
    import { viewProvider } from "./viewFactory";
    import { setup } from "./platform_server.appsetup";
    
    const mountpoint = document.createElement("div");
    mountpoint.setAttribute("class", "base");
    document.body.appendChild(mountpoint);
    
    const config = setup();
    
    /**
     * Setup a development server connection which automatically connects
     * the client with the server using the user "admin"
     * Mind: This is only for development, in a production environment you should
     * replace this with a proper authentication against the server (e.g. UAA).
     *
     */
    setupServerConnectionForDevelopment(config.store, "../api", "admin", "admin");
    
    const progressComponentProvider =
      FrameFactories.createProgressComponentProvider();
    
    function Page(): JSX.Element | null {
      const rootRegionRef: string[] = [];
      const RegionUi = FrameFactories.regionUiProvider(rootRegionRef);
    
      return (
        <RegionUi
          regionReference={rootRegionRef}
          layoutProvider={FrameFactories.layoutProvider}
          regionUiProvider={FrameFactories.regionUiProvider}
          viewProvider={viewProvider}
          progressComponentProvider={progressComponentProvider}
        />
      );
    }
    
    ReactDOM.render(
      <Provider store={config.store}>
        <Page />
      </Provider>,
      mountpoint
    );

##### Restart the application in `platform_server` mode

Now we can compile the TypeScript files to JavaScript and restart the
application in `platform_server` mode by calling the following commands in the
terminal:

    
    
    npm run compile
    npm run start:platform_server

and if everything has been set up correctly, we should be able to create a new
person document that gets persisted in the backend.

Click on the menu item `Person` and in the upcoming overview of Person
documents on the `Add Person` button in the top left corner. Fill out all
required fields of the Person form and save your document. The form then
disappears and a newly created document is shown in the list of Person
documents.

__ |  The function `setupServerConnectionForDevelopment` in the `platform_server.index.tsx` sets up a server connection using the user 'admin'. This is only a helper function for development. In a production environment you should replace this with a proper authentication against the server (e.g. UAA).  
---|---  
  
### 6.5. Using Relationships between Models

#### 6.5.1. Before you start

Make sure you are familiar with the A12 Client. It is recommended that you
have done the following tutorials:

  * Setting up the template project with the use of the A12 Server and A12 Models

  * You should be able to setup a Overview-Engine and a Form-Engine in the Client

#### 6.5.2. Goal of this tutorial

This tutorial describes how to configure the relationship feature in a Client
application.

In the end we want to have a relationship between products and brands which is
editable via forms.

A product can be assigned to one brand (1:1). A brand can have multiple
products (1:n).

We will use two different UI components for those relationships, the dropdown
selection for the 1:1 relationship and the dual pane for the 1:n relationship.

#### 6.5.3. Set up the models

We set up a domain with brands and products to model relationships between
them.

##### Base and Relationship models

Relationships are defined with the help of new model types which build upon
the common A12 Document and UI Models.

__ |  You will find a detailed guide on how to create all models necessary for a relationship in the A12 overall documentation. We recommend using the A12 Simple Model Editor for creating and editing the new model types.  
---|---  
  
Please download a set of all the required models from
[here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/7b69406e9e00f66c1308c6fdb8a47d40/relationship-
example-models.zip). They should be unpacked and moved to
`./resources/models/` to create a file system structure similar to this:

  * models/

    * relationships/

      * **ProductBrand.json** \- the relationship model

    * **DomainProduct.json** \- the document model of the product

    * **Product.json** \- the form model of the product form. It already contains the bindingConfiguration as annotation.

    * **Product-overview.json** \- the overview model of the product overview

    * **DomainBrand.json** \- the document model of the brand

    * **Brand.json** \- the form model of the brand form. It already contains the bindingConfiguration as annotation.

    * **Brand-overview.json** \- the overview model of the brand overview

    * **DomainProductBrand_AdditionalFieldsModel.json** \- the document model defining the data of the relationship link

    * **ProductBrand-LinkForm.json** \- the form model for the form shown to edit the link data

    * **BrandLink-overview.json** \- for viewing the brand candidates of the product

    * **ProductBrand-Brand-LinkOverview-overview.json** \- for viewing the established brand links of the product

    * **ProductLink-overview.json** \- for viewing the product candidates of the brand

    * **ProductBrand-Product-LinkOverview-overview.json** \- for viewing the established product links of the brand

##### Application Model

Setup your application model to have a product and a brand module in its array
of modules. Both modules should have two scenes, one for the Overview-Engine
and the other one for the Form-Engine. It should look like the following:

the ProductModule and BrandModule

    
    
    {
      "name": "ProductModule",
      "menu": {
        "name": "product",
        "label": [
          {
            "locale": "en",
            "text": "Product"
          }
        ],
        "state": {
          "model": "Product"
        }
      },
      "flows": [
        {
          "name": "ProductFlow",
          "scenes": [
            {
              "name": "ProductOverview",
              "description": "Overview of Product Documents",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "Product"
                },
                {
                  "key": "instance",
                  "isSet": false
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "REGION_CLEAR",
                    "layout": {
                      "name": "MasterDetail"
                    }
                  },
                  {
                    "type": "VIEW_ADD",
                    "name": "OverviewCRUD",
                    "models": [
                      {
                        "modelType": "overview",
                        "name": "Product-overview"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "ProductForm",
              "description": "Form showing on Product Document",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "DomainProduct"
                },
                {
                  "key": "instance",
                  "isSet": true
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "VIEW_ADD",
                    "name": "FormCRUD",
                    "models": [
                      {
                        "modelType": "form",
                        "name": "Product"
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    {
      "name": "BrandModule",
      "menu": {
        "name": "brand",
        "label": [
          {
            "locale": "en",
            "text": "Brand"
          }
        ],
        "state": {
          "model": "Brand"
        }
      },
      "flows": [
        {
          "name": "BrandFlow",
          "scenes": [
            {
              "name": "BrandOverview",
              "description": "Overview of Brand Documents",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "Brand"
                },
                {
                  "key": "instance",
                  "isSet": false
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "REGION_CLEAR"
                  },
                  {
                    "type": "VIEW_ADD",
                    "name": "OverviewCRUD",
                    "models": [
                      {
                        "modelType": "overview",
                        "name": "Brand-overview"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "BrandForm",
              "description": "Form showing on Brand Document",
              "matchConditions": [
                {
                  "key": "model",
                  "mustEqual": "DomainBrand"
                },
                {
                  "key": "instance",
                  "isSet": true
                }
              ],
              "sceneChange": {
                "onEnter": [
                  {
                    "type": "VIEW_ADD",
                    "name": "FormCRUD",
                    "models": [
                      {
                        "modelType": "form",
                        "name": "Brand"
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }

#### 6.5.4. Provide some sample products and brands

To be able to play around with the relationships feature we need sample data
in the form of documents. We provide a set downloadable
[here](../../../../../../static/attachments/2feb37fb6589995949047cf86e91e375be2cc2b2/d67e4eb9cd631013585fea1f220aa154/relationship-
example-documents.zip). Unpack them and move them to `./resources/documents`.

#### 6.5.5. Configure the Server

We are using the server setting with an in-memory database which gets wiped
out on every server restart. So let's instruct the server to upload the models
and documents during the start up phase.

This can be achieved by extending the `copyResources` task in
`./resources/server/build.gradle`. Add the following code at the end of the
task:

    
    
    from('../models/relationships') {
      include '*.json'
      into 'com/mgmtp/a12/platform/business-models'
    }
    from('../documents') {
        include '*.json'
        into 'com/mgmtp/a12/services/import/document'
    }

This will copy the models and documents to the correct directories for the
server to pick them up.

Next we need to instruct the server to pick the documents up by extending the
server configuration in `./resources/server/application.properties`. Add the
following line at the end of the file:

    
    
    mgm.services.core.imports.document-resources=classpath:/com/mgmtp/a12/services/import/document/*.json

You need to recompile and restart the server, if it is currently running. If
everything went well, you should now be able to see new main menu entries, and
when clicking e.g. on "Product" a list of the sample documents we have added
for product and brands is displayed.

![Sample documents for
products](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/601e290bca8d04f37a0a7900d7b2e4d6/product_documents.png)

Note, that opening one document by clicking on a row will only show the plain
form without embedded relationship components as we need to do some additional
steps described in the following.

#### 6.5.6. About the relationship

The `ProductBrand.json` relationship model which is included in the provided
model package describes the following setup:

  * The relationship is called _ProductBrand_ and its English display label is _ProductBrand_.

  * Entity 1 is in role _Product_ (for English locales displayed as _produces_) and its document model has the name _DomainProduct_

  * Multiplicity is `0…​unlimited`, meaning that an arbitrary amount (including zero) of products can be linked to the brand.

  * Entity 2 is in role _Brand_ (for English locales displayed as _is manufactured by_) and its document model has the name _DomainBrand_.

  * Multiplicity is `0…​1`. Multiplicity refers to the other entity; i.e. a product can be linked to one or no brand.

  * The Link Document model has the name _DomainProductBrand_AdditionalFieldsModel_.

  * Duplicates are not allowed which means that a product can be assigned to a brand only once.

  * The following properties are basically ignored: `associationType`, `ordered`, `navigable`, `storage`, all under `candidateConstraints`, `embeddedGroupPath`.

Please note that the relationship refers to three document models, not two!

  1. Document Model for Entity 1 (name _DomainProduct_)

  2. Document Model for Entity 2 (name _DomainBrand_)

  3. Document Model for a (Relationship) Link, i.e. for the additional fields on the links, termed the "Link Document Model" (name _DomainProductBrand_AdditionalFieldsModel_).

#### 6.5.7. UI configuration for the relationship between product and brand

There is a new engine in town: the UI relationship engine completely manages
the links. It is very powerful and customizable, see [Relationship Engine for
the Client](https://wiki.mgm-tp.com/confluence/x/E-RwBw) (mgm internal only).
Most importantly, it can be integrated into a form and placed as either a
section or a control element. The sample application showcases some variants:

  * inside of a form

  * as a section: dual pane, table list, quadro pane

  * as a control: dropdown

  * in standalone mode (without a form).

For this tutorial with a relationship between product and brands, we can
decide on which "side" the relationship should be editable. On the product
side you would assign it to brands (by creating links), and on the brand side
you would assign product to this brand. Since A12 relationships are bi-
directional and completely managed, you are free to allow editing on both
sides.

The UI relationship engine is configured via a bindingConfiguration which is
added as annotation to the Form Model of the form in which the relationship
shall be displayed.

__ |  The provided `Product.json` and `Brand.json` Form Models already contain the necessary bindingConfiguration annotations. Binding Configurations can be modeled with the A12 Simple Model Editor.  
---|---  
  
#### 6.5.8. Register the relationship extension in the appsetup

##### Setup the view for a relationship Form-Engine

We recommend using the CRUD Form Engine view which supports the integration of
the Relationship Engine by default.

The `viewFactory.tsx` should look like the following, providing the CRUD
views:

src/main/viewFactory.tsx

    
    
    import * as React from "react";
    
    import { FrameFactories } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import { CRUDViews } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    import { StaticPageFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/static-page";
    
    const staticPageComponentProvider = StaticPageFactories.createViewProvider();
    
    function createCRUDViewProvider(): (
      componentName: string
    ) => React.ComponentType<View> | undefined {
      const components: { [name: string]: React.ComponentType<View> | undefined } =
        {
          FormCRUD: CRUDViews.FormEngineView,
          OverviewCRUD: CRUDViews.OverviewEngineView
        };
      return function provider(name) {
        return components[name];
      };
    }
    
    const crudViewProvider = createCRUDViewProvider();
    
    function Placeholder(props: View): JSX.Element {
      return <div>ERROR: NO COMPONENT FOUND</div>;
    }
    
    export function viewProvider(componentName: string): React.ComponentType<View> {
      return (
        staticPageComponentProvider(componentName) ||
        crudViewProvider(componentName) ||
        FrameFactories.viewProvider(componentName) ||
        Placeholder
      );
    }

When you now would open a document from the Overview-Engine, the Relationship-
Engine would not yet be rendered inside the form, because we first need to
register the relationship extension from the Client.

##### Register relationship extension in application setup

Within the appsetup of the platform_server, we register the
`RelationshipDataProvider` and the relationship sagas with the help of
`RelationshipFactories`, and the `RelationshipReducers`.

Our final `platform_server.appsetup.ts` looks like the following. Your
appsetup may look a bit different, but make sure you set up all mentioned
relationship artifacts properly:

src/main/platform_server.appsetup.ts

    
    
    import {
      ApplicationFactories,
      ApplicationSetup,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    import { LocaleSelectors } from "@com.mgmtp.a12.client/client-core/lib/core/locale";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import {
      formEngineDataReducers,
      formEngineSagas,
      createFormEngineMiddlewares
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";
    import { CRUDFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    import { configure } from "@com.mgmtp.a12.client/client-core/lib/extensions/platform-server-connectors";
    import {
      RelationshipFactories,
      RelationshipReducers
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/relationship";
    
    import * as model from "./appmodel.json";
    
    // creating the relationshipDataProvider
    const relationshipDataProvider =
      RelationshipFactories.createRelationshipDataProvider();
    
    export function setup(): ApplicationSetup {
      // Note: ConnectionLocator needs to be configured. This can be achieved e.g. by UAA.
      const platformServerConnectors = configure({
        localeProvider: () => LocaleSelectors.locale()(config.store.getState())
      });
    
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: platformServerConnectors.loaders.dataLoaders,
        dataProviders: [
          ApplicationFactories.createEmptyDocumentDataProvider(),
    
          // add the relationshipDataProvider defined above
          relationshipDataProvider
        ]
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: platformServerConnectors.loaders.modelLoaders,
        dataHandlers,
        additionalMiddlewares: [
          ...createFormEngineMiddlewares(),
          CRUDFactories.createCRUDMiddleware()
        ],
        customSagas: [
          ...formEngineSagas,
          ...CRUDFactories.createSagas(),
    
          // add the relationship sagas
          ...RelationshipFactories.createSagas({ dataHandlers })
        ],
        dataReducers: [
          ...formEngineDataReducers,
    
          // add the Relationship specific dataReducers
          ...RelationshipReducers.dataReducers
        ],
        composeEnhancer: enableReduxDevTools()
      });
    
      return config;
    }
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

Recompile and restart the server a last time. You should now be able to open a
few products, assign a brand to each of them and then open a brand form and
see all assigned products for this brand in the dual pane.

![Assigned products for one
brand](../../../../../../static/image/2feb37fb6589995949047cf86e91e375be2cc2b2/ab10c3b1b087763fa63f804a6273681b/brand_product_relationship.png)

##### Setting the Model Graph

In our example the devtool function `setupServerConnectionForDevelopment` used
in `platform_server.index.ts` takes care of setting the Model Graph. As soon
as you using a proper authentication (e.g. UAA) you need to take care of
setting the Model Graph by yourself. A simple and safe way is to do it
immediately after the user logged in using a saga. The saga needs then to be
registered in the `customSagas` property of
`ApplicationFactories.createApplicationSetup`. The following code snippet
shows how this could look like. Mind you need to exchange
`USER_LOGGED_IN_ACTION` with the actual action which gets dispatched when the
user logged in.

Example set Model Graph saga

    
    
    import { SagaIterator } from "redux-saga";
    import { call, put, takeLatest } from "typed-redux-saga";
    import actionCreatorFactory from "typescript-fsa";
    
    import { ModelActions } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import { build as buildModelGraph } from "@com.mgmtp.a12.dataservices/dataservices-access/lib";
    import {
      ConnectorLocator,
      RestServerConnector
    } from "@com.mgmtp.a12.utils/utils-connector/lib/main";
    
    
    
    // custom saga for loading the model graph
    export function* LoadModelGraphSaga(): SagaIterator<void> {
      yield* takeLatest(USER_LOGGED_IN_ACTION, LoadModelGraphWorker);
    }
    
    // the worker of above saga
    function* LoadModelGraphWorker(): SagaIterator<void> {
      const serverConnecter =
        ConnectorLocator.getInstance().getServerConnector() as RestServerConnector;
      const modelGraph = yield* call(() =>
        serverConnecter.fetchData(buildModelGraph()).then(r => r.json())
      );
      yield* put(ModelActions.setModelGraph(modelGraph));
    }

### 6.6. Adding a New Locale

In this tutorial you will learn how to add a new locale to your Client
application. You can use the template project as starting point.

There are many parts of the application that can be localized with
functionality provided by the Client:

  * menu entries and subentries of the application frame menu

  * labels of react components of the Client core

  * labels of components of Client extensions

  * labels, error messages and warnings of the forms and overviews rendered by the A12 Engines

  * static pages

  * your custom components

#### 6.6.1. Configuring a New Locale

Let's assume, you want to add the locale "nl_NL" to your application. As a
first step you need to add this locale to the application configuration as
seen in the following code snippet:

src/main/config/dev.config.ts

    
    
    Container.config.bind(Container.identifier.Locales).toConstantValue([
      Locale.fromString("en_US"),
      Locale.fromString("nl_NL") // added locale
    ]);

This will make the new locale available for other Client functions.

#### 6.6.2. Initial Locale

If you want the newly added locale to be the initially selected locale, when
the application is started, you can achieve this by adding the locale to your
application setup.

src/main/appsetup.ts

    
    
    // ...
    
    export function setup(): ApplicationSetup {
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: []
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model,
        modelLoaders: [],
        dataHandlers,
    
        // add the initial local here
        locale: { language: "nl", country: "NL" },
    
        composeEnhancer: enableReduxDevTools()
      });
    
      return config;
    }

__ |  If you already started the application the default locale "en_US" was added to the locale storage of the application in your browser under the key `locale`. This one is preferred over the initial locale set in the application setup, therefore you need to delete this entry in order to make the initial locale take effect!  
---|---  
  
#### 6.6.3. Working with Custom Localization Resources

If you want to add a translation in the new locale, the easiest solution is to
provide a custom `LocalizationTreeMap`.

##### Creating a Custom LocalizationTreeMap

Create a new file `customResources.ts` in `./src/main/config`.

In this file add a new `LocalizationTreeMap`, in which you add your
translations for the new locale, mapped to the known localizable keys.

It could look like this small example, where only some of the available keys
are used.

src/config/customResources.ts

    
    
    import { LocalizationTreeMap } from "@com.mgmtp.a12.utils/utils-localization/lib/main";
    
    const resources: LocalizationTreeMap = {
      nl_NL: {
        application: {
          title: "Zakelijke Applicatie Platform Model"
        }
      }
    };
    export default resources;

All localizable keys, that are currently supported, can be found in the
provided `LOCALE_RESOURCE_KEYS` constant in `core/locale`. Extensions might
have their own constants. You have to reuse these keys, if you want to
localize the built-in components.

##### Provide the Custom Resources to the Localizer

In the most basic case, the application `Localizer` is created with the
`defaultLocalizerFactory` from utils-localization library. The creation of the
localizer should be part of the application setup routine.

This localizer factory function also allows to pass the custom
LocalizationTreeMap from `customResources.ts` which then contributes
additional texts. Those texts will then always be preferred over the texts
within the `Localizable` objects themselves.

In a more advanced scenario, where the `Localizer` function already is a
custom implementation itself, it is, of course, also possible to use the
custom LocalizationTreeMap in this implementation and thus refer to those
additional texts.

If you now compile and start the application, the application title should be
localized in your added locale. You might notice that you don't see any menu
entries anymore, as no translation is provided for them in the current locale.
The next section will be about how to localize them.

#### 6.6.4. Menu and case labels

If you want to localize the labels of menu entries and sidebar cases, you can
achieve this via extending the application model.

First you need to add your locale to the locales available in the model:

src/main/appmodel.json

    
    
    {
      "header": {
        "id": "Client_Template",
        "modelType": "application",
        "modelVersion": "4.0.0",
        "locales": [
          {
            "code": "en"
          },
          {
            "code": "nl_NL"
          }
        ]
      },
      // ...

For menu entries of your application model modules you can now add labels in
the added locale like this:

src/main/appmodel.json

    
    
    // ...
    "modules": [
      {
        "name": "WelcomeModule",
        "menu": {
          "name": "welcome",
          "label": [
            {
              "locale": "en",
              "text": "Welcome"
            },
            {
              "locale": "nl_NL",
              "text": "Welkom"
            }
          ],
          "state": {
            "page": "welcome_page"
          }
        },
        // ...

The same works also for submenu entries.

If you use the case feature in you application model, you can localize the
case labels in the same way, e.g.:

src/main/appmodel.json

    
    
    // ...
    "cases": [
      {
        "name": "FirstCase",
        "label": [
          {
            "locale": "en",
            "text": "Table"
          },
          {
            "locale": "nl_NL",
            "text": "Tabel"
          }
        ],
        "sceneChange": {
          "onEnter": [
            {
              "type": "VIEW_ADD",
              "name": "CaseConcept.TableCase"
            }
          ]
        }
      }
      //...

#### 6.6.5. Static pages

Static pages can be localized by using the `LocalizerContext` (from utils-
localization-react) which is setup in the application configuration.

But in order to use it, you need to provide it via the static-page-imports:

src/main/static/static-page-imports.ts

    
    
    import * as React from "react";
    
    import { ActionContentbox } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/action-contentbox/action-contentbox.view";
    import { ContentBoxElements } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/template/contentbox.tpl.view";
    import { LocalizerContext } from "@com.mgmtp.a12.utils/utils-localization-react/lib/main";
    
    declare const window: Window & {
      modules?: { [key: string]: object };
    };
    
    window.modules = window.modules || {};
    window.modules["static-page-imports"] = {
      React,
      ContentBoxElements,
      ActionContentbox,
    
      // add LocalizerContext here
      LocalizerContext
    };
    
    export {
      React,
      ContentBoxElements,
      ActionContentbox,
      // add LocalizerContext here as well
      LocalizerContext
    };

Now you can add your translation texts to the `customResources.ts` file:

src/config/customResources.ts

    
    
    import { LocalizationTreeMap } from "@com.mgmtp.a12.utils/utils-localization/lib/main";
    
    const resources: LocalizationTreeMap = {
      nl_NL: {
        // overrides the default translation from the client library
        application: {
          title: "Zakelijke Applicatie Platform Model"
        },
        // translations for application-specific use cases
        custom: {
          staticPages: {
            welcome: {
              title: "Welkom",
              heading: "Rubriek"
            }
          }
        }
      },
      en: {
        // You might want to add the locale entry for the default locale english as well
        custom: {
          staticPages: {
            welcome: {
              title: "Welcome",
              heading: "Heading"
            }
          }
        }
      }
    };
    
    export default resources;

After this you can use the localizer to localize your static page via
localized texts. E.g.:

src/main/static/pages/welcome_page.tsx

    
    
    import {
      React,
      ContentBoxElements,
      ActionContentbox,
      LocalizerContext
    } from "../static-page-imports"; // The indirection is necessary for the webpack detection
    
    export default function WelcomePage(): JSX.Element {
      const localizer = React.useContext(LocalizerContext).localizer;
      return (
        <ActionContentbox
          headingElements={
            <ContentBoxElements.Title
              text={localizer({ key: "custom.staticPages.welcome.title" })}
            />
          }
        >
          <h2>{localizer({ key: "custom.staticPages.welcome.heading" })}</h2>
        </ActionContentbox>
      );
    }

#### 6.6.6. Custom components

Your custom components can be localized in the same way as static pages using
the localization API, most specifically the `LocalizerContext`.

For example:

    
    
    import * as React from "react";
    
    import { ActionContentbox } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/action-contentbox/action-contentbox.view";
    import { ContentBoxElements } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/template/contentbox.tpl.view";
    
    import { LocalizerContext } from "../static/static-page-imports";
    
    export default function CustomComponent(): JSX.Element {
      const localizer = React.useContext(LocalizerContext).localizer;
    
      return (
        <ActionContentbox
          headingElements={
            <ContentBoxElements.Title
              key="title"
              text={localizer({ key: "customComponent.title" })}
            />
          }
        >
          <p>{localizer({ key: "customComponent.content" })}</p>
        </ActionContentbox>
      );
    }

#### 6.6.7. Forms and Overviews

The Forms and Overviews in the client are powered by the model-driven A12
Engines. How to localize these components shall not be covered in this
tutorial, but you can find details in the Engines documentation and in the
documentation of the A12 modeling tools.

#### 6.6.8. Relationship extension

Localization of Relationships is also not covered in this tutorial. You can
find details about the localization of this extension in the respective
chapter.

### 6.7. Implementing a timer with Redux Saga

The implementation of a timer is a perfect exercise to get a deep dive into
the core principles of the React/ Redux architecture which is the basis of the
Client library.

  * Views in React

  * Actions and Reducers in Redux

  * Connection of views to the Redux store

  * Asynchronous operations with Redux Saga

__ |  Please keep in mind that this tutorial covers more advanced concepts of React and Redux. If you are new to web development with JavaScript and React, we would recommend to have a look at some beginner courses first, e.g. <https://reactjs.org/community/courses.html>.  
---|---  
  
You can start this tutorial from the empty template project.

#### 6.7.1. Create a new folder

At first, we create a new folder `./src/main/components` and in there, a new
folder `./src/main/components/timer`. This second folder will contain all the
timer related functions.

#### 6.7.2. Implement the timer actions

At first, we create a new file for the timer actions.

src/main/components/timer/actions.ts

    
    
    import { actionCreatorFactory } from "typescript-fsa";
    
    const actionCreator = actionCreatorFactory("Timer");
    
    export namespace TimerActions {
      export const start = actionCreator("START");
      export const stop = actionCreator("STOP");
      export const reset = actionCreator("RESET");
      export const increase = actionCreator("INCREASE");
    }

#### 6.7.3. Implement the timer reducer

Second, we create a new file for the timer reducer. It increases the timer
state for each `increase` action by 1 and sets it to 0 for a `reset` action.

src/main/components/timer/reducer.ts

    
    
    import { Action } from "redux";
    
    import { TimerActions } from "./actions";
    
    export namespace TimerReducers {
      export interface StateType {
        status: "Stopped" | "Started";
        seconds: number;
      }
    
      export function timer(
        state: StateType = { status: "Stopped", seconds: 0 },
        action: Action
      ): object {
        if (TimerActions.start.match(action)) {
          return { ...state, status: "Started" };
        } else if (TimerActions.stop.match(action)) {
          return { ...state, status: "Stopped" };
        } else if (TimerActions.reset.match(action)) {
          return { ...state, seconds: 0 };
        } else if (TimerActions.increase.match(action)) {
          return { ...state, seconds: state.seconds + 1 };
        }
        return state;
      }
    }

#### 6.7.4. Create the timer view component

We setup a view with three buttons - start, stop and reset - and a simple text
showing the seconds of the timer.

We use the connect function of redux to connect the Timer view component with
the application's redux state.

Via the mapStateToProps function the view will be updated, when the state
changes.

Via the mapDispatchToProps function the user interactions like button clicks
trigger dispatches of redux actions which lead to state changes by the
reducers.

src/main/components/timer/view.tsx

    
    
    import * as React from "react";
    import { connect } from "react-redux";
    import { Dispatch } from "redux";
    
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import { ButtonGroup } from "@com.mgmtp.a12.widgets/widgets-core/lib/button-group/main/button-group.view";
    import { Button } from "@com.mgmtp.a12.widgets/widgets-core/lib/button/main/button.view";
    import { LayoutGrid } from "@com.mgmtp.a12.widgets/widgets-core/lib/layout/layout-grid/main/layout-grid.view";
    import { Tag } from "@com.mgmtp.a12.widgets/widgets-core/lib/tag/main/tag/tag.view";
    
    import { TimerActions } from "./actions";
    
    export interface DispatchProps {
      onStart(): void;
      onStop(): void;
      onReset(): void;
    }
    export type OwnProps = View;
    export interface StateProps {
      readonly seconds: number;
      readonly status: "Stopped" | "Started";
    }
    
    export function Timer(
      props: StateProps & DispatchProps & OwnProps
    ): JSX.Element {
      return (
        <LayoutGrid.Grid>
          <Tag>{props.seconds} seconds</Tag>
          <ButtonGroup>
            <Button onClick={props.onStart} disabled={props.status === "Started"}>
              Start
            </Button>
            <Button onClick={props.onStop} disabled={props.status === "Stopped"}>
              Stop
            </Button>
            <Button onClick={props.onReset}>Reset</Button>
          </ButtonGroup>
        </LayoutGrid.Grid>
      );
    }
    
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    function mapStateToProps({ timer: { seconds, status } }: any) {
      return {
        seconds,
        status
      };
    }
    
    function mapDispatchToProps(dispatch: Dispatch) {
      return {
        onStart: () => {
          dispatch(TimerActions.start());
        },
        onStop: () => {
          dispatch(TimerActions.stop());
        },
        onReset: () => {
          dispatch(TimerActions.reset());
        }
      };
    }
    
    export default connect<StateProps, DispatchProps, OwnProps>(
      mapStateToProps,
      mapDispatchToProps
    )(Timer);

#### 6.7.5. Create a `runTimer()` saga

After a `start` action, the redux saga function `runTimer()` should trigger an
`increase` action each second and should stop triggering it as soon as it
receives a `stop` action.

We implement the saga in a new file in our timer component.

src/main/components/timer/sagas.ts

    
    
    import {
      actionChannel,
      call,
      put,
      race,
      SagaGenerator,
      take
    } from "typed-redux-saga";
    
    import { TimerActions } from "./actions";
    
    export namespace TimerSagas {
      export function* runTimer(): SagaGenerator<void> {
        const channel = yield* actionChannel(TimerActions.start.type);
    
        while (yield* take(channel)) {
          while (true) {
            const winner = yield* race({
              stopped: take(TimerActions.stop.type),
              increase: call(wait, 1000)
            });
            if (!winner.stopped) {
              yield* put(TimerActions.increase());
            } else {
              break;
            }
          }
        }
      }
    
      const wait = (ms: number) =>
        new Promise(resolve => {
          setTimeout(resolve, ms);
        });
    }

#### 6.7.6. Register the timer reducer and saga in the application setup

Here we just show the necessary code to register the new timer reducer
function and saga, which has to be put in the `appsetup`. Other already
existing functions like `enableReduxDevTools` shall not be overwritten.

src/main/appsetup.ts

    
    
    import {
      ApplicationFactories,
      ApplicationSetup,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import { DataHandlers } from "@com.mgmtp.a12.client/client-core/lib/core/data";
    
    import * as model from "./appmodel.json";
    // import the prepared modules
    import { TimerReducers } from "./components/timer/reducer";
    import { TimerSagas } from "./components/timer/sagas";
    
    export function setup(): ApplicationSetup {
      const dataHandlers: DataHandlers = {
        dataEditors: [],
        dataLoaders: []
      };
    
      const config = ApplicationFactories.createApplicationSetup({
        model: model as ApplicationModel,
        modelLoaders: [],
        dataHandlers,
    
        // add the timer reducers
        reducerMap: { timer: TimerReducers.timer },
    
        // add the timer saga
        customSagas: [TimerSagas.runTimer],
    
        composeEnhancer: enableReduxDevTools()
      });
    
      return config;
    }
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

#### 6.7.7. Register the timer view in the `viewFactory.tsx`

src/main/viewFactory.tsx

    
    
    import * as React from "react";
    
    import { FrameFactories } from "@com.mgmtp.a12.client/client-core/lib/core/frame";
    import { View } from "@com.mgmtp.a12.client/client-core/lib/core/view";
    import { CRUDFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/crud";
    import { StaticPageFactories } from "@com.mgmtp.a12.client/client-core/lib/extensions/static-page";
    
    import Timer from "./components/timer/view";
    
    // add this interface for a map of views
    interface ViewMap {
      [name: string]: React.ComponentType<View>;
    }
    
    // create this instance of the view map which provides the Timer view
    // under the name 'Timer'
    const Views: ViewMap = {
      Timer
    };
    
    const staticPageComponentProvider = StaticPageFactories.createViewProvider();
    
    function Placeholder(componentName: string): JSX.Element {
      return <div>ERROR: NO COMPONENT FOUND</div>;
    }
    
    export function viewProvider(componentName: string): React.ComponentType<View> {
      return (
        staticPageComponentProvider(componentName) ||
        CRUDFactories.createCRUDRenderer(componentName) ||
        FrameFactories.viewProvider(componentName) ||
        // add the view map instance here
        Views[componentName] ||
        Placeholder
      );
    }

#### 6.7.8. Create a timer module in the application model

Add the following module to the modules array in the `src/main/appmodel.json`.

new TimerModule

    
    
    {
      "name": "TimerModule",
      "menu": {
        "name": "timer",
        "label": { "en": "Timer" },
        "state": { "page": "timer" }
      },
      "flows": [{
        "name": "TimerFlow",
        "scenes": [{
          "name": "TimerScene",
          "matchConditions": [{ "key": "page", "mustEqual": "timer" }],
          "sceneChange": { "onEnter": [{ "type": "VIEW_ADD", "name": "Timer" }] }
        }]
      }]
    }

#### 6.7.9. Summary

After recompiling and refreshing the page in the browser, there is a new
module `Timer` which can be selected from the menu.

It shows a simple timer with three buttons. A click on `start` will start the
counting of seconds. You can now switch to different modules, re-open the
timer module and you will notice that the timer clock is still running due to
the asynchronous code execution of the saga.

## 7\. Recipes

In the following sections we want to share best practices and recipes for
developing an A12 Client Application.

### 7.1. Writing Tests for the Client

#### 7.1.1. React Components

Testing of React components may consist of two parts:

  1. Testing the pure React component with [enzyme](https://airbnb.io/projects/enzyme/)

  2. If the React component is connected to the redux store, we recommend testing the `mapStateToProps` and `mapDispatchToProps` functions individually.

In addition, we highly recommend to stub and mock Client internal
functionality via proper libraries like [Sinon](https://sinonjs.org/) and
[TypeMoq](https://github.com/florinn/typemoq).

#### 7.1.2. ActionCreators / Reducers

In Redux, _action creators_ are functions which return plain objects. When
testing action creators, we want to test whether the correct action creator
was called and also whether the right action was returned.

A _reducer_ should return the new state after applying the action to the
previous state.

Because these functions are pure, they are easy to test without mocking.

##### Example

The following example shows one test case for an action creator. The test file
can be found in `sample-application/test/features/dataEditor/actions.spec.ts`.

    
    
    import { expect } from "chai";
    import { Action } from "typescript-fsa";
    
    import {
      commitAuthorRequested,
      CommitAuthorRequestedPayload
    } from "../../../src/modules/data_handling/dataEditor/actions";
    
    describe("@com.mgmtp.a12.client.sample-application.features.dataEditor", () => {
      describe("ActionCreators", () => {
        describe(
          "When the ActionCreator commitAuthorRequested is called with " +
            "an activity id and an onEventButtonClick callback",
          () => {
            it("creates an action of this type with the given id and a callback function as payload", () => {
              const payload: CommitAuthorRequestedPayload = {
                activityId: "1",
                onEventButtonClick: () => {}
              };
              const expectedAction: Action<CommitAuthorRequestedPayload> = {
                type: commitAuthorRequested.type,
                payload
              };
              expect(commitAuthorRequested(payload)).to.be.deep.equal(expectedAction);
            });
          }
        );
      });
    });

#### 7.1.3. DataEditor / DataLoader / ModelLoader

Whenever you have to deal with the retrieval and persistance of data or models
in your application, it is likely that you get in touch with these components.

The features documentation provides more information about the DataLoader and
DataEditor. The ModelLoader works quite the same, but is concerned with the
retrieval and persistence of models.

When testing these classes, we recommend to use a mocking library like
[TypeMoq](https://github.com/florinn/typemoq).

#### 7.1.4. Sagas

Our preferred way of testing sagas is to run the whole saga and assert that
the expected effects have occurred. Internal Client sagas should be stubbed
with a library like [Sinon](https://sinonjs.org/).

This approach is also recommended by the official [redux-saga
docs](https://redux-saga.js.org/docs/advanced/Testing.html).

##### Example

The test code can found in `sample-
application/test/features/dataEditor/sagas.spec.ts`

    
    
    import { expect } from "chai";
    import { Action } from "redux";
    import { runSaga } from "redux-saga";
    import * as Sinon from "sinon";
    
    import { ActivityActions, ActivityMap, ActivitySagas } from "../../../../core/activity";
    import { createActivity } from "../../../../test/utils/activity";
    import { commitAuthorRequested } from "../../../src/modules/data_handling/dataEditor/actions";
    import { handleCommitAuthorRequested } from "../../../src/modules/data_handling/dataEditor/sagas";
    
    describe("@com.mgmtp.a12.client.sample-application.features.dataEditor", () => {
      describe("commitAuthorSaga", () => {
        describe("When a commitAuthorRequest action is dispatched with a given activityId", () => {
          const payload = { activityId: "1" };
          const commitAuthorRequest = commitAuthorRequested(payload);
    
          const dispatched: object[] = [];
    
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          function setupAndRunSaga(state: any = { activities: {} }): Promise<any> {
            return runSaga(
              {
                dispatch(action: Action) {
                  dispatched.push(action);
                },
                getState() {
                  return state;
                }
              },
              handleCommitAuthorRequested,
              commitAuthorRequest
            ).toPromise();
          }
    
          afterEach(() => {
            dispatched.length = 0;
          });
    
          describe("When store contains an empty activity map", () => {
            beforeEach(async () => {
              await setupAndRunSaga();
            });
    
            it("dispatches a commit started activity with the given activity id", () => {
              expect(dispatched).to.deep.equal([
                {
                  type: ActivityActions.commit.started.type,
                  payload: payload
                }
              ]);
            });
          });
    
          describe(
            "When store contains some activities where one of them is dependent " +
              "on the activity for the given activityId",
            () => {
              beforeEach(async () => {
                Sinon.stub(
                  ActivitySagas,
                  "waitForResponseCancelRequested"
                  // eslint-disable-next-line require-yield
                ).callsFake(function* () {
                  return true;
                });
    
                const activities: ActivityMap = {
                  1: createActivity({ id: "1" }),
                  2: createActivity({ id: "2", initiatingActivityId: "1" })
                };
    
                await setupAndRunSaga({ activities });
              });
    
              it("dispatches a commit started activity with the given activity id", () => {
                expect(dispatched).to.deep.equal([
                  {
                    type: ActivityActions.cancelRequested.type,
                    payload: { activityIds: ["2"] }
                  },
                  {
                    type: ActivityActions.commit.started.type,
                    payload: payload
                  }
                ]);
              });
            }
          );
        });
      });
    });

## 8\. Frequently Asked Questions

Since Client 1.0, we collect questions that are asked frequently. Please
address new questions to Technical Professional Services - we will answer them
here if they are of general interest.

### 8.1. General

#### 8.1.1. How to define the initial locale of the application?

This is described in the Section Localization > Current Locale.

#### 8.1.2. How to connect a different Backend?

Client provides the `DataLoader` API for this purpose. You can register your
own loaders in the setup.

Have a look at the integration of the A12 server into the sample application -
it uses the provided connectors which themselves are an extension on top of
the core.

#### 8.1.3. How to enable Redux DevTools in the Client?

The Redux DevTools provide a store enhancer which can be passed as parameter
when calling the factory function
`ApplicationFactories.createApplicationSetup`. A function creating the
enhancer could look like this:

    
    
    import { ComposeEnhancer } from "@com.mgmtp.a12.client/client-core/lib/core/application/internal/factories";
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    
    /**
     * Trick to enable Redux DevTools with TS: see https://www.npmjs.com/package/redux-ts
     */
    export function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }

### 8.2. Engines

#### 8.2.1. How to render a UI engine?

The following module from the application model contains one scene which
renders the Overview-Engine for the model `CRUD-overview` when this scene
matches an activity with the specified match conditions.

    
    
    {
      "name": "CRUD Module",
      "menu": {
        "name": "crud",
        "label": { "en": "CRUD" },
        "activityDescriptor": { "model": "CRUD" }
      },
      "flows": [
        {
          "name": "CRUD Flow",
          "scenes": [
            {
              "name": "CRUD Overview Scene",
              "matchConditions": [
                  { "key": "model", "mustEqual": "CRUD" },
                  { "key": "instance", "isSet": false }
              ],
              "sceneChange": {
                "onEnter": [
                  { "type": "REGION_CLEAR" },
                  {
                    "type": "VIEW_ADD",
                    "name": "OverviewCRUD",
                    "models": [ { "modelType": "overview", "name": "CRUD-overview" } ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }

The Client first loads all models that are listed in all `VIEW_ADD` directives
of that scene and puts them into the Redux store. It also loads the referenced
models, if these have not already been loaded. In this example, it is the
`CRUD-overview` overview model as well as the referenced `DomainCRUD` document
model.

As soon as the relevant models for the specified view `OverviewCRUD` are
available, the ui component itself selects the appropriate models from the
store and uses them to initialize and render the Overview-Engine.

Please keep in mind that each scene working with A12 models requires a key
`model`. The value for this `model` key must match the model you specify in
the models list of the `VIEW_ADD` directives. Of course, you may add
additional document models which will be loaded into the store and can be used
for project specific operations.

**Remark:** From the `model` key, the Client derives the specific model names
(for data and UI models), i.e.

  * **Document model:** `Domain` and the value of the key `model`, e.g. `DomainCRUD`

  * **Form model:** just the value of the key `model`, e.g. `CRUD`

  * **Overview model:** the value of the key `model` and `-overview`, e.g. `CRUD-overview`

#### 8.2.2. How to render two UI engines for distinct document models?

You need to add another scene into your module to render more than one UI
engine in the same content area.

You can find an example in the sample application under `features > Dashboard
> Multiple Activities`. The example dashboard contains two tiles with static
content, one tile with an Overview-Engine for the `CRUD` models and another
tile with an Overview-Engine for the `Offer` models.

##### DO NOT add another `VIEW_ADD` directive for a different UI engine

Please be aware that it is not possible to use just one scene for rendering
two UI engines. You could think that we take the module from above and simply
add another `VIEW_ADD` directive, e.g.

    
    
    {
      "name": "CRUD Overview Scene",
      "matchConditions": [
        { "key": "model", "mustEqual": "CRUD" },
        { "key": "instance", "isSet": false }
      ],
      "sceneChange": {
        "onEnter": [
          { "type": "REGION_CLEAR" },
          {
            "type": "VIEW_ADD",
            "name": "OverviewCRUD",
            "models": [ { "modelType": "overview", "name": "CRUD-overview" } ]
          },
          {
            "type": "VIEW_ADD",
            "name": "OverviewCRUD",
            "models": [ { "modelType": "overview", "name": "Offer-overview" } ]
          }
        ]
      }
    }

The second `VIEW_ADD` directive wants to initialize the Overview-Engine for
the `Offer-overview` model which references the `DomainOffer` model.

Note that the match conditions for this overall scene only have one `model`
key. Its value is `CRUD`. The Client is not able to successfully render this
second Overview-Engine, because it expects `CRUD` models and documents.

#### 8.2.3. How to compute values / modify document with Form-Engine?

In Client, you should never change the document inside the Form-Engine state.
It will create an inconsistency between engine and store. Instead, you should
change the document in `activity.data` \- which in turn should update the
engine document. The Form-Engine's internal document should only be used in
non-standard based scenarios.

We provide the `FormEngineStateAdapter` exactly for this reason. It allows you
to pass a document from the store to the Form-Engine. Please refer to the [API
documentation of
`FormEngineStateAdapter`](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-
bundle/typedoc/modules/extensions_form_engine.formenginestateadapter-1.html)
for more details.

### 8.3. Miscellaneous

#### 8.3.1. How to get access to the Client git repository?

The Client git repository can be found on the [mgm
Bitbucket](https://bitbucket.mgm-tp.com/projects/A12/repos/client/browse) (mgm
internal only).

Every mgm employee has access to this git repository and if not they can be
requested to the mgm TPI team.

After this, the following folder structure will be created in the local file
system:

    
    
    ├── core
    ├── documentation
    ├── template
    └── build.gradle

The folders are

  * **core** ; contains the platform code (core, extensions, devtools) and the sample application (devapp) used by developers as a showcase. This module should be used only by Client developers and is not intended for external usage (by client projects for example). Application developers should be using this module as npm package, not the source code itself.

  * **template** ; contains template code which demonstrates how initial setup of the Client might be. Intention here is to be used as a template / starting point by the client projects.

In this tutorial we are going to focus **only** at the **template** module.

## 9\. Troubleshooting

### 9.1. Redux DevTools out of sync for some Activity properties

All deprecated properties in the activity which has been moved to the data
holder might be out of sync when inspecting them in the Redux-DevTools. Make
sure to inspect the respective data holder instead, i.e. the data holder whose
descriptor is equal to the activity descriptor.

The following properties are affected:

  * data

  * dirty

  * busy

  * loadingState

  * savingState

  * error

  * slices

  * datasourceActivityId

You do not need to worry when accessing these properties in the code. Since
activities are always accessed via selectors from the store, the runtime make
sure that all of them have the correct values.

### 9.2. Views are remounting on every render

If you experience constant remounting of your React components, please check
your usage of `FrameFactories.createProgressComponentProvider`. Since this
factory will create a new provider on each execution, make sure to call it
only once outside of React's rendering lifecycle.

## 10\. Migration

This chapter collects migration guides for different parts of the Client which
changed from one version to another.

The following migration guides are contained:

  * How to migrate Application Models from TypeScript to JSON

  * How to migrate to the Kernel API

  * How to migrate from the Form-Engine to the Form-Engine

  * How to migrate from the Overview-Engine to the Overview-Engine

### 10.1. Migration to JSON Application Models and the latest Application
Model Version

This section covers how to migrate application models from TypeScript code to
json files. This should be done to enable the application model migration tool
to handle these json files.

If your existing application models were created with the Simple Model Editor
(SME), they should already be JSON files. However, the SME before version
2.0.0 stored the application models in a slightly different structure that
contains a wrapper around the actual application model. Please see Align SME
Application Models to find out how to do this.

#### 10.1.1. TS Code to JSON Migration

[JavaScript To JSON](https://www.convertonline.io/convert/js-to-json)

Above website offers a JavaScript code to JSON migration. In order to use it
successfully, the complete Application Model object needs to be copy-pasted
into the respective text area. The resulting JSON will be printed into the
bottom text area automatically. This json must be copied into a new file in
your project. Let us assume it is called "app_model.json".

If data privacy is critical, you can also migrate your current application
model from JavaScript to JSON by using the following script:

conversion.js

    
    
    const { applicationModelVariableName: applicationModel } = require("./path/to/the/app-model.js");
    console.log(JSON.stringify(applicationModel));

You have to replace `"./path/to/the/app-model.js"` with the path to your `app-
model.js` and `applicationModelVariableName` with the export name of your
application model. Common names are `appModel` or `applicationModel`.

Afterwards, you just execute:

    
    
    node migration.js

The resulting console output then needs to be copied into the new json file of
your project.

#### 10.1.2. Align SME Application Models

The output of an older SME version will look similar to this:

app_model_from_sme.json

    
    
    {
      id: "-1",
      appModel: {
        name: "MyAppModel",
        languages: ["en"],
        modules: [],
        ...
      }
    }

In order to get the expected structure, the surrounding brackets, the id, its
value and the appModel property need to be removed.

The result should look like follows:

updated_app_model.json

    
    
    {
      name: "MyAppModel",
      languages: ["en"],
      modules: [],
      ...
    }

#### 10.1.3. Application Model Migration to Version 1.0.0

After migrating the application model to JSON, it has to be updated to the
latest version by applying the newly introduced appmodel-migration tool to
them.

For this, install the migration tool with

    
    
    npm install -g @com.mgmtp.a12.client/client-application-model-migration

Now you can run it to migrate your "app_model.json" file to the latest
version.

    
    
    appmodel-migration <path to app_model.json> -b

The given path can also point to a directory which will be searched
(recursively) for application model json files which will then be migrated
together.

Note: The (optional) -b argument creates a backup of your model file before
migration in case you do not have it under version control and might need to
reset to this state again later on.

#### 10.1.4. Import Application Model from JSON in Your Project

    
    
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import * as model from "./app_model.json";
    
    const appModel = model as ApplicationModel;

Above code shows how this "app_model.json" file can be imported and then used
as an Application Model. In order for the compiler to accept this code, the
TypeScript compiler option "resolveJsonModule" must be enabled. This is
usually done in the tsconfig.json which holds your project's compiler
settings.

### 10.2. Migration to new Kernel API

This chapter will cover how to migrate to the new Kernel API. This changes are
necessary if you want to use the new Form-Engine or Overview-Engine.

#### 10.2.1. NPM Dependencies

To use the new Kernel API in your application you have to add the following
packages to your application:

  * @com.mgmtp.a12.kernel/kernel-md-facade

  * @com.mgmtp.a12.kernel/kernel-core-runtime-api-ts

#### 10.2.2. DocumentLoader and DataProvider

In case you write your own document loader or data provider it is required to
transform the document in a desirable runtime format. Therefore, you have to
call the following before it is stored in the Redux store.

    
    
    const runtimeDocument = new DocumentServiceFactory().getDocumentService().parseDates(documentJson, documentModel);

This API also provides the inverted functionality, when you want to send the
document to the server.

    
    
    const documentJSON = new DocumentServiceFactory().getDocumentService().formatDates(runtimeDocument, documentModel);

#### 10.2.3. Models in Store

We provide model loader for document models that injects the generated code
into the document model. The structure can be checked by
`Model.isDocumentValidationModel`.

### 10.3. Form-Engine Migration

This section will be about how to migrate from the old deprecated Form-Engine
to the new Form-Engine in the Client. It will just explain how the integration
and basic configuration of the engine can be migrated. The complete migration
concerning the engine is contained in the Engines documentation.

The migration contains the following parts:

  * Prerequisites

  * Changes in the appsetup

  * Changes concerning the view

#### 10.3.1. Prerequisites

##### NPM Dependencies

To use the new Form-Engine in your application you have to add the following
package to your application:

  * @com.mgmtp.a12.formengine/formengine-core

##### New Kernel-API

In order to work with the new Form-Engine you have to migrate to the new
Kernel-API before. You can find the migration guide for the new Kernel-API
here

#### 10.3.2. AppSetup

In order to use the Form-Engine in your project you have to

  * call `createFormEngineMiddlewares` and add the returned middlewares to the `additionalMiddlewares`

If you need to customize your middlewares (like setting up an external
enumeration provider or disabling boolean coalescing), you have to pass your
`MiddlewareOptions` directly. Do not call `createEngineMiddlewares`
separately, as the engine middlewares need to be wrapped to receive the
correct state. `createFormEngineMiddlewares` does this automatically.

  * add the `formEngineSagas` to your customSagas

  * add the `formEngineDataReducers` to your activity reducers.

Your setup should than look somehow like this:

    
    
    import { ApplicationFactories } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    import { ApplicationModel } from "@com.mgmtp.a12.client/client-core/lib/core/model";
    import {
      formEngineDataReducers,
      formEngineSagas,
      createFormEngineMiddlewares
    } from "@com.mgmtp.a12.client/client-core/lib/extensions/form-engine";
    
    import * as appModel from "./appmodel.json";
    import { dataHandlers } from "./dataHandlers";
    
    ApplicationFactories.createApplicationSetup({
      additionalMiddlewares: [...createFormEngineMiddlewares()],
      customSagas: [...formEngineSagas],
      model: appModel as ApplicationModel,
      modelLoaders: [],
      dataHandlers: dataHandlers,
      dataReducers: [...formEngineDataReducers]
    });

#### 10.3.3. ViewViews.FormEngine

The view component `ViewViews.FormEngine` was deprecated and replaced by
`FormEngineViews.FormEngineView`. This view accumulates already the
ScrollHandler, ContentBox and Form-Engine and is a connected component, which
receives the current state as props. Configuration is done via props, which
have now a slightly different structure than before.

##### additionalOptions

You can now give all the additionalOptions directly to the `FormEngineView`.
This means instead of writing

    
    
    export function viewViewsComponentProvider(props: View): JSX.Element {
      const additionalOptions = {
        cardView: true
      };
      return (
        <ViewViews.FormEngine {...props} additionalOptions={additionalOptions} />
      );
    }

you can now write:

    
    
    export function formEngineViewsComponentProvider(props: View): JSX.Element {
      return <FormEngineViews.FormEngine {...props} cardView={true} />;
    }

##### readonly

If the engine is readonly is now determined by the UI-state of the engine,
therefore this can not be set via a props anymore. You can change the UI-state
of the Form-Engine by dispatching the following action:

    
    
    FormEngineActions.command({
      activityId: formEngineActivityId,
      engineEvent: Commands.setReadonly(true)
    });

In this example the activityId must be the id of the activity which holds the
Form-Engine UI-state.

Keep in mind that the engine state has to be initialized before you can
dispatch this action! With the selector `FormEngineSelectors.engineState` you
can select the Form-Engine state from an activity. It will return undefined if
no such state is present.

You also have the possibility to connect the Form-Engine yourself. In this
case you can decide in `mapStateToProps` if the engine should be readonly or
not. In the section Connecting a custom view you can find more information on
how to connect the Form-Engine by yourself.

##### Events

There are no callback functions anymore for events. Every event coming from
the UI, like a clicking on an EventButton triggers an Event-Action. This event
actions are treated in middlewares, which dispatch Command-Actions to trigger
a store change.

The Client wraps this actions into a FormEngineEventAction, which contains
next to the original engineEvent-action the activity id. In order to react to
the events or commands you have to register middlewares, sagas or reducers
which are listening to the corresponding actions.

The following part describes how your code which handles the old event-
callback could be rewritten to work with the new Form-Engine. All the examples
use middlewares, which you need then to register as additionalMiddlewares in
the appsetup. It is also possible to write sagas, which you need then to
register as customSagas in the appsetup.

###### onEvent

If the form-engine dispatches a generic event, the action
`FormEngineEventAction.event` with the engineEvent `Events.eventButton` will
be dispatched by the Client. If you want to react to an event you have to
register a middleware which listens to this action.

This means if your old code looked something like this:

    
    
    export function viewViewsComponentProvider(props: View): JSX.Element {
      return <ViewViews.FormEngine {...props} onEvent={handleOnEvent} />;
    }

You now have to write and register a middleware which should look like this:

    
    
    export const onEventButtonClickedMiddleware: Middleware<{}, EngineState> =
      api => next => action => {
        if (
          FormEngineActions.event.match(action) &&
          Events.eventButton.match(action.payload.engineEvent)
        ) {
          const event = action.payload
            .engineEvent as Action<Events.EventButtonPayload>;
          handleOnEvent(event.payload.name);
        }
    
        return next(action);
      };

###### onRowEvent

In order to react to customRowActions you have to register a middleware which
listens to `Events.Repeat.customRowAction`. The middleware looks similar to
the one described in onEvent.

###### onValueChanged

When the user changes an input, the new Form-Engine will already parse the
input in the UI. If the input was valid the engine dispatches an
Events.valueChange action. If the value was invalid, e.g. a string was put in
a number field, the engine dispatches an Events.parseError action. In order to
react to this changes you have to register middlewares.

The event actions are dispatched by the UI and the actual document is not
changed yet. The default middleware from the Form-Engine will handle these
changes, conduct computations and the setting of dependent values and will in
the end dispatch a command action to set the actual data, as well as an action
to set the message state, if it changed.

If you want to react to a change in the document you should register a
middleware which compares the document before and after an action was treated
by all other middlewares and reducers.

This is the recommended way. However, you can also directly listen to the
command action `ActivityActions.setData` which is always dispatched by the
Form-Engine to set a changed document in the store. To be sure that the
document really changed you can compare the document before and after the
action was treated. But be aware, that also other middlewares or reducers
outside of the Form-Engine could change the document as well!

###### onValidationStateChanged

In order to react to changes of the validation state you can register a
middleware which listens to `Commands.setMessageState`. The middleware looks
similar to the one described in onEvent.

#### 10.3.4. CRUD

If you used the CRUD view `CRUDForm` before in your application model, you
need to register your own view which uses the `FormEngineViews.FormEngineView`
now. You cannot use the function `CRUDFactories.createCRUDRenderer` anymore,
because this one will return the deprecated `ViewViews.FormEngine`.

You also need to add the `CRUDFactories.createCRUDMiddleware()` in your
appsetup. For more information see Working with A12 Models.

### 10.4. Overview-Engine Migration

This section will be about how to migrate from the old deprecated Overview-
Engine to the new Overview-Engine in the Client.

The migration contains the following parts:

  * Prerequisites

  * Changes concerning the view

#### 10.4.1. Prerequisites

##### New Kernel-API

In order to work with the new Overview-Engine you have to migrate to the new
Kernel-API before. You can find the migration guide for the new Kernel-API
here

#### 10.4.2. ViewViews.OverviewEngine

The view component `ViewViews.OverviewEngine` was deprecated and replaced by
`ViewViews.OverviewEngineView`.

#### 10.4.3. CRUD

If you used the CRUD view `CRUDOverview` before in your application model, you
need to register your own view which uses the `CRUDViews.OverviewEngineView`
now. You cannot use the function `CRUDFactories.createCRUDRenderer` anymore,
because this one will return the deprecated `ViewViews.OverviewEngine`.

You also need to add the `CRUDFactories.createCRUDMiddleware()` in your
appsetup. For more information see Working with A12 Models.

## 11\. API Documentation

The API documentation can be found
[here](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-bundle/typedoc/index.html).

## 12\. Migration Instructions

### 12.1. 2022.06

#### 12.1.1. Breaking Changes

##### Integration of dependencies

The versions of the A12 dependencies were increased. Please see documentation
of the respective products for further migration instructions.

##### Appmodel migration

For the following changes, the appmodel version was increased. Please refer to
the general application model migration section to find out how to perform the
migration.

###### New localization API

As part of a larger effort to improve the localization, multiple changes were
done. To get an overview, please see the documentation of Utils for more
details about new interface / typings and the general concept of the new
localization approach first.

Every type usage of old localization interfaces, like `ILocalizerService` and
`ILocalizable`, was replaced with their new counterparts, like `Localizer` and
`Localizable`, causing changes in multiple locations. In the same way,
localized texts, which were previously typed as `string`, were changed to use
the new localization typings as well. Please see the [API
documentation](../../../../../../content/2022.06/CLIENT/12/asciidoc/client-
documentation-bundle/typedoc/index.html) about all affected places.

All label properties inside the namespace `ApplicationModel` were changed to
use the new type `LocalizedModelText`.

The following exports were removed from the `core/locale` module, because they
were replaced or not needed anymore with the new localization.

    
    
    LocaleFactories
    LocalizedResourceBundle and ResourceBundle
    LocalizableDescriptor and Localizer
    LocaleHooks

The `LocalizerService` symbol for the inversify container was removed.

    
    
    export const Container = {
      config: new InversifyContainer(),
      identifier: {
    
        Locales: Symbol("Locales"),
        // LocalizerService is not necessary anymore
    
        // others...
      }
    };

Note that the `Locales` symbol is still included.

For examples on how to use the new localization API in client, please see the
examples in the Utils documentation.

###### Improved typing of ApplicationModel.Menu

To improve the modelling of module menus in the SME, the `state` property of the interface `ApplicationModel.Menu` was renamed to `activityDescriptor`. In addition, its typing was improved from `any` to `{ readonly [key: string]: string | undefined }`. If your menu state does not conform to this type, you will have to update it manually (for example, if your values were to be numbers, by converting them into strings).

###### Main Menu optional for Modules

The `menu` property of the interface `ApplicationModel.Module` was made
optional. This was done to allow specifying modules that do not want or need
an entry in the main menu. If your code expects this property to exist, you
will need to update it to check for the existence of a module menu and handle
it accordingly.

###### Clarified use of View and Container

The property `ComponentProvider` of the interface `View` was renamed to
`Provider`. This was done to align the api with other providers like the
`LayoutProvider`. In the course of this, additional renamings were done:

For the client core:

Before | After  
---|---  
`FrameViews.ProviderProps.viewComponentProvider` | `FrameViews.ProviderProps.viewProvider`  
`FrameFactories.viewComponentProvider` | `FrameFactories.viewProvider`  
`ModuleRegistryProvider.getViewComponentProvider` | `ModuleRegistryProvider.getViewProvider`  
  
For the `static-page` extension:

Before | After  
---|---  
`StaticPageExternalViewComponentProvider` | `StaticPageExternalViewProvider`  
`StaticPageFactories.ViewComponentProvider` | `StaticPageFactories.ViewProvider`  
`StaticPageFactories.createExternalViewComponentProvider` | `StaticPageFactories.createExternalViewProvider`  
`StaticPageFactories.createViewComponentProvider` | `StaticPageFactories.createViewProvider`  
  
To adapt to these changes, please update your imports.

The property `container` of the interface `ApplicationModel.Directive.Add` was
renamed to `name`. Additionally, the property `container` of the interface
`Relationship.ComponentConfiguration` was renamed to `name` as well. This
change was done to clarify that this property should specify the name of the
rendered ui component (the view).

##### New features

###### Removal of ContentBoxRenderMap

The property `contentBoxRenderMap` was removed from the type
`EngineCompositionProps`.

    
    
    // FormEngineContentBoxRenderer.PropsType was removed
    export type EngineCompositionProps = View &
    FormEngineRenderer.PropsType &
    ScrollHandlerProps;

It is no longer necessary to wrap the `FormEngineRenderer` component inside of
the `FormEngineContentBoxRenderer` component. If your setup looked like this:

    
    
    import {
      FormEngineContentBoxRenderer,
      FormEngineRenderer,
      ScrollHandler
    } from "@com.mgmtp.a12.formengine/formengine-core/lib/view";
    
    <ScrollHandler {...props}>
      <FormEngineContentBoxRenderer {...props} config={config}>
        <FormEngineRenderer {...props} config={config} />
      </FormEngineContentBoxRenderer>
    </ScrollHandler>

remove the wrapper and just use the `FormEngineRenderer` on its own. To
customize the Contentbox of the form engine, please use the `widgetMap`
property and supply your own `ActionContentbox` widget.

    
    
    import {
      FormEngineRenderer,
      ScrollHandler
    } from "@com.mgmtp.a12.formengine/formengine-core/lib/view";
    
    <ScrollHandler {...props}>
      <FormEngineRenderer {...props} config={config} />
    </ScrollHandler>

This change was done because the component `FormEngineContentBoxRenderer` was
deprecated with form engine 34 and should not be used anymore. For additional
information, please see the [migration instructions of the form
engine](../../../../../../content/2022.06/ENGINES/34/asciidoc/formengine-
documentation-bundle/index.html#_migration_instructions).

###### Removal of stylus

The previously used `Stylus` library used for styling and theming was removed
in favor of using `styled-components`. Because of this switch, the dependency
to `@com.mgmtp.a12.widgets/widgets-styles` was removed. Please see the
[widgets documentation](https://a12.mgm-tp.com/showcase/#/) for more
information and detailed migration instructions.

###### Form Engine UI State moved

The data holder responsible for holding the form engine state was removed. The
data is now accessible within the `uiState` slice of the default data holder.
For example, if you want to provide an initial form engine state, you can
create an activity like so:

    
    
    ActivityActions.create({
      activityDescriptor: { someKey: "some value" },
      slices: { uiState: { readonly: true } } // set up your ui state here
    })

Here, the Form Engine will be set to readonly. When only a partial state is
provided (like here), the remaining values will be set to their default
values.

###### Amount of filtered entries displayed

The property `totalDocumentsCount` of the interface
`Activity.Data.DocumentListData` was changed changed to include `undefined`.
Therefore, the interface now looks like this:

    
    
    export interface DocumentListData {
      readonly documents: (Activity.Data.Document | undefined)[];
      readonly totalDocumentsCount: number | undefined;
    }

This was done to reflect the fact that when using infinite scrolling the
document count is not known until the first server request returned with the
actual data. If your code expects `totalDocumentsCount` to always be of type
`number`, you will need to update it to check whether its defined or not and
react accordingly.

##### Development

###### Redux DevTools Integration

The parameter `storeEnhancer` for the function
`ApplicationFactories.createApplicationSetup` was replaced with
`composeEnhancer`. This was done to fix a bug that prevented actions that were
dispatched via the redux dev tools from triggering their respective
middlewares. If you currently use the redux devtools integration in your code
like this:

    
    
    import { StoreEnhancer } from "redux";
    
    import { ApplicationFactories } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION__?(): StoreEnhancer;
    };
    
    function enableReduxDevTools(): StoreEnhancer | undefined {
      return typeof window !== "undefined" && window.__REDUX_DEVTOOLS_EXTENSION__ !== undefined
         ? window.__REDUX_DEVTOOLS_EXTENSION__()
         : undefined;
    }
    
    const config = ApplicationFactories.createApplicationSetup({
      // ...
      storeEnhancer: enableReduxDevTools()
      // ...
    });

, you will need to adapt the following code:

    
    
    import {
      ApplicationFactories,
      ComposeEnhancer
    } from "@com.mgmtp.a12.client/client-core/lib/core/application";
    
    declare let window: Window & {
      __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: ComposeEnhancer;
    };
    
    function enableReduxDevTools(): ComposeEnhancer | undefined {
      return typeof window !== "undefined" && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ !== undefined
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        : undefined;
    }
    
    const config = ApplicationFactories.createApplicationSetup({
      // ...
      composeEnhancer: enableReduxDevTools(),
      // ...
    });

Notice that while the previous `StoreEnhancer` was imported from `redux`, the
new `ComposeEnhancer` is imported from the client core.

###### RESOURCE_KEYS removed from breaking change management

All resource keys will be excluded from breaking change management in the
future. New features, that require some kind of default localization, could
not be implemented in a non-breaking way in the past. This change was
necessary to get rid of this restriction.

The following objects are affected:

  * CDM_RESOURCE_KEYS

  * CRUD_RESOURCE_KEYS

  * DIRTY_HANDLING_RESOURCE_KEYS

  * FRAME_RESOURCE_KEYS

  * HETEROGENEITY_RESOURCE_KEYS

  * LOCALE_RESOURCE_KEYS

  * LOCALE_SELECT_RESOURCE_KEYS

  * RELATIONSHIP_RESOURCE_KEYS

#### 12.1.2. Deprecation

##### Form Engine UI State moved

The `slice` property of the interface `Activity` was deprecated with client
12.0.0. It will be removed in the future, because it is not very usable due to
the impossibility to change this property after creation. Please use the
`slices` property of the default data holder instead. See the documentation of
the data holders on how to modify properties inside a data holder.

### 12.2. Application Model Migration Tool

To migrate your application models, first install or update the migration tool
with

    
    
    npm install -g @com.mgmtp.a12.client/client-application-model-migration

Then run the following command to perform the migration:

    
    
    appmodel-migration <path to appmodel files> -b

Note that if the given path points to a directory instead, it will be searched
recursively for app models to migrate. In case you do not have your app models
under version control, you can set the optional `-b` flag to create backups of
your models. Use the `-h` flag to display all available options.

* * *

1. Knowing _which_ model(s) to load, is the responsibility of the selected data loader; the details will be described later on. 

2. While mixing loading data from parent activities and services is possible, we focus on the most common type here to keep things simple. 

3. Note that multi step wizards can also be realized with just one form by using one screen per step. 

Last updated 2023-01-30 18:18:17 +0100

