Compiling the MQTT specification takes place in three stages : 
The first stage involves writing the various functionalities of MQTT in the PlusCal-2 language, which serves as input to the next phase. 
This next phase includes a PlusCal-2 compiler that translates these into TLA+ specifications. 
The compiler goes through four steps to perform this translation of a PlusCal-2 algorithm. 
The PlusCal-2 parser provides a complete view of the syntax and structure of a PlusCal-2 algorithm, enabling the detection of syntax errors. 
When an incorrect syntax is detected, the user is informed via an error message specifying the error's location in the file.
Once syntax errors have been checked, the parser generates an abstract syntax tree (AST) for the algorithm and sends it to the PlusCal-2 normalizer. 
The latter traverses the AST to simplify complex constructs specific to PlusCal-2 but which cannot be directly represented in TLA+. 
Next, the PlusCal-2 translator converts the AST into blocks of statements identified by labels in an intermediate language format. 
This intermediate language organizes all the information needed to generate the TLA+ specifications. 
The main aim of the PlusCal-2 translator is to simplify the structure and layout of data in PlusCal-2 algorithms, making it easier to create TLA+ specifications and configuration data for the TLC model checker. 
Finally, the TLA+ code generator is responsible for creating the TLA+ specification. It considers all the data collected in the previous stages and builds an essential structure for a TLA+ module. More specifically, the primary role of this phase is to produce two files for the TLC model checker. The first file, called "TLA", contains the TLA+ specifications for the algorithm, while the second file, the configuration file, contains the algorithm's configuration parameters.\\
The command used to launch the PlusCal-2 compiler is as follows: java pcal [file name].pcal
