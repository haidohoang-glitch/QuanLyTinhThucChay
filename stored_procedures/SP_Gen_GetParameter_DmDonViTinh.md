# Stored Procedure: `Gen_GetParameter_DmDonViTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:39.363000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.013000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmDonViTinh] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmDonViTinh] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
