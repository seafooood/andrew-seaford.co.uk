## How To Merge Nodes In Dify

### Introduction

In this tutorial we are going to learn how to split a DIFY workflow into two streams and then merge the streams into one final end node. We will use the *IF/ELSE* node to split the workflow into two steams and then use the *VARIABLE AGGREGATOR* to combine the steams into one stream.

The variable aggregation node (formerly the variable assignment node) is a key node in the workflow. It is responsible for integrating the output results from different branches, ensuring that regardless of which branch is executed, its results can be referenced and accessed through a unified variable. This is particularly useful in multi-branch scenarios, as it maps variables with the same function from different branches into a single output variable, avoiding the need for repeated definitions in downstream nodes.

https://docs.dify.ai/guides/workflow/node/variable-assigner

