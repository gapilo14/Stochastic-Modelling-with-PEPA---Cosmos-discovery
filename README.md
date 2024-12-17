# Celestia Blockchain Optimization
This project focuses on analyze an optimizing the performance of [Celestia](https://celestia.org/), a modular blockchain platform. 

## Objectives
Celestia Blockchain Optimization is a project related to the [Formal Methods for System Verification](https://www.unive.it/data/insegnamento/398280) course of the [Computer Science and Information Technology](https://www.unive.it/web/en/7056/home) course of the [Ca' Foscari University of Venice](https://www.unive.it/pag/13526). 
The course objective is to understand the behaviour of a system (blockchain-related), analyze it formally, propose the encoded version with the [PEPA](https://www.dcs.ed.ac.uk/pepa/) algebra and compute some performance analysis. 

## About Celestia
Celestia separates key blockchain functions consensus, data availability, and execution enabling scalability and flexibility compared to traditional monolithic blockchains like Bitcoin and Ethereum. 
One key feature of Celestia is Data Availability Sampling (DAS) that ensures scalability and accessibility by allowing lightweight nodes to verify data availability without storing it entirely. 
Unfortunally this double the block creation time respect Cosmos, the original blockchain analyzed, requiring diferent timeouts and time increasers. 

## Our contribution
The presentation contains our formal analysis of Celestia. We started from Cosmos, another blockchain oerating with the same behavious.
After observing the new system behavious we computed performance metrics starting from the steady state distribution of Celestia's components. In the metrics section we also proposed the optimal parammeters to increase the throughput on the "commit" component of the Celestia blockchain.

## Further information
For further informations, feel free to get in touch with the contriibutors [Gabriele Pilotto](mailto:gapilo.14@outlook.com) and [Pietro Visconti](mailto:pietro.visconti2001@gmail.com).
