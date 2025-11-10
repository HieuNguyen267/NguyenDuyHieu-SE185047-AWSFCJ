
E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo title : "Các bước chuẩn bị"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo title : "Các bước chuẩn bị" ) 
) 
title : "Các bước chuẩn bị"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo date :  "`r Sys.Date()`"    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo date :  "`r Sys.Date()`"  ) 
) 
date :  "`r Sys.Date()`" 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo weight : 2   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo weight : 2 ) 
) 
weight : 2

E:\thuctap\report mau\fcj-workshop-template-main>(
echo chapter : false   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo chapter : false ) 
) 
chapter : false

E:\thuctap\report mau\fcj-workshop-template-main>(
echo pre : " <b> 5.2. </b> "   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo pre : " <b> 5.2. </b> " ) 
) 
pre : " <b> 5.2. </b> "

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ---   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo --- ) 
) 
---

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### IAM permissions   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### IAM permissions ) 
) 
#### IAM permissions

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Gắn IAM permission policy sau vào tài khoản aws user của bạn để triển khai và dọn dẹp tài nguyên trong workshop này.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Gắn IAM permission policy sau vào tài khoản aws user của bạn để triển khai và dọn dẹp tài nguyên trong workshop này. ) 
) 
Gắn IAM permission policy sau vào tài khoản aws user của bạn để triển khai và dọn dẹp tài nguyên trong workshop này.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo {   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo { ) 
) 
{

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     "Version": "2012-10-17",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     "Version": "2012-10-17", ) 
) 
    "Version": "2012-10-17",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     "Statement": [   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     "Statement": [ ) 
) 
    "Statement": [

E:\thuctap\report mau\fcj-workshop-template-main>(
echo         {   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo         { ) 
) 
        {

E:\thuctap\report mau\fcj-workshop-template-main>(
echo             "Sid": "VisualEditor0",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo             "Sid": "VisualEditor0", ) 
) 
            "Sid": "VisualEditor0",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo             "Effect": "Allow",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo             "Effect": "Allow", ) 
) 
            "Effect": "Allow",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo             "Action": [   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo             "Action": [ ) 
) 
            "Action": [

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "cloudformation:*",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "cloudformation:*", ) 
) 
                "cloudformation:*",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "cloudwatch:*",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "cloudwatch:*", ) 
) 
                "cloudwatch:*",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AcceptTransitGatewayPeeringAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AcceptTransitGatewayPeeringAttachment", ) 
) 
                "ec2:AcceptTransitGatewayPeeringAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AcceptTransitGatewayVpcAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AcceptTransitGatewayVpcAttachment", ) 
) 
                "ec2:AcceptTransitGatewayVpcAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AllocateAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AllocateAddress", ) 
) 
                "ec2:AllocateAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateAddress", ) 
) 
                "ec2:AssociateAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateIamInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateIamInstanceProfile", ) 
) 
                "ec2:AssociateIamInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateRouteTable", ) 
) 
                "ec2:AssociateRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateSubnetCidrBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateSubnetCidrBlock", ) 
) 
                "ec2:AssociateSubnetCidrBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateTransitGatewayRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateTransitGatewayRouteTable", ) 
) 
                "ec2:AssociateTransitGatewayRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AssociateVpcCidrBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AssociateVpcCidrBlock", ) 
) 
                "ec2:AssociateVpcCidrBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AttachInternetGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AttachInternetGateway", ) 
) 
                "ec2:AttachInternetGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AttachNetworkInterface",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AttachNetworkInterface", ) 
) 
                "ec2:AttachNetworkInterface",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AttachVolume",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AttachVolume", ) 
) 
                "ec2:AttachVolume",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AttachVpnGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AttachVpnGateway", ) 
) 
                "ec2:AttachVpnGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AuthorizeSecurityGroupEgress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AuthorizeSecurityGroupEgress", ) 
) 
                "ec2:AuthorizeSecurityGroupEgress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:AuthorizeSecurityGroupIngress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:AuthorizeSecurityGroupIngress", ) 
) 
                "ec2:AuthorizeSecurityGroupIngress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateClientVpnEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateClientVpnEndpoint", ) 
) 
                "ec2:CreateClientVpnEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateClientVpnRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateClientVpnRoute", ) 
) 
                "ec2:CreateClientVpnRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateCustomerGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateCustomerGateway", ) 
) 
                "ec2:CreateCustomerGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateDhcpOptions",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateDhcpOptions", ) 
) 
                "ec2:CreateDhcpOptions",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateFlowLogs",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateFlowLogs", ) 
) 
                "ec2:CreateFlowLogs",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateInternetGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateInternetGateway", ) 
) 
                "ec2:CreateInternetGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateLaunchTemplate",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateLaunchTemplate", ) 
) 
                "ec2:CreateLaunchTemplate",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateNetworkAcl",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateNetworkAcl", ) 
) 
                "ec2:CreateNetworkAcl",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateNetworkInterface",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateNetworkInterface", ) 
) 
                "ec2:CreateNetworkInterface",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateNetworkInterfacePermission",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateNetworkInterfacePermission", ) 
) 
                "ec2:CreateNetworkInterfacePermission",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateRoute", ) 
) 
                "ec2:CreateRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateRouteTable", ) 
) 
                "ec2:CreateRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateSecurityGroup",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateSecurityGroup", ) 
) 
                "ec2:CreateSecurityGroup",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateSubnet",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateSubnet", ) 
) 
                "ec2:CreateSubnet",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateSubnetCidrReservation",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateSubnetCidrReservation", ) 
) 
                "ec2:CreateSubnetCidrReservation",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTags",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTags", ) 
) 
                "ec2:CreateTags",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGateway", ) 
) 
                "ec2:CreateTransitGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGatewayPeeringAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGatewayPeeringAttachment", ) 
) 
                "ec2:CreateTransitGatewayPeeringAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGatewayPrefixListReference",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGatewayPrefixListReference", ) 
) 
                "ec2:CreateTransitGatewayPrefixListReference",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGatewayRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGatewayRoute", ) 
) 
                "ec2:CreateTransitGatewayRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGatewayRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGatewayRouteTable", ) 
) 
                "ec2:CreateTransitGatewayRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateTransitGatewayVpcAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateTransitGatewayVpcAttachment", ) 
) 
                "ec2:CreateTransitGatewayVpcAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpc",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpc", ) 
) 
                "ec2:CreateVpc",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpcEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpcEndpoint", ) 
) 
                "ec2:CreateVpcEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpcEndpointConnectionNotification",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpcEndpointConnectionNotification", ) 
) 
                "ec2:CreateVpcEndpointConnectionNotification",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpcEndpointServiceConfiguration",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpcEndpointServiceConfiguration", ) 
) 
                "ec2:CreateVpcEndpointServiceConfiguration",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpnConnection",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpnConnection", ) 
) 
                "ec2:CreateVpnConnection",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpnConnectionRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpnConnectionRoute", ) 
) 
                "ec2:CreateVpnConnectionRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:CreateVpnGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:CreateVpnGateway", ) 
) 
                "ec2:CreateVpnGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteCustomerGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteCustomerGateway", ) 
) 
                "ec2:DeleteCustomerGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteFlowLogs",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteFlowLogs", ) 
) 
                "ec2:DeleteFlowLogs",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteInternetGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteInternetGateway", ) 
) 
                "ec2:DeleteInternetGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteNetworkInterface",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteNetworkInterface", ) 
) 
                "ec2:DeleteNetworkInterface",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteNetworkInterfacePermission",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteNetworkInterfacePermission", ) 
) 
                "ec2:DeleteNetworkInterfacePermission",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteRoute", ) 
) 
                "ec2:DeleteRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteRouteTable", ) 
) 
                "ec2:DeleteRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteSecurityGroup",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteSecurityGroup", ) 
) 
                "ec2:DeleteSecurityGroup",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteSubnet",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteSubnet", ) 
) 
                "ec2:DeleteSubnet",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteSubnetCidrReservation",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteSubnetCidrReservation", ) 
) 
                "ec2:DeleteSubnetCidrReservation",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTags",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTags", ) 
) 
                "ec2:DeleteTags",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGateway", ) 
) 
                "ec2:DeleteTransitGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGatewayPeeringAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGatewayPeeringAttachment", ) 
) 
                "ec2:DeleteTransitGatewayPeeringAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGatewayPrefixListReference",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGatewayPrefixListReference", ) 
) 
                "ec2:DeleteTransitGatewayPrefixListReference",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGatewayRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGatewayRoute", ) 
) 
                "ec2:DeleteTransitGatewayRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGatewayRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGatewayRouteTable", ) 
) 
                "ec2:DeleteTransitGatewayRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteTransitGatewayVpcAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteTransitGatewayVpcAttachment", ) 
) 
                "ec2:DeleteTransitGatewayVpcAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteVpc",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteVpc", ) 
) 
                "ec2:DeleteVpc",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteVpcEndpoints",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteVpcEndpoints", ) 
) 
                "ec2:DeleteVpcEndpoints",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteVpcEndpointServiceConfigurations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteVpcEndpointServiceConfigurations", ) 
) 
                "ec2:DeleteVpcEndpointServiceConfigurations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteVpnConnection",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteVpnConnection", ) 
) 
                "ec2:DeleteVpnConnection",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DeleteVpnConnectionRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DeleteVpnConnectionRoute", ) 
) 
                "ec2:DeleteVpnConnectionRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:Describe*",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:Describe*", ) 
) 
                "ec2:Describe*",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DetachInternetGateway",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DetachInternetGateway", ) 
) 
                "ec2:DetachInternetGateway",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DisassociateAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DisassociateAddress", ) 
) 
                "ec2:DisassociateAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:DisassociateRouteTable",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:DisassociateRouteTable", ) 
) 
                "ec2:DisassociateRouteTable",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:GetLaunchTemplateData",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:GetLaunchTemplateData", ) 
) 
                "ec2:GetLaunchTemplateData",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:GetTransitGatewayAttachmentPropagations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:GetTransitGatewayAttachmentPropagations", ) 
) 
                "ec2:GetTransitGatewayAttachmentPropagations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ModifyInstanceAttribute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ModifyInstanceAttribute", ) 
) 
                "ec2:ModifyInstanceAttribute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ModifySecurityGroupRules",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ModifySecurityGroupRules", ) 
) 
                "ec2:ModifySecurityGroupRules",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ModifyTransitGatewayVpcAttachment",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ModifyTransitGatewayVpcAttachment", ) 
) 
                "ec2:ModifyTransitGatewayVpcAttachment",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ModifyVpcAttribute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ModifyVpcAttribute", ) 
) 
                "ec2:ModifyVpcAttribute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ModifyVpcEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ModifyVpcEndpoint", ) 
) 
                "ec2:ModifyVpcEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ReleaseAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ReleaseAddress", ) 
) 
                "ec2:ReleaseAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:ReplaceRoute",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:ReplaceRoute", ) 
) 
                "ec2:ReplaceRoute",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:RevokeSecurityGroupEgress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:RevokeSecurityGroupEgress", ) 
) 
                "ec2:RevokeSecurityGroupEgress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:RevokeSecurityGroupIngress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:RevokeSecurityGroupIngress", ) 
) 
                "ec2:RevokeSecurityGroupIngress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:RunInstances",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:RunInstances", ) 
) 
                "ec2:RunInstances",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:StartInstances",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:StartInstances", ) 
) 
                "ec2:StartInstances",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:StopInstances",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:StopInstances", ) 
) 
                "ec2:StopInstances",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:UpdateSecurityGroupRuleDescriptionsEgress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:UpdateSecurityGroupRuleDescriptionsEgress", ) 
) 
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ec2:UpdateSecurityGroupRuleDescriptionsIngress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ec2:UpdateSecurityGroupRuleDescriptionsIngress", ) 
) 
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:AddRoleToInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:AddRoleToInstanceProfile", ) 
) 
                "iam:AddRoleToInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:AttachRolePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:AttachRolePolicy", ) 
) 
                "iam:AttachRolePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:CreateInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:CreateInstanceProfile", ) 
) 
                "iam:CreateInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:CreatePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:CreatePolicy", ) 
) 
                "iam:CreatePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:CreateRole",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:CreateRole", ) 
) 
                "iam:CreateRole",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:DeleteInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:DeleteInstanceProfile", ) 
) 
                "iam:DeleteInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:DeletePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:DeletePolicy", ) 
) 
                "iam:DeletePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:DeleteRole",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:DeleteRole", ) 
) 
                "iam:DeleteRole",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:DeleteRolePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:DeleteRolePolicy", ) 
) 
                "iam:DeleteRolePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:DetachRolePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:DetachRolePolicy", ) 
) 
                "iam:DetachRolePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:GetInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:GetInstanceProfile", ) 
) 
                "iam:GetInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:GetPolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:GetPolicy", ) 
) 
                "iam:GetPolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:GetRole",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:GetRole", ) 
) 
                "iam:GetRole",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:GetRolePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:GetRolePolicy", ) 
) 
                "iam:GetRolePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:ListPolicyVersions",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:ListPolicyVersions", ) 
) 
                "iam:ListPolicyVersions",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:ListRoles",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:ListRoles", ) 
) 
                "iam:ListRoles",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:PassRole",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:PassRole", ) 
) 
                "iam:PassRole",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:PutRolePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:PutRolePolicy", ) 
) 
                "iam:PutRolePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "iam:RemoveRoleFromInstanceProfile",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "iam:RemoveRoleFromInstanceProfile", ) 
) 
                "iam:RemoveRoleFromInstanceProfile",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:CreateFunction",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:CreateFunction", ) 
) 
                "lambda:CreateFunction",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:DeleteFunction",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:DeleteFunction", ) 
) 
                "lambda:DeleteFunction",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:DeleteLayerVersion",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:DeleteLayerVersion", ) 
) 
                "lambda:DeleteLayerVersion",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:GetFunction",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:GetFunction", ) 
) 
                "lambda:GetFunction",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:GetLayerVersion",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:GetLayerVersion", ) 
) 
                "lambda:GetLayerVersion",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:InvokeFunction",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:InvokeFunction", ) 
) 
                "lambda:InvokeFunction",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "lambda:PublishLayerVersion",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "lambda:PublishLayerVersion", ) 
) 
                "lambda:PublishLayerVersion",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "logs:CreateLogGroup",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "logs:CreateLogGroup", ) 
) 
                "logs:CreateLogGroup",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "logs:DeleteLogGroup",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "logs:DeleteLogGroup", ) 
) 
                "logs:DeleteLogGroup",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "logs:DescribeLogGroups",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "logs:DescribeLogGroups", ) 
) 
                "logs:DescribeLogGroups",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "logs:PutRetentionPolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "logs:PutRetentionPolicy", ) 
) 
                "logs:PutRetentionPolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:ChangeTagsForResource",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:ChangeTagsForResource", ) 
) 
                "route53:ChangeTagsForResource",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:CreateHealthCheck",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:CreateHealthCheck", ) 
) 
                "route53:CreateHealthCheck",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:CreateHostedZone",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:CreateHostedZone", ) 
) 
                "route53:CreateHostedZone",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:CreateTrafficPolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:CreateTrafficPolicy", ) 
) 
                "route53:CreateTrafficPolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:DeleteHostedZone",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:DeleteHostedZone", ) 
) 
                "route53:DeleteHostedZone",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:DisassociateVPCFromHostedZone",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:DisassociateVPCFromHostedZone", ) 
) 
                "route53:DisassociateVPCFromHostedZone",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:GetHostedZone",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:GetHostedZone", ) 
) 
                "route53:GetHostedZone",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53:ListHostedZones",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53:ListHostedZones", ) 
) 
                "route53:ListHostedZones",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53domains:ListDomains",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53domains:ListDomains", ) 
) 
                "route53domains:ListDomains",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53domains:ListOperations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53domains:ListOperations", ) 
) 
                "route53domains:ListOperations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53domains:ListTagsForDomain",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53domains:ListTagsForDomain", ) 
) 
                "route53domains:ListTagsForDomain",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:AssociateResolverEndpointIpAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:AssociateResolverEndpointIpAddress", ) 
) 
                "route53resolver:AssociateResolverEndpointIpAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:AssociateResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:AssociateResolverRule", ) 
) 
                "route53resolver:AssociateResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:CreateResolverEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:CreateResolverEndpoint", ) 
) 
                "route53resolver:CreateResolverEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:CreateResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:CreateResolverRule", ) 
) 
                "route53resolver:CreateResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:DeleteResolverEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:DeleteResolverEndpoint", ) 
) 
                "route53resolver:DeleteResolverEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:DeleteResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:DeleteResolverRule", ) 
) 
                "route53resolver:DeleteResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:DisassociateResolverEndpointIpAddress",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:DisassociateResolverEndpointIpAddress", ) 
) 
                "route53resolver:DisassociateResolverEndpointIpAddress",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:DisassociateResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:DisassociateResolverRule", ) 
) 
                "route53resolver:DisassociateResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:GetResolverEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:GetResolverEndpoint", ) 
) 
                "route53resolver:GetResolverEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:GetResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:GetResolverRule", ) 
) 
                "route53resolver:GetResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:ListResolverEndpointIpAddresses",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:ListResolverEndpointIpAddresses", ) 
) 
                "route53resolver:ListResolverEndpointIpAddresses",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:ListResolverEndpoints",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:ListResolverEndpoints", ) 
) 
                "route53resolver:ListResolverEndpoints",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:ListResolverRuleAssociations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:ListResolverRuleAssociations", ) 
) 
                "route53resolver:ListResolverRuleAssociations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:ListResolverRules",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:ListResolverRules", ) 
) 
                "route53resolver:ListResolverRules",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:ListTagsForResource",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:ListTagsForResource", ) 
) 
                "route53resolver:ListTagsForResource",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:UpdateResolverEndpoint",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:UpdateResolverEndpoint", ) 
) 
                "route53resolver:UpdateResolverEndpoint",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "route53resolver:UpdateResolverRule",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "route53resolver:UpdateResolverRule", ) 
) 
                "route53resolver:UpdateResolverRule",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:AbortMultipartUpload",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:AbortMultipartUpload", ) 
) 
                "s3:AbortMultipartUpload",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:CreateBucket",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:CreateBucket", ) 
) 
                "s3:CreateBucket",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:DeleteBucket",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:DeleteBucket", ) 
) 
                "s3:DeleteBucket",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:DeleteObject",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:DeleteObject", ) 
) 
                "s3:DeleteObject",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetAccountPublicAccessBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetAccountPublicAccessBlock", ) 
) 
                "s3:GetAccountPublicAccessBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketAcl",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketAcl", ) 
) 
                "s3:GetBucketAcl",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketOwnershipControls",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketOwnershipControls", ) 
) 
                "s3:GetBucketOwnershipControls",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketPolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketPolicy", ) 
) 
                "s3:GetBucketPolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketPolicyStatus",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketPolicyStatus", ) 
) 
                "s3:GetBucketPolicyStatus",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketPublicAccessBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketPublicAccessBlock", ) 
) 
                "s3:GetBucketPublicAccessBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetObject",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetObject", ) 
) 
                "s3:GetObject",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetObjectVersion",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetObjectVersion", ) 
) 
                "s3:GetObjectVersion",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:GetBucketVersioning",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:GetBucketVersioning", ) 
) 
                "s3:GetBucketVersioning",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListAccessPoints",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListAccessPoints", ) 
) 
                "s3:ListAccessPoints",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListAccessPointsForObjectLambda",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListAccessPointsForObjectLambda", ) 
) 
                "s3:ListAccessPointsForObjectLambda",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListAllMyBuckets",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListAllMyBuckets", ) 
) 
                "s3:ListAllMyBuckets",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListBucket",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListBucket", ) 
) 
                "s3:ListBucket",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListBucketMultipartUploads",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListBucketMultipartUploads", ) 
) 
                "s3:ListBucketMultipartUploads",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListBucketVersions",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListBucketVersions", ) 
) 
                "s3:ListBucketVersions",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListJobs",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListJobs", ) 
) 
                "s3:ListJobs",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListMultipartUploadParts",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListMultipartUploadParts", ) 
) 
                "s3:ListMultipartUploadParts",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListMultiRegionAccessPoints",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListMultiRegionAccessPoints", ) 
) 
                "s3:ListMultiRegionAccessPoints",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:ListStorageLensConfigurations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:ListStorageLensConfigurations", ) 
) 
                "s3:ListStorageLensConfigurations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:PutAccountPublicAccessBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:PutAccountPublicAccessBlock", ) 
) 
                "s3:PutAccountPublicAccessBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:PutBucketAcl",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:PutBucketAcl", ) 
) 
                "s3:PutBucketAcl",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:PutBucketPolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:PutBucketPolicy", ) 
) 
                "s3:PutBucketPolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:PutBucketPublicAccessBlock",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:PutBucketPublicAccessBlock", ) 
) 
                "s3:PutBucketPublicAccessBlock",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "s3:PutObject",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "s3:PutObject", ) 
) 
                "s3:PutObject",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:CreateSecret",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:CreateSecret", ) 
) 
                "secretsmanager:CreateSecret",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:DeleteSecret",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:DeleteSecret", ) 
) 
                "secretsmanager:DeleteSecret",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:DescribeSecret",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:DescribeSecret", ) 
) 
                "secretsmanager:DescribeSecret",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:GetSecretValue",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:GetSecretValue", ) 
) 
                "secretsmanager:GetSecretValue",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:ListSecrets",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:ListSecrets", ) 
) 
                "secretsmanager:ListSecrets",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:ListSecretVersionIds",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:ListSecretVersionIds", ) 
) 
                "secretsmanager:ListSecretVersionIds",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:PutResourcePolicy",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:PutResourcePolicy", ) 
) 
                "secretsmanager:PutResourcePolicy",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:TagResource",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:TagResource", ) 
) 
                "secretsmanager:TagResource",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "secretsmanager:UpdateSecret",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "secretsmanager:UpdateSecret", ) 
) 
                "secretsmanager:UpdateSecret",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "sns:ListTopics",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "sns:ListTopics", ) 
) 
                "sns:ListTopics",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:DescribeInstanceProperties",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:DescribeInstanceProperties", ) 
) 
                "ssm:DescribeInstanceProperties",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:DescribeSessions",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:DescribeSessions", ) 
) 
                "ssm:DescribeSessions",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:GetConnectionStatus",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:GetConnectionStatus", ) 
) 
                "ssm:GetConnectionStatus",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:GetParameters",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:GetParameters", ) 
) 
                "ssm:GetParameters",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:ListAssociations",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:ListAssociations", ) 
) 
                "ssm:ListAssociations",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:ResumeSession",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:ResumeSession", ) 
) 
                "ssm:ResumeSession",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:StartSession",   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:StartSession", ) 
) 
                "ssm:StartSession",

