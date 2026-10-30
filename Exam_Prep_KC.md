# Exam Prep

## KC - Assessment Scenario Certification Preparation

#### 1. A federal contractor located in Seattle is expanding their cloud presence to Germany, which has strict rules on data that originated in Germany leaving the region, known as data sovereignty. They know that they will have auditors auditing both regions. What selection criteria should be prioritized for this customer's expansion needs?
- [ ] Customer requirements
- [ ] Proximity to customers
- [ ] Services available within the Region
- [x] Data governance, legal requirements ✅

> **💡 Why:** Data sovereignty and auditors mean the law decides where data may live. When choosing a Region, compliance and data governance come first; latency, price and service availability are secondary.
>
> **🔑 Keywords:** `data sovereignty`, `strict rules`, `leaving the region`, `auditors`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) · [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

#### 2. A federal contractor located in Seattle is expanding their cloud presence to Germany, which has strict rules on data that originated in Germany leaving the region, known as data sovereignty. They know that they will have auditors auditing both regions. Which services would be considered global for this customer? (Select THREE.)
- [ ] Amazon Elastic Compute Cloud (Amazon EC2)
- [x] Amazon Cloud Front ✅
- [x] Amazon Route 53 ✅
- [ ] Amazon Machine Images (AMIs)
- [x] AWS Identity and Access Management (IAM) ✅

> **💡 Why:** Global services are not tied to one Region: CloudFront, Route 53 and IAM. EC2 instances and AMIs are Regional resources.
>
> **🔑 Keywords:** `global`, `which services`
>
> **📖 Official docs:** [Global services (fault isolation boundaries)](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html)

#### 3. A financial company is working with AWS for their new website. Administrators update images and related content on a monthly basis. They have noticed that the website's images take a while to load, especially for some of the global customers.
What service would be beneficial for reducing the latency on image downloads?
- [x] Amazon CloudFront ✅
- [ ] Amazon Simple Storage Service (Amazon S3)
- [ ] Amazon Elastic Compute Cloud (Amazon EC2)
- [ ] Amazon Elastic Block Store (Amazon EBS)

> **💡 Why:** CloudFront is the CDN. It caches content at edge locations close to viewers, so global customers get lower latency.
>
> **🔑 Keywords:** `take a while to load`, `global customers`, `reducing the latency`
>
> **📖 Official docs:** [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) · [How CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)

#### 4. A financial company is working with AWS for their new website. Administrators update images and related content on a monthly basis. They have noticed that the website's images take a while to load, especially for some of the global customers.
Where should the images that are used for the website stored?
- [ ] Amazon Glacier
- [x] Amazon Simple Storage Service (Amazon S3) ✅
- [ ] Amazon CloudFront
- [ ] Amazon Elastic Block Store (Amazon EBS)

> **💡 Why:** S3 is the origin store for static files such as images; CloudFront only caches copies. Glacier is for archives, EBS is block storage for one EC2 instance.
>
> **🔑 Keywords:** `images`, `stored`, `updated monthly`
>
> **📖 Official docs:** [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

#### 5. A financial company is working with AWS for their new website. Administrators update images and related content on a monthly basis. They have noticed that the website's images take a while to load, especially for some of the global customers.
What AWS CLI output format is most readable by a person, and should be selected by the SysOps administrator to show the customer the results of the image search?
- [ ] Text
- [ ] JavaScript Object Notation (JSON)
- [ ] Command
- [x] Table ✅

> **💡 Why:** The CLI `--output table` format is formatted for people. JSON is the default and is meant for programs; text is for scripts.
>
> **🔑 Keywords:** `most readable by a person`, `output format`
>
> **📖 Official docs:** [AWS CLI output format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html)

#### 6. A financial company is working with AWS for their new website. Administrators update images and related content on a monthly basis. They have noticed that the website's images take a while to load, especially for some of the global customers. Which AWS Command Line Interface (AWS CLI) command should the SysOps administrator use to check all the permissions that are needed to run the required action of the image archive before the action is executed?
- [ ] --output
- [ ] --filter
- [x] --dry-run ✅
- [ ] --query

> **💡 Why:** `--dry-run` checks that you have the required permissions without actually running the action. `--query` filters output, `--output` sets the format, and `--filter` narrows what is returned.
>
> **🔑 Keywords:** `check all the permissions`, `before the action is executed`
>
> **📖 Official docs:** [ec2 run-instances (--dry-run)](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html)

#### 7. A startup tech has just created a mobile app that allows a customer to place a lunch order for delivery with local restaurants through a third party courier. They want to provide the customer and the restaurant with a notification that the delivery has been completed, as the building is secure and all food orders are left in the lobby.
What services could be used to provide the startup's customer with a notification of the food delivery? (Select TWO.)
- [ ] Amazon Lightsail
- [ ] Amazon Elastic Compute Cloud (Amazon EC2)
- [x] AWS Lambda ✅
- [x] Amazon Simple Notification Service (Amazon SNS) ✅
- [ ] Amazon Machine Images (AMIs)

> **💡 Why:** Lambda runs code when an event happens (delivery completed) and SNS pushes the notification to subscribers. Lightsail, EC2 and AMIs are not messaging services.
>
> **🔑 Keywords:** `notification`, `delivery has been completed`
>
> **📖 Official docs:** [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) · [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

#### 8. A startup tech has just created a mobile app that allows a customer to place a lunch order for delivery with local restaurants through a third party courier. They want to provide the customer and the restaurant with a notification that the delivery has been completed, as the building is secure and all food orders are left in the lobby.
Which IP address provides metadata service for all the instances associated with the mobile app?
- [ ] 127.255.255.255
- [ ] 169.254.255.255
- [x] 169.254.169.254 ✅
- [ ] 100.127.255.255

> **💡 Why:** The instance metadata service always lives at the link-local address 169.254.169.254.
>
> **🔑 Keywords:** `IP address`, `metadata service`, `all the instances`
>
> **📖 Official docs:** [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

#### 9. A SysOps engineer working at a local university has decided to launch Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce their hardware footprint. They are new to AWS and will only need to launch in one region until their business grows. When does user data run when you provision an instance?
- [ ] Creation
- [x] Initialization ✅
- [ ] Deployment
- [ ] Termination

> **💡 Why:** User data scripts run at instance initialization (first boot), not at creation, deployment or termination.
>
> **🔑 Keywords:** `user data run`, `provision an instance`
>
> **📖 Official docs:** [Run commands at launch (user data)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)

#### 10. A SysOps engineer working at a local university has decided to launch Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce their hardware footprint. They are new to AWS and will only need to launch in one region until their business grows. What type of Amazon EC2 instance would be a best practice for selection?
- [ ] Reserved
- [ ] Dedicated
- [ ] Spot
- [x] On-Demand ✅

> **💡 Why:** On-Demand needs no commitment, which suits a team that is new to AWS and has uncertain usage. Reserved needs a 1 or 3 year commitment, Spot can be interrupted, Dedicated is for isolation or licensing.
>
> **🔑 Keywords:** `new to AWS`, `only need to launch in one region until their business grows`
>
> **📖 Official docs:** [EC2 instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

#### 11. A SysOps engineer working at a local university has decided to launch Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce their hardware footprint. They are new to AWS and will only need to launch in one region until their business grows. What actions should the customer take if they would like new hardware to support the Amazon EC2 instance? (Select TWO.)
- [x] Stop the instance ✅
- [ ] Terminate the instance
- [x] Start the instance ✅
- [ ] Reboot the instance
- [ ] Create a new instance

> **💡 Why:** Stopping and then starting an instance usually moves it to new underlying host hardware. A reboot keeps the same host, and terminate deletes the instance.
>
> **🔑 Keywords:** `new hardware`, `support the Amazon EC2 instance`
>
> **📖 Official docs:** [Stop and start EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)

#### 12. A floral warehouse has just expanded delivery of wholesale flowers and plants to another region of the country and has experienced unexpected growth. They have an online ordering system that promises 48 hour delivery; therefore, they need quick notification of orders to the fulfillment center and a way to track their inventory more efficiently. As a consultant working with a floral warehouse customer that wants to enhance the infrastructure to support the growth, but needs to meet compliance requirements.
Which feature would support the warehouse manager's goal of having their customers receiving real time messages without requiring the customers to make additional requests to the server?
- [ ] Request tracing
- [ ] Sticky sessions
- [x] WebSockets ✅
- [ ] Operational monitoring

> **💡 Why:** WebSockets keep a persistent two-way connection, so the server can push messages without the client asking again.
>
> **🔑 Keywords:** `real time messages`, `without requiring ... additional requests to the server`
>
> **📖 Official docs:** [ALB listeners (WebSocket support)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)

#### 13. A floral warehouse has just expanded delivery of wholesale flowers and plants to another region of the country and has experienced unexpected growth. They have an online ordering system that promises 48 hour delivery; therefore, they need quick notification of orders to the fulfillment center and a way to track their inventory more efficiently. As a consultant working with a floral warehouse customer that wants to enhance the infrastructure to support the growth, but needs to meet compliance requirements.
Which failover configuration of Amazon Route 53 would support the warehouse's website so that it is available for the majority of the time, even if there are unhealthy instances?
- [x] Active-active failover ✅
- [ ] Active-passive failover
- [ ] Mixed failover configurations
- [ ] Active-active-passive failover

> **💡 Why:** In active-active failover all resources answer queries, and Route 53 stops sending traffic to unhealthy ones. The site stays up most of the time even if some instances fail. Active-passive keeps a standby that is used only after a failure.
>
> **🔑 Keywords:** `available for the majority of the time`, `even if there are unhealthy instances`
>
> **📖 Official docs:** [Route 53 active-active and active-passive failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html)

#### 14. A floral warehouse has just expanded delivery of wholesale flowers and plants to another region of the country and has experienced unexpected growth. They have an online ordering system that promises 48 hour delivery; therefore, they need quick notification of orders to the fulfillment center and a way to track their inventory more efficiently. As a consultant working with a floral warehouse customer that wants to enhance the infrastructure to support the growth, but needs to meet compliance requirements.
What functions does Amazon Route 53 provide for a website? (Select THREE.)
- [x] Routes traffic to the website based on the domain name that is entered. ✅
- [ ] Hosting for the website located in different Edge Locations.
- [x] Registers domain names. ✅
- [ ] Configures the best route for automatic scaling to a resource.
- [x] Completes health checks of the resource to ensure it can be reached. ✅

> **💡 Why:** Route 53 does DNS routing by domain name, domain registration and health checks. It does not host websites or handle auto scaling.
>
> **🔑 Keywords:** `functions`, `domain name`, `health checks`, `registers`
>
> **📖 Official docs:** [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

#### 15. A floral warehouse has just expanded delivery of wholesale flowers and plants to another region of the country and has experienced unexpected growth. They have an online ordering system that promises 48 hour delivery; therefore, they need quick notification of orders to the fulfillment center and a way to track their inventory more efficiently. As a consultant working with a floral warehouse customer that wants to enhance the infrastructure to support the growth, but needs to meet compliance requirements.
Which services can be used to store session-related information off from an Amazon Elastic Compute Cloud (Amazon EC2) instance so that the instance remains stateless? (Select TWO.)
- [ ] Amazon Simple Storage Service (Amazon S3)
- [x] Amazon ElastiCache ✅
- [x] Amazon DynamoDB ✅
- [ ] Amazon Auto Scaling
- [ ] Amazon Relational Database Service (Amazon RDS)

> **💡 Why:** ElastiCache (in-memory) and DynamoDB (key-value) are common external session stores. Keeping session data off the instance leaves the instance stateless.
>
> **🔑 Keywords:** `session-related information`, `off from an EC2 instance`, `stateless`
>
> **📖 Official docs:** [Session management with caching](https://aws.amazon.com/caching/session-management/) · [What is Amazon ElastiCache?](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) · [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 16. A trucking company is looking to track their fleet better and to ensure that they have updated information on the trucks each time they reach the office. Many of the trucks are out on the road for days at a time, but may be at the office for a break period that can last up to a day.
A trucking company is looking to minimize dependence on their current cloud service provider so they are not "locked in", while increasing their development of various applications. The company is trying to decide if they should use containers or go serverless. They know they only need secure, compute capacity when the trucks are at their home base, which may last a day a couple times a month. Sometimes they support partner companies when they are in town; therefore, they may need to accommodate those users once every couple months. What type of solution would be most ideal for the trucking company?
- [ ] On-premises
- [x] Serverless ✅
- [ ] Internet of Things (IoT)
- [ ] Hybrid

> **💡 Why:** Serverless fits sporadic usage: you pay only when the code runs, with no idle servers. The trucks are at base only about a day a couple of times a month.
>
> **🔑 Keywords:** `only need ... compute capacity`, `a day a couple times a month`, `go serverless`
>
> **📖 Official docs:** [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

#### 17. A trucking company is looking to track their fleet better and to ensure that they have updated information on the trucks each time they reach the office. Many of the trucks are out on the road for days at a time, but may be at the office for a break period that can last up to a day.
A trucking company is looking to minimize dependence on their current cloud service provider so they are not "locked in", while increasing their development velocity of various applications. The company is trying to decide if they should use containers or go serverless. They know they only need secure, compute capacity when the trucks are at their home base, which may last a day a couple times a month. Sometimes they support partner companies when they are in town; therefore, they may need to accommodate those users once every couple of months.
What type of Amazon Elastic Compute Cloud (Amazon EC2) instance should be used with AWS Lambda for the most economic benefit, while maintaining security and resiliency for the trucking company's use case?
- [ ] Reserved
- [ ] Dedicated
- [x] Spot ✅
- [ ] On-Demand

> **💡 Why:** The scenario is occasional and short-lived, so Spot's deep discount gives the 'most economic benefit'. The workload can tolerate interruption.
>
> **🔑 Keywords:** `most economic benefit`, `occasional use`
>
> **📖 Official docs:** [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) · [EC2 instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
>
> **⚠️ Note:** Spot can be interrupted, so it only suits interruption-tolerant work.

#### 18. A trucking company is looking to track their fleet better and to ensure that they have updated information on the trucks each time they reach the office. Many of the trucks are out on the road for days at a time, but may be at the office for a break period that can last up to a day.
A trucking company is looking to minimize dependence on their current cloud service provider so they are not "locked in", while increasing their development velocity of various applications. The company is trying to decide if they should use containers or go serverless. They know they only need secure, compute capacity when the trucks are at their home base, which may last a day a couple times a month. Sometimes they support partner companies when they are in town; therefore, they may need to accommodate those users once every couple of months.
Which data streaming service could be added to the trucking company's serverless design to analyze data that can be customized for future applications?
- [x] Amazon Kinesis ✅
- [ ] Amazon Cognito
- [ ] AWS Lambda
- [ ] Amazon Redshift

> **💡 Why:** Kinesis is AWS's streaming data service for collecting and analysing data in real time. Cognito is user authentication, Lambda is compute, Redshift is a data warehouse.
>
> **🔑 Keywords:** `data streaming service`, `analyze`
>
> **📖 Official docs:** [What is Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)


#### 19. A trucking company is looking to track their fleet better and to ensure that they have updated information on the trucks each time they reach the office. Many of the trucks are out on the road for days at a time, but may be at the office for a break period that can last up to a day.
A trucking company is looking to minimize dependence on their current cloud service provider so they are not "locked in", while increasing their development velocity of various applications. The company is trying to decide if they should use containers or go serverless. They know they only need secure, compute capacity when the trucks are at their home base, which may last a day a couple times a month. Sometimes they support partner companies when they are in town; therefore, they may need to accommodate those users once every couple of months. How many IAM policies support AWS Lambda authentication?
- [x] Two ✅
- [ ] Four
- [ ] Three
- [ ] One

> **💡 Why:** Lambda access is controlled by two policy types: identity-based policies and resource-based policies.
>
> **🔑 Keywords:** `How many IAM policies`, `Lambda authentication`
>
> **📖 Official docs:** [Managing permissions in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)

#### 20. A FinTech bank has created a new credit card line; therefore, will need to expand its database to capture new customer profiles and link existing customer profiles to the new card line, while maintaining security and PCI compliance requirements. The bank is entirely in the cloud and provides their customer's with unique financial visualizations about their financial habits. Their customers use a mobile app and website for their account transactions and profiles.
What rationale should be used for selecting Amazon DynamoDB as the database to support the mobile application? (Select THREE.)
- [x] Provides single-digit latency ✅
- [x] Supports document and key-value store models ✅
- [ ] Ensures read replicas are highly available
- [x] Utilizes unordered collections of name-value pairs ✅
- [ ] Support for Business Intelligence(BI) tools

> **💡 Why:** DynamoDB is a NoSQL database with single-digit millisecond latency, supporting document and key-value models. Its items are name-value pairs. Read replicas and BI tool support are not DynamoDB selling points.
>
> **🔑 Keywords:** `single-digit latency`, `document and key-value`, `name-value pairs`
>
> **📖 Official docs:** [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 21. A FinTech bank has created a new credit card line; therefore, will need to expand its database to capture new customer profiles and link existing customer profiles to the new card line, while maintaining security and PCI compliance requirements. The bank is entirely in the cloud and provides their customer's with unique financial visualizations about their financial habits. Their customers use a mobile app and website for their account transactions and profiles.
What Amazon DynamoDB attribute can store name-value pair collections that are enclosed in { }?
- [ ] List type
- [ ] Binary type
- [ ] Metadata tags
- [x] Map type ✅

> **💡 Why:** The DynamoDB Map type holds name-value pairs inside curly braces { }. The List type uses square brackets [ ].
>
> **🔑 Keywords:** `name-value pair collections`, `enclosed in { }`
>
> **📖 Official docs:** [DynamoDB data types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html)

#### 22. A FinTech bank has created a new credit card line; therefore, will need to expand its database to capture new customer profiles and link existing customer profiles to the new card line, while maintaining security and PCI compliance requirements. The bank is entirely in the cloud and provides their customer&#039;s with unique financial visualizations about their financial habits. Their customers use a mobile app and website for their account transactions and profiles.
Which database solution would be the most ideal and cost effective architectural choice for storing the customer's personal profile information indefinitely?
- [ ] Amazon Aurora
- [ ] Amazon Redshift
- [x] Amazon DynamoDB ✅ 
- [ ] Amazon ElastiCache

> **💡 Why:** DynamoDB is serverless, scalable and cheap for storing profile items long term. Aurora costs more, Redshift is analytics, and ElastiCache is an in-memory cache, not a durable store.
>
> **🔑 Keywords:** `personal profile information`, `indefinitely`, `cost effective`
>
> **📖 Official docs:** [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 23. A FinTech bank has created a new credit card line; therefore, will need to expand its database to capture new customer profiles and link existing customer profiles to the new card line, while maintaining security and PCI compliance requirements. The bank is entirely in the cloud and provides their customer's with unique financial visualizations about their financial habits. Their customers use a mobile app and website for their account transactions and profiles.
What database should be used to track the customer's monthly session data, which can provide insight into the mobile app features that customers use the most and thus help develop cost- effective enhancements for version updates?
- [ ] Amazon Aurora
- [x] Amazon DynamoDB ✅
- [ ] Amazon Neptune
- [ ] Amazon ElastiCache

> **💡 Why:** Session data is high-volume, simple key-value data, which DynamoDB handles well. Neptune is a graph database.
>
> **🔑 Keywords:** `monthly session data`, `mobile app`, `features customers use most`
>
> **📖 Official docs:** [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 24. The automotive industry is now developing a specific unmanned ground vehicle (UGV) to be used by the military that provides alerts to the operator of hazardous conditions, loss of connection, or vehicle damage. They know they will need to align with the National Institute of Standards and Technology (NIST) guidelines 800-171 regarding the vehicle's security strength to protect its location at all times. The application used by each UGV will be hosted in its own virtual private cloud (VPC) and run in a private subnet.
What type of network connection should be used to allow the UGV applications to securely share data between each other?
- [ ] AWS Direct Connect
- [x] VPC peering ✅
- [ ] Dedicated Hosts
- [ ] Internet gateway

> **💡 Why:** VPC peering connects two VPCs privately over the AWS network, without the internet. Direct Connect links on-premises to AWS, and an internet gateway exposes traffic to the internet.
>
> **🔑 Keywords:** `own virtual private cloud (VPC)`, `securely share data between each other`
>
> **📖 Official docs:** [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)

#### 25. The automotive industry is now developing a specific unmanned ground vehicle (UGV) to be used by the military that provides alerts to the operator of hazardous conditions, loss of connection, or vehicle damage. They know they will need to align with the National Institute of Standards and Technology (NIST) guidelines 800-171 regarding the vehicle&#039;s security strength to protect its location at all times. The application used by each UGV will be hosted in its own virtual private cloud (VPC) and run in a private subnet.
The operator has reported the UGV application is unable to send egress traffic after recent maintenance on the computer system. You have already validated that the application has access permissions for data transfer.
What troubleshooting step should be considered? (Select TWO.)
- [ ] Ensure the correct key pair is being used for data encryption and decryption with Secure Sockets Layer (SSL).
- [x] Validate the security group permissions to the service ports, and the source/destination IP addresses. ✅
- [x] Confirm the network access control lists (network ACLs) provide access to the IP protocols and service ports. ✅
- [ ] Review the Amazon CloudWatch log to determine if edge locations are no longer caching the data.
- [ ] Determine if the direct connection to the endpoint is causing additional delays.

> **💡 Why:** When egress traffic fails after maintenance and IAM permissions are fine, check network-layer controls: security group rules and network ACLs. Security groups are stateful, while NACLs are stateless and need explicit allow rules in both directions.
>
> **🔑 Keywords:** `unable to send egress traffic`, `private subnet`, `already validated permissions`
>
> **📖 Official docs:** [Compare security groups and network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html) · [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

#### 26. The automotive industry is now developing a specific unmanned ground vehicle (UGV) to be used by the military that provides alerts to the operator of hazardous conditions, loss of connection, or vehicle damage. They know they will need to align with the National Institute of Standards and Technology (NIST) guidelines 800-171 regarding the vehicle&#039;s security strength to protect its location at all times. The application used by each UGV will be hosted in its own virtual private cloud (VPC) and run in a private subnet.
The operator wants to view the logs produced by the application in Amazon CloudWatch Logs.
What type of connectivity solution should be used to send the application log data to CloudWatch Logs without going through the internet?
- [ ] AWS VPN CloudHub
- [ ] NAT instance
- [x] Interface VPC endpoint ✅
- [ ] Gateway VPC endpoint

> **💡 Why:** CloudWatch Logs is reachable privately through an interface VPC endpoint (AWS PrivateLink). Gateway endpoints only cover S3 and DynamoDB.
>
> **🔑 Keywords:** `CloudWatch Logs`, `without going through the internet`
>
> **📖 Official docs:** [CloudWatch Logs and interface VPC endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html)

#### 27. The local power company has recently installed a new power grid within the community. They are working with the local government to acquire funding for a second power grid, but must show data that shows the cost reductions and how that translates to increased consumption time windows. This data needs to be kept for a minimum of 10 years in case of audit or by inquiry of a government agency. The power company wants to engage the community and gain their support, as their individual and communal power consumption is reflected in the data.
The power company has determined they will access the data at the end of each quarter, but the CEO wants to be able to access this data at anytime without wait.
 What storage solution would support this use case the best?
- [ ] Amazon Simple Storage Service (Amazon S3)
- [x] Amazon S3 STANDARD Infrequent Access (IA) ✅
- [ ] Amazon Elastic Block Store (Amazon EBS)
- [ ] Amazon Glacier

> **💡 Why:** Quarterly access means infrequent access, and the CEO's 'anytime without wait' means millisecond retrieval. Glacier (per the course) has a retrieval wait, and Standard costs more for rarely used data.
>
> **🔑 Keywords:** `end of each quarter`, `anytime without wait`, `10 years`
>
> **📖 Official docs:** [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

#### 28. The local power company has recently installed a new power grid within the community. They are working with the local government to acquire funding for a second power grid, but must show data that shows the cost reductions and how that translates to increased consumption time windows. This data needs to be kept for a minimum of 10 years in case of audit or by inquiry of a government agency. The power company wants to engage the community and gain their support, as their individual and communal power consumption is reflected in the data.
The CFO of the company has inquired why there is a sudden increase in the cost of using Amazon Simple Storage Service (Amazon S3). Another department has noted that there is a HTTP 503 slowdown response for any PUT or DELETE requests.
What could be the issue?
- [ ] Amazon EC2 Auto Scaling has not been enabled
- [ ] Elastic Load Balancing (ELB) has not been enabled
- [x] Versioning has been enabled ✅
- [ ] Cross-origin resource sharing (CORS) configuration has not been enabled

> **💡 Why:** With versioning on, every overwrite or delete keeps a version or delete marker. Millions of versions raise storage cost and S3 throttles requests with 503 Slow Down.
>
> **🔑 Keywords:** `sudden increase in cost`, `HTTP 503 slowdown`, `PUT or DELETE`
>
> **📖 Official docs:** [Troubleshooting S3 versioning (503 Slow Down)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-versioning.html)

#### 29. The local power company has recently installed a new power grid within the community. They are working with the local government to acquire funding for a second power grid, but must show data that shows the cost reductions and how that translates to increased consumption time windows. This data needs to be kept for a minimum of 10 years in case of audit or by inquiry of a government agency. The power company wants to engage the community and gain their support, as their individual and communal power consumption is reflected in the data.
The AWS Storage Gateway has encountered a failure, which is causing read and write operations to fail. Upon inspection, you determine that the cache disk is still accessible and useable.
What step should be taken to reconfigure the gateway and resume functionality quickly?
- [x] Reconnect the gateway ✅
- [ ] Delete the disk from the gateway
- [ ] Create a new gateway
- [ ] Mount the cache disks to an ephemeral drive

> **💡 Why:** If the cache disk failed but is still accessible, reconnect it. If it is inaccessible or unusable, delete it from the gateway configuration.
>
> **🔑 Keywords:** `cache disk is still accessible and useable`, `resume functionality quickly`
>
> **📖 Official docs:** [Storage Gateway: cache disk failure](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshoot-volume-issues.html)

#### 30. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
The SysOps Department Manager has decided to use tags to classify log groups with Amazon CloudWatch Logs. The CFO sees tagging as an added benefit that will help them obtain a detailed view of costs across the hospital.
Which statements describe a tag restriction? (Select THREE.)
- [ ] Maximum tags per group is 20
- [x] Tag key length between 1 – 128 Unicode characters ✅
- [ ] Tag keys can start with aws:
- [x] Keys and values are case-sensitive in a tag ✅
- [x] Tag value length maximum of 256 Unicode characters ✅

> **💡 Why:** Tag rules: key 1 to 128 characters, value up to 256 characters, keys and values are case-sensitive. The `aws:` prefix is reserved, and the limit is 50 tags, not 20.
>
> **🔑 Keywords:** `tag restriction`, `Unicode characters`, `case-sensitive`
>
> **📖 Official docs:** [Tagging AWS resources: restrictions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)

#### 31. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
A Support Engineer is trying to retrieve AWS CloudTrail log files.
What file extension is associated with this type of log file?
- [ ] .log
- [x] .gz ✅
- [ ] .aws
- [ ] .png

> **💡 Why:** CloudTrail delivers log files to S3 as gzip-compressed JSON, so the extension is .gz.
>
> **🔑 Keywords:** `CloudTrail log files`, `file extension`
>
> **📖 Official docs:** [Find your CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html)

#### 32. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
The Support Engineer has been notified that AWS Config is not aggregating data from an organization within the hospital. After investigation, it is found that AWS Config cannot access the organization's details because of an invalid AWS Identity and Access Management (IAM) role.
What corrective step should be taken based on this issue?
- [ ] Integrate AWS Config and AWS Organizations through an application programming interface (API)
- [ ] Enable AWS Config in the source account
- [ ] Enable all features in AWS Organizations
- [x] Select or create a valid IAM role ✅

> **💡 Why:** AWS Config's troubleshooting table says an invalid IAM role is fixed by creating or selecting a valid IAM role.
>
> **🔑 Keywords:** `not aggregating data`, `organization`, `invalid IAM role`
>
> **📖 Official docs:** [AWS Config aggregation troubleshooting](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data-troubleshooting.html)

#### 33. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
A Support Engineer is reviewing Amazon CloudWatch metrics.
Which metric will provide her with insight on the number of bytes written to all instance store volumes that are available to an instance?
- [ ] DiskReadBytes
- [x] DiskWriteBytes ✅
- [ ] DiskReadOps
- [ ] DiskWriteOps

> **💡 Why:** DiskWriteBytes is bytes written to all instance store volumes available to the instance. DiskReadBytes is the read counterpart, and the Ops metrics count operations, not bytes.
>
> **🔑 Keywords:** `bytes written`, `instance store volumes`
>
> **📖 Official docs:** [EC2 instance metrics in CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)

#### 34. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
The Support Engineer is considering the soft and hard limits of the current configuration and trying to determine what resources can be modified.
Which resources have soft limits? (Select TWO.)
- [x] ListMetrics ✅
- [x] DescribeAlarms ✅
- [ ] Metric Data
- [ ] Period
- [ ] Actions

> **💡 Why:** The API request-rate quotas ListMetrics and DescribeAlarms are the adjustable (soft) limits in this list.
>
> **🔑 Keywords:** `soft limits`, `can be modified`
>
> **📖 Official docs:** [CloudWatch service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html)

#### 35. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data life cycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
The hospital CEO has requested additional information on what exactly they are responsible for regarding security because they might be asked questions during an audit.
Which statements describe the sole security responsibilities of the hospital (customer) that can be supported with by evidence from monitoring? (Select THREE.)
- [x] Resource access ✅
- [ ] Hardware and software at or below the hypervisor level
- [x] Customer-stored data ✅
- [x] Network logins ✅
- [ ] Patch management at the infrastructure level

> **💡 Why:** The customer is responsible for security in the cloud: who can access resources, the data they store, and network logins. AWS handles hardware, hypervisor and infrastructure patching.
>
> **🔑 Keywords:** `sole security responsibilities`, `customer`, `evidence from monitoring`
>
> **📖 Official docs:** [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

#### 36. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
The non-profit organization uses AWS Organizations to establish authentication and access controls. The CFO has been set up as an IAM user with full permissions on AWS Organizations. The CFO is now trying to make a request to AWS Organizations and keeps getting an "access denied" message. He has called you to assist him with troubleshooting the issue.
Which troubleshooting steps should be considered? (Select TWO.)
- [ ] Double check that the CFO has valid credentials.
- [ ] Instruct the CFO to log out and sign in again by using root credentials to make the request.
- [x] Validate that the CFO has correctly signed their request. ✅
- [ ] Ensure that the proper wait period has been completed, and then have the CFO repeat the request.
- [x] Verify that the CFO has the permissions to call the action and the requested resource. ✅

> **💡 Why:** For 'access denied' in AWS Organizations, check that the request was signed correctly and that the user has permission for the action and resource.
>
> **🔑 Keywords:** `access denied`, `AWS Organizations`, `valid credentials`
>
> **📖 Official docs:** [Troubleshooting AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_troubleshoot.html)

#### 37. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
The Support Specialist has created an AWS Identity and Access Management (IAM) policy for a new employee.
Which IAM tag and associated tag condition key should be applied to control the new employee's ability to complete specific tasks based on their identity?
- [ ] iam:ResourceTag/key-name
- [x] aws:PrincipalTag/key-name ✅
- [ ] aws:RequestTag/key-name
- [ ] aws:TagKeys

> **💡 Why:** `aws:PrincipalTag/key-name` matches tags on the user or role making the request, which controls what that identity can do. ResourceTag is a tag on the resource, and RequestTag is a tag sent in the request.
>
> **🔑 Keywords:** `based on their identity`, `tag condition key`
>
> **📖 Official docs:** [ABAC for AWS (tag-based IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)

#### 38. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
The Director has asked you about AWS Trusted Advisor.
What statement do you provide regarding its purpose and function?
- [ ] A service the will allow for SSL/TLS certificates to be provisioned, managed, and deployed with other cloud- based AWS services.
- [ ] A firewall that protects web applications from attacks. These protection are based on rules that are configured on defined conditions.
- [ ] A service the that provides automated security assessments to ultimately improve the security and compliance of an application that is deployed on AWS.
- [x] A customer support service that provides cloud performance monitoring and security. ✅

> **💡 Why:** Trusted Advisor is the online support tool that inspects your account and gives best-practice recommendations on performance, security, cost and fault tolerance. The other options describe ACM, WAF and Inspector.
>
> **🔑 Keywords:** `AWS Trusted Advisor`, `purpose and function`
>
> **📖 Official docs:** [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

#### 39. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
Which is an AWS Identity and Access Management (IAM) policy that is supported by tag- based conditions?
- [ ] Organize resources by group
- [ ] Ability to allocate costs to a user
- [x] Limit Amazon Elastic Compute Cloud (Amazon EC2) application programming interface (API) calls to only development environments ✅
- [ ] Run automated start/stop scripts during business hours only

> **💡 Why:** Tag-based conditions let an IAM policy limit actions by tag, for example EC2 API calls only on resources tagged as development.
>
> **🔑 Keywords:** `IAM policy`, `tag-based conditions`
>
> **📖 Official docs:** [ABAC for AWS (tag-based IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) · [Tagging best practices (whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)

#### 40. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
Your manager has asked you create business-relevant tag groupings to organize resources. The non-profit organization wants to ensure that resources are being used in the most frugal and secure manner.
Which tags would be beneficial for automation? (Select TWO.)
- [ ] Confidentiality
- [x] Date/Time ✅
- [ ] Version
- [x] Opt in/Opt out ✅
- [ ] Cost Center/Business Unit

> **💡 Why:** Date/Time and Opt in/Opt out are automation tags, used by scripts to start or stop resources or include or exclude them. Cost Center, Version and Confidentiality are business or security tags.
>
> **🔑 Keywords:** `beneficial for automation`, `frugal`
>
> **📖 Official docs:** [Tagging best practices (whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)

#### 41. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore} staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits. The travel company is planning to deploy a new phone app so customers can book travel. This app will store a lot of personal data about their customers so the customers can book their travel more quickly, including their names, addresses, credit card information, passport numbers, and other details. A challenge is that a hacker could obtain this data or even appear at the customer's home while the customer is on travel.
What potential solutions could the Cloud Engineer use to secure customer information in cloud deployments from hacker penetration? (Select THREE.)
- [ ] Application access via edge locations and Amazon CloudFront caches is supposed by automatic scaling for capacity needs" (or something similar
- [ ] Automation of secure deployments with AWS CloudFormation and AWS Config
- [x] Data encryption when in transit with Transport Layer Security (TLS) and at rest with AWS Key Management Service (AWS KMS) ✅
- [x] Permission policies for all types of testing, which is obtained through root credentials and use of access controls ✅
- [x] Network firewalls built into Amazon Virtual Private Cloud (Amazon VPC) with the use of Amazon GuardDuty ✅

> **💡 Why:** Protect customer data with encryption in transit (TLS) and at rest (KMS), permission policies and access controls, and network firewalls such as VPC controls with GuardDuty threat detection.
>
> **🔑 Keywords:** `secure customer information`, `hacker penetration`, `personal data`
>
> **📖 Official docs:** [Security pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
>
> **⚠️ Note:** One option mentions permission policies 'obtained through root credentials'. That is marked correct here, but root credentials are not a recommended practice in real life.

#### 42. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits. The Cloud Engineer is planning his AWS CloudFormation templates to support the upcoming deployment of the travel company's new phone app.
What is the maximum number of outputs that can be declared per template?
- [ ] 40
- [ ] 100
- [ ] 80
- [x] 200 ✅

> **💡 Why:** A CloudFormation template can declare at most 200 outputs.
>
> **🔑 Keywords:** `maximum number of outputs`, `per template`
>
> **📖 Official docs:** [CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html)

#### 43. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
The Cloud Engineer is trying to implement more automation by using AWS CloudFormation and by having resources make additional calls to AWS. She wants to use AWS CodeDeploy to deploy applications on existing instances.
What should be specified if a service role has been defined with the respective role's policy?
For example: AWS::IAM::Policy or AWS::IAM::ManagedPolicy
- [ ] An IAM Role Policy that acts as a Service Role
- [x] The resources that will use the role; also, a policy dependency must be added ✅
- [ ] A template that defines a service role without any dependencies
- [ ] An IAM Role Policy that acts as a Resource Role

> **💡 Why:** A resource that uses a role must wait for the role's policy. Specify the resources that will use the role and add a dependency (`DependsOn`) on the policy.
>
> **🔑 Keywords:** `service role`, `role's policy`, `AWS::IAM::Policy`
>
> **📖 Official docs:** [DependsOn attribute (CloudFormation)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html)

#### 44. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
The Cloud Engineer is reviewing the AWS CloudFormation output fields that were created by a colleague. There is an error within the export output field, but he is not sure what it is at this time.
The Cloud Engineer must conduct an error review. What restrictions to cross-stack references for the exported resource output should he consider? (Select THREE.)
- [x] Cross-stack references cannot be created across Regions. ✅
- [ ] Values can be imported from any Region that it has been exported previously.
- [x] Names must be unique within a Region. ✅
- [ ] An output value can be modified or removed even if it references another stack in one of its outputs.
- [x] A stack cannot be deleted if it references another stack in one of its outputs. ✅

> **💡 Why:** Cross-stack exports: no cross-Region references, export names are unique per Region, and a stack cannot be deleted while another stack imports its outputs.
>
> **🔑 Keywords:** `cross-stack references`, `exported resource output`, `restrictions`
>
> **📖 Official docs:** [CloudFormation exported outputs: restrictions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html)

#### 45. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
The Cloud Engineer is working with the Department Manager, and she is explaining AWS CloudFormation templates and their respective sections. She explains that as the template is built, the values in one section might refer to another section.
Which template section would provide additional information about the template, and would come after the description?
- [ ] Resources
- [ ] Conditions
- [x] Metadata ✅
- [ ] Outputs

> **💡 Why:** Template section order: Format version, Description, Metadata, Parameters, Rules, Mappings, Conditions, Transform, Resources, Outputs. Metadata follows Description.
>
> **🔑 Keywords:** `after the description`, `additional information about the template`
>
> **📖 Official docs:** [CloudFormation template anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

#### 46. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology: The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
Which statements describe best practices for AWS CloudFormation that a Cloud Engineer might require his team to use as a standard for efficiency? (Select THREE.)
- [x] Reuse templates to build stacks for different environments ✅
- [ ] Ensure there are no dependencies between layers
- [x] Plan and organize stacks before creating them ✅
- [x] Organize resources in the same stack based on their ownership and lifecycles ✅
- [ ] Disperse resources across multiple stacks based on their tags

> **💡 Why:** CloudFormation best practices: reuse templates across environments, plan and organize stacks first, and group resources by ownership and lifecycle.
>
> **🔑 Keywords:** `best practices`, `standard for efficiency`
>
> **📖 Official docs:** [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)

#### 47. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
The Cloud Engineer has received the error Status-start_failed when he tries to launch another Amazon Elastic Compute Cloud (Amazon EC2) instance. He has verified that there are 20 instances.
Which actions can he take so that the new instance can be created? (Select TWO.)
- [x] Request a limit increase ✅
- [ ] Launch a different type of instance
- [ ] Create the instance again
- [x] Delete excess instances ✅
- [ ] Place the instance in another account

> **💡 Why:** The instance limit was reached (20). Either request a limit increase or delete excess instances. A different instance type or retrying does not fix a quota problem.
>
> **🔑 Keywords:** `Status-start_failed`, `20 instances`, `launch another`
>
> **📖 Official docs:** [Troubleshoot launching EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html)

#### 48. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
The Cloud Engineer is troubleshooting one of his employee's AWS CloudFormation stacks. The employee stated that she made some changes to the stack outside of AWS CloudFormation. He located the stack ID and is working with AWS Premium Support.
What implications could this have on the stack?
- [ ] The stack should be recoverable with modifications in AWS CloudFormation
- [ ] There will be no impact to the stack or the respective templates
- [ ] The stack's templates will need to be re-configured
- [x] The stack might be in an unrecoverable state ✅

> **💡 Why:** Changes made outside CloudFormation cause configuration drift. The stack can end up in a state CloudFormation cannot recover from.
>
> **🔑 Keywords:** `changes ... outside of AWS CloudFormation`, `Premium Support`, `implications`
>
> **📖 Official docs:** [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) · [Detect drift on CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)

#### 49. A startup tech has just created a mobile app that allows a customer to place a lunch order for delivery with local restaurants through a third party courier. They want to provide the customer and the restaurant with a notification that the delivery has been completed, as the building is secure and all food orders are left in the lobby.
What steps would be required of the SysOps administrator if they want to change an Amazon Elastic Block Store (Amazon EBS) volume from gp2 to io1 to accommodate the restaurant's growth? (Select THREE.)
- [x] Take a snapshot of the Amazon Elastic Block Store (Amazon EBS) volume. ✅
- [ ] Change the setting of the Amazon Elastic Block Store (Amazon EBS)volume so that it scales.
- [x] Create a new Amazon Elastic Block Store (Amazon EBS) volume. ✅
- [ ] Make a soft limit request with AWS.
- [x] Delete the old volume. ✅

> **💡 Why:** The course approach for moving from gp2 to io1: snapshot the volume, create a new io1 volume from it, and delete the old volume.
>
> **🔑 Keywords:** `change ... from gp2 to io1`, `steps`
>
> **📖 Official docs:** [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
>
> **⚠️ Note:** Modern EBS Elastic Volumes can also change volume type in place, but the answer here follows the course material.

***

## KC - Scenario Test Strategy Practice

#### 1. A federal contractor located in Seattle is expanding their cloud presence to Germany, which has strict rules on data that originated in Germany leaving the region, known as data sovereignty. They know that they will have auditors auditing both regions. How should access be provided to auditors?
- [ ] Identity federation
- [x] IAM Role ✅
- [ ] IAM User
- [ ] Root account

> **💡 Why:** Auditors should get temporary, scoped access through an IAM role. Creating IAM users or sharing root credentials gives standing access that is harder to control.
>
> **🔑 Keywords:** `auditors`, `how should access be provided`
>
> **📖 Official docs:** [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

#### 2. A SysOps engineer working at a local university has decided to launch Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce their hardware footprint. They are new to AWS and will only need to launch in one region until their business grows. What is the first step when you launch an Amazon EC2 instance?
- [ ] Launch access and control permissions.
- [ ] Select instance type and size.
- [x] Determine the Amazon Machine Image (AMI) that will be used. ✅
- [ ] Provide configuration details.

> **💡 Why:** Launching an instance starts with choosing an AMI, the template with the OS and software. Instance type, configuration and permissions come after.
>
> **🔑 Keywords:** `first step`, `launch an Amazon EC2 instance`
>
> **📖 Official docs:** [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

#### 3. A trucking company is looking to track their fleet better and to ensure that they have updated information on the trucks each time they reach the office. Many of the trucks are out on the road for days at a time, but may be at the office for a break period that can last up to a day.
A trucking company is looking to minimize dependence on their current cloud service provider so they are not "locked in", while increasing their development velocity of various applications. The company is trying to decide if they should use containers or go serverless. They know they only need secure, compute capacity when the trucks are at their home base, which may last a day a couple times a month. Sometimes they support partner companies when they are in town; therefore, they may need to accommodate those users once every couple of months.
Which statements describe when the company might find that containers are a more ideal option? (Select THREE.)
- [x] Desire to manage the resources and their respective policies, and oversee security. ✅
- [x] Have a requirement for portability and maintaining a status of vendor-agnosticism. ✅
- [x] Move software from one environment to another through isolation. ✅
- [ ] Ensure that the Cloud Service Provider provisions the infrastructure and manages capacity.

> **💡 Why:** Containers fit when you want control over resources, policies and security, need portability and vendor neutrality, and want isolation to move software between environments. Having the provider manage infrastructure and capacity is the serverless benefit.
>
> **🔑 Keywords:** `not locked in`, `vendor-agnosticism`, `portability`, `isolation`
>
> **📖 Official docs:** [What is Amazon ECS?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

#### 4. A FinTech bank has created a new credit card line; therefore, will need to expand its database to capture new customer profiles and link existing customer profiles to the new card line, while maintaining security and PCI compliance requirements. The bank is entirely in the cloud and provides their customer's with unique financial visualizations about their financial habits. Their customers use a mobile app and website for their account transactions and profiles.
What AWS service should be prioritized for the bank's database if they want to graph connected data on their customers' financial behaviors?
- [ ] Amazon ElastiCache
- [ ] Amazon DynamoDB
- [ ] Amazon Aurora
- [x] Amazon Neptune ✅

> **💡 Why:** Neptune is the managed graph database for highly connected data.
>
> **🔑 Keywords:** `graph connected data`, `financial behaviors`
>
> **📖 Official docs:** [What is Amazon Neptune?](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

#### 5. The automotive industry is now developing a specific unmanned ground vehicle (UGV) to be used by the military that provides alerts to the operator of hazardous conditions, loss of connection, or vehicle damage. They know they will need to align with the National Institute of Standards and Technology (NIST) guidelines 800-171 regarding the vehicle's security strength to protect its location at all times. The application used by the UGV will be hosted in a private subnet.
What needs to be updated after establishing a network address translation (NAT) gateway for the unmanned vehicle application so operators can connect and retrieve location data securely? (Select THREE.)
- [x] Specify a public subnet for creation ✅
- [x] Update the route table ✅
- [ ] Provide access through relevant security groups
- [x] Specify an Elastic IP address for association ✅
- [ ] Implement redundancy in different Availability Zones

> **💡 Why:** After creating a NAT gateway: place it in a public subnet, assign an Elastic IP, and update the private subnet's route table to send internet traffic to it.
>
> **🔑 Keywords:** `NAT gateway`, `public subnet`, `Elastic IP`, `route table`
>
> **📖 Official docs:** [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) · [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

#### 6. A local hospital is preparing for an audit and needs to show that they are in compliance with HIPAA requirements. This includes security, data lifecycle management, and compliance. They have experienced problems in the past with an employee that has accessed patient records that were not relevant to their immediate job tasks. The CEO of the hospital wants to ensure that mitigation to this issue has been resolved and has had the SysOps team employ various AWS monitoring and security services.
The SysOps Engineer is troubleshooting an Amazon CloudWatch agent used to publish log data to Amazon CloudWatch Logs, which will then be archived.
What output is displayed in the AWS Command Line Interface (AWS CLI) when you verify that the CloudWatch agent is running? (Select THREE.)
- [ ] Action
- [x] Version ✅
- [ ] Effect
- [x] Status ✅
- [x] Start Time ✅

> **💡 Why:** The CloudWatch agent status command returns JSON with status, start time and version. Action and Effect are IAM policy fields.
>
> **🔑 Keywords:** `verify the CloudWatch agent is running`, `CLI output`
>
> **📖 Official docs:** [Troubleshooting the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/troubleshooting-CloudWatch-Agent.html)

#### 7. A non-profit organization has multiple committees that have individual accounts. They are looking at ways to reduce cost, yet ensure that expenses are best utilized across the committees and are finding that individual accounts are no longer working. Since they receive donations, they want to ensure that they can provide use and expense details to their donors when requested.
The Support Specialist has noticed the service control policies (SCPs) in AWS Organizations has exceeded its maximum size. She has begun removing some of the white space characters outside the quotation marks.
What is the maximum size of an SCP document so she can correct the error?
- [ ] 1,510 bytes
- [ ] 2,048 characters
- [ ] 10,240 characters
- [x] 5,120 bytes ✅

> **💡 Why:** An SCP document has a maximum size of 5,120 bytes, and removing white space is the usual way to shrink it.
>
> **🔑 Keywords:** `maximum size of an SCP document`, `white space characters`
>
> **📖 Official docs:** [AWS Organizations quotas (SCP size)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html)

#### 8. A global travel company has announced a company restructure in order to re-invest profits into customer facing technology. The IT budget has been re-allocated by 20% for the upcoming year; therefore, staff will be forced to make standardizations and efficiencies with the new budget until the new technology generates increased profits.
A Cloud Engineer is working with AWS CloudFormation, and is determining which situations to apply the WaitCondition and Creation Policy attributes.
Which situations should the WaitCondition be applied to, in addition to the CreationPolicy? (Select TWO.)
- [ ] Coordinating the creation of stack resources
- [ ] Sending responses to resources within an AWS virtual private cloud (VPC)
- [ ] Automatically scaling resource
- [x] Tracking the status of configuration process ✅
- [x] Tracking the configuration of Amazon Elastic Compute Cloud (Amazon EC2) instances ✅

> **💡 Why:** A wait condition is for tracking the status of configuration processes and of EC2 instance configuration. CreationPolicy is the usual choice for EC2 and Auto Scaling resources.
>
> **🔑 Keywords:** `WaitCondition`, `CreationPolicy`, `tracking`
>
> **📖 Official docs:** [AWS::CloudFormation::WaitCondition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html)

#### 9. The local power company has recently installed a new power grid within the community. They are working with the local government to acquire funding for a second power grid, but must show data that shows the cost reductions and how that translates to increased consumption time windows. This data needs to be kept for a minimum of 10 years in case of audit or by inquiry of a government agency. The power company wants to engage the community and gain their support, as their individual and communal power consumption is reflected in the data. The CEO has decided that the company will now begin processing the big data in real time through the use of Amazon Kinesis. The architecture has been developed with, an intermediate and backup Amazon Simple Storage Service (Amazon S3) bucket for potential delivery failures and source records.
What other services should be used for transformed records after they are processed by Amazon Kinesis Data Firehose? (Select TWO.)
- [ ] Amazon Elastic Block Store (Amazon EBS)
- [ ] Amazon Simple Storage Service (Amazon S3)
- [x] Amazon Redshift cluster ✅
- [ ] Amazon Elasticsearch Service (Amazon ES)
- [x] Amazon Glacier ✅

> **💡 Why:** Firehose can load transformed records into Redshift (analytics). The 10-year retention requirement points to Glacier as the archive tier.
>
> **🔑 Keywords:** `Kinesis Data Firehose`, `transformed records`, `kept for 10 years`
>
> **📖 Official docs:** [What is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) · [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
>
> **⚠️ Note:** Firehose's documented destinations are S3, Redshift, OpenSearch, Splunk and HTTP endpoints. Glacier is normally reached through S3 lifecycle rules.

***

## KC - Cloud Computing

#### 1. What is the pricing model that enables AWS customers to pay for resources on an as- needed basis? (Select the best answer.)
- [ ] Pay as you buy
- [ ] Pay as you reserve
- [ ] Pay as you decommission
- [x] Pay as you go ✅

> **💡 Why:** Pay as you go means you pay only for what you use, when you use it.
>
> **🔑 Keywords:** `as-needed basis`, `pay for resources`
>
> **📖 Official docs:** [AWS Pricing](https://aws.amazon.com/pricing/)

#### 2. All are a cloud deployment model EXCEPT:
- [ ] Platform as a service (PaaS)
- [ ] Software as a service (SaaS)
- [x] System administration as a service ✅
- [ ] Infrastructure as a service (IaaS)

> **💡 Why:** The cloud models are IaaS, PaaS and SaaS. 'System administration as a service' is not one.
>
> **🔑 Keywords:** `EXCEPT`, `deployment model`
>
> **📖 Official docs:** [Types of cloud computing](https://aws.amazon.com/types-of-cloud-computing/)

#### 3. True or False? AWS owns and maintains the network-connected hardware required for application services, while you provision and use what you need.
- [x] True ✅
- [ ] False

> **💡 Why:** AWS owns and maintains the hardware, while you provision and use what you need.
>
> **🔑 Keywords:** `AWS owns and maintains`, `you provision`
>
> **📖 Official docs:** [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)

#### 4. Which of these is not a primary benefit of cloud computing over on-premises computing? Select the best answer.
- [ ] Eliminate guessing on your infrastructure capacity needs
- [ ] Benefit from massive economies of scale
- [ ] Increased speed and agility
- [x] Pay for racking, stacking, and powering servers ✅

> **💡 Why:** Racking, stacking and powering servers are on-premises costs. The cloud removes them.
>
> **🔑 Keywords:** `not a primary benefit`, `racking, stacking`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

#### 5. All are benefits of AWS Cloud computing EXCEPT (Choose two):
- [x] High latency ✅
- [ ] Temporary and disposable resources
- [ ] High availability
- [x] Multiple procurement cycles ✅
- [ ] Fault-tolerant databases

> **💡 Why:** Cloud computing gives low latency and removes procurement cycles. High latency and multiple procurement cycles are on-premises drawbacks.
>
> **🔑 Keywords:** `EXCEPT`, `benefits`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

#### 6. What is a reason businesses are switching to cloud computing?
- [ ] Instant configuration
- [ ] Finite infrastructure
- [x] Increased speed and agility ✅
- [ ] Over provisioning

> **💡 Why:** Businesses move to the cloud for speed and agility: resources are available in minutes. Finite infrastructure and over-provisioning are problems it removes.
>
> **🔑 Keywords:** `reason businesses are switching`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

#### 7. True or False? Cloud computing provides a simple way to access servers, storage, databases, and a broad set of application services over the internet. You own the network-connected hardware required for these services and AWS provisions what you need.
- [ ] True
- [x] False ✅

> **💡 Why:** This statement is false: AWS owns the hardware, and you do not.
>
> **🔑 Keywords:** `You own the network-connected hardware`
>
> **📖 Official docs:** [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)

#### 8. Economies of scale result from ___. Select the best answer.
- [ ] having to invest heavily in data centers and servers
- [x] having hundreds of thousands of customers aggregated in the cloud ✅
- [ ] having many different cloud providers
- [ ] having hundreds of cloud services available over the internet

> **💡 Why:** Economies of scale come from aggregating usage from a very large customer base, which lowers cost per unit.
>
> **🔑 Keywords:** `economies of scale`, `hundreds of thousands of customers`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

#### 9. What are the three ways to access AWS services? Select three responses.
- [x] Software development kits SDKs ✅
- [x] AWS Management Console ✅
- [x] AWS Command Line Interface AWS CLI ✅
- [ ] Calling technical support
- [ ] Through the AWS Marketplace

> **💡 Why:** You reach AWS through the Management Console, the CLI and the SDKs.
>
> **🔑 Keywords:** `three ways to access`
>
> **📖 Official docs:** [Interacting with AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/interacting-with-aws.html)

***

## KC - Cloud Economics

#### 1. For certain services like Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS), you can invest in reserved capacity. Reserved Instances are available in what three payment options? (Select THREE.)
- [ ] Scheduled Instance (Sl)
- [x] Partial up-front reserved instance (PURI) ✅
- [x] No up-front (NURI) ✅
- [ ] All up-front capacity reservation (AUCR)
- [x] All up-front reserved instance (AURI) ✅

> **💡 Why:** Reserved Instance payment options are No Upfront, Partial Upfront and All Upfront.
>
> **🔑 Keywords:** `Reserved Instances`, `payment options`
>
> **📖 Official docs:** [Amazon EC2 Reserved Instances pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/)

#### 2. What type of AWS data transfer is free for Amazon Simple Storage Service (Amazon S3)? (Select THREE.)
- [x] Up to 1 GB data transfer OUT from Amazon S3 to the internet ✅
- [x] Outbound data transfer from Amazon S3 to Amazon CloudFront ✅
- [ ] Outbound data transfer from Amazon S3 to all Regions
- [x] Data transfer IN to Amazon S3 from Internet ✅

> **💡 Why:** Data transfer into S3 is free, and so is transfer from S3 to CloudFront. The course also counts a small free allowance for outbound transfer to the internet.
>
> **🔑 Keywords:** `free`, `data transfer IN`, `to CloudFront`
>
> **📖 Official docs:** [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)
>
> **⚠️ Note:** The size of the free outbound allowance has changed over time. Check the current S3 pricing page.

#### 3. True or false? To receive the discounted rate associated with Reserved Instances, you must make a full, up-front payment for the term of the agreement.
- [x] False ✅
- [ ] True

> **💡 Why:** False: you can choose No Upfront or Partial Upfront and still get a discount.
>
> **🔑 Keywords:** `must make a full, up-front payment`
>
> **📖 Official docs:** [Amazon EC2 Reserved Instances pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/)

#### 4. There is no charge for which of the following? (Select TWO.)
- [ ] Outbound data transfer
- [x] Inbound data transfer ✅
- [ ] Compute
- [x] Data transfer between services ✅
- [ ] Storage

> **💡 Why:** Inbound data transfer is free, and so is transfer between services inside AWS in the same Region. Compute and storage are charged.
>
> **🔑 Keywords:** `no charge`
>
> **📖 Official docs:** [Amazon EC2 on-demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

#### 5. How often do you pay for compute resources from the time you launch a resource until you terminate it with the "pay as you go" pricing model?
- [ ] Daily
- [x] Secondly and hourly ✅
- [ ] Quarterly
- [ ] Monthly

> **💡 Why:** Pay as you go bills compute by the second or the hour, from launch to termination.
>
> **🔑 Keywords:** `how often do you pay`, `launch ... until you terminate`
>
> **📖 Official docs:** [Amazon EC2 on-demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

#### 6. As AWS grows, the general cost of doing business is reduced and savings are passed back to the customer in the form of lower pricing. What is this optimization called?
- [ ] Economies of optimization
- [x] Economies of scale ✅
- [ ] Economies of labor
- [ ] Economies of scope

> **💡 Why:** As AWS grows its aggregate usage, its unit costs fall, and it passes savings on. This is economies of scale.
>
> **🔑 Keywords:** `general cost of doing business is reduced`, `passed back`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

#### 7. True or false? AWS offers a variety of services at no charge. For example, Amazon Virtual Private Cloud (Amazon VPC), AWS Identity and Access Management (IAM), consolidated billing, AWS Elastic Beanstalk, AWS Auto Scaling, AWS OpsWorks and AWS CloudFormation. Although there is no charge for these services, there may be charges associated with other AWS services used in conjunction with these services.
- [x] True ✅
- [ ] False

> **💡 Why:** AWS offers several services at no charge (VPC, IAM, Auto Scaling, CloudFormation and others). You still pay for the resources they create.
>
> **🔑 Keywords:** `no charge`, `there may be charges associated with other services`
>
> **📖 Official docs:** [AWS Pricing](https://aws.amazon.com/pricing/)

#### 8. When are free AWS data transfers applicable? (Select TWO.)
- [ ] Free inbound data transfer across all AWS services in all Regions
- [ ] Free outbound data transfer across all AWS services in all Regions
- [x] Free outbound data transfers within the same Region, within the same Availability Zone, and that use a private IP address ✅
- [x] Free inbound data transfer for Amazon Elastic Compute Cloud (Amazon EC2) instances ✅

> **💡 Why:** Inbound data transfer to EC2 is free, and so is outbound transfer within the same Region or AZ over a private IP.
>
> **🔑 Keywords:** `free data transfers`, `private IP address`
>
> **📖 Official docs:** [Amazon EC2 on-demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

#### 9. True or false? Unlimited services are available via the AWS Free Tier to new AWS customers for 12 months following their AWS signup date.
- [ ] True
- [x] False ✅

> **💡 Why:** False: Free Tier offers have limits on usage and duration, and not every service is included.
>
> **🔑 Keywords:** `Unlimited services`, `12 months`
>
> **📖 Official docs:** [AWS Free Tier](https://aws.amazon.com/free/)

***

## KC - AWS Global Infrastructure

#### 1. Which component of the AWS global infrastructure does Amazon CloudFront use to ensure low-latency delivery?
- [ ] AWS Regions
- [ ] AWS Availability Zone
- [ ] Amazon Virtual Private Cloud (Amazon VPC)
- [x] AWS Edge Locations ✅

> **💡 Why:** CloudFront delivers content from edge locations close to users.
>
> **🔑 Keywords:** `CloudFront`, `low-latency delivery`
>
> **📖 Official docs:** [How CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)

#### 2. You can run applications and workloads from a Region to ___ latency to end users.
- [ ] increase
- [ ] maintain
- [ ] measure
- [x] decrease ✅

> **💡 Why:** Running in a Region near your users decreases latency.
>
> **🔑 Keywords:** `latency to end users`
>
> **📖 Official docs:** [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

#### 3. True or False? Each Availability Zone is designed to be isolated from failures in other Availability Zones.
- [x] True ✅
- [ ] False

> **💡 Why:** True: each AZ is isolated so a failure in one does not spread to others.
>
> **🔑 Keywords:** `isolated from failures`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 4. Which of the following are geographic areas that host two or more Availability Zones?
- [x] AWS Regions ✅
- [ ] Compute zones
- [ ] Edge locations
- [ ] AWS Origins

> **💡 Why:** A Region is a geographic area that hosts multiple Availability Zones.
>
> **🔑 Keywords:** `geographic areas`, `two or more Availability Zones`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 5. ___ means the infrastructure has built in component redundancy and ___ means that resources dynamically adjust to increases or decreases in capacity requirements.
- [x] Fault tolerant, elastic and scalable ✅
- [ ] Fault tolerant, no human intervention
- [ ] Elastic and scalable, no human intervention
- [ ] Elastic and scalable, fault tolerant

> **💡 Why:** Fault tolerant means built-in redundancy of components. Elastic and scalable means resources adjust to demand.
>
> **🔑 Keywords:** `built in component redundancy`, `dynamically adjust`
>
> **📖 Official docs:** [Reliability pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

#### 6. True or False? Availability Zones within a Region are connected through low-latency links.
- [x] True ✅
- [ ] False

> **💡 Why:** True: AZs in a Region are linked with low-latency, high-throughput private networking.
>
> **🔑 Keywords:** `connected through low-latency links`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 7. Which of these statements about Availability Zones is not true? Select the best answer.
- [x] A data center can be used for more than one Availability Zone. ✅
- [ ] Availability Zones are connected to each other using high-speed private links.
- [ ] Availability Zones are designed for fault isolation.
- [ ] Availability Zones are made up of one or more data centers.

> **💡 Why:** An AZ is made of one or more data centers, but a data center belongs to only one AZ. Sharing one across AZs would defeat fault isolation.
>
> **🔑 Keywords:** `not true`, `data center can be used for more than one`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 8. What is true about Regions? Select two responses.
- [x] Each region is located in a separate geographic area. ✅
- [ ] Regions are the physical locations of your customers.
- [x] Each region is a physical location that has multiple Availability Zones. ✅
- [ ] All regions are located in one specific geographic area.

> **💡 Why:** Each Region is in a separate geographic area and has multiple AZs. Regions are not customer locations.
>
> **🔑 Keywords:** `true about Regions`
>
> **📖 Official docs:** [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 9. AWS highly recommends provisioning your compute resources across ___ Availability Zones. Select the best answer.
- [ ] single
- [ ] no
- [x] multiple ✅
- [ ] all

> **💡 Why:** AWS recommends spreading compute across multiple AZs for availability.
>
> **🔑 Keywords:** `provisioning ... across ___ Availability Zones`
>
> **📖 Official docs:** [Reliability pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) · [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### 10. True or False? Edge locations are only located in the same general area as Regions.
- [ ] True
- [x] False ✅

> **💡 Why:** False: edge locations exist in many more cities than Regions.
>
> **🔑 Keywords:** `only located in the same general area as Regions`
>
> **📖 Official docs:** [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

***

## KC - Compute

#### 1. Which category of service does Amazon Lightsail belong to?
- [ ] Infrastructure as a service (IaaS)
- [x] Platform as a service (PaaS) ✅
- [ ] Function as a service (FaaS)
- [ ] Software as a service (SaaS)

> **💡 Why:** The course classes Lightsail as PaaS: it bundles compute, storage and networking into simple preconfigured plans.
>
> **🔑 Keywords:** `category of service`, `Lightsail`
>
> **📖 Official docs:** [What is Amazon Lightsail?](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
>
> **⚠️ Note:** Many sources describe Lightsail as a simple virtual private server service. The marked answer follows the course.

#### 2. True or False? You can launch multiple instances of different types from a single Amazon Machine Image (AMI) when you launch an Amazon Elastic Compute Cloud (Amazon EC2) instance.
- [ ] False
- [x] True ✅

> **💡 Why:** True: you can launch several instances, including of different types, from one AMI.
>
> **🔑 Keywords:** `multiple instances of different types`, `single AMI`
>
> **📖 Official docs:** [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

#### 3. If your project requires you to run monthly reports that iterate through very large amounts of data, which Amazon Elastic Compute Cloud (Amazon EC2) purchasing option should you consider?
- [ ] On-Demand Instances
- [ ] Spot Instances
- [ ] Dedicated Hosts
- [x] Scheduled Reserved Instances ✅

> **💡 Why:** Scheduled Reserved Instances fit recurring, predictable windows, like monthly reporting jobs.
>
> **🔑 Keywords:** `monthly reports`, `very large amounts of data`
>
> **📖 Official docs:** [EC2 instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
>
> **⚠️ Note:** AWS has since retired Scheduled Reserved Instances, so this is old exam content.

#### 4. Which Amazon Elastic Compute Cloud (Amazon EC2) feature ensures your instances will not share a physical host with instances from any other AWS customer?
- [x] Dedicated Instances ✅
- [ ] Amazon Virtual Private Cloud
- [ ] Reserved Instances
- [ ] Placement groups

> **💡 Why:** Dedicated Instances run on hardware dedicated to a single customer and not shared with other accounts.
>
> **🔑 Keywords:** `will not share a physical host`
>
> **📖 Official docs:** [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)

#### 5. With the "Pay as you go" pricing model, what is the billing interval for compute resources from the time you launch a resource until you terminate it?
- [x] Monthly ✅
- [ ] Daily
- [ ] Quarterly
- [ ] Hourly and by the second

> **💡 Why:** The course marks Monthly as the billing interval, meaning charges are accumulated and invoiced monthly.
>
> **🔑 Keywords:** `billing interval`, `pay as you go`
>
> **📖 Official docs:** [Amazon EC2 on-demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
>
> **⚠️ Note:** This conflicts with Cloud Economics Q5 (secondly and hourly). Current EC2 pricing bills per second for Linux On-Demand, so check which wording your exam uses.

#### 6. Your web application needs four instances to support steady traffic all the time. On the last day of the month, the traffic triples. What is the most cost-effective way to handle this pattern?
- [x] Run four Reserved Instances constantly, then add eight On-Demand Instances on the last day of each month. ✅
- [ ] Run four On-Demand Instances constantly, then add eight more On-Demand Instances on the last day of each month.
- [ ] Run 12 Reserved Instances all of the time.
- [ ] Run four On-Demand Instances consistently, then add eight Reserved Instances on the last day of each month.

> **💡 Why:** Use Reserved Instances for the steady four instances and On-Demand for the short monthly spike of eight more.
>
> **🔑 Keywords:** `steady traffic all the time`, `last day of the month`, `most cost-effective`
>
> **📖 Official docs:** [EC2 instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

#### 7. Which of the following must be specified when launching a new Amazon Elastic Compute Cloud (Amazon EC2) Windows instance? Select two responses.
- [x] Amazon Machine Image (AMI) ✅
- [ ] Password for the administrator account
- [ ] Amazon EC2 instance ID
- [x] Amazon EC2 instance type ✅

> **💡 Why:** To launch an instance you must choose an AMI and an instance type.
>
> **🔑 Keywords:** `must be specified when launching`
>
> **📖 Official docs:** [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

#### 8. Why is AWS more economical than traditional data centers for applications with varying compute workloads? Select the best answer.
- [ ] Customers can permanently run enough instances to handle peak workloads.
- [ ] Customers retain full administrative access to their Amazon EC2 instances
- [ ] Amazon EC2 costs are billed on a monthly basis.
- [x] Amazon EC2 instances can be launched on-demand when needed. ✅

> **💡 Why:** The cloud lets you launch instances on demand and pay only while they run, so you avoid paying for peak capacity all the time.
>
> **🔑 Keywords:** `varying compute workloads`, `economical`
>
> **📖 Official docs:** [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

***

## KC - Identity and Access Management [IAM]

#### 1. In the shared responsibility model, AWS has the responsibility of providing what?
- [ ] Security in the cloud
- [x] Security of the cloud ✅
- [ ] Security to the cloud
- [ ] Security for the cloud

> **💡 Why:** AWS is responsible for security of the cloud (infrastructure). Customers are responsible for security in the cloud.
>
> **🔑 Keywords:** `AWS has the responsibility`
>
> **📖 Official docs:** [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

#### 2. In the shared responsibility model, which of the following are examples of "security in the cloud?" (Select TWO.)
- [ ] Protecting the global infrastructure
- [x] Which AWS services are used with the content ✅
- [ ] Compliance with compute security standards and regulations
- [ ] Physical security of the facilities where the services operate
- [x] In which country content is stored ✅

> **💡 Why:** Choosing which services to use and which country (Region) your content is stored in are customer decisions: security in the cloud.
>
> **🔑 Keywords:** `security in the cloud`, `examples`
>
> **📖 Official docs:** [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

#### 3. Which of the following are some of the security benefits that AWS offers? (Select TWO.)
- [ ] Shared collaboration model
- [x] Infrastructure that meets compliance requirements ✅
- [ ] Inventory and application management
- [ ] Data storage
- [x] Secure global infrastructure ✅

> **💡 Why:** AWS offers compliance-ready infrastructure and a secure global infrastructure.
>
> **🔑 Keywords:** `security benefits that AWS offers`
>
> **📖 Official docs:** [Cloud security at AWS](https://aws.amazon.com/security/)

#### 4. True or False? AWS is responsible for the security of everything above the hypervisor layer.
- [ ] True
- [x] False ✅

> **💡 Why:** False: AWS secures everything up to and including the hypervisor. The customer secures what is above it (guest OS, applications, data).
>
> **🔑 Keywords:** `everything above the hypervisor`
>
> **📖 Official docs:** [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

#### 5. Which of the following is the responsibility of AWS under the shared responsibility model?
- [ ] Managing custom Amazon Machine Images (AMIs)
- [ ] Configuring third-party applications
- [x] Maintaining physical hardware ✅
- [ ] Securing application access and data

> **💡 Why:** AWS maintains the physical hardware. AMIs, third-party apps and data access are customer responsibilities.
>
> **🔑 Keywords:** `responsibility of AWS`
>
> **📖 Official docs:** [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

#### 6. Which resource provides trusted users with temporary security credentials that can control access to your AWS resources?
- [ ] AWS Identity and Access Management (IAM) User
- [x] AWS Security Token Service (AWS STS) ✅
- [ ] Application authentication
- [ ] AWS Command Line Interface (AWS CLI)

> **💡 Why:** AWS STS issues temporary security credentials for trusted users.
>
> **🔑 Keywords:** `temporary security credentials`
>
> **📖 Official docs:** [Temporary security credentials (AWS STS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

#### 7. Which of the following are AWS Identity and Access Management (IAM) best practices? (Select TWO.)
- [ ] Leave unused and unnecessary users and credentials in place.
- [ ] Provide users with default administrative privileges.
- [x] Monitor activity in your AWS account. ✅
- [x] Rotate credentials regularly. ✅
- [ ] Do not use groups to assign permissions to IAM users; provide each user with their own set of custom permissions.

> **💡 Why:** IAM best practices include monitoring account activity and rotating credentials regularly.
>
> **🔑 Keywords:** `IAM best practices`
>
> **📖 Official docs:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

#### 8. True or False? AWS Identity and Access Management (IAM) is appropriate for operating system (OS) and application authentication.
- [x] False ✅
- [ ] True

> **💡 Why:** False: IAM controls access to AWS resources, not OS or application authentication.
>
> **🔑 Keywords:** `operating system (OS) and application authentication`
>
> **📖 Official docs:** [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

#### 9. Where can a customer find information about prohibited actions on AWS infrastructure?
- [ ] AWS Billing Console
- [ ] AWS Trusted Advisor
- [ ] AWS Identity and Access Management (IAM)
- [x] AWS Acceptable Use Policy ✅

> **💡 Why:** The AWS Acceptable Use Policy lists prohibited uses of AWS.
>
> **🔑 Keywords:** `prohibited actions`
>
> **📖 Official docs:** [AWS Acceptable Use Policy](https://aws.amazon.com/aup/)

#### 10. True or False? The access key and secret access key are used to log into the AWS Management Console.
- [ ] True
- [x] False ✅

> **💡 Why:** False: access keys are for programmatic access (CLI, SDK, API). The console uses a user name and password.
>
> **🔑 Keywords:** `access key and secret access key`, `log into the Management Console`
>
> **📖 Official docs:** [Managing IAM access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

#### 11. True or False? Using AWS Identity and Access Management (IAM) groups is the recommended way to manage the permission of IAM users by job function.
- [x] True ✅
- [ ] False

> **💡 Why:** True: assign permissions to IAM groups by job function and put users in the groups.
>
> **🔑 Keywords:** `groups`, `job function`
>
> **📖 Official docs:** [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)

#### 12. After initial login, what does AWS recommend as the best practice for the AWS account root user?
- [ ] Delete the root user account
- [x] Delete root user access keys ✅
- [ ] Revoke all permissions on the root user account
- [ ] Restrict permission on the root user account

> **💡 Why:** Best practice is to delete the root user's access keys and avoid using root for daily work. The root user itself cannot be deleted.
>
> **🔑 Keywords:** `root user`, `after initial login`
>
> **📖 Official docs:** [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)

#### 13. How would a system administrator add an additional layer of login security to a user's access to the AWS Management Console?
- [x] Enable multi-factor authentication (MFA) ✅
- [ ] Audit AWS Identity and Access Management (IAM) roles
- [ ] Enable AWS CloudTrail
- [ ] Use Amazon Cloud Directory

> **💡 Why:** Multi-factor authentication adds a second factor on top of the password.
>
> **🔑 Keywords:** `additional layer of login security`
>
> **📖 Official docs:** [MFA in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)

#### 14. Which of the following are advantages of AWS Cloud security? (Select TWO.)
- [ ] AWS infrastructure security auditing is periodic and manual.
- [ ] AWS uses single-factor access control systems.
- [x] You retain complete control and ownership of your data Region. ✅
- [ ] AWS retains complete control and ownership of your data Region.
- [x] AWS uses multi-factor access control systems. ✅

> **💡 Why:** With AWS you keep control and ownership of your data Region, and AWS uses multi-factor access control systems.
>
> **🔑 Keywords:** `advantages of AWS Cloud security`
>
> **📖 Official docs:** [Cloud security at AWS](https://aws.amazon.com/security/)

#### 15. What is AWS Trusted Advisor?
- [ ] A Professional Services offering hat helps you migrate to the cloud.
- [ ] A partner program that helps you validate your application deployment.
- [x] An online tool that helps you configure resources to follow best practices. ✅
- [ ] An AWS service that helps you manage access to your account.

> **💡 Why:** Trusted Advisor is an online tool that checks your resources against best practices.
>
> **🔑 Keywords:** `What is AWS Trusted Advisor`
>
> **📖 Official docs:** [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

#### 16.Which of the following are included in AWS Assurance Programs? (Select TWO.)
- [x] Laws, regulations, and privacy ✅
- [ ] Industry best practices
- [x] Certifications and attestations ✅
- [ ] Customer testimonials
- [ ] Partner validations

> **💡 Why:** AWS assurance programs cover laws, regulations and privacy, plus certifications and attestations.
>
> **🔑 Keywords:** `Assurance Programs`
>
> **📖 Official docs:** [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)

#### 17. When you create an AWS Identity and Access Management (IAM) policy, what are the two types of access that can be granted to a user? (Select TWO.)
- [x] AWS Management Console access ✅
- [ ] Administrative root access
- [ ] Institutional access
- [ ] Authorized access
- [x] Programmatic access ✅

> **💡 Why:** An IAM user can be given console access, programmatic access, or both.
>
> **🔑 Keywords:** `two types of access`, `IAM policy`
>
> **📖 Official docs:** [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)

#### 18. The AWS risk and compliance program is made up of which of the following components? (Select THREE.)
- [x] Risk management ✅
- [x] Information security ✅
- [ ] Physical security
- [ ] Automation environment
- [x] Controlled environment ✅

> **💡 Why:** The AWS risk and compliance program covers risk management, a controlled environment and information security.
>
> **🔑 Keywords:** `risk and compliance program`, `components`
>
> **📖 Official docs:** [AWS Risk and Compliance whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html)

***

## KC - Amazon Virtual Private Cloud [VPC]

#### 1. Which AWS networking service enables a company to create a virtual network within AWS? Select the best answer.
- [ ] Amazon Route 53
- [ ] AWS Config
- [ ] AWS Direct Connect
- [x] Amazon Virtual Private Cloud (Amazon VPC) ✅

> **💡 Why:** Amazon VPC lets you create an isolated virtual network in AWS.
>
> **🔑 Keywords:** `create a virtual network`
>
> **📖 Official docs:** [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

#### 2. What is the minimum size subnet you can have in an Amazon Virtual Private Cloud (Amazon VPC)?
- [ ] /30
- [ ] /26
- [ ] /24
- [x] /28 ✅

> **💡 Why:** The smallest VPC subnet is /28 (16 IP addresses).
>
> **🔑 Keywords:** `minimum size subnet`
>
> **📖 Official docs:** [Subnet CIDR blocks (sizes, reserved IPs)](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

#### 3. What is the maximum IPv4 address range size you can have in an Amazon Virtual Private Cloud (Amazon VPC)?
- [ ] /30
- [ ] /28
- [ ] /24
- [x] /16 ✅

> **💡 Why:** The largest VPC IPv4 range is /16.
>
> **🔑 Keywords:** `maximum IPv4 address range`
>
> **📖 Official docs:** [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html)

#### 4. You must allow resources in a private subnet to access the internet. Which of the following provides this capability?
- [ ] Network access control lists (network ACLs)
- [ ] Route tables
- [ ] Security groups
- [x] Network address translation (NAT) Gateway ✅

> **💡 Why:** A NAT gateway gives private-subnet resources outbound-only internet access.
>
> **🔑 Keywords:** `private subnet`, `access the internet`
>
> **📖 Official docs:** [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

#### 5. True or False? Private subnets have direct access to the internet.
- [ ] True
- [x] False ✅

> **💡 Why:** False: a private subnet has no direct route to an internet gateway.
>
> **🔑 Keywords:** `Private subnets have direct access`
>
> **📖 Official docs:** [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

#### 6. Which component of the AWS global infrastructure does Amazon CloudFront use to ensure low-latency delivery? Select the best answer.
- [ ] AWS Regions
- [ ] AWS Availability Zones
- [x] AWS edge locations ✅
- [ ] Amazon Virtual Private Cloud (Amazon VPC)

> **💡 Why:** CloudFront serves content from edge locations.
>
> **🔑 Keywords:** `CloudFront`, `low-latency delivery`
>
> **📖 Official docs:** [How CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)

#### 7. Which of the following is an optional security control that can be applied at the subnet layer of a VPC?
- [ ] Security group
- [ ] Firewall
- [ ] Web application firewall (WAF)
- [x] Network Access Control List (NACL) ✅

> **💡 Why:** A network ACL is an optional layer applied at the subnet level. Security groups apply at the instance level.
>
> **🔑 Keywords:** `optional security control`, `subnet layer`
>
> **📖 Official docs:** [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

#### 8. What happens when you create a new virtual private cloud (VPC) with Amazon Virtual Private Cloud (Amazon VPC)? Select the best answer.
- [x] A main route table is created by default. ✅
- [ ] Three subnets are created by default, with one subnet for each Availability Zone.
- [ ] Three subnets are created by default in one Availability Zone.
- [ ] An internet gateway is created by default.

> **💡 Why:** Creating a VPC automatically creates a main route table. It does not create subnets or an internet gateway.
>
> **🔑 Keywords:** `created by default`
>
> **📖 Official docs:** [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

#### 9. How many internet gateways (IGWs) can you attach to an Amazon VPC at any one time?
- [ ] 4
- [x] 1 ✅
- [ ] 3
- [ ] 2

> **💡 Why:** A VPC can have only one internet gateway attached at a time.
>
> **🔑 Keywords:** `how many internet gateways`
>
> **📖 Official docs:** [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)

#### 10. You are a solutions architect who works for a large retail company that is migrating its existing infrastructure to AWS. You recommend they use a custom Amazon Virtual Private Cloud (Amazon VPC). They will need a public subnet for their web servers and a private subnet for their databases. They require web servers and database servers to be highly available, with a minimum of two web servers and two database servers each.
How many subnets should you have to maintain high availability? Select the best answer.
- [x] 4 ✅
- [ ] 2
- [ ] 3
- [ ] 1

> **💡 Why:** You need a public and a private subnet in each of two AZs, which makes four subnets, to keep both tiers highly available.
>
> **🔑 Keywords:** `public subnet`, `private subnet`, `highly available`, `minimum of two`
>
> **📖 Official docs:** [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

#### 11. What is used to divide an Amazon Virtual Private Cloud (Amazon VPC)?
- [ ] Classless Inter-Domain Routing (CIDR) block
- [x] Subnet ✅
- [ ] Availability Zones
- [ ] Route table

> **💡 Why:** Subnets divide a VPC into smaller segments.
>
> **🔑 Keywords:** `used to divide`
>
> **📖 Official docs:** [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

#### 12. What defines a subnet?
- [ ] Route table
- [x] Classless Inter-Domain Routing (CIDR) block ✅
- [ ] Instance
- [ ] Availability Zones

> **💡 Why:** A subnet is defined by its CIDR block.
>
> **🔑 Keywords:** `what defines a subnet`
>
> **📖 Official docs:** [Subnet CIDR blocks (sizes, reserved IPs)](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

#### 13. How many IP addresses in a subnet are reserved by AWS?
- [ ] Three
- [ ] Four
- [ ] Two
- [x] Five ✅

> **💡 Why:** AWS reserves five IP addresses in each subnet: the first four and the last one.
>
> **🔑 Keywords:** `reserved by AWS`
>
> **📖 Official docs:** [Subnet CIDR blocks (sizes, reserved IPs)](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

#### 14. Which statement describes an elastic network interface?
- [ ] A static IPv4 address designed for dynamic cloud computing.
- [ ] Enables the creation of a private connection between your Amazon Virtual Private Cloud (Amazon VPC) without requiring access over the internet or through a
- [ ] network address translation (NAT) instance.
- [x] A virtual network interface that you can attach to an instance in an Amazon Virtual Private Cloud (Amazon VPC). ✅
- [ ] An Amazon managed resource designed to operate like a network address translation (NAT) instance, but is simpler to manage and is highly available within an Availability Zone.

> **💡 Why:** An elastic network interface is a virtual network card that you attach to an instance in a VPC.
>
> **🔑 Keywords:** `elastic network interface`
>
> **📖 Official docs:** [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

#### 15. True or False. Within a Region, you can create multiple Amazon Virtual Private Cloud (Amazon VPC) and have complete control of the network configuration for each VPC.
- [x] True ✅
- [ ] False

> **💡 Why:** True: you can create several VPCs in a Region (default quota applies), and you control each one's networking.
>
> **🔑 Keywords:** `multiple VPCs`, `complete control`
>
> **📖 Official docs:** [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)

***

## KC - Storage

#### 1. True or False? Amazon Simple Storage Service (Amazon S3) is an object storage suitable for the storage of flat files like Microsoft Word documents, photos, and so on.
- [x] True ✅
- [ ] False

> **💡 Why:** S3 is object storage for flat files such as documents and photos.
>
> **🔑 Keywords:** `object storage`, `flat files`
>
> **📖 Official docs:** [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

#### 2. Amazon Simple Storage Service (Amazon S3) replicates all objects ___.
- [ ] on multiple S3 buckets
- [x] in multiple Availability Zones within the same Region ✅
- [ ] on multiple volumes within an Availability Zone
- [ ] across multiple Regions for higher durability

> **💡 Why:** S3 stores objects redundantly across multiple AZs within the same Region.
>
> **🔑 Keywords:** `replicates all objects`
>
> **📖 Official docs:** [Data protection in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

#### 3. Which of the following can be used as a storage class for an Amazon Simple Storage Service (Amazon S3) object lifecycle policy? (Select THREE.)
- [x] Amazon Simple Storage Service Glacier ✅
- [ ] Storage gateway
- [ ] Amazon DynamoDB
- [ ] S3 - Reduced Redundancy Storage
- [x] S3 - Infrequent Access ✅
- [x] S3 Standard Access ✅

> **💡 Why:** S3 lifecycle policies can transition objects between S3 Standard, S3 Infrequent Access and Glacier.
>
> **🔑 Keywords:** `storage class`, `lifecycle policy`
>
> **📖 Official docs:** [Managing S3 object lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) · [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

#### 4. The name of an Amazon Simple Storage Service (Amazon S3) bucket must be unique ___.
- [ ] within a Region
- [ ] across all of your AWS accounts
- [x] worldwide across all AWS accounts ✅
- [ ] within your AWS account

> **💡 Why:** S3 bucket names are globally unique across all AWS accounts.
>
> **🔑 Keywords:** `name ... must be unique`
>
> **📖 Official docs:** [S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html)

#### 5. What can you use Amazon Simple Storage Service (Amazon S3) for with your web application?
- [x] Store static content such as images, video, CSS, JavaScript, and so on ✅
- [ ] Generate user-specific content
- [ ] Distribute static and dynamic content
- [ ] Host a robust content delivery network (CDN) to deliver entire websites with dynamic, static, and streaming content

> **💡 Why:** S3 is ideal for static content such as images, video, CSS and JavaScript. Delivering static and dynamic content is CloudFront's role.
>
> **🔑 Keywords:** `web application`, `static content`
>
> **📖 Official docs:** [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

#### 6. Amazon Elastic Block Store (Amazon EBS) is recommended when data ___. (Select TWO.)
- [ ] must be stored in a different Availability Zone than the one the Amazon Elastic Compute Cloud (Amazon EC2) instance is in
- [ ] requires object-level storage
- [x] must be quickly accessible, requiring long-term persistence ✅
- [x] requires an encryption solution ✅

> **💡 Why:** EBS is for data that needs quick access with long-term persistence and supports encryption.
>
> **🔑 Keywords:** `recommended when data`, `persistence`, `encryption`
>
> **📖 Official docs:** [What is Amazon EBS?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) · [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)

#### 7. True or False? By default, all data stored in Amazon Simple Storage Service (Amazon S3) is viewable by the public.
- [ ] True
- [x] False ✅

> **💡 Why:** False: new S3 buckets and their objects are private by default.
>
> **🔑 Keywords:** `by default`, `viewable by the public`
>
> **📖 Official docs:** [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

#### 8. Regarding Amazon Simple Storage Service Glacier, what is a vault?
- [ ] An object (photos, videos, files, or documents)
- [x] A container for storing archives ✅
- [ ] A policy that identifies who can access content stored in Amazon S3 Glacier.
- [ ] The rules that determine who can (or cannot) access archives

> **💡 Why:** A Glacier vault is a container for storing archives.
>
> **🔑 Keywords:** `vault`, `Glacier`
>
> **📖 Official docs:** [Working with S3 Glacier vaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html)

#### 9. True or False? Access control lists are used to make entire buckets public, like one hosting a website on Amazon Simple Storage Service (Amazon S3).
- [x] False ✅
- [ ] True

> **💡 Why:** False: ACLs are not how you make a whole bucket public. Static website hosting uses a bucket policy and public access settings.
>
> **🔑 Keywords:** `entire buckets public`, `hosting a website`
>
> **📖 Official docs:** [Permissions for S3 static website (bucket policy)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html)

#### 10. Which of the following are features of Amazon Elastic Block Store (Amazon EBS)? (Select TWO.)
- [ ] Amazon EBS data is automatically backed up to tape.
- [x] Amazon EBS volumes can be encrypted transparently to workloads on the attached instance. ✅
- [ ] Data on an Amazon EBS volume is lost when the attached instance is stopped.
- [x] Amazon EBS is automatically replicated within an Availability Zone. ✅

> **💡 Why:** EBS volumes can be encrypted transparently and are replicated within their AZ. Data on an EBS volume persists after stopping.
>
> **🔑 Keywords:** `features of Amazon EBS`
>
> **📖 Official docs:** [What is Amazon EBS?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) · [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)

***

## KC - Databases

#### 1. You are designing an ecommerce web application that will scale to hundreds of thousands of concurrent users. Which database technology is best suited to hold the session state in this example?
- [ ] Data warehouse using Amazon Redshift
- [x] NoSQL database table using Amazon DynamoDB ✅
- [ ] Amazon Simple Storage Service (Amazon S3)
- [ ] Relational database using Amazon Relational Database Service (Amazon RDS)

> **💡 Why:** DynamoDB is the NoSQL choice for session state at huge scale.
>
> **🔑 Keywords:** `session state`, `hundreds of thousands of concurrent users`
>
> **📖 Official docs:** [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 2. You need to find an item in an Amazon DynamoDB table using an attribute other than the item's primary key. Which of the following operations should you use?
- [ ] Query
- [x] Scan ✅
- [ ] GET
- [ ] POST

> **💡 Why:** Scan reads the whole table and filters by any attribute. Query needs the key.
>
> **🔑 Keywords:** `attribute other than the primary key`
>
> **📖 Official docs:** [Scan operation in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html)

#### 3. Which AWS Cloud service is best suited for online analytic processing (OLAP)?
- [ ] Amazon Relational Database Service (Amazon RDS)
- [x] Amazon Redshift ✅
- [ ] Amazon DynamoDB
- [ ] Amazon Simple Storage Service Glacier

> **💡 Why:** Redshift is the data warehouse for OLAP analytics.
>
> **🔑 Keywords:** `online analytic processing (OLAP)`
>
> **📖 Official docs:** [What is Amazon Redshift?](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

#### 4. In Amazon DynamoDB, an attribute is ___
- [ ] a data value
- [x] a fundamental data element ✅
- [ ] a collection of items
- [ ] an operation on a table

> **💡 Why:** An attribute is a fundamental data element in DynamoDB.
>
> **🔑 Keywords:** `attribute`, `DynamoDB`
>
> **📖 Official docs:** [DynamoDB core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

#### 5. When you create a table in Amazon DynamoDB, in addition to the table name, you must specify the ___ of the table.
- [ ] sort key
- [ ] local secondary index
- [ ] global secondary index
- [x] primary key ✅

> **💡 Why:** DynamoDB requires a primary key when you create a table.
>
> **🔑 Keywords:** `must specify`, `in addition to the table name`
>
> **📖 Official docs:** [DynamoDB core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

#### 6. ___ is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases.
- [ ] Amazon DynamoDB
- [ ] Amazon Redshift
- [x] Amazon Aurora ✅
- [ ] Amazon Neptune

> **💡 Why:** Aurora is up to 5x faster than MySQL and 3x faster than PostgreSQL.
>
> **🔑 Keywords:** `five times faster than MySQL`, `three times faster than PostgreSQL`
>
> **📖 Official docs:** [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

#### 7. If you are developing an application that requires a database with extremely fast ___ performance, fast scalability, and flexibility in the database schema, which database should you choose?
- [ ] Amazon Redshift
- [x] Amazon DynamoDB ✅
- [ ] Amazon ElastiCache
- [ ] Amazon Relational Database Service (Amazon RDS)

> **💡 Why:** DynamoDB gives very fast performance, fast scalability and a flexible schema.
>
> **🔑 Keywords:** `extremely fast performance`, `flexibility in the database schema`
>
> **📖 Official docs:** [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

#### 8. True or False? Amazon Relational Database Service (Amazon RDS) automatically patches the database software and backs up your database, storing the backups for a user-defined retention period and enabling point-in-time recovery.
- [ ] False
- [x] True ✅

> **💡 Why:** True: RDS automates patching and backups with a retention period and point-in-time recovery.
>
> **🔑 Keywords:** `automatically patches`, `point-in-time recovery`
>
> **📖 Official docs:** [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

***

## KC - Billing and Support

#### 1. What are the four support plans offered by AWS? Choose four answers.
- [ ] Individual
- [x] Developer ✅
- [x] Enterprise ✅
- [ ] Start-up
- [x] Basic ✅
- [x] Business ✅

> **💡 Why:** The four support plans in this course are Basic, Developer, Business and Enterprise.
>
> **🔑 Keywords:** `four support plans`
>
> **📖 Official docs:** [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) · [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)
>
> **⚠️ Note:** AWS has restructured its support plans, and the legacy Developer, Business and Enterprise On-Ramp plans are being retired. The marked answer follows the older course material.

#### 2. What are the characteristics of the Developer Support Plan? Select two responses.
- [x] One primary contact can open a case ✅
- [ ] Unlimited contacts can open a case
- [ ] Assigned to a Technical Account Manager (TAM)
- [ ] 24/7 access to Cloud Support Engineers via email, chat, and phone
- [x] Business hours access to Cloud Support Associates via email ✅

> **💡 Why:** Developer Support allows one primary contact and business-hours email access to Cloud Support Associates.
>
> **🔑 Keywords:** `Developer Support Plan`, `characteristics`
>
> **📖 Official docs:** [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) · [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

#### 3. Which of the following is not available in the Business Support Plan? Select the best answer.
- [ ] Access to Cloud Support Engineers for technical issues
- [x] Access to a Well-Architected review delivered by AWS Solutions Architects ✅
- [ ] Access to third-party software support
- [ ] Access to the Personal Health Dashboard and the AWS Health API

> **💡 Why:** Well-Architected reviews delivered by Solutions Architects are an Enterprise feature, not Business.
>
> **🔑 Keywords:** `not available in the Business Support Plan`
>
> **📖 Official docs:** [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) · [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

#### 4. Which of the AWS Support levels offers 24/7 support via phone or chat? Select two responses.
- [x] Business Support ✅
- [ ] Basic Support
- [ ] Developer Support
- [x] Enterprise Support ✅

> **💡 Why:** Business and Enterprise offer 24/7 phone and chat access.
>
> **🔑 Keywords:** `24/7 support via phone or chat`
>
> **📖 Official docs:** [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) · [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

#### 5. Your company's IT management team is looking for an online tool to provide recommendations to save money, improve system availability and performance, and to help close security gaps. What tool can help the management team?
- [ ] AWS Config
- [x] AWS Trusted Advisor ✅
- [ ] Configuration recorder
- [ ] Cloud Detective

> **💡 Why:** Trusted Advisor gives recommendations on cost, performance, security and fault tolerance.
>
> **🔑 Keywords:** `save money`, `improve availability and performance`, `security gaps`
>
> **📖 Official docs:** [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

#### 6. AWS Support has five different severity levels for support cases. What are they? Select five responses.
- [ ] Medium
- [x] High ✅
- [x] Criticial ✅
- [x] Urgent ✅
- [x] Normal ✅
- [x] Low ✅
- [ ] System Down

> **💡 Why:** The five severity levels are Low, Normal, High, Urgent and Critical.
>
> **🔑 Keywords:** `five severity levels`
>
> **📖 Official docs:** [Choosing a case severity](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)

#### 7. What is the response time of urgent issues for Enterprise Support Plan customers? Select the best answer.
- [x] 1 hour or less ✅
- [ ] 12 hours or less
- [ ] 30 minutes or less
- [ ] 4 hours or less

> **💡 Why:** For Enterprise Support, an urgent case has a response time of 1 hour or less.
>
> **🔑 Keywords:** `response time of urgent issues`, `Enterprise`
>
> **📖 Official docs:** [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

#### 8. A Basic Support Plan allows how many support cases per month? Select the best answer.
- [ ] 1
- [ ] 5
- [x] 0 ✅
- [ ] 10

> **💡 Why:** Basic Support has no technical support cases. It covers account and billing questions only.
>
> **🔑 Keywords:** `Basic Support Plan`, `support cases per month`
>
> **📖 Official docs:** [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html)

#### 9. What will AWS Trusted Advisor tell you? Select three responses.
- [x] Whether or not you are using fault tolerance ✅
- [x] How well the infrastructure is performing ✅
- [x] Deployed resources that are not being used, but are incurring charges ✅
- [ ] Assess the risk of a single Region deployment
- [ ] When security groups have been closed

> **💡 Why:** Trusted Advisor reports on fault tolerance, performance and idle resources that cost money.
>
> **🔑 Keywords:** `what will Trusted Advisor tell you`
>
> **📖 Official docs:** [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

#### 10. Which AWS Support plan includes the assistance of a Technical Account Manager (TAM)? Select the best answer.
- [ ] Basic Support Plan
- [ ] Developer Support Plan
- [ ] Business Support Plan
- [x] Enterprise Support Plan ✅

> **💡 Why:** A Technical Account Manager comes with the Enterprise plan.
>
> **🔑 Keywords:** `Technical Account Manager (TAM)`
>
> **📖 Official docs:** [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

***

## KC - Cloud Architecting

#### 1. Which of the following is not one of the four areas of the performance efficiency pillar in the Well-Architected Framework? Select the best answer.
- [x] Traceability ✅
- [ ] Monitoring
- [ ] Selection
- [ ] Tradeoffs

> **💡 Why:** The four areas of performance efficiency are Selection, Review, Monitoring and Tradeoffs. Traceability belongs to the Security pillar.
>
> **🔑 Keywords:** `four areas`, `performance efficiency pillar`
>
> **📖 Official docs:** [Performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

#### 2. Which is not a characteristic of the Amazon EC2 Scaling service? Select the best answer.
- [ ] Responds to changing conditions by adding or terminating Amazon Elastic
- [ ] Compute Cloud (Amazon EC2) instances
- [x] Sends traffic to healthy instances ✅
- [ ] Launches instances from a specified Amazon Machine Image (AMI)
- [ ] Enforces a minimum number of running Amazon Elastic Compute Cloud (Amazon EC2) instances

> **💡 Why:** Auto Scaling adds or removes instances, enforces minimums and launches from an AMI. Sending traffic to healthy instances is Elastic Load Balancing's job.
>
> **🔑 Keywords:** `not a characteristic`, `Auto Scaling`
>
> **📖 Official docs:** [What is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) · [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

#### 3. Which options will help increase the availability of a web server farm? Select two responses.
- [ ] Use Amazon CloudFront to deliver content to end users with low latency.
- [ ] Deploy the instances in an Amazon Virtual Private Cloud (Amazon VPC).
- [x] Launch the web server instance across multiple Availability Zones. ✅
- [ ] Add more CPU and RAM to each instance.
- [x] Leverage Scaling to recover from failed instances. ✅

> **💡 Why:** Use multiple AZs and Auto Scaling to replace failed instances for higher availability.
>
> **🔑 Keywords:** `increase the availability`, `web server farm`
>
> **📖 Official docs:** [Reliability pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) · [What is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

#### 4. Which design principles are recommended when considering performance efficiency? Select two responses.
- [x] Utilize serverless architectures ✅
- [x] Democratize advanced technologies ✅
- [ ] Promote expenditure awareness
- [ ] Enable traceability
- [ ] Match supply with demand

> **💡 Why:** Performance efficiency design principles include serverless architectures and democratizing advanced technologies.
>
> **🔑 Keywords:** `design principles`, `performance efficiency`
>
> **📖 Official docs:** [Performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

#### 5. Which AWS offering enables customers to find, buy, and immediately start using software solutions in their AWS environment? Select the best answer.
- [x] AWS Marketplace ✅
- [ ] AWS Database Migration Service (AWS DMS)
- [ ] AWS SDK
- [ ] AWS Storage Gateway

> **💡 Why:** AWS Marketplace is the catalog for finding, buying and deploying third-party software.
>
> **🔑 Keywords:** `find, buy, and immediately start using software`
>
> **📖 Official docs:** [What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html)

#### 6. In a physical data center, security is typically considered in what area? Select the best answer
- [ ] In an edge location
- [x] Only in the perimeter ✅
- [ ] In the closest availability zones
- [ ] In the closest region

> **💡 Why:** Physical data centers often rely on perimeter-only security. In AWS you apply security at every layer.
>
> **🔑 Keywords:** `physical data center`, `security typically considered`
>
> **📖 Official docs:** [Security pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

#### 7. To view all categories of instance metadata from within a running instance, which URL should you use? Select the best answer
- [ ] https://196.245.196.245/latest/meta-data/
- [x] https://169.254.169.254/latest/meta-data/ ✅
- [ ] https://245.196.245.196/latest/meta-data/
- [ ] https://254.169.254.169/latest/meta-data/

> **💡 Why:** The metadata URL is http(s)://169.254.169.254/latest/meta-data/.
>
> **🔑 Keywords:** `view all categories of instance metadata`
>
> **📖 Official docs:** [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

#### 8. What is defined as the ability for a system to remain operational even if some of the components of that system fail? Select the best answer.
- [x] Fault tolerance ✅
- [ ] High availability
- [ ] High durability
- [ ] DNS failovers

> **💡 Why:** Fault tolerance means the system stays operational when components fail.
>
> **🔑 Keywords:** `remain operational even if some components fail`
>
> **📖 Official docs:** [Reliability pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

#### 9. Which best describes a system that is always available, without the need for human intervention? Select the best answer.
- [ ] Elastic
- [ ] Fault tolerant
- [x] Highly available ✅
- [ ] Scalable

> **💡 Why:** Highly available systems keep running automatically without human intervention.
>
> **🔑 Keywords:** `always available`, `without human intervention`
>
> **📖 Official docs:** [Reliability pillar (Well-Architected)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

***

## KC - Balancing - Scaling - Monitoring

#### 1. Which of the following AWS tools help your application scale up or down based on demand? Select two responses.
- [ ] AWS CloudFormation
- [x] Elastic Load Balancing ✅
- [x] Scaling ✅
- [ ] Auto Availability Zones
- [ ] Agile Load Balancing

> **💡 Why:** Elastic Load Balancing and Auto Scaling help an application scale with demand.
>
> **🔑 Keywords:** `scale up or down based on demand`
>
> **📖 Official docs:** [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) · [What is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

#### 2. Which service would you use to send alerts based on Amazon CloudWatch alarms? Select the best answer.
- [ ] AWS Trusted Advisor
- [ ] AWS CloudTrail
- [ ] Amazon Route 53
- [x] Amazon Simple Notification Service (Amazon SNS) ✅

> **💡 Why:** CloudWatch alarms notify through SNS.
>
> **🔑 Keywords:** `send alerts`, `CloudWatch alarms`
>
> **📖 Official docs:** [CloudWatch alarms that send email (SNS)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

#### 3. Which is not a characteristic of the Amazon EC2 Scaling service? Select the best answer.
- [ ] Responds to changing conditions by adding or terminating Amazon Elastic
- [ ] Compute Cloud (Amazon EC2) instances
- [ ] Enforces a minimum number of running Amazon Elastic Compute Cloud (Amazon EC2) instances
- [ ] Launches instances from a specified Amazon Machine Image (AMI)
- [x] Sends traffic to healthy instances ✅

> **💡 Why:** Distributing traffic to healthy instances is the load balancer's job, not Auto Scaling's.
>
> **🔑 Keywords:** `not a characteristic`, `Auto Scaling`
>
> **📖 Official docs:** [What is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) · [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

#### 4. Which of the following must be configured on an Elastic Load Balancing load balancer to accept incoming traffic?
- [ ] A network interface
- [x] A listener ✅
- [ ] An instance
- [ ] A port

> **💡 Why:** A load balancer needs a listener, which checks for connection requests on a protocol and port.
>
> **🔑 Keywords:** `configured on an Elastic Load Balancing load balancer`, `accept incoming traffic`
>
> **📖 Official docs:** [Elastic Load Balancing listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)

#### 5. What are the minimum elements required to create an Auto Scaling launch configuration. Select three responses.
- [ ] Block device mapping
- [x] Amazon Machine Image (AMI) ✅
- [x] Launch configuration name ✅
- [ ] Security group
- [x] Instance type ✅

> **💡 Why:** An Auto Scaling launch configuration needs at minimum an AMI, a name and an instance type.
>
> **🔑 Keywords:** `minimum elements`, `launch configuration`
>
> **📖 Official docs:** [Auto Scaling launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html)
>
> **⚠️ Note:** AWS now recommends launch templates over launch configurations.

#### 6. How long does Amazon CloudWatch keep metric data? Select the best answer.
- [x] 15 months ✅
- [ ] 2 weeks
- [ ] 12 months
- [ ] 1 month

> **💡 Why:** CloudWatch keeps metric data for 15 months.
>
> **🔑 Keywords:** `how long`, `metric data`
>
> **📖 Official docs:** [CloudWatch concepts (metric retention)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)

#### 7. Amazon CloudWatch supports which types of monitoring plans? Select two responses.
- [ ] Basic monitoring, which has an additional cost
- [x] Basic monitoring, which is free ✅
- [ ] Detailed monitoring, which is free
- [ ] Ad hoc monitoring, which has an additional cost
- [x] Detailed monitoring, which has an additional cost ✅

> **💡 Why:** Basic monitoring is free. Detailed monitoring costs extra and gives one-minute data.
>
> **🔑 Keywords:** `monitoring plans`
>
> **📖 Official docs:** [EC2 basic vs detailed monitoring](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)

#### 8. Which of the following is a type of Elastic Load Balancing health check? (Select THREE.)
- [x] A ping ✅
- [ ] An Amazon Elastic Compute Cloud (Amazon EC2) instance status check.
- [x] A connection attempt ✅
- [x] A page request ✅
- [ ] A key pair verification

> **💡 Why:** Load balancer health checks use a ping, a connection attempt or a page request.
>
> **🔑 Keywords:** `type of health check`
>
> **📖 Official docs:** [Classic Load Balancer health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html)

#### 9. What are the three types of load balancers that Amazon Elastic Load Balancing offers?
- [x] Network Load Balancer ✅
- [ ] Internet Load Balancer
- [x] Classic Load Balancer ✅
- [ ] Scaling Load Balancer
- [ ] Compute Load Balancer
- [x] Application Load Balancer ✅

> **💡 Why:** The load balancer types named here are Network, Classic and Application.
>
> **🔑 Keywords:** `three types of load balancers`
>
> **📖 Official docs:** [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

***
