<properties
   pageTitle="Learn Hadoop in HDInsight with the Sample Gallery | Windows Azure"
   description="Quickly learn Hadoop by running sample applications from the HDInsight Getting Started Gallery. Use sample data or supply your own."
   services="hdinsight"
   documentationCenter=""
   tags="azure-portal"
   authors="mumian"
   manager="paulettm"
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="07/09/2015"
	wacn.date=""/>

# Learn Hadoop by using the Azure HDInsight Getting Started Gallery

The HDInsight Getting Started Gallery provides an easy and quick way learn Hadoop by running sample applications in HDInsight. Some of the samples come with sample data. You can supply your own data for the remaining samples. Currently, there are the following six samples (with more coming):

- Solutions with your Azure data
	- Windows Azure website log analysis
	- Windows Azure storage analytics
- Solutions with sample data
	- Sensor data analysis
<!-- deleted by customization - Twitter trend analysis -->
	- Website log analysis
	- Mahout movie recommendation
<!-- deleted by customization 

[AZURE.INCLUDE [hdinsight-azure-preview-portal](../includes/hdinsight-azure-preview-portal.md)]
-->

* [Learn Hadoop by using the HDInsight Getting Started Gallery](/documentation/articles/hdinsight-learn-hadoop-use-sample-gallery-v1)

![HDInsight Hadoop, Storm, and HBase Getting Started Gallery solutions including sample data.][hdinsight.sample.gallery]
<!-- deleted by customization

The following video shows how to run the Twitter trend analysis sample:

<center><a href="https://www.youtube.com/embed/7ePbHot1SN4">https://www.youtube.com/embed/7ePbHot1SN4></a></center>
-->

The Dashboard can be accessed by browsing to http://<YourHDInsightClusterName>.azurehdinsight.cn/ or from the Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->.

**To run a sample from the Getting Started Gallery**
<!-- deleted by customization

1. Sign in to the [Azure preview portal][azure.portal].
2. Click **Browse All** from the left menu, click **HDInsight Clusters**, and then click your cluster name.
3. Click **Dashboard** from the top menu.
4. Enter the user name and password for the HTTP user (also called the cluster user).
6. Click **Getting Started Gallery** at the top of the page.
7. Click one of the samples. Each sample gives detailed steps for running it. The following image shows the Twitter trend analysis sample:

	![HDInsight Twitter trend analysis sample][hdinsight.twitter.sample]
-->
<!-- keep by customization: begin -->
1.	Sign in to the [Azure Management Portal][azure.portal].
2.	Click **HDInsight** in the left menu. You will see a list of existing HDInsight clusters, including Hadoop, Storm, and HBase clusters. 
3.	Click the cluster where you want to run the sample.
4.	Click **QUERY CONSOLE** at the bottom of the page.
5.	Enter the Hadoop user name and password for the cluster.
6.	Click **Getting Started Gallery** at the top of the page.
<!-- keep by customization: end -->

## Next steps
Other ways to learn about HDInsight include:

- [HDInsight learning map][hdinsight.learn.map]
- [HDInsight infographic][hdinsight.infographic]

<!--Image references-->
[hdinsight.sample.gallery]: ./media/hdinsight-learn-hadoop-use-sample-gallery/HDInsight-Getting-Started-Gallery.png
[hdinsight.twitter.sample]: ./media/hdinsight-learn-hadoop-use-sample-gallery/HDInsight-Twitter-Trend-Analysis-sample.png

<!--Link references-->
[hdinsight.learn.map]: /documentation/articles/hdinsight-learn-map
[hdinsight.infographic]: http://go.microsoft.com/fwlink/?linkid=523960
[azure.portal]:https://manage.windowsazure.cn
