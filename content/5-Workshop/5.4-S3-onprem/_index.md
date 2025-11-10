
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Access S3 from on-premises"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Access S3 from on-premises" ) 
) 
title : "Access S3 from on-premises"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date : "`r Sys.Date()`"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date : "`r Sys.Date()`" ) 
) 
date : "`r Sys.Date()`"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 4   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 4 ) 
) 
weight : 4

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.4. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.4. </b> " ) 
) 
pre : " <b> 5.4. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Overview   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Overview ) 
) 
#### Overview

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + In this section, you will create an Interface endpoint to access Amazon S3 from a simulated on-premises environment. The Interface endpoint will allow you to route to Amazon S3 over a VPN connection from your simulated on-premises environment.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + In this section, you will create an Interface endpoint to access Amazon S3 from a simulated on-premises environment. The Interface endpoint will allow you to route to Amazon S3 over a VPN connection from your simulated on-premises environment. ) 
) 
+ In this section, you will create an Interface endpoint to access Amazon S3 from a simulated on-premises environment. The Interface endpoint will allow you to route to Amazon S3 over a VPN connection from your simulated on-premises environment.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Why using **Interface endpoint**:    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Why using **Interface endpoint**:  ) 
) 
+ Why using **Interface endpoint**: 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     + Gateway endpoints only work with resources running in the VPC where they are created. Interface endpoints work with resources running in VPC, and also resources running in on-premises environments. Connectivty from your on-premises environment to the cloud can be provided by AWS Site-to-Site VPN or AWS Direct Connect.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     + Gateway endpoints only work with resources running in the VPC where they are created. Interface endpoints work with resources running in VPC, and also resources running in on-premises environments. Connectivty from your on-premises environment to the cloud can be provided by AWS Site-to-Site VPN or AWS Direct Connect. ) 
) 
    + Gateway endpoints only work with resources running in the VPC where they are created. Interface endpoints work with resources running in VPC, and also resources running in on-premises environments. Connectivty from your on-premises environment to the cloud can be provided by AWS Site-to-Site VPN or AWS Direct Connect.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     + Interface endpoints allow you to connect to services powered by AWS PrivateLink. These services include some AWS services, services hosted by other AWS customers and partners in their own VPCs (referred to as PrivateLink Endpoint Services), and supported AWS Marketplace Partner services. For this workshop, we will focus on connecting to Amazon S3.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     + Interface endpoints allow you to connect to services powered by AWS PrivateLink. These services include some AWS services, services hosted by other AWS customers and partners in their own VPCs (referred to as PrivateLink Endpoint Services), and supported AWS Marketplace Partner services. For this workshop, we will focus on connecting to Amazon S3. ) 
) 
    + Interface endpoints allow you to connect to services powered by AWS PrivateLink. These services include some AWS services, services hosted by other AWS customers and partners in their own VPCs (referred to as PrivateLink Endpoint Services), and supported AWS Marketplace Partner services. For this workshop, we will focus on connecting to Amazon S3.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png) ) 
) 
![Interface endpoint architecture](/images/5-Workshop/5.4-S3-onprem/diagram3.png)
