<properties 
   pageTitle="Azure Automation Runbook Types"
   description="Describes the difference types of runbooks that you can use in Azure Automation and considerations that you should take into account when determining which type to use. "
   services="automation"
   documentationCenter=""
   authors="bwren"
   manager="stevenka"
   editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="09/24/2015"
	wacn.date=""/>

# Azure Automation runbook types

Azure Automation supports three types of runbooks that are  briefly described in the following table.  The sections below provide further information about each type including considerations on when to use each.


| Type |  Description |
|:---|:---|
<!-- deleted by customization | [Graphical](#graphical-runbooks) | Based on Windows PowerShell Workflow and created and edited completely in graphical editor in Azure Management Portal. | -->
| [PowerShell Workflow](#powershell-workflow-runbooks) | Text runbook based on Windows PowerShell Workflow. |
| [PowerShell](#powershell-runbooks) | Text runbook based on Windows PowerShell script. |
<!-- deleted by customization

## Graphical runbooks

[Graphical runbooks](/documentation/articles/automation-runbook-types#graphical-runbooks) are created and edited with the graphical editor in the Azure Management Portal.  You can export them to a file and then import them into another automation account, but you cannot create or edit them with another tool.  Graphical runbooks generate PowerShell Workflow code, but you can't directly view or modify the code. Graphical runbooks cannot be converted to one of the [text formats](/documentation/articles/automation-runbook-types), nor can a text runbook be converted to graphical format.

### Advantages

- Create runbooks with minimal knowledge of [PowerShell Workflow](/documentation/articles/automation-powershell-workflow).
- Visually represent management processes.
- Use [checkpoints](/documentation/articles/automation-powershell-workflow#checkpoints) to resume runbook in case of error.
- Use [parallel processing](/documentation/articles/automation-powershell-workflow#parallel-processing) to perform mulitple activities in parallel.
- Can include other Graphical runbooks and PowerShell Workflow runbooks as child runbooks to create high level workflows.
-->


### Limitations

- Can't edit runbook outside of Azure Management Portal.
- May require a [Workflow Script Control](/documentation/articles/automation-powershell-workflow#activities) containing PowerShell Workflow code to perform complex logic.
- Can't view or directly edit the PowerShell Workflow code created by the graphical workflow.  Note that you can view the code in any Workflow Script activities.
- Runbook takes longer to start than PowerShell runbooks since it needs to be compiled before running.
- PowerShell runbooks can only be included as child runbooks by using the Start-AzureAutomationRunbook cmdlet which creates a new job.


## PowerShell Workflow runbooks

PowerShell Workflow runbooks are text runbooks based on [Windows PowerShell Workflow](/documentation/articles/automation-powershell-workflow).  You directly edit the code of the runbook using the text editor in the Azure Management Portal.  You can also use any offline text editor and [import the runbook](http://msdn.microsoft.com/zh-cn/library/azure/dn643637.aspx) into Azure Automation.

### Advantages

- Implement all complex logic with PowerShell Workflow code.
- Use [checkpoints](/documentation/articles/automation-powershell-workflow#checkpoints) to resume runbook in case of error.
- Use [parallel processing](/documentation/articles/automation-powershell-workflow#parallel-processing) to perform multiple actions in parallel.
- Can include other <!-- deleted by customization Graphical runbooks and -->PowerShell Workflow runbooks as child runbooks to create high level workflows.


### Limitations

- Author must be familiar with PowerShell Workflow.
- Runbook must deal with the additional complexity of PowerShell Workflow such as [deserialized objects](/documentation/articles/automation-powershell-workflow#code-changes).
- Runbook takes longer to start than PowerShell runbooks since it needs to be compiled before running.
- PowerShell runbooks can only be included as child runbooks by using the Start-AzureAutomationRunbook cmdlet which creates a new job.


## PowerShell runbooks

PowerShell runbooks are based on Windows PowerShell.  You directly edit the code of the runbook using the text editor in the Azure Management Portal.  You can also use any offline text editor and [import the runbook](http://msdn.microsoft.com/zh-cn/library/azure/dn643637.aspx) into Azure Automation.

### Advantages

- Implement all complex logic with PowerShell code without the additional complexities of PowerShell Workflow. 
- Runbook starts faster than <!-- deleted by customization Graphical or -->PowerShell Workflow runbooks since it doesn't need to be compiled before running.

### Limitations

- Must be familiar with PowerShell scripting.
- Can't use [parallel processing](/documentation/articles/automation-powershell-workflow#parallel-processing) to perform multiple actions in parallel.
- Can't use [checkpoints](/documentation/articles/automation-powershell-workflow#checkpoints) to resume runbook in case of error.
- Can't run runbooks on [Hybrid Runbook Worker](/documentation/articles/automation-hybrid-runbook-worker).
- PowerShell Workflow runbooks and <!-- deleted by customization Graphical runbooks -->can only be included as child runbooks by using the Start-AzureAutomationRunbook cmdlet which creates a new job.

### Known Issues
Following are current known issues with PowerShell runbooks.

- PowerShell runbooks cannot cannot retrieve an unencrypted [variable asset](/documentation/articles/automation-variables) with a null value.
- PowerShell runbooks cannot retrieve a [variable asset](/documentation/articles/automation-variables) with *~* in the name.
- Get-Process in a loop in a PowerShell runbook may crash after about 80 iterations. 
- A PowerShell runbook may fail if it attempts to write a very large amount of data to the output stream at once.   You can typically work around this issue by outputting just the information you need when working with large objects.  For example, instead of outputting something like *Get-Process*, you can output just the required fields with *Get-Process | Select ProcessName, CPU*.

## Considerations

You should take into account the following additional considerations when determining which type to use for a particular runbook.

- You can't convert runbooks from one type to another.
- There are limitations using runbooks of different types as a child runbook.  See [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks) for more information.



  
## Related articles

<!-- deleted by customization
- [Graphical authoring in Azure Automation](/documentation/articles/automation-graphical-authoring-intro)
-->
- [Learning Windows PowerShell Workflow](/documentation/articles/automation-powershell-workflow)
- [Creating or Importing a Runbook](http://msdn.microsoft.com/zh-cn/library/azure/dn643637.aspx)


