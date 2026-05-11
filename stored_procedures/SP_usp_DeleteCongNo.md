# Stored Procedure: `usp_DeleteCongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.043000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@CongNoID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteCongNo]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteCongNo]
	@CongNoID int
AS

SET NOCOUNT ON

Update [dbo].[CongNo]
Set DeletedStatus = 1
WHERE
	[CongNoID] = @CongNoID

--endregion

```
