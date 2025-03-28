The structure of python packages, modules and classes demonstrates the Requirements Analysis and Software Architecture Design Approach

Demonstrates Functional Decomposition, Abstraction and Extensibility 

Re "Treat the shelf like a database to the extent possible, would you store Pandas DataFrames in a database?" - some comments -  shelf is object 
key/value DB, while the output from the Stats Models has Tabular Data Model/Structure - that lands itself more naturally to Tabular Data Structures
like Pandas and Relational DB. Nevertheless all persistence is implemeneted to fit native key/value DB approach as per the requirements 

A more "profitable approach" even when using key/value db would be to persist the Pandas DFs (tabular data structures) and then read, casche and query them in RAM 
during the session of the UI Manager (of course in PROD context, analysis of volumetrics feasibility would play a role too)

Note: On purpose, only one unit test is implemented, focused on the Data Manager module to demonstrate the overall approach to testing  (while at the same time saving 
time considering that this is a demo task). The use of fixtures for test preparation and test data reuse is demonstrated too 

print() instead of logging is used for more straighforward and streamlined visualization of intermediate numerical results from the app, considering it is a toy example