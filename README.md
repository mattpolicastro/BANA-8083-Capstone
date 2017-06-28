---
title: MS-BANA Analytics Capstone
author: Matt Policastro
---

## Summary

This repository contains all writing, code, and process documents related to the capstone project undertaken to satisfy the requirements of the MS of Business Analytics program at the University of Cincinnati's Lindner College of Business. This capstone performs a smaller-scale replication of [Liu and Cho's work](http://cho.pol.illinois.edu/wendy/papers/talismanic.pdf) (in collaboration [with Wang](https://experts.illinois.edu/en/publications/pear-a-massively-parallel-evolutionary-computation-approach-for-p)) on identifying biased electoral district schemes in a new context.

Instead of electoral districts, this capstone examines three of the five Cincinnati Police Department (CPD) districts containing twenty-five of the City of Cincinnati's fifty-two neighbourhoods (). Two of the districts are excluded for the following reasons:

1. Districts Two and Three contain a number of neighbourhoods adjacent to only one neighbour and introduce some "holes" (e.g. the City of Norwood) which complicate the simulation.
2. Fundamentally, the districting problem is a set assignment problem with a possible solution size of *S(n, K)* (a Stirling number of the second order for *n* units in *K* sets). Sorting all fifty neighbourhoods into five districts gives 7.401E+32 possible solutions, whereas twenty-five neighbourhoods in three districts gives only 1.41198E+11 possible solutions. As this capstone will not be leveraging supercomputing resources (as was done in the primary research), the reduction in potential solution set size is meaningful.

The simulation relies on a multi-objective evolutionary algorithm, focussed on three criteria: geographic compactness, population, and crime report density. (All data is sourced from the City of Cincinnati and the 2010 U.S. Census.) These criteria ignore many salient factors such as road maps, socioeconomic makeup, etc. but provide an adequate proxy for replicating the methods in question.

Once a set of reasonable alternatives has been developed, the analysis will examine: the computational efforts and efficiency of small-scale parallel computation vs. stochastic methods; the similarity or dissimilarity of the existing CPD districts and the alternatives.

The results of this capstone do not form a rigorous analysis of biased districting but an application case study in a new context.

## Process

- [x] Conduct literature review of primary sources/related articles
- [x] Source and clean population/crime/geographic data
- [ ] *(In progress) Develop the code to conduct the simulation*
- [ ] Analyse computational runtime data
- [ ] Quantify similarity/dissimilarity

## Primary sources:

* Yan Y. Liu, Wendy K. Tam Cho. (2016). Toward a Talismanic Redistricting Tool: A Computational Method for Identifying Extreme Redistricting Plans. *Election Law Journal*, *15(4)*, 351–366. DOI: 10.1089/elj.2016.0384
* Liu, Y. Y., Cho, W. K. T., & Wang, S. (2016). PEAR: a massively parallel evolutionary computation approach for political redistricting optimization and analysis. *Swarm and Evolutionary Computation*, *30*, 78–92. DOI: 10.1016/j.swevo.2016.04.004
