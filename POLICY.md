# Privacy Policy for FBS3R Validator API

**Effective Date:** May 2025  
**Repository:** https://github.com/neatpeak/fbs3r-validator

## Overview

The FBS3R Validator API is designed to validate structural and semantic elements of FB(S³)R documents. This service accepts document uploads and performs automated validation tasks.

## Data Processing

1. **Uploaded Files**
   - Uploaded files are used **solely for the purpose of validation**.
   - Files are **not stored or logged**, unless you explicitly request archiving using the `/validate/archive` endpoint.

2. **Validation Results**
   - Validation results are **temporarily processed in memory**.
   - If you use the `/validate/archive` endpoint, the result and filename are **stored** in our system for retrieval via `/validate/history`.

3. **PDF Report Generation**
   - When you request a PDF report, the file is processed and the resulting PDF is **returned immediately without being stored**.

## Data Retention

- **Archived data** is retained **only if explicitly archived by the user**.
- No other data is stored after processing unless requested.

## Data Security

- All data transmissions occur over **HTTPS**.
- We do not share any data with third parties.

## Contact

If you have any questions or concerns, please contact us via  
[https://github.com/neatpeak/fbs3r-validator/issues](https://github.com/neatpeak/fbs3r-validator/issues)

---

*This policy applies to all users of the FBS3R Validator API starting May 2025.*