E:\thuctap\report mau\fcj-workshop-template-main>(
echo                 "ssm:TerminateSession"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo                 "ssm:TerminateSession" ) 
) 
                "ssm:TerminateSession"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo             ],   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo             ], ) 
) 
            ],

E:\thuctap\report mau\fcj-workshop-template-main>(
echo             "Resource": "*"   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo             "Resource": "*" ) 
) 
            "Resource": "*"

E:\thuctap\report mau\fcj-workshop-template-main>(
echo         }   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo         } ) 
) 
        }

E:\thuctap\report mau\fcj-workshop-template-main>(
echo     ]   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo     ] ) 
) 
    ]

E:\thuctap\report mau\fcj-workshop-template-main>(
echo }   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo } ) 
) 
}

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ```   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ``` ) 
) 
```

E:\thuctap\report mau\fcj-workshop-template-main>(
echo #### Khởi tạo tài nguyên bằng CloudFormation   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo #### Khởi tạo tài nguyên bằng CloudFormation ) 
) 
#### Khởi tạo tài nguyên bằng CloudFormation

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Trong lab này, chúng ta sẽ dùng N.Virginia region (us-east-1).   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Trong lab này, chúng ta sẽ dùng N.Virginia region (us-east-1). ) 
) 
Trong lab này, chúng ta sẽ dùng N.Virginia region (us-east-1).

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Để chuẩn bị cho môi trường làm workshop, chúng ta deploy CloudFormation template sau (click link): [PrivateLinkWorkshop ](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.us-east-1.amazonaws.com/reinvent-endpoints-builders-session/Nested.yaml&stackName=PLCloudSetup). Để nguyên các lựa chọn mặc định.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Để chuẩn bị cho môi trường làm workshop, chúng ta deploy CloudFormation template sau (click link): [PrivateLinkWorkshop ](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.us-east-1.amazonaws.com/reinvent-endpoints-builders-session/Nested.yaml&stackName=PLCloudSetup). Để nguyên các lựa chọn mặc định. ) 
) 
Để chuẩn bị cho môi trường làm workshop, chúng ta deploy CloudFormation template sau (click link): [PrivateLinkWorkshop ](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.us-east-1.amazonaws.com/reinvent-endpoints-builders-session/Nested.yaml&stackName=PLCloudSetup). Để nguyên các lựa chọn mặc định.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack1.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack1.png) ) 
) 
![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack1.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Lựa chọn 2 mục acknowledgement    | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Lựa chọn 2 mục acknowledgement  ) 
) 
+ Lựa chọn 2 mục acknowledgement 

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + Chọn Create stack   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + Chọn Create stack ) 
) 
+ Chọn Create stack

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack2.png) ) 
) 
![create stack](/images/5-Workshop/5.2-Prerequisite/create-stack2.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo Quá trình triển khai CloudFormation cần khoảng 15 phút để hoàn thành.   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo Quá trình triển khai CloudFormation cần khoảng 15 phút để hoàn thành. ) 
) 
Quá trình triển khai CloudFormation cần khoảng 15 phút để hoàn thành.

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![complete](/images/5-Workshop/5.2-Prerequisite/complete.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![complete](/images/5-Workshop/5.2-Prerequisite/complete.png) ) 
) 
![complete](/images/5-Workshop/5.2-Prerequisite/complete.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + 2 VPCs đã được tạo   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + 2 VPCs đã được tạo ) 
) 
+ 2 VPCs đã được tạo

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![vpcs](/images/5-Workshop/5.2-Prerequisite/vpcs.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![vpcs](/images/5-Workshop/5.2-Prerequisite/vpcs.png) ) 
) 
![vpcs](/images/5-Workshop/5.2-Prerequisite/vpcs.png)

E:\thuctap\report mau\fcj-workshop-template-main>(
echo + 3 EC2s đã được tạo   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo + 3 EC2s đã được tạo ) 
) 
+ 3 EC2s đã được tạo

E:\thuctap\report mau\fcj-workshop-template-main>(
echo ![EC2](/images/5-Workshop/5.2-Prerequisite/ec2.png)   | findstr /R "^date:"  1>nul  
 if not errorlevel 1 (echo date: 2025-01-01T00:00:00Z )  else (echo ![EC2](/images/5-Workshop/5.2-Prerequisite/ec2.png) ) 
) 
![EC2](/images/5-Workshop/5.2-Prerequisite/ec2.png)
