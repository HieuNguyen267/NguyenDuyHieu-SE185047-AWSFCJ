---
title: "Blog 1"
date: 2025-10-08
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---
---
[Microsoft Workloads on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/)

# **Di chuyển ứng dụng .NET Framework sang Linux với AWS Transform cho .NET**

Bởi Neeraj Handa, Artur Rodrigues, Juveria Kanodia, and Mark Fawaz ngày 17 tháng năm 2025 tại [Artificial Intelligence](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/), [AWS Transform](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/generative-ai/aws-transform/), [Generative AI](https://aws.amazon.com/blogs/modernizing-with-aws/category/artificial-intelligence/generative-ai/), [Technical How-to](https://aws.amazon.com/blogs/modernizing-with-aws/category/post-types/technical-how-to/), [Windows on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-on-windows/) [Permalink](https://aws.amazon.com/blogs/modernizing-with-aws/port-your-net-framework-applications-to-linux-with-aws-transform-for-net/).

Gần đây, chúng tôi đã [công bố khả năng ra mắt chung (general availability) của AWS Transform cho .NET](https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-net-generally-available/), dịch vụ AI “agentic” đầu tiên dành cho hiện đại hóa các ứng dụng .NET ở quy mô. Với [AWS Transform cho .NET](https://aws.amazon.com/transform/net/), bạn có thể tăng tốc việc hiện đại hóa các ứng dụng .NET Framework sang .NET đa nền tảng lên đến 4 lần. Vì .NET 8 và các phiên bản tiếp theo là đa nền tảng (cross-platform), bạn có thể chạy các ứng dụng .NET 8 trên Linux và giảm chi phí đồng thời cải thiện bảo mật, hiệu năng, tính hiệu quả và khả năng mở rộng.

Trong bài viết này, bạn sẽ học cách di chuyển (port) một ứng dụng web .NET Framework sang .NET 8 bằng AWS Transform cho .NET.

## **Tiền đề (Prerequisites)**

Để làm theo hướng dẫn này, bạn nên có các điều kiện sau:

1. Visual Studio 2022\.

2. [AWS Toolkit với Amazon Q.](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022)

3. [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) trong tài khoản AWS của bạn.

4. [Đăng ký (subscription) AWS Transform.](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html)

## **Hướng dẫn từng bước (Walkthrough)**

### **Bước 1: Xác thực trong AWS Toolkit cho Visual Studio**

Để truy cập AWS Toolkit trong Visual Studio 2022, từ thanh menu chọn **Extensions → AWS Toolkit → Getting Started**. Trong bảng AWS Toolkit, dưới mục *Amazon Q Developer & AWS Transform*, chọn **Enable**.

![][image1]

*Hình 1 – Các tùy chọn xác thực của AWS Toolkit*

Tiếp theo, để xác thực, bạn có hai lựa chọn: **Amazon Q Developer** và **AWS Transform**. Để đăng ký người dùng vào AWS Transform, làm theo hướng dẫn trong trang [tài liệu](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html) của chúng tôi. Nếu bạn đăng nhập dưới quyền người dùng AWS Transform, bạn có thể truy cập chức năng transformation. Ngoài ra, nếu bạn [đăng ký Amazon Q Developer Pro](https://aws.amazon.com/q/developer/pricing/), bạn sẽ nhận được các lợi ích bổ sung như hỗ trợ hoàn thiện mã và chat trong IDE, cũng như chức năng transformation trong Visual Studio.![][image2]

*Hình 2 – Các trường thông tin Amazon Q Developer & AWS Transform trong AWS Toolkit*

Khi bạn tạo một profile mới, nhập tên vào trường *Profile Name*. Ví dụ, họ chọn *arturQDeveloper*. Thiết lập ***Start URL*** — URL này có thể tìm trong phần thiết lập AWS Transform hoặc Amazon Q Developer.

Xác nhận rằng *Profile Region* là đúng. AWS Transform và Amazon Q Developer hiện hỗ trợ ở các vùng **us-east-1** và **eu-central-1**. Đảm bảo vùng IAM Identity Center (**SSO Region**) trùng khớp với lựa chọn của bạn. 

Cuối cùng, để xác thực, chọn **Connect**, hệ thống sẽ mở trình duyệt để bạn nhập tên người dùng và mật khẩu.

![][image3]

*Hình 3 – Cấu hình hồ sơ (profile) AWS Transform*

### **Bước 2: Clone ứng dụng mẫu (sample)**

Để khám phá ứng dụng mẫu mà bạn sẽ di chuyển sang .NET 8 trong bài viết này, clone [repository mẫu](https://github.com/aws-samples/bobs-used-bookstore-classic/tree/transform-blog) về một thư mục trên hệ thống của bạn. Trong ví dụ, thư mục là *C:\\code.* 

Các bước sau minh họa người dùng “bob” nhân bản (clone) kho lưu trữ và chuyển sang nhánh

PowerShell

C:\\code\> git clone https://github.com/aws-samples/bobs-used-bookstore-classic 

Cloning into 'bobs-used-bookstore-classic'...  

C:\\code\> cd bobs-used-bookstore-classic  

C:\\code\\bobs-used-bookstore-classic\> git checkout transform-blog branch 'transform-blog' set up to track 'origin/transform-blog'. 

Switched to a new branch 'transform-blog'


Branch transform-blog chứa thư mục với các gói NuGet riêng mà bạn sẽ dùng như một nguồn NuGet riêng (private NuGet feed).

Mở giải pháp BobsBookstoreClassic.sln trong Visual Studio để xem cấu trúc mã nguồn và chạy ứng dụng cục bộ. 

#### **Tổng quan ứng dụng mẫu**

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

Ứng dụng Bob’s Used Books Classic là một ứng dụng thương mại điện tử mẫu sử dụng ASP.NET MVC nhắm tới .NET Framework 4.8. Giải pháp này bao gồm nhiều dự án. Tệp *`BobsBookstoreClassic.sln`* nằm ở thư mục gốc của cây ứng dụng.

* **Bookstore.Web**: ứng dụng web ASP.NET MVC — giao diện người dùng

* **Bookstore.Domain**: mô hình miền và interface (phát hành như gói NuGet riêng)

* **Bookstore.Data**: lớp truy cập dữ liệu (repository, services)

* **Bookstore.Common**: các lớp tiện ích chia sẻ

* **Bookstore.Web.Tests** và **Bookstore.Domain**.Tests: các dự án kiểm thử đơn vị (unit test).

Trong repository clone, bạn sẽ tìm thư mục *nuget-packages*, chứa hai gói NuGet của *Bookstore.Common*. Nhiều dự án doanh nghiệp sử dụng các gói NuGet riêng để chia sẻ phụ thuộc nội bộ. AWS Transform cho .NET có thể truy vấn và cập nhật các tham chiếu gói NuGet từ các nguồn riêng này.

Giải pháp BobsBookstoreClassic yêu cầu dự án *Bookstore.Web* tham chiếu tới gói *Bookstore.Common* phiên bản 1.0.0, tương thích với .NET Framework 4.8. Gói khác trong thư mục là *Bookstore.Common* phiên bản 2.0.0, tương thích với .NET 8.0. AWS Transform cho .NET sẽ tự động dùng phiên bản 2.0.0 trong mã nguồn mà bạn di chuyển. 

Dự án Bookstore.Web tham chiếu đến gói cục bộ Bookstore.Common phiên bản 1.0.0.

\<ItemGroup\>

  	\<PackageReference Include\="Bookstore.Common"\>

   		 \<Version\>1.0.0\</Version\>

  	\</PackageReference\>

  	\<\!-- Các tham chiếu gói khác \--\>

\</ItemGroup\>

### 

### **Bước 3: Thiết lập nguồn NuGet riêng (private NuGet feed)**

Trong môi trường doanh nghiệp, các tổ chức có thể dùng các giải pháp quản lý gói để lưu các gói NuGet riêng cho nội bộ. Để minh họa hỗ trợ cho NuGet riêng trong AWS Transform cho .NET, ứng dụng mẫu này dùng nguồn NuGet đơn giản dựa trên thư mục cục bộ để dễ tái hiện.

1. Trong Visual Studio, chọn **Tools → NuGet Package Manager → Package Manager Settings.![][image4]***Hình 4 – Tùy chọn menu Package Manager Settings*

2. Trong cửa sổ thiết lập Package Manager Settings, chọn ***Package sources***, rồi bấm biểu tượng \+ để thêm nguồn mới. (Hinh 5\)

   ![][image5]  
   *Hình 5 – Thêm một nguồn gói (package source) mới*

3. Chọn nguồn mới, đặt tên (ví dụ **BobsUsedBookstoreLocal**) và nhập đường dẫn thư mục **nuget-packages** của repository clone làm *Source*. Nhấn **Update** rồi **OK** để đóng hộp thoại.![][image6]*Hình 6 – Cấu hình nguồn gói cho các gói NuGet riêng cục bộ*

4. Để xác minh nguồn gói được cấu hình đúng, trong **Solution Explorer** chọn **Bookstore.Web**, vào menu **Project** chọn **Manage NuGet Packages**.![][image7]*Hình 7 – Tùy chọn menu xem gói NuGet* 

5. Trong dropdown ***Package source***, chọn **BobsUsedBookstoreLocal**. ![][image8]

   *Hình 8 – Chọn nguồn gói cục bộ (local package feed)*

6. Trong *Top-level packages*, chọn **Bookstore.Common**. Dropdown *Version* nên hiển thị **phiên bản 2.0.0**. ![][image9]

   *Hình 9 – Các phiên bản gói NuGet trong Trình quản lý gói (Package Manager)*

### **Bước 4: Bắt đầu di chuyển (Begin porting)**

Để bắt đầu quá trình di chuyển

1. Mở file **Startup.cs** trong dự án **Bookstore.Web.** Khi mở file C\#, hệ thống kích hoạt language server, một thành phần của AWS Toolkit cần thiết để Amazon Q phân tích code.

2. Trong Solution Explorer, nhấn chuột phải vào giải pháp **BobsBookstoreClassic.**

3. Chọn **Port project with AWS Transform**.![][image10]

   *Hình 10 – Chọn tùy chọn Port solution with AWS Transform*

Các tùy chọn cấu hình transformation:

* ***Exclude .NET Standard projects from the transformation plan***: kiểm tra tùy chọn này nếu bạn muốn loại bỏ các dự án .NET Standard khỏi kế hoạch di chuyển — các dự án này đã hỗ trợ đa nền tảng và có thể tiếp tục hoạt động trên cả môi trường legacy và hiện đại nếu giữ nguyên.

* ***Transform MVC Razor Views to ASP.NET Core Razor Views***: chuyển đổi các view Razor từ MVC sang định dạng Razor của ASP.NET Core. AWS Transform hiện hỗ trợ chuyển đổi mã Razor bên trong file view MVC.

* ***Check the NuGet sources and get .NET compatible package versions***: xác thực và cập nhật các tham chiếu gói NuGet từ tất cả nguồn gói trong Visual Studio, bao gồm cả các nguồn riêng (private ones).

Sau khi chọn cấu hình xong, bấm **Start** để bắt đầu porting.![][image11]

*Hình 11 – Cấu hình cho AWS Transform cho .NET*

Ngăn **Code Transformation Plan** xuất hiện, hiển thị chi tiết chuyển đổi của giải pháp của bạn. Trong phần Code groups, AWS Transform tự động nhóm các dự án liên quan lại với nhau để di chuyển hiệu quả, xác định toàn bộ các phụ thuộc của các dự án cấp cao trong giải pháp, và tạo chuỗi chuyển đổi logic dựa trên các phụ thuộc đó.![][image12]

*Hình 12 – Kế hoạch chuyển đổi (Transformation Plan) – Các nhóm mã (Code groups)*

### **Bước 4: Xem tổng quan di chuyển**

Khi công việc transformation hoàn thành, AWS Transform hiển thị một bản tóm tắt *Transformation summary*, cho biết trạng thái di chuyển từng dự án. 

Để tải xuống bản tóm tắt quá trình chuyển đổi, tải xuống tóm tắt dưới dạng tệp .md và chọn thư mục lưu trữ trên máy của bạn.![][image13]

*Hình 14 – Bản tóm tắt quá trình chuyển đổi* 

Bản tóm tắt hiển thị tổng quan các dự án đã được hiện đại hóa, cùng với thông tin chi tiết như các thay đổi quan trọng, phụ thuộc, cấu hình build và lỗi nếu có.	

Ví dụ, bản tóm tắt có thể có nội dung như sau:

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

Bản tóm tắt là nguồn thông tin quan trọng về những gì đã được thay đổi trong quá trình di chuyển. 

### **Bước 5: Xem từng file và chấp nhận thay đổi**

Để xem các thay đổi chi tiết, chọn **View diffs** trong panel **Transformation summary**.![][image14]

*Hình 15 – Nút “View diffs” trong bản tóm tắt chuyển đổi* 

 AWS Transform sẽ hiển thị các file đã bị sửa đổi trong hub **AWS Transform Hub**.

![][image15]

*Image 16 – Ngăn View diffs* 

Bài viết này tập trung vào việc xem xét các tệp chính thể hiện những thay đổi chuyển đổi quan trọng. Mặc dù AWS Transform for .NET sửa đổi nhiều tệp trong dự án của bạn, chúng ta sẽ xem xét các thay đổi thiết yếu.

Để xác nhận rằng AWS Transform for .NET đã thay đổi nền tảng đích cho các dự án .NET, hãy xem lại tệp dự án **Bookstore.Web**. Để làm điều này, chọn nút **Show changes** bên cạnh đường dẫn: **C:\\code\\bobs-used-bookstore-classic\\app\\Bookstore.Web.csproj.**

**![][image16]**

*Hình 17 – Hiển thị thay đổi cho Bookstore.Web.csproj* 

Trong **cửa sổ View diff** xuất hiện, hãy lưu ý rằng AWS Transform for .NET đã thay đổi nền tảng mục tiêu (target framework) của Bookstore.Web sang **.**NET 8\.

![][image17]

*Hình 18 – So sánh sự khác biệt cho Bookstore.Web.csproj* 

Bạn cũng sẽ nhận thấy rằng AWS Transform for .NET đã thay đổi tham chiếu cho **Bookstore.Common** sang phiên bản 2.0.0, là phiên bản gói NuGet nhắm tới **.**NET 8\.

![][image18]

*Hình 19 – Nâng cấp phiên bản gói NuGet* 

Để xác nhận rằng AWS Transform for .NET đã thực hiện các thay đổi trong các tệp mã nguồn, hãy xem lại thay đổi của tệp: **`C:\code\bobs-used-bookstore-classic\app\Bookstore.Web\Controllers\AddressController.cs`**

Bạn sẽ thấy rằng AWS Transform for .NET đã thay đổi các tham chiếu namespace để tương thích với .NET 8\.

![][image19]

*Hình 20 – So sánh sự khác biệt cho AddressController.cs* 

Để xác nhận rằng AWS Transform for .NET đã thay đổi mã Razor trong các view MVC của bạn, hãy xem các thay đổi được thực hiện trong:  
**`C:\code\bobs-used-bookstore-classic\app\Bookstore.Web\Areas\Admin\Views\ReferenceData\CreateUpdate.cshtml`**

Bạn sẽ thấy rằng AWS Transform for .NET đã thay đổi lệnh gọi phương thức **Html.GetSelectListForEnum**.

![][image20]

*Hình 21 – So sánh sự khác biệt cho CreateUpdate.cshtml (Mã Razor trong MVC view)*

Chọn nút **Select All** nằm trong bảng **Show Diff**. Thao tác này sẽ chọn tất cả các tệp đã được chỉnh sửa hiển thị trong bảng.![][image21]

*Hình 22 – Chọn tất cả thay đổi* 

Chọn nút **Apply Changes**. AWS Transform for .NET sẽ áp dụng các thay đổi mã được đề xuất và các chuyển đổi vào **mã nguồn gốc của bạn**, cập nhật các tệp bằng mã đã được sửa đổi mới.

![][image22]

*Hình 23 – Áp dụng thay đổi*

### **Bước 6: Chạy ứng dụng / Các công việc còn tồn**

Mã nguồn ban đầu sử dụng Autofac để kích hoạt cơ chế dependency injection. Để xem lại mã gốc, trong Solution Explorer, dưới dự án **Bookstore.Web**, mở tệp **App\_Start\\DependencyInjectionSetup.cs.bak.** ASP.NET Core trong .NET 8 đi kèm cơ chế Dependency Injection tích hợp sẵn. Trong bài viết này, bạn sẽ thêm mã trong middleware của ASP.NET Core, sử dụng dependency injection tích hợp để thay thế chức năng do Autofac cung cấp. Tuy nhiên, trong các ứng dụng của riêng bạn, bạn có thể đánh giá xem gói ưa thích có hỗ trợ .NET 8 hay không và tiếp tục sử dụng nếu muốn.

Trong **Bookstore.Web**, mở **Program.cs.**

Sao chép và dán đoạn mã sau để thay thế nội dung của **Program.cs**.

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

                .ToList()

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

Để xác minh ứng dụng đã được chuyển đổi của bạn:

1. Trong Visual Studio, nhấn **F5** hoặc chọn **Debug,  Start Debugging.**

2. Ứng dụng sẽ khởi chạy trong trình duyệt mặc định của bạn.

3. Xác nhận rằng ứng dụng đã được chuyển đổi của bạn chạy đúng như mong đợi.

![][image23]

*Hình 24 – Ứng dụng .NET 8 đã được chuyển đổi chạy trong trình duyệt*

### **Dọn dẹp (Cleanup)**

Để dọn các tài nguyên sử dụng cho bài viết này, bạn chỉ cần xóa mã nguồn ứng dụng clone khỏi hệ thống file của bạn. Không có dịch vụ AWS nào được tạo ra trong bài viết này cần dọn qua console AWS.

## **Kết luận (Conclusion)**

Việc ra mắt chính thức của AWS Transform mang đến những tính năng mới đầy thú vị cho các nhà phát triển .NET. Giờ đây, khách hàng có thể hoàn tất quá trình chuyển đổi các ứng dụng MVC, bao gồm cả các ứng dụng có Razor views, hỗ trợ các dự án chứa gói NuGet riêng, và truy cập báo cáo tóm tắt quá trình chuyển đổi (transformation summary report), trong đó trình bày chi tiết các thay đổi đã được thực hiện. Đây là một giải pháp tiết kiệm chi phí, không phát sinh thêm phí khi sử dụng AWS Transform for .NET.

Lợi ích của việc chuyển ứng dụng sang Linux là vô cùng thuyết phục: [Các ứng dụng giảm 40% chi phí vận hành, vì bạn tiết kiệm được chi phí bản quyền Windows, chạy nhanh hơn từ 1,5 đến 2 lần nhờ hiệu năng được cải thiện, và xử lý khối lượng công việc tăng trưởng hiệu quả hơn 50% nhờ khả năng mở rộng vượt trội.](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/)

Chúng tôi trân trọng mời bạn [chuyển đổi các ứng dụng .NET](https://aws.amazon.com/transform/net/) của mình — chưa bao giờ có thời điểm nào tốt hơn để thực hiện điều đó.

---

AWS hiện có nhiều dịch vụ hơn đáng kể, cùng nhiều tính năng hơn trong từng dịch vụ, so với bất kỳ nhà cung cấp đám mây nào khác, giúp việc di chuyển các ứng dụng hiện có của bạn lên đám mây trở nên nhanh hơn, dễ dàng hơn và tiết kiệm chi phí hơn, đồng thời cho phép bạn xây dựng gần như mọi thứ bạn có thể tưởng tượng. Hãy mang đến cho các ứng dụng Microsoft của bạn hạ tầng mà chúng cần để thúc đẩy những kết quả kinh doanh mà bạn mong muốn. Truy cập các blog [.NET on AWS](https://aws.amazon.com/blogs/dotnet/) và [AWS Database](https://aws.amazon.com/blogs/database/) của chúng tôi để tìm hiểu thêm hướng dẫn và các lựa chọn bổ sung cho khối lượng công việc Microsoft (Microsoft workloads) của bạn. [Liên hệ với chúng tôi](https://pages.awscloud.com/MAP-windows-contact-us.html) ngay hôm nay để bắt đầu hành trình di cư và hiện đại hóa (migration and modernization journey) của bạn.

Neeraj Handa

Neeraj Handa là Kiến trúc sư Giải pháp Chuyên biệt (Specialist Solutions Architect) tại Amazon Web Services (AWS), nơi anh hợp tác với các khách hàng doanh nghiệp để đẩy nhanh quá trình phát triển và hiện đại hóa ứng dụng bằng cách sử dụng các dịch vụ AI sinh (generative AI services). Anh đam mê việc hỗ trợ các tổ chức chuyển đổi vòng đời phát triển phần mềm (software development lifecycle) nhằm đạt được năng suất cao hơn và chất lượng phần mềm tốt hơn thông qua việc ứng dụng các công nghệ trí tuệ nhân tạo (AI technologies).

### Artur Rodrigues

Artur Rodrigues là Kiến trúc sư Giải pháp Chính (Principal Solutions Architect) chuyên về Generative AI tại Amazon Web Services (AWS), nơi anh giúp các nhà phát triển khai thác các công nghệ AI tiên tiến để nâng cao quy trình làm việc và thúc đẩy đổi mới sáng tạo. Ngoài công việc, Artur yêu thích đạp xe và khám phá thiên nhiên tươi đẹp của British Columbia, Canada.

### Juveria Kanodia

Juveria Kanodia là Trưởng Bộ phận Kỹ thuật (Head of Engineering) trong tổ chức AWS Agentic AI .NET Modernization. Cô lãnh đạo nhóm kỹ sư phát triển các giải pháp tận dụng những tiến bộ mới nhất trong AI sinh và AI tác nhân (generative and agentic AI) để chuyển đổi khối lượng công việc Windows cho doanh nghiệp. Juveria có hơn 20 năm kinh nghiệm lãnh đạo kỹ thuật trong các dịch vụ quy mô lớn dựa trên AI và B2B. Cô có bằng Thạc sĩ Khoa học Máy tính tại Rochester Institute of Technology (RIT), chuyên ngành Khai phá dữ liệu (Data Mining), và sở hữu nhiều bằng sáng chế trong lĩnh vực điện toán đám mây và trí tuệ nhân tạo.and B2B large-scale services. Juveria has a Master's Degree in Computer Science from RIT, with specialization in Data Mining, and holds several patents in cloud computing and AI.

### Mark Fawaz

Mark Fawaz là Kỹ sư Phần mềm Cao cấp (Senior Software Development Engineer – SDE) trong tổ chức AWS Agentic AI, tập trung vào việc hỗ trợ khách hàng di chuyển, hiện đại hóa và tối ưu hóa các khối lượng công việc .NET và Windows của họ trên nền tảng AWS.

[image1]: ../../../static/images/3-BlogImage/Blog1/blog1-1.png

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