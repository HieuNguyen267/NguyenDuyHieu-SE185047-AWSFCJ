---
title: "Worklog Week 9"
date: 2025-11-07
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---
### Week 9 Goals:

* Configure Amazon S3 for secure image uploads (bucket policy, CORS, ACL).
* Build upload service with presigned URL flow integrated into backend API.

### Tasks for Week 9

| Day | Task | Start Date | End Date | Reference Material |
|-----|------|------------|----------|--------------------|
| 1   | Create S3 bucket for product images; enforce private access; enable versioning. | 03/11/2025 | 03/11/2025 | AWS S3 docs |
| 2   | Configure CORS for CloudFront/SPA origins and limit MIME types. | 04/11/2025 | 04/11/2025 | AWS S3 docs |
| 3   | Implement presigned URL generator service (PUT/GET), size/type validation. | 05/11/2025 | 05/11/2025 | AWS SDK docs |
| 4   | Integrate upload endpoints into backend; attach metadata (uploader, productId). | 06/11/2025 | 06/11/2025 | `AWSJewelry` proposal |
| 5   | End-to-end test upload from React: obtain URL → PUT image → retrieve via CDN. | 07/11/2025 | 07/11/2025 | Postman, CloudFront |

### Achievements of Week 9:
* S3 bucket hardened (private by default, versioning, minimal CORS for SPA origins).
* Presigned URL service added with content-type/size guardrails and metadata tagging.
* Upload API wired to product context, returning CDN-ready object keys.
* Frontend verified: image upload succeeds and assets delivered through CloudFront.
