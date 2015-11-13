<properties 
	pageTitle="Testing a runbook in Azure Automation"
	description="Before you publish a runbook in Azure Automation, you can test it to ensure that works as expected.  This article describes how to test a runbook and view its output."
	services="automation"
	documentationCenter=""
	authors="bwren"
	manager="stevenka"
	editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="09/23/2015"
	wacn.date=""/>

# Testing a runbook in Azure Automation
When you test a runbook, the [Draft version](/documentation/articles/automation-creating-importing-runbook#publishing-a-runbook) is executed and any actions that it performs are completed. No job history is created, but the [Output](/documentation/articles/automation-runbook-output-and-messages#output-stream) and [Warning and Error](/documentation/articles/automation-runbook-output-and-messages#message-streams) streams are displayed in the Test output Pane. Messages to the [Verbose Stream](/documentation/articles/automation-runbook-output-and-messages#message-streams) are displayed in the Output Pane only if the [$VerbosePreference variable](/documentation/articles/automation-runbook-output-and-messages#preference-variables) is set to Continue.

Even though the draft version is being run, the runbook still executes the workflow normally and performs any actions against resources in the environment. For this reason, you should only test runbooks at non-production resources.

The procedure to test each [type of runbook](/documentation/articles/automation-runbook-types) is the same<!-- deleted by customization , and there is no difference in testing between the textual editor and the graphical editor in the Azure preview portal -->.  

<!-- deleted by customization

## To test a runbook in the Azure preview portal

You can work with any [runbook type](/documentation/articles/automation-runbook-types) in the Azure preview portal.

1. Open the Draft version of the runbook in either the [textual editor](/documentation/articles/automation-editing-a-runbook#Portal) or [graphical editor](/documentation/articles/automation-graphical-authoring-intro).
2. Click the **Test** button to open the Test blade.
3. If the runbook has parameters, they will be listed in the left pane where you can provide values to be used for the test.
4. If you want to run the test on a [Hybrid Runbook Worker](/documentation/articles/automation-hybrid), then change **Run Settings** to **Hybrid Worker** and select the name of the target group.  Otherwise, keep the default **Azure** to run the test in the cloud.
5. Click the **Start** button to start the test.
6. If the runbook is [PowerShell Workflow](/documentation/articles/automation-runbook-types#powershell-workflow-runbooks) or [Graphical](/documentation/articles/automation-runbook-types#graphical-runbooks), then you can stop or suspend it while it is being tested with the buttons underneath the Output Pane. When you suspend the runbook, it completes the current activity before being suspended. Once the runbook is suspended, you can stop it or restart it.
7. Inspect the output from the runbook in the output pane.
-->



## To test a runbook in the Azure Management Portal

You can only work with [PowerShell Workflow runbooks](/documentation/articles/automation-runbook-types#powershell-workflow-runbooks) in the Azure Management Portal.


1. [Open the Draft version of the runbook](/documentation/articles/automation-edit-textual-runbook#to-edit-a-runbook-with-the-azure-portal).
2. Click the **Test** button to start the test.  If the runbook has parameters, you will receive a dialog box to provide values to be used for the test.
6. You can stop or suspend the runbook while it is being tested with the buttons underneath the Output Pane. When you suspend the runbook, it completes the current activity before being suspended. Once the runbook is suspended, you can stop it or restart it.
7. Inspect the output from the runbook in the output pane.


## Related articles

- [Creating or importing a runbook in Azure Automation](/documentation/articles/automation-creating-importing-runbook)
<!-- deleted by customization 
- [Graphical runbooks in Azure Automation](/documentation/articles/automation-graphical-authoring-intro)
-->
- [Editing textual runbooks in Azure Automation](/documentation/articles/automation-edit-textual-runbook)
- [Runbook output and messages in Azure Automation](/documentation/articles/automation-runbook-output-and-messages)