
The SIGIRO project seeks to create an intelligent system for managing water resources in Marrakech-Safi and Tunisia's northwest regions. 
The project introduces a systematic monitoring process to ensure adaptive control to address climate change. SIGIRO gathers data using the MQTT protocol, 
which has been the target of several cyberattacks in recent years. The absence of a formal description of these attacks leaves the field open to interpretation, 
leading to distinct implementations for a given attack. We formalize these attacks, provide descriptions, and check their exactness. 
We offer a systematic approach to formalizing seven attack scenarios targeting the MQTT protocol. Using the LTL temporal logic formalism, we generate 12 LTL formulas, 
each precisely describing a specific attack scenario. We classify these formulas into four categories according to a sequence of observation and injection events. 
These events are the abstract elements needed to control the attacks' implementation. We verify our proposed formulas using the TLC Model Checker. We show the procedure 
to encode the LTL formula using TLA+ language. For each attack formula, the verification process generates a counterexample proving the occurrence of the formalized attack. 
These counterexamples model the execution sequence leading to the breach while providing key metrics such as the number of states generated, the number of pending states, 
the elapsed time, and the identification of redundant states. Based on the execution traces obtained, we formulate proposals for enhancing the specification of the MQTT protocol.
