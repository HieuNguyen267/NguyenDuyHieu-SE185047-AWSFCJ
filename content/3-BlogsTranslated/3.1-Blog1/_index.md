---
title: "Blog 1"
date: 2025-10-08
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---
---
[Microsoft Workloads on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/)

# **Migrate .NET Framework applications to Linux with AWS Transform for .NET**

By Neeraj Handa, Artur Rodrigues, Juveria Kanodia, and Mark Fawaz on May 17, 2025 at [Artificial Intelligence](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/), [AWS Transform](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/generative-ai/aws-transform/), [Generative AI](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/generative-ai/), [Technical How-to](https://aws.amazon.com/blogs/modernizing-with-aws/category/post-types/technical-how-to/), [Windows on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-on-windows/) [Permalink](https://aws.amazon.com/blogs/modernizing-with-aws/port-your-net-framework-applications-to-linux-with-aws-transform-for-net/).

Recently, we have [Announcing the general availability of AWS Transform for .NET](https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-net-generally-available/), the first “agent” AI service for modernizing .NET applications at scale. With [AWS Transform to .NET](https://aws.amazon.com/transform/net/), you can accelerate the modernization of .NET Framework applications to cross-platform .NET by up to 4x. Because .NET 8 and beyond are cross-platform, you can run .NET 8 applications on Linux and reduce costs while improving security, performance, efficiency, and scalability.

In this article, you will learn how to migrate (port) a .NET Framework web application to .NET 8 using AWS Transform for .NET.

## **Prerequisites**

To follow this guide, you should have the following:

1. Visual Studio 2022\.

2. [AWS Toolkit with Amazon Q.](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022)

3. [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in your AWS account.

4. [AWS Transform subscription.](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html)

## **Walkthrough**

### **Step 1: Authenticate in AWS Toolkit for Visual Studio**

To access AWS Toolkit in Visual Studio 2022, from the menu bar, select **Extensions → AWS Toolkit → Getting Started**. In the AWS Toolkit panel, under Amazon *Q Developer & AWS Transform*, select **Enable**.

![][image1]

*Figure 1 – AWS Toolkit authentication options*

Next, to authenticate, you have two options: **Amazon Q Developer** and **AWS Transform** To enroll users in AWS Transform, follow the instructions on the page [document](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html) our. If you are logged in as the AWS Transform user, you can access the transformation functionality. Additionally, if you [Sign up for Amazon Q Developer Pro](https://aws.amazon.com/q/developer/pricing/), you'll get additional benefits like code completion and chat support in the IDE, as well as transformation functionality in Visual Studio.![][image2]

*Figure 2 – Amazon Q Developer & AWS Transform fields in AWS Toolkit*

When you create a new profile, enter a name in the field.*Profile Name*For example, they choose*arturQDeveloper*. Establish ***Start URL***— This URL can be found in the AWS Transform or Amazon Q Developer settings.

Confirm that *Profile Region* is correct. AWS Transform and Amazon Q Developer are currently supported in the following regions:**us-east-1** and **eu-central-1**. Ensure the IAM Identity Center region (**SSO Region**) matches your selection.

Finally, to authenticate, select**Connect**, the system will open a browser for you to enter your username and password.

![][image3]

*Figure 3 – AWS Transform profile configuration*

### **Step 2: Clone the sample application**

To explore the sample application that you will migrate to .NET 8 in this article, clone [repository model](https://github.com/aws-samples/bobs-used-bookstore-classic/tree/transform-blog) about a folder on your system. In the example, the folder is *C:\\code.* 

The following steps illustrate user “bob” cloning the repository and switching to a branch

PowerShell

C:\\code\> git clone https://github.com/aws-samples/bobs-used-bookstore-classic 

Cloning into 'bobs-used-bookstore-classic'...  

C:\\code\> cd bobs-used-bookstore-classic  

C:\\code\\bobs-used-bookstore-classic\> git checkout transform-blog branch 'transform-blog' set up to track 'origin/transform-blog'. 

Switched to a new branch 'transform-blog'


Branch transform-blog Contains a directory with private NuGet packages that you will use as a private NuGet feed.

Open solution BobsBookstoreClassic.sln in Visual Studio to view the source code structure and run the application locally. 

#### **Sample application overview**

PowerShell

C:\\code\\bobs-used-bookstore-classic

├───app

│   ├───Bookstore.Data

│   ├───Bookstore.Domain

│   ├───Bookstore.Domain.Tests

│   ├───Bookstore.Web

│   └───Bookstore.Web.Tests

├───db-scripts

└───nuget-packages

Application Bob’s Used Books Classic is a sample e-commerce application using ASP.NET MVC targeting .NET Framework 4.8. This solution consists of multiple projects. Files *`BobsBookstoreClassic.sln`* located at the root of the application tree.

* **Bookstore.Web**: ASP.NET MVC web application — user interface

* **Bookstore.Domain**: domain model and interface (released as a separate NuGet package)

* **Bookstore.Data**: data access layer (repository, services)

* **Bookstore.Common**: shared utility classes

* **Bookstore.Web.Tests** and **Bookstore.Domain**.Tests: unit test projects.

In the repository clone, you will find the folder *nuget-packages*, which contains two NuGet packages of *Bookstore.Common*. Many enterprise projects use private NuGet packages to share internal dependencies. AWS Transform for .NET can query and update NuGet package references from these private sources.

BobsBookstoreClassic Solution Project Requirements *Bookstore.Web* reference to package*Bookstore.Common* version 1.0.0, compatible with .NET Framework 4.8. Other packages in the folder are *Bookstore.Common* version 2.0.0, compatible with .NET 8.0. AWS Transform for .NET will automatically use version 2.0.0 in the source code you migrate. 

The Bookstore.Web project references the local package Bookstore.Common version 1.0.0.

\<ItemGroup\>

  	\<PackageReference Include\="Bookstore.Common"\>

   		 \<Version\>1.0.0\</Version\>

  	\</PackageReference\>

  	\<\!-- Other package references \--\>

\</ItemGroup\>

### 

### **Step 3: Set up a private NuGet feed**

In an enterprise environment, organizations can use package management solutions to host private NuGet packages for internal use. To demonstrate support for private NuGet in AWS Transform for .NET, this sample application uses a simple, local directory-based NuGet source for easy reproducibility.

1. In Visual Studio, select**Tools → NuGet Package Manager → Package Manager Settings.![][image4]***Figure 4 – Package Manager Settings menu options*

2. In the Package Manager Settings window, select ***Package sources***, then click the \+ icon to add a new source. (Figure 5\)

   ![][image5]  
   *Figure 5 – Adding a new package source*

3. Select the new source, give it a name (e.g., **BobsUsedBookstoreLocal**), and enter the folder path **nuget-packages** of the repository clone do*Source*. Press **Update.** Already **OK** to close the dialog box.![][image6]*Figure 6 – Configuring package sources for local private NuGet packages*

4. To verify that the package source is configured correctly, in **Solution Explorer,** select **Bookstore.Web**, go to menu**Project** select **Manage NuGet Packages**.![][image7]*Figure 7 – View NuGet Packages Menu Option*

5. In the dropdown***Package source***, select **BobsUsedBookstoreLocal**. ![][image8]

   *Figure 8 – Select local package feed*

6. In *Top-level packages*, select **Bookstore.Common**. Dropdown *Version* should be displayed **version 2.0.0**. ![][image9]

   *Figure 9 – NuGet package versions in Package Manager*

### **Step 4: Begin porting**

To start the migration process

1. Open file [**Startup.cs**](http://Startup.cs) in the project **Bookstore.Web.**When opening a C\# file, the system activates the language server, a component of AWS Toolkit required for Amazon Q to analyze the code.

2. In Solution Explorer, right-click the solution**BobsBookstoreClassic.**

3. Cpick**Port project with AWS Transform**.![][image10]

   *Figure 10 – Select the Port solution with AWS Transform option*

Transformation configuration options:

* ***Exclude .NET Standard projects from the transformation plan***: Check this option if you want to exclude .NET Standard projects from the migration plan — these projects are cross-platform supported and can continue to work on both legacy and modern environments if left intact.

* ***Transform MVC Razor Views to ASP.NET Core Razor Views***: Convert Razor views from MVC to ASP.NET Core's Razor format. AWS Transform now supports converting Razor code inside MVC view files.

* ***Check the NuGet sources and get .NET compatible package versions***: validate and update NuGet package references from all package sources in Visual Studio, including private ones.

After selecting the configuration, click **Start** to start porting.![][image11]

*Figure 11 – Configuration for AWS Transform for .NET*

Prevent**Code Transformation Plan** appears, showing the transformation details of your solution. In the Code groups section, AWS Transform automatically groups related projects together for efficient migration, identifies all dependencies of high-level projects in the solution, and creates a logical transformation chain based on those dependencies.![][image12]

*Figure 12 – Transformation Plan – Code groups*

### **Step 4: View the move overview**

When the transformation job is complete, AWS Transform displays a summary. *Transformation summary*, indicating the migration status of each project.

To download the conversion summary, download the summary as an .md file and select a folder to save it on your computer.![][image13]

*Figure 14 – Conversion process summary*

The summary shows an overview of the modernized projects, along with details like critical changes, dependencies, build configuration, and errors if any.	

For example, the summary might read something like this:

*\*\*SolutionTransformationSummary\*\**

*\# Comprehensive .NET 8 Migration Summary for Bookstore Application*

*The Bookstore application has been migrated from .NET Framework 4.8 to .NET 8.0, affecting multiple projects in the solution. This migration involved standardizing all projects to the modern SDK-style format and updating associated dependencies and infrastructure components.*

*\#\# Core Project Changes*

*\- \*\*All Projects\*\*:*

  *\- Converted from legacy XML project format to modern SDK-style format*

  *\- Removed AssemblyInfo.cs files in favor of project-file managed metadata*

  *\- Migrated from packages.config to PackageReference format*

  *\- Added dependencies on Bookstore.Common v2.0.0 across projects*

*\- \*\*Bookstore.Domain & Bookstore.Data\*\*:*

  *\- Updated target framework from net48 to net8.0*

  *\- Removed framework-specific conditional compilation constants*

  *\- Added System.Configuration.ConfigurationManager package in Data project*

  *\- Maintained Entity Framework 6.5.1 and AWSSDK dependencies*

*\#\# Web Application Modernization*

*\- \*\*Hosting Model\*\*:*

  *\- Replaced Global.asax with Program.cs using WebApplication builder pattern*

  *\- Migrated from Web.config to appsettings.json*

*\- \*\*Infrastructure Updates\*\*:*

  *\- Switched from OWIN middleware to ASP.NET Core middleware components*

  *\- Replaced Autofac with built-in ASP.NET Core dependency injection*

  *\- Updated from System.Web.Mvc to Microsoft.AspNetCore.Mvc namespaces*

  *\- Relocated static files from Content/Scripts to wwwroot directory*

*\- \*\*Authentication\*\*:*

  *\- Updated cookie handling mechanisms to ASP.NET Core APIs*

*\- AWS Cognito integration requires reimplementation*

*\#\# Test Projects*

*\- \*\*All Test Projects\*\*:*

  *\- Updated to .NET 8.0 target framework*

  *\- Added Microsoft.NET.Test.Sdk and xunit.runner.visualstudio*

  *\- Simplified build process with automatic dependency resolution*

  *\- Updated test framework dependencies to latest versions with wildcard versioning*

The summary is an important source of information about what was changed during the migration. 

### **Step 5: View each file and accept changes**

To see detailed changes, select **View diffs** in the panel **Transformation summary**.![][image14]

*Figure 15 – “View diffs” button in the conversion summary*

AWS Transform will display modified files in the hub.**AWS Transform Hub**.

![][image15]

*Image 16 – Ngăn View diffs* 

This article focuses on reviewing key files that represent significant transformation changes. Although AWS Transform for .NET modifies multiple files in your project, we will look at the essential changes.

To confirm that AWS Transform for .NET changed the target platform for .NET projects, review the project file **Bookstore.Web**. To do this, select the button **Show changes** next to the path: **C:\\code\\bobs-used-bookstore-classic\\app\\Bookstore.Web.csproj.**

**![][image16]**

*Figure 17 – Showing changes to Bookstore.Web.csproj*

In **View diff window** appears, note that AWS Transform for .NET has changed the target framework of Bookstore.Web to **.**NET 8\.

![][image17]

*Figure 18 – Compare the differences for Bookstore.Web.csproj*

You'll also notice that AWS Transform for .NET has changed the reference for **Bookstore.Common** to version 2.0.0, which is the target NuGet package version **.**NET 8\.

![][image18]

*Figure 19 – Upgrading NuGet package version*

To confirm that AWS Transform for .NET made changes to the source files, review the file changes: **`C:\code\bobs-used-bookstore-classic\app\Bookstore.Web\Controllers\AddressController.cs`**

You will see that AWS Transform for .NET has changed namespace references to be compatible with .NET 8\.

![][image19]

*Figure 20 – Compare the differences for AddressController.cs*

To confirm that AWS Transform for .NET changed the Razor code in your MVC views, look at the changes made in:  
**`C:\code\bobs-used-bookstore-classic\app\Bookstore.Web\Areas\Admin\Views\ReferenceData\CreateUpdate.cshtml`**

You will see that AWS Transform for .NET has changed the method call**Html.GetSelectListForEnum**.

![][image20]

*Figure 21 – Compare the differences for CreateUpdate.cshtml (Razor code in MVC view)*

Select the button **Select All** in the table **Show Diff** This will select all edited files shown in the table.![][image21]

*Figure 22 – Select all changes*

Select the button **Apply Changes**. AWS Transform for .NET will apply the recommended code changes and transformations to **your source code**, update the files with the new modified code.

![][image22]

*Figure 23 – Applying changes*

### **Step 6: Run the application / Pending jobs**

The original source code uses Autofac to enable dependency injection. To review the original code, in Solution Explorer, under project**Bookstore.Web**, open file **App\_Start\\DependencyInjectionSetup.cs.bak.**ASP.NET Core in .NET 8 comes with built-in Dependency Injection. In this article, you will add code to ASP.NET Core middleware that uses built-in dependency injection to replace the functionality provided by Autofac. However, in your own applications, you can evaluate whether your preferred package supports .NET 8 and continue using it if you want.

In **Bookstore.Web**, open **Program.cs.**

Copy and paste the following code to replace the contents of **Program.cs**.

using Microsoft.AspNetCore.Hosting;

using Microsoft.Extensions.Configuration;

using Microsoft.Extensions.DependencyInjection;

using Microsoft.Extensions.Hosting;

using Microsoft.Extensions.Logging;

using System;

using System.Configuration;

using System.Data.Entity;

using System.Linq;

using System.Collections.Generic;

namespace Bookstore

{

    public class Program

    {

        public static void Main(string\[\] args)

        {

            var builder \= WebApplication.CreateBuilder(args);

            // Apply environment settings from AppSettings

            builder.Configuration.GetSection("AppSettings")

                .GetChildren()

                .Where(setting \=\> setting.Key \== "Environment")

                .ToList() .

                .ForEach(setting \=\> builder.Environment.EnvironmentName \= setting.Value);

            // Store configuration in static ConfigurationManager

            ConfigurationManager.Configuration \= builder.Configuration;

            // Add services to the container

            builder.Services.AddControllersWithViews()

                .AddRazorOptions(options \=\> {

                    // Add area view location formats

                    options.ViewLocationFormats.Add("/Areas/{2}/Views/{1}/{0}.cshtml");

                    options.ViewLocationFormats.Add("/Areas/{2}/Views/Shared/{0}.cshtml");

                    options.AreaViewLocationFormats.Add("/Areas/{2}/Views/{1}/{0}.cshtml");

                    options.AreaViewLocationFormats.Add("/Areas/{2}/Views/Shared/{0}.cshtml");

                });

            AddServices(builder.Services, builder);

var app \= builder.Build();

            // Configure the HTTP request pipeline

            if (app.Environment.IsDevelopment())

                app.UseDeveloperExceptionPage();

            else

            {

                app.UseExceptionHandler("/Home/Error");

                app.UseHsts();

            }

            // ...

        }

    }

}

To verify your converted app:

1. In Visual Studio, click **F5** or select **Debug,  Start Debugging.**

2. The application will launch in your default browser.

3. Confirm that your converted app runs as expected.

![][image23]

*Figure 24 – Converted .NET 8 application running in the browser*

### **Cleanup**

To clean up the resources used for this article, simply delete the cloned application source code from your file system. None of the AWS services created in this article need to be cleaned up via the AWS console.

## **Conclusion**

The official launch of AWS Transform brings exciting new features to .NET developers. Customers can now complete the transformation of MVC applications, including applications with Razor views, support for projects containing native NuGet packages, and access a transformation summary report detailing the changes made. This is a cost-effective solution, with no additional charges for using AWS Transform for .NET.

The benefits of porting applications to Linux are compelling: [Applications reduce operating costs by 40% because you save on Windows licensing costs, run 1.5 to 2 times faster due to improved performance, and handle growing workloads 50% more efficiently thanks to superior scalability.](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/)

We cordially invite you [Convert .NET applications](https://aws.amazon.com/transform/net/) of your own — there's never been a better time to do it.

---

AWS now offers significantly more services and more features within each service, than any other cloud provider, making it faster, easier, and more cost-effective to migrate your existing applications to the cloud, and allowing you to build almost anything you can imagine. Give your Microsoft applications the infrastructure they need to drive the business outcomes you want. Visit the blogs[.NET on AWS](https://aws.amazon.com/blogs/dotnet/) and [AWS Database](https://aws.amazon.com/blogs/database/) Visit our website to learn more guidance and additional options for your Microsoft workloads. [Contact us](https://pages.awscloud.com/MAP-windows-contact-us.html) today to start your migration and modernization journey.

Neeraj Handa

Neeraj Handa is a Specialist Solutions Architect at Amazon Web Services (AWS), where he collaborates with enterprise customers to accelerate application development and modernization using generative AI services. He is passionate about helping organizations transform their software development lifecycle to achieve higher productivity and better software quality through the application of AI technologies.

### Artur Rodrigues

Artur Rodrigues is a Principal Solutions Architect specializing in Generative AI at Amazon Web Services (AWS), where he helps developers harness cutting-edge AI technologies to enhance workflows and drive innovation. Outside of work, Artur enjoys cycling and exploring the beautiful nature of British Columbia, Canada.

### Juveria Kanodia

Juveria Kanodia is Head of Engineering in the AWS Agentic AI .NET Modernization organization. She leads engineering teams developing solutions that leverage the latest advances in generative and agentic AI to transform Windows workloads for the enterprise. Juveria has over 20 years of technical leadership experience in large-scale AI-based services and B2B. She holds a Master's Degree in Computer Science from Rochester Institute of Technology (RIT), with a concentration in Data Mining, and holds multiple patents in the areas of cloud computing and artificial intelligence. Juveria has a Master's Degree in Computer Science from RIT, with a specialization in Data Mining, and holds several patents in cloud computing and AI.

### Mark Fawaz

Mark Fawaz is a Senior Software Development Engineer (SDE) in the AWS Agentic AI organization, focused on helping customers migrate, modernize, and optimize their .NET and Windows workloads on the AWS platform.

[image1]: ../../../static../../../static/images/3-BlogImage/Blog1/blog1-1.png

[image2]: ../../../static/images/3-BlogImage/Blog1/blog1-2.png

[image3]: ../../../static/images/3-BlogImage/Blog1/blog1-3.png

[image4]: ../../../static/images/3-BlogImage/Blog1/blog1-4.png

[image5]: ../../../static/images/3-BlogImage/Blog1/blog1-5.png

[image6]: ../../../static/images/3-BlogImage/Blog1/blog1-6.png

[image7]: ../../../static/images/3-BlogImage/Blog1/blog1-7.png

[image8]: ../../../static/images/3-BlogImage/Blog1/blog1-8.png

[image9]: ../../../static/images/3-BlogImage/Blog1/blog1-9.png

[image10]: ../../../static/images/3-BlogImage/Blog1/blog1-10.png

[image11]: ../../../static/images/3-BlogImage/Blog1/blog1-11.png

[image12]: ../../../static/images/3-BlogImage/Blog1/blog1-12.png

[image13]: ../../../static/images/3-BlogImage/Blog1/blog1-13.png

[image14]: ../../../static/images/3-BlogImage/Blog1/blog1-14.png

[image15]: ../../../static/images/3-BlogImage/Blog1/blog1-15.png

[image16]: ../../../static/images/3-BlogImage/Blog1/blog1-16.png

[image17]: ../../../static/images/3-BlogImage/Blog1/blog1-17.png

[image18]: ../../../static/images/3-BlogImage/Blog1/blog1-18.png

[image19]: ../../../static/images/3-BlogImage/Blog1/blog1-19.png

[image20]: ../../../static/images/3-BlogImage/Blog1/blog1-20.png

[image21]: ../../../static/images/3-BlogImage/Blog1/blog1-21.png

[image22]: ../../../static/images/3-BlogImage/Blog1/blog1-22.png

[image23]: ../../../static/images/3-BlogImage/Blog1/blog1-23.